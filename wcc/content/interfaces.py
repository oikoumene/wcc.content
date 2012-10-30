from zope.interface import Interface
from Products.ATContentTypes.interfaces.image import IATImage
from Products.ATContentTypes.interfaces.file import IATFile

class IProductSpecific(Interface):
    pass

class ITranslatableImage(IATImage):
    pass

class ITranslatableFile(IATFile):
    pass
