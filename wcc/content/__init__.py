from zope.i18nmessageid import MessageFactory
from wcc.content.config import packageName, permissions
from wcc.content import TranslatableFileImage

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('wcc.content')

def initialize(context):
    """ initializer called when used as a zope2 product """

    from Products.CMFCore import utils
    from Products.Archetypes import atapi
    from Products.ATContentTypes import permission as atct
    from plone.app.blob import content

    replacement_types = (
        ('TranslatableFile', TranslatableFileImage.addATTranslatableBlobFile),
        ('TranslatableImage', TranslatableFileImage.addATTranslatableBlobImage),
    )

    for name, constructor in replacement_types:
        utils.ContentInit("%s: %s" % (packageName, name),
            content_types = (content.ATBlob,),
            permission = permissions.get(name),
            extra_constructors = (constructor,),
            ).initialize(context)

