import json
import os

# from flask import Flask
import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import query

from app import app
from app.models import Cart, Product, User
from app.utils.db import db

SQL_ENGINE = create_engine(os.getenv('DATABASE_URL'), client_encoding='utf8', implicit_returning=True)

def clean_data(df: pd.DataFrame):
    df = df.replace(to_replace=r'–', value='-', regex=True)
    df = df.replace(to_replace=r"’", value="'", regex=True)
    df = df.replace(to_replace=r'”', value='"', regex=True)
    return df

def insert_data(df: pd.DataFrame, tablename: str):
    app.logger.info("Inserting to database")
    df.to_sql(name=tablename, con=SQL_ENGINE, schema='public', if_exists='append', index=False, method='multi')
    app.logger.info("--------------")
    app.logger.info("")

def request_data_from_external_api(endpoint: str):
    app.logger.info("Requesting data from external api")
    return requests.get(f"{os.getenv('FAKESTORE_API')}/{endpoint}").json()

def seed_products():
    app.logger.info("--------------")
    app.logger.info("Seed Products")
    app.logger.info("")

    req = request_data_from_external_api('products')

    app.logger.info("Building dataframe and cleaning data")
    df = pd.DataFrame(req)
    df = clean_data(df)

    insert_data(df, 'products')

def seed_users():
    app.logger.info("--------------")
    app.logger.info("Seed Users")
    app.logger.info("")    

    req = request_data_from_external_api('users')

    users = list()
    user = dict()
    for r in req:
        user = r
        user['first_name'] = r['name']['firstname']
        user['last_name'] = r['name']['lastname']
        user['address'] = json.dumps(user['address'])
        del user['name']
        del user['__v']
        users.append(user)

    df = pd.DataFrame(users)

    insert_data(df, 'users')

def seed_carts():
    app.logger.info("--------------")
    app.logger.info("Seed Carts")
    app.logger.info("")
    
    req = request_data_from_external_api('carts')

    for r in req:
        r['created_at'] = r['date']
        r['user_id'] = r['userId']
        r['products'] = json.dumps(r['products'])
        del r['userId']
        del r['__v']
        del r['date']
    
    # normalize data from external api
    req[-1]['id'] = 7
    req[1]['user_id'] = 7
    req[4]['user_id'] = 5

    df = pd.DataFrame(req)

    insert_data(df, 'carts')


@app.cli.command("seed-tables")
def seed_tables():
    # TODO: run migrate before

    app.logger.info("Truncating tables")
    db.session.query(Cart).delete()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.commit()

    seed_products()
    seed_users()
    seed_carts()
