import qrcode
import vobject
from PIL import Image

# Create a vCard object
# vCard fields:
# fn (Formatted Name) - Full formatted name
# n (Name) - Structured name (family, given, additional, prefixes, suffixes)
# nickname - Nickname
# photo - Photo/avatar
# bday - Birthday
# anniversary - Anniversary
# gender - Gender
# adr (Address) - Structured address (street, city, region, postal code, country)
# tel - Telephone number (can have types like WORK, HOME, CELL)
# email - Email address (can have types like WORK, HOME)
# impp - Instant messaging address
# lang - Language(s) spoken
# tz - Time zone
# geo - Geographic coordinates
# title - Job title
# role - Role/occupation
# logo - Organization logo
# org - Organization name
# member - Group membership
# related - Related people
# categories - Categories/tags
# note - Notes
# rev - Last revision date
# sound - Pronunciation of name
# url - Website URL
# key - Public encryption key
# uid - Unique identifier


class ContactInfo:
    def __init__(self,
                 formatted_name="",
                 family_name="",
                 given_name="",
                 additional_name="",
                 name_prefix="",
                 name_suffix="",
                 nickname="",
                 photo="",
                 birthday="",
                 anniversary="", 
                 gender="",
                 street="",
                 city="",
                 region="",
                 postal_code="",
                 country="",
                 telephone="",
                 email="",
                 im_address="",
                 languages="",
                 timezone="",
                 geo_coords="",
                 title="",
                 role="",
                 logo="",
                 organization="",
                 member="",
                 related="",
                 categories="",
                 note="",
                 revision="",
                 sound="",
                 url="",
                 key="",
                 uid=""):
        self.formatted_name = formatted_name
        self.family_name = family_name
        self.given_name = given_name
        self.additional_name = additional_name
        self.name_prefix = name_prefix
        self.name_suffix = name_suffix
        self.nickname = nickname
        self.photo = photo
        self.birthday = birthday
        self.anniversary = anniversary
        self.gender = gender
        self.street = street
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country
        self.telephone = telephone
        self.email = email
        self.im_address = im_address
        self.languages = languages
        self.timezone = timezone
        self.geo_coords = geo_coords
        self.title = title
        self.role = role
        self.logo = logo
        self.organization = organization
        self.member = member
        self.related = related
        self.categories = categories
        self.note = note
        self.revision = revision
        self.sound = sound
        self.url = url
        self.key = key
        self.uid = uid

        assert self.formatted_name, "Formatted name is required"
        assert (self.telephone or self.email), "Telephone or email is required"

    def generate_vcard(self):
        self.card = vobject.vCard()

        # RELEVANT FIELDS
        self.card.add('fn').value = self.formatted_name
        self.card.add('n').value = vobject.vcard.Name(
            family=self.family_name or 'Doe',
            given=self.given_name or 'John',
            additional=self.additional_name,
            prefix=self.name_prefix,
            suffix=self.name_suffix
        )
        if self.telephone:
            self.card.add('tel').value = self.telephone
        if self.email:
            self.card.add('email').value = self.email

        self.card.add('title').value = self.title
        self.card.add('org').value = self.organization


        # OPTIONAL FIELDS

        if self.nickname:
            self.card.add('nickname').value = self.nickname
        if self.photo:
            self.card.add('photo').value = self.photo
        if self.birthday:
            self.card.add('bday').value = self.birthday
        if self.anniversary:
            self.card.add('anniversary').value = self.anniversary
        if self.gender:
            self.card.add('gender').value = self.gender
        if any([self.street, self.city, self.region, self.postal_code, self.country]):
            self.card.add('adr').value = vobject.vcard.Address(
                street=self.street,
                city=self.city,
                region=self.region,
                code=self.postal_code,
                country=self.country
            )
        if self.im_address:
            self.card.add('impp').value = self.im_address
        if self.languages:
            self.card.add('lang').value = self.languages
        if self.timezone:
            self.card.add('tz').value = self.timezone
        if self.geo_coords:
            self.card.add('geo').value = self.geo_coords
        if self.role:
            self.card.add('role').value = self.role
        if self.logo:
            self.card.add('logo').value = self.logo
        if self.member:
            self.card.add('member').value = self.member
        if self.related:
            self.card.add('related').value = self.related
        if self.categories:
            self.card.add('categories').value = self.categories
        if self.note:
            self.card.add('note').value = self.note
        if self.revision:
            self.card.add('rev').value = self.revision
        if self.sound:
            self.card.add('sound').value = self.sound
        if self.url:
            self.card.add('url').value = self.url
        if self.key:
            self.card.add('key').value = self.key
        if self.uid:
            self.card.add('uid').value = self.uid

        return self.card.serialize()
    
    def generate_qr(self):
        vcard_str = self.generate_vcard()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add the vCard data to QR code
        qr.add_data(vcard_str)
        qr.make(fit=True)

        # Create an image from the QR Code with a logo in the center
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Open and resize the logo image
        if self.logo:
            try:
                logo = Image.open(self.logo)
                # Convert QR code to RGBA if it isn't already
                qr_image = qr_image.convert('RGBA')
                
                # Preserve logo's aspect ratio
                logo_size = qr_image.size[0] // 4
                logo_width, logo_height = logo.size
                ratio = min(logo_size / logo_width, logo_size / logo_height)
                new_size = (int(logo_width * ratio), int(logo_height * ratio))
                logo = logo.resize(new_size, Image.Resampling.LANCZOS)
                
                # Convert logo to RGBA if it isn't already
                if logo.mode != 'RGBA':
                    logo = logo.convert('RGBA')
                
                # Calculate position to place logo in center
                pos = ((qr_image.size[0] - logo.size[0]) // 2,
                      (qr_image.size[1] - logo.size[1]) // 2)
                
                # Paste the logo onto the QR code using alpha channel as mask
                qr_image.paste(logo, pos, logo)
            except Exception as e:
                print(f"Could not add logo to QR code: {str(e)}")

        # Save the QR code image
        qr_image.save('contact_qr.png')
