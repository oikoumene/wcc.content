from Products.ATContentTypes import permission as atct

packageName = 'wcc.content'

permissions = {
    'TranslatableImage': atct.permissions.get('Image'),
    'TranslatableFile': atct.permissions.get('File')
}
