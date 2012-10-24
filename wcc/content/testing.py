from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import wcc.content


WCC_CONTENT = PloneWithPackageLayer(
    zcml_package=wcc.content,
    zcml_filename='testing.zcml',
    name="WCC_CONTENT")

WCC_CONTENT_INTEGRATION = IntegrationTesting(
    bases=(WCC_CONTENT, ),
    name="WCC_CONTENT_INTEGRATION")

WCC_CONTENT_FUNCTIONAL = FunctionalTesting(
    bases=(WCC_CONTENT, ),
    name="WCC_CONTENT_FUNCTIONAL")
