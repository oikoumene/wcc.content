from plone.app.layout.viewlets.common import LogoViewlet as BaseLogoViewlet
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class FooterTextViewlet(ViewletBase):

    index = ViewPageTemplateFile('footer_text.pt')

    def value(self):
        field = self.context.getField('footer_text')
        if field:
            return field.get(self.context)
        return ''
