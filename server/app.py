#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    all_bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]
    response = make_response(all_bakeries, 200)
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    bakery_dict = bakery.to_dict()
    response = make_response(bakery_dict, 200)
    
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    by_price = sorted(BakedGood.query.all(), key=lambda b: b.price)
    baked_good_dicts = [b.to_dict() for b in by_price]
    response = make_response(baked_good_dicts, 200)

    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive = sorted(BakedGood.query.all(), key=lambda b: b.price, reverse=True)[0].to_dict()
    response = make_response(most_expensive, 200)
    
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
