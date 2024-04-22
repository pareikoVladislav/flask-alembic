from extensions import db


class Victims(db.Model):
    __tablename__ = 'victims'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"{self.title}"

    def save(self):
        db.session.add()
        db.session.commit()

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        db.session.commit()
