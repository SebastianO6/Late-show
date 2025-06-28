from server.app import db

class Appearance(db.Model):
    __tablename__ = 'appearance'
    id = db.Column(db.Integer, primary_key=True) 
    rating = db.Column(db.Integer, nullable=False) 
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False) 
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False) 

    __table_args__ = (
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='rating_range'),
    )

    def __repr__(self):
        return f'<Appearance Episode: {self.episode_id}, Guest: {self.guest_id}, Rating: {self.rating}>'