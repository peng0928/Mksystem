# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


# 连接数据库


def dbHandle():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="521014",
        charset="utf8",
        database='mk',
        use_unicode=False
    )
    return conn


class MkspidePipeline:
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("""select * from mkapp01_c_data where title= %s""", item['title'])
        # 是否有重复数据
        repetition = cursor.fetchone()
        # 重复
        if not repetition:
            # 插入数据库
            sql = "INSERT INTO mkapp01_c_data(mark,people,title,url,text_data) VALUES(%s,%s,%s,%s,%s)"
            try:
                cursor.execute(sql,
                               (item['mark'], item['people'], item['title'], item['url'], item['text_data']))
                cursor.connection.commit()
            except BaseException as e:
                print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
                dbObject.rollback()
            return item
        cursor.close()
        dbObject.close()
