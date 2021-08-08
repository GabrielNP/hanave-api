import json
import os

# from flask import Flask
import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import query

from app import app
from app.models import Product, User
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

    db.session.query(Product).delete()
    app.logger.info("Truncating table")
    db.session.commit()

    req = request_data_from_external_api('products')

    app.logger.info("Building dataframe and cleaning data")
    df = pd.DataFrame(req)
    df = clean_data(df)

    insert_data(df, 'products')

def seed_users():
    app.logger.info("--------------")
    app.logger.info("Seed Users")
    app.logger.info("")

    db.session.query(User).delete()
    app.logger.info("Truncating table")
    db.session.commit()

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

def seed_categories():
    pass


@app.cli.command("seed-tables")
def seed_tables():
    seed_products()
    seed_categories()
    seed_users()
