gender=db.Column(db.String(50))
    add_proof=db.Column(db.String(50),primary_key=False)
    card_type=db.Column(db.String(50),primary_key=True)
    expiry=db.Column(db.String,primary_key=False)
    address=db.Column(db.String(2000),nullable=False)
    date_created=db.