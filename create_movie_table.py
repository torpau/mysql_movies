from data.db import Base, engine
from data.models.movies import *

def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
