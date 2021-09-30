class Subject:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class Enclosure:
    def __init__(self, url, type, length):
        self.url = url
        self.type = type
        self.length = length

    def __str__(self):
        return f"enclosure:\n\turl: {self.url}\n\ttype: {self.type}\n\tlength: {self.length}"

class Item:
    def __init__(self, title, link, pub_date, subjects, tags, description, guid_link, enclosure):
        self.title = title
        self.link = link
        self.pub_date = pub_date
        self.subjects = subjects
        self.tags = tags
        self.description = description
        self.guid_link = guid_link
        self.enclosure = enclosure

    def __str__(self):
        if self.enclosure:
            enclosure_url = self.enclosure.url
            enclosure_type = self.enclosure.type
            enclosure_length = self.enclosure.length
        else:
            enclosure_url, enclosure_type, enclosure_length = None, None, None
        return f"title: {self.title}\n" \
               f"link: {self.link}\n" \
               f"pub_date: {self.pub_date}\n" \
               f"subjects: {', '.join([str(i) for i in self.subjects])}\n" \
               f"tags: {self.tags}\n" \
               f"description: {self.description}\n" \
               f"guid_link: {self.guid_link}\n" \
               f"enclosure:\n\turl: {enclosure_url}\n\ttype: {enclosure_type}\n\tlength: {enclosure_length}\n"


