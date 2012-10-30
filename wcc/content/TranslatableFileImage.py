from wcc.content.interfaces import ITranslatableImage, ITranslatableFile
from plone.app.blob.content import addATBlob
from Products.Archetypes.interfaces import ISchema, IBaseObject
from zope.component import adapter
from zope.interface import implementer
from archetypes.schemaextender.extender import cachingInstanceSchemaFactory

from zope.interface import implements
from plone.app.blob import markings

markings.interfaces['TranslatableImage'] = (
    [ITranslatableImage] + markings.interfaces['Image']
)

markings.interfaces['TranslatableFile'] = (
    [ITranslatableFile] + markings.interfaces['File']
)

def addATTranslatableBlobImage(container, id, **kwargs):
    return addATBlob(container, id, subtype='TranslatableImage', **kwargs)

def addATTranslatableBlobFile(container, id, **kwargs):
    return addATBlob(container, id, subtype='TranslatableFile', **kwargs)



@implementer(ISchema)
@adapter(ITranslatableFile)
def fileSchemaFactory(context):
    schema = cachingInstanceSchemaFactory(context)
    schema['file'].languageIndependent = False
    return schema

@implementer(ISchema)
@adapter(ITranslatableImage)
def imageSchemaFactory(context):
    schema = cachingInstanceSchemaFactory(context)
    schema['image'].languageIndependent = False
    return schema

