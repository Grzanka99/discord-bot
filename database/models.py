from extensions import db, ma


class CommandsModel(db.Model):
    __tablename__ = 'commands'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cmd_name = db.Column(db.Text)
    cmd_desc = db.Column(db.Text)

    @classmethod
    def get_commands(cls):
        return cls.query.all()
