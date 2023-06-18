# -*- coding: utf-8 -*-
"""
Функции для взаимодействия с БД

@author: kate

"""

import sqlite3


def create_tables(sql_script_path='../data/create_tables.sql', db_file_path='../data/sqlite.db'):
    """
    Создание таблиц в БД

    Parameters
    ----------
    sql_script_path : str, optional
        Путь к файлу со скриптом. The default is 'data/create_tables.sql'.
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    None.

    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        with open(sql_script_path, 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)
    finally:
        cursor.close()
        sqlite_connection.close()


def fillup_tables(sql_script_path='../data/fillup_tables.sql', db_file_path='../data/sqlite.db'):
    """
    Заполнение таблиц в БД данными из приложенного файла

    Parameters
    ----------
    sql_script_path : str, optional
        Путь к файлу со скриптом. The default is '../data/fillup_tables.sql'.
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    None.

    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        with open(sql_script_path, 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)
    finally:
        cursor.close()
        sqlite_connection.close()


def get_goods_list(db_file_path='../data/sqlite.db'):
    """
    Получение списка существующих товаров

    Parameters
    ----------
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    goods_list : list of strings
        Список существующих товаров.

    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        sql_query = "SELECT name FROM Goods"
        cursor.execute(sql_query)
        goods = cursor.fetchall()
        goods_list = [good[0] for good in goods]
    finally:
        cursor.close()
        sqlite_connection.close()
    return goods_list


def get_all_goods_info(db_file_path='../data/sqlite.db'):
    """
    Получение всей информации о существующих товарах

    Parameters
    ----------
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    goods_list : list of strings
        Список существующих товаров с описанием.

    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        sql_query = "SELECT * FROM Goods"
        cursor.execute(sql_query)
        goods = cursor.fetchall()
        goods_list = [str(good) for good in goods]
    finally:
        cursor.close()
        sqlite_connection.close()
    return goods_list

def get_item_quantity(item_name, db_file_path='../data/sqlite.db'):
    """
    Получение количества определённого товара

    Parameters
    ----------
    item_name : str
        Идентификатор товара.
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    item_quantity : int
        Количество запрошенного товара.
    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        sql_query = ("SELECT quantity FROM Goods WHERE name = '" +
                     str(item_name) + "';")
        cursor.execute(sql_query)
        item_quantity = cursor.fetchall()
        item_quantity = item_quantity[0][0]
    finally:
        cursor.close()
        sqlite_connection.close()
    return item_quantity


def set_item_quantity(item_name, new_item_quantity, db_file_path='../data/sqlite.db'):
    """
    Задание количества определённого товара

    Parameters
    ----------
    item_name : str
        Идентификатор товара.
    new_item_quantity : int
        Новое количество товара
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    
    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        sql_query = (
            "UPDATE Goods SET quantity = " + str(new_item_quantity) +
            " WHERE name = '" + item_name + "';"
            )
        cursor.execute(sql_query)
        sqlite_connection.commit()
    finally:
        cursor.close()
        sqlite_connection.close()

def add_item(item_name, item_quantity, db_file_path='../data/sqlite.db'):
    """
    Добавление нового товара с заданным количеством

    Parameters
    ----------
    item_name : str
        Идентификатор товара.
    item_quantity : int
        Количество нового товара
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    
    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        sql_query = (
            "INSERT INTO Goods (name, quantity) VALUES ('" +
            str(item_name) + "', '" + str(item_quantity) + "')"
            )
        cursor.execute(sql_query)
        sqlite_connection.commit()
    finally:
        cursor.close()
        sqlite_connection.close()

def delete_item(item_name, db_file_path='../data/sqlite.db'):
    """
    Удаление товара

    Parameters
    ----------
    item_name : str
        Идентификатор товара.
    db_file_path : str, optional
        Путь к файлу с БД. The default is '../data/sqlite.db'.

    Returns
    -------
    
    """
    try:
        sqlite_connection = sqlite3.connect(db_file_path)
        cursor = sqlite_connection.cursor()
        sql_query = (
            "DELETE FROM Goods WHERE name = '" + str(item_name) + "'"
            )
        cursor.execute(sql_query)
        sqlite_connection.commit()
    finally:
        cursor.close()
        sqlite_connection.close()
