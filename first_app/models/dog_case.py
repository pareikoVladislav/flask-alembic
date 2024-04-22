from extensions import db


class DogCaseModel(db.Model):
    __tablename__ = 'dog_cases'

    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(45), nullable=False)
    evidence_id = db.Column(db.Integer, db.ForeignKey('evidence.id'))
    victims_id = db.Column(db.Integer, db.ForeignKey('victims.id'))
    seriousness = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())

    evidence = db.relationship('Evidence', backref='dog_cases')
    victims = db.relationship('Victims', backref='victims')

    def __repr__(self):
        return f"Incident '{self.case_type}'"

    def save(self):
        db.session.add()
        db.session.commit()

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        db.session.commit()
