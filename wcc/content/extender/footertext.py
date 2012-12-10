from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.public import TextField
from five import grok
from archetypes.schemaextender.interfaces import ISchemaExtender
from plone.app.collection.interfaces import ICollection
from Products.ATContentTypes.interfaces.topic import IATTopic
from Products.Archetypes.atapi import AnnotationStorage
from Products.Archetypes.atapi import RichWidget
from Products.ATContentTypes.configuration import zconf
from wcc.content import MessageFactory as _

class ExtensionTextField(ExtensionField, TextField):
    pass



class CollectionAdapter(grok.Adapter):
    grok.context(ICollection)
    grok.implements(ISchemaExtender)

    fields = [
        ExtensionTextField('footer_text',
            required=False,
            searchable=True,
            storage=AnnotationStorage(migrate=True),
            validators=('isTidyHtmlWithCleanup',),
            default_output_type='text/x-html-safe',
            default='<p></p>',
            widget=RichWidget(
                        description='',
                        label=_(u'label_footer_text', default=u'Footer Text'),
                        rows=25,
                        allow_file_upload=zconf.ATDocument.allow_document_upload),
        )
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields


class TopicAdapter(CollectionAdapter):
    grok.context(IATTopic)
