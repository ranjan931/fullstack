from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    intensity = Column(Integer, nullable=False)
    likelihood = Column(Integer, nullable=False)
    relevance = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    country = Column(String, nullable=True)
    topics = Column(String, nullable=True)
    region = Column(String, nullable=True)
    city = Column(String, nullable=True)

# Ensure you replace 'sqlite:///your_database.db' with your actual database URL
engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

data_list = [
    {'region': 'Northern America', 'relevance': 2, 'intensity': 6, 'city': '', 'year': 0, 'country': 'United States of America', 'topics': '', 'likelihood': 3},
    {'region': 'Northern America', 'relevance': 2, 'intensity': 6, 'city': '', 'year': 0, 'country': 'United States of America', 'topics': '', 'likelihood': 3},
    {'region': 'Northern America', 'relevance': 2, 'intensity': 6, 'city': '', 'year': 0, 'country': 'United States of America', 'topics': '', 'likelihood': 3},
    {'region': 'Central America', 'relevance': 3, 'intensity': 6, 'city': '', 'year': 0, 'country': 'Mexico', 'topics': '', 'likelihood': 2},
    {'region': 'World', 'relevance': 2, 'intensity': 6, 'city': '', 'year': 0, 'country': '', 'topics': '', 'likelihood': 3},
    # Add more data as needed...
]

# Function to safely convert values to integers
def safe_int(value, default=0):
    try:
        return int(value)
    except ValueError:
        return default

for data in data_list:
    data_record = Data(
        intensity=safe_int(data.get('intensity', 0)),
        likelihood=safe_int(data.get('likelihood', 0)),
        relevance=safe_int(data.get('relevance', 0)),
        year=safe_int(data.get('year', 0)),
        country=data.get('country', ''),
        topics=data.get('topics', ''),
        region=data.get('region', ''),
        city=data.get('city', '')
    )
    session.add(data_record)

try:
    session.commit()
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
