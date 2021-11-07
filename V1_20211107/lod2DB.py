from ConfigAPI.core import app, DB
import logging
import traceback



class Log(DB.Model):
    __tablename__ = 'logs'
    id = DB.Column(DB.Integer, primary_key=True) # auto incrementing
    logger = DB.Column(DB.String(100)) # the name of the logger. (e.g. myapp.views)
    level = DB.Column(DB.String(100)) # info, debug, or error?
    trace = DB.Column(DB.String(4096)) # the full traceback printout
    msg = DB.Column(DB.String(4096)) # any custom log you may have included
    created_at = DB.Column(DB.DateTime, default=DB.func.now()) # the current timestamp

    def __init__(self, logger=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])


class SQLAlchemyHandler(logging.Handler):

    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc() ##CHANGE HERE, removed exc parameter
        log = Log(
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg'],)
        DB.session.add(log)
        DB.session.commit()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = SQLAlchemyHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

loggers = [logger, app.logger, logging.getLogger('sqlalchemy'), logging.getLogger('flask.app')]

for l in loggers:
    l.addHandler(ch)

#DB.create_all()
