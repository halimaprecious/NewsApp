
class Source:
    '''defines source class objects'''
    def __init__(self,id,name, description, language, country, url):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.country = country
        self.url = url


class Article:

    '''Defines article class objects'''
    def __init__(self,title, description,url, urlToImage, content, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt
