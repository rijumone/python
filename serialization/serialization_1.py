import json
from dataclasses import dataclass, asdict
import pandas as pd
from featuretools import EntitySet, Relationship


@dataclass
class Dataclass:
    def to_json(self) -> str:
        return json.dumps(asdict(self))

@dataclass
class Price(Dataclass):
    '''Class for storing any kind of price.'''
    name: str
    price: int

@dataclass
class Holding(Dataclass):
    '''Class for keeping track of a holding in Portfolio.'''
    symbol: str
    buy_price: Price
    quantity: int
    target: float
    stoploss: float

    def to_json(self) -> str:
        return json.dumps(asdict(self))

@dataclass
class CustomEntity(Dataclass):
    entity_set: EntitySet

def main():
    holding = Holding(
        'HDFCBANK', Price('buy', 97.89), 5, 112.1, 95.4
    )
    print(holding.to_json())

    
    es = EntitySet('user').entity_from_dataframe(
        entity_id='parent', dataframe=pd.DataFrame({
            'id': [10, 14, 24, 34, 54, 64, 84, ],
            'age': [10, 14, 24, 34, 54, 64, 84, ],
            'salary': [1, 1, 10000, 25000, 50000, 60000, 80000, ]
        }))
    es.entity_from_dataframe(
        entity_id='child',  dataframe=pd.DataFrame({
            'id': [10, 14, 24, 34, 54, 64, 84, ],
            'user_id': [10, 14, 24, 34, 54, 64, 84, ],
            'sex': [0, 1, 0, 1, 1, 0, 1]
        }))
    es.add_relationship(
        Relationship(
            es['parent']['id'],
            es['child']['user_id']
        )
    )
    es.entity_from_dataframe(
        entity_id='child_0',  dataframe=pd.DataFrame({
            'id': [10, 14, 24, 34, 54, 64, 84, ],
            'user_id': [10, 14, 24, 34, 54, 64, 84, ],
            'diet': [0, 1, 0, 1, 1, 0, 1]
        }))
    es.add_relationship(
        Relationship(
            es['parent']['id'],
            es['child_0']['user_id']
        )
    )
    # print(es)
    e_s = CustomEntity(entity_set=es)
    print(e_s.to_json())

    

if __name__ == '__main__':
    main()
