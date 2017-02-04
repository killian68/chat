# -*- coding: utf-8 -*-
import pymysql
import tkinter.messagebox


class SQLretriever:

    def __init__(self, req, hos, use, pas, dat):
        self.request = req
        self.host = hos
        self.user = use
        self.password = pas
        self.database = dat

    def retrieve(self):

        try:
            dbconnector = pymysql.connect(self.host, self.user, self.password, self.database)
            self.result = dbconnector.cursor()
            self.result.execute(self.request)
            dbconnector.close()
        except Exception as err:
            tkinter.messagebox.showwarning(title='Error', message=err)
            self.result = []
        finally:
            return self.result

    def update(self):
        try:
            dbconnector = pymysql.connect(self.host, self.user, self.password, self.database)
            self.result = dbconnector.cursor()
            self.result.execute(self.request)
            self.result.close()
            dbconnector.commit()
            dbconnector.close()
        except Exception as err:
            tkinter.messagebox.showwarning(title='Error', message=err)
