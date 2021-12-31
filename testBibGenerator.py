from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
if __name__ == '__main__':
    db = BibDatabase()
    db.entries = [
        {'journal': 'Nice Journal',
         'comments': 'A comment',
         'pages': '12--23',
         'month': 'jan',
         'abstract': 'This is an abstract. This line should be long enough to test\nmultilines...',
         'title': 'An amazing title',
         'year': '2013',
         'volume': '12',
         'ID': 'Cesar2013',
         'author': 'Jean César',
         'keyword': 'keyword1, keyword2',
         'ENTRYTYPE': 'article'}]

    writer = BibTexWriter()
    with open('./data/bibtex.bib', 'w', encoding='utf-8') as bibfile:
        bibfile.write(writer.write(db))