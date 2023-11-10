from db import Db

global main_win_created
main_win_created = False

global add_win_created
add_win_created = False

global gold_win_created
gold_win_created = False

global id_category
id_category = int()

global id_word
id_word = int()

global win_show 
win_show = False

d = Db()

def insert_category_to_db(data):
    d.insert_category(data)

def get_categories():
    data = d.select_all_category()
    return data

def delete_category_by_id(id):
    d.delete_category_by_id(id)

def insert_word_to_db(data):
    global id_word
    id_word = d.insert_word(data)

def insert_verb_to_db(data):
    global id_word
    data[0] = id_word
    d.insert_verb(data)

def count_libox_records():
    count = d.count_libox()
    return count

#select_words_from_t-word_that_is_not_in_libox
def select_words_id_for_libbox():
    data = d.select_words_id_for_libox()
    return data

def insert_word_to_libox(id):
    d.inser_word_to_libox(id)

def select_libox_id():
    data = d.select_libox()
    return data

def update_state_T_word(id):
    d.update_word_state(id)

def select_word_by_id(id):
    data = d.select_one_word(id)
    return data

#update state and level of libox tabel
def update_libox(id,level):
    d.update_libox(id,level)

def get_id_by_name(name):
    return d.get_id(name)

def get_verb_forms(id):
    return d.get_verb_forms(id)

#set gold coulmn = 1 in word table and delete it from libox table
def set_word_gold(id):
    d.set_gold(id)

def get_word_type(id):
    return d.get_word_type(id)

def insert_future_word(word):
    d.insert_future_word(word)

def select_all_future_word():
    data = d.select_future_word()
    return data

def delete_future_word(word):
    d.delete_future_word(word)

def data_for_statistics():
    data = d.get_data_for_statistics()
    return data  

def select_all_gold_words():
    data = d.select_all_golds()
    return data   

def reset_database():
    d.delete_all_libbox_recordes()



