import os

# from flask import Flask
import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import query

from app import app
from app.models import Product
from app.utils.db import db

SQL_ENGINE = create_engine(os.getenv('DATABASE_URL'), client_encoding='utf8', implicit_returning=True)

def clean_data(df: pd.DataFrame):
    df = df.replace(to_replace=r'–', value='-', regex=True)
    df = df.replace(to_replace=r"’", value="'", regex=True)
    df = df.replace(to_replace=r'”', value='"', regex=True)
    return df

def seed_products():
    app.logger.info("--------------")
    app.logger.info("Seed Products")
    app.logger.info("")

    db.session.query(Product).delete()
    app.logger.info("Truncating table")
    db.session.commit()

    app.logger.info("Requesting data from external api")
    req = requests.get(f"{os.getenv('FAKESTORE_API')}/products").json()

    app.logger.info("Building dataframe and cleaning data")
    df = pd.DataFrame(req)
    df = clean_data(df)

    app.logger.info("Inserting to database")
    df.to_sql(name='products', con=SQL_ENGINE, schema='public', if_exists='append', index=False, method='multi')
    app.logger.info("--------------")

def seed_users():
    pass

def seed_categories():
    pass


@app.cli.command("seed-tables")
def seed_tables():
    seed_products()
    seed_categories()
    seed_users()