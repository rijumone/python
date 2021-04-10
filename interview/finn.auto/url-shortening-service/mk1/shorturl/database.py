import tempfile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shorturl.config import config


class DatabaseConnection:

    # db_fd, _tmp_file = tempfile.mkstemp()
    # print(_tmp_file)
    _tmp_file = config['database']['path']
    db_engine = create_engine(
        f'sqlite:///{_tmp_file}',
        # echo=True,
    )

    def get_db_session(self, ):
        return sessionmaker(bind=self.db_engine, autocommit=False)()
