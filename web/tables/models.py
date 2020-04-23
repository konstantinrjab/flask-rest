from app import db


class Table(db.Model):
    __tablename__ = 'tables'

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, creator_id):
        self.creator_id = creator_id

    def __repr__(self):
        return '<Table %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'creator_id': self.creator_id
        }
