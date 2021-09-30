from bs4 import BeautifulSoup
import requests

from item_class import Enclosure, Item, Subject
from database import add_enclosure, add_item, add_subjects, add_full_info

URL = 'https://1prime.ru/export/rss2/index.xml'


def parse():
    soup = BeautifulSoup(requests.get(URL).text, 'xml')
    all_items = soup.find_all('item')
    print_first(all_items[0])
    class_items = []
    for item in all_items:
        try:
            try:
                tags = item.find('tags').text
            except AttributeError:
                tags = ""
            guid = item.find('guid')
            enclosure = item.find('enclosure')
            upload_to_database(item, guid, tags, enclosure)
            class_items.append(make_class_item(item, guid, tags, enclosure))
            print(class_items)
        except Exception as e:
            print(e)
        continue
    for i in class_items:
        print(i)


def make_class_item(item, guid, tags, enclosure):
    class_enclosure = Enclosure(url=enclosure.get('url'),
                                type=enclosure.get('type'),
                                length=enclosure.get('length'))
    class_subjects = []
    for i in item.find_all('dc:subject'):
        class_subject = Subject(text=i.text)
        class_subjects.append(class_subject)
    class_item = Item(title=item.title.text,
                      link=item.link.text,
                      pub_date=item.find('pubDate').text,
                      subjects=class_subjects,
                      tags=tags,
                      description=item.find('description').text,
                      guid_link=guid.text,
                      enclosure=class_enclosure)
    return class_item


def upload_to_database(item, guid, tags, enclosure):
    temp = []
    id_enclosure = add_enclosure(enclosure.get('url'), enclosure.get('type'), enclosure.get('length'))
    id_item = add_item(item.title.text, item.link.text, item.find('pubDate').text, tags,
                       item.find('description').text, guid.text, id_enclosure)
    for i in item.find_all('dc:subject'):
        id_subject = add_subjects(i.text)
        temp.append(id_subject)
    for i in temp:
        add_full_info(id_item, i)


def print_first(item):
    try:
        tags = item.find('tags').text
    except AttributeError:
        tags = ""
    guid = item.find('guid')
    enclosure = item.find('enclosure')
    class_subjects = []
    for i in item.find_all('dc:subject'):
        class_subjects.append(i.text)
    print(f"First item of data:\n"
          f"title: {item.title.text}\n"
          f"link: {item.link.text}\n"
          f"pubDate: {item.find('pubDate').text}\n"
          f"subjects: {class_subjects}\n"
          f"tags: {tags}\n"
          f"description: {item.find('description').text}\n"
          f"guid_link: {guid.text}\n"
          f"enclosure:\n"
          f"\turl: {enclosure.get('url')}\n"
          f"\ttype: {enclosure.get('type')}\n"
          f"\tlength: {enclosure.get('length')}\n")
