from datetime import date
import sqlite3
import os.path
from typing import Coroutine

class Db():
    def __init__(self):
        self.df()
        self.check_db()
        self.check_app_date()

    def check_db(self):
        if not os.path.isfile('i2.db'):
            conn = sqlite3.connect('i2.db')
            c = conn.cursor()

            c.execute("""CREATE TABLE T_category (
                category_id INTEGER PRIMARY KEY ,
                name text NOT NULL,
                description text
                ) """)

            c.execute("""CREATE TABLE T_word (

                word_id INTEGER PRIMARY KEY ,
                category_id integer NOT NULL,

                word text NOT NULL,
                role integer NOT NULL,

                app1 text,
                app2 text,
                app3 text,
                examples_app1 text,
                examples_app2 text,
                examples_app3 text,

                examples text,

                state integer NOT NULL,
                gold integer NOT NULL,
                type integer NOT NULL
                ) """)

            c.execute("""CREATE TABLE T_libox (
                word_id integer NOT NULL,
                level integer NOT NULL,
                state integer NOT NULL
                ) """)

            c.execute("""CREATE TABLE T_verb (
                word_id integer NOT NULL,

                third_person text NOT NULL,
                past_simple text NOT NULL,
                past_participle text NOT NULL,
                ing text NOT NULL
                ) """)

            c.execute("""CREATE TABLE date (
                li_date text NOT NULL
                ) """)

            c.execute("""CREATE TABLE future_word_T (
                word text NOT NULL
                ) """)

            conn.commit()
            conn.close()

    def df(self):
        conn = sqlite3.connect('i2.db')
        c = conn.cursor()
        
        conn.commit()
        conn.close()
    def check_app_date(self):
        conn = sqlite3.connect('i2.db')
        c = conn.cursor()

        today = date.today()
        d1 = today.strftime("%d")
        c.execute("SELECT li_date FROM date")
        li_d = c.fetchone()
        if li_d == None :
            c.execute( f"INSERT INTO date (li_date) VALUES ('{d1}')")
        elif li_d[0] != d1:
            c.execute("UPDATE date SET li_date=:d1 WHERE li_date=:li_d",{'d1':d1,'li_d':li_d[0]})
            c.execute("UPDATE T_libox SET state =1")

        conn.commit()
        conn.close()

#execute_sql() run all sql commands
#The only way to interact with db
    def execute_sql(self,command):
        conn = sqlite3.connect('i2.db')
        c = conn.cursor()

        if command[0:6] == "SELECT":
            c.execute(command)
            result = c.fetchall()
            return result
        else:
            c.execute(command)

        conn.commit()
        conn.close()

    def insert_word(self,data):
        conn = sqlite3.connect('i2.db')
        c = conn.cursor()

        word = [data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],0,0,data[10]]

        command  = '''INSERT INTO T_word  (category_id,word,role,app1,app2,app3,examples_app1,examples_app2,examples_app3,examples,state,gold,type)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

        #command = f"INSERT INTO T_word (category_id,word,role,app1,app2,app3,examples_app1,examples_app2,examples_app3,examples,state,gold,type) VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}','{str(data[6])}','{data[7]}','{data[8]}','{data[9]}','{0}','{0}','{data[10]}')"
        #self.execute_sql(command,word)

        c.execute(command,word)
        conn.commit()
        conn.close()
        
        command = "SELECT * FROM T_word ORDER BY word_id DESC LIMIT 1"
        word = self.execute_sql(command)
        return word[0][0]
        #category_id = data[0]
        #word = data[1]
        #role = data[2]
        #app1 = data[3]
        #app2 = data[4]
        #app3 = data[5]
        #examples_app1 = data[6]
        #examples_app2 = data[7]
        #examples_app3 = data[8]
        #examples = data[9]
        #state = data[10]
        #gold = data[11]
        #type = data[12]

    def insert_verb(self,data):
        command = f"INSERT INTO T_verb (word_id,third_person,past_simple,past_participle,ing) VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}')"
        self.execute_sql(command)
    
    def insert_category(self,data):
        command = f"INSERT INTO T_category (name,description) VALUES ('{data[0]}','{data[1]}')"
        self.execute_sql(command)

    def select_all_category(self):
        command = "SELECT category_id,name FROM T_category"
        data = self.execute_sql(command)
        return data

    def delete_category_by_id(self,id):
        command = f"DELETE FROM T_category WHERE category_id='{id}'"
        self.execute_sql(command)

    # def insert_verb(self,data):
    #     command = f"INSERT INTO T_verb (word_id,third_person,past_simple,past_participle,ing) VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}')"
    #     self.execute_sql(command)

    def count_libox(self):
        command = "SELECT COUNT(*) FROM T_libox"
        count = self.execute_sql(command)
        return count[0][0]

    def select_words_id_for_libox(self):
        command = "SELECT word_id FROM T_word WHERE state=0 AND gold=0"
        data = self.execute_sql(command)
        return data

#insert word to libox by word_id
    def inser_word_to_libox(self,id):
        command = f"INSERT INTO T_libox (word_id,level,state) VALUES ('{id}','{0}','{1}')"
        self.execute_sql(command)

#update state = 1 where state = 0 in word table
    def update_word_state(self,id):
        command = f"UPDATE T_word SET state=1 WHERE word_id='{id}'"
        self.execute_sql(command)

#get recordes from libox where state = 1
    def select_libox(self):
        command = "SELECT * FROM T_libox WHERE state= 1"
        data = self.execute_sql(command)
        return data

#get one word by id
    def select_one_word(self,id):
        command = f"SELECT word,role,app1,app2,app3,examples_app1,examples_app2,examples_app3,examples FROM T_word WHERE word_id='{id}'"
        data = self.execute_sql(command)
        return data

#update state and level of libox tabel
    def update_libox(self,id,level):
        command = f"UPDATE T_libox SET state=0 ,level='{level}' WHERE word_id='{id}'"
        self.execute_sql(command)
    
#get id by name from word table
    def get_id(self,name):
        command = f"SELECT word_id FROM T_word WHERE word='{name}'"
        return self.execute_sql(command)

#select all from verb table by id
    def get_verb_forms(self,id):
        command = f"SELECT third_person,past_simple,past_participle,ing FROM T_verb WHERE word_id='{id}'"
        return self.execute_sql(command)

#set a word gold and delete from libox table
    def set_gold(self,id):
        command = f"UPDATE T_word SET gold=1 WHERE word_id='{id}'"
        self.execute_sql(command)
        command = f"DELETE FROM T_libox WHERE word_id='{id}'"
        self.execute_sql(command)

    def get_word_type(self,id):
        command = f"SELECT type FROM T_word WHERE word_id='{id}'"
        return self.execute_sql(command)

    def insert_future_word(self,word):
        command = f"INSERT INTO future_word_T (word) VALUES ('{word}')"
        self.execute_sql(command)
    
    def select_future_word(self):
        command = "SELECT * FROM future_word_T"
        return self.execute_sql(command)
    
    def delete_future_word(self,word):
        command = f"DELETE FROM future_word_T WHERE word='{word}'"
        self.execute_sql(command)

    def get_data_for_statistics(self):
        command = f"SELECT COUNT(word_id) FROM T_word"
        allwords = self.execute_sql(command)
        command = f"SELECT COUNT(CASE gold when '1' then 1 else null end) FROM T_word"
        goldwords = self.execute_sql(command)
        command = f"SELECT COUNT(CASE state when '1' then 1 else null end) FROM T_libox"
        wating_words = self.execute_sql(command)

        data = [allwords[0][0],goldwords[0][0],wating_words[0][0]]
        return data

    def select_all_golds(self):
        command = "SELECT word FROM T_word WHERE gold= 1"
        return self.execute_sql(command)
        
    def delete_all_libbox_recordes(self):
        command = "DELETE  FROM T_libox"
        self.execute_sql(command)
        command = "UPDATE T_word SET state=0 ,gold=0 WHERE state=1"
        self.execute_sql(command)


#d1 = Db()
#data = [1,"por","good/",'ssd','',"app1 examples",'','app2_examples he order me','','']
#data = [1,'orders','ordered','ordered','ordering']

