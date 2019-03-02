from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from .models import ProductDOC, db_connect, create_product_doc_table


class DocParserPipeline(object):

    def __init__(self):
        self.total = 0
        engine = db_connect()
        create_product_doc_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        self.total +=1
        session = self.Session()
        url = item['url']
        code = item['code']
        if code:
            products = session.query(ProductDOC).filter_by(code_1c=code).all()
            print(products)
            for p in products:
                p.url = url
                session.commit()

    def close_spider(self, spider):
        print("Итого {}".format(self.total))

