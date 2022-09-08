from main import Item, db

db.create_all()

iphone12 = Item(name="Iphone 12", serial_number='2321111111', price=999,
                            description="The iPhone is a smartphone made by Apple that combines a computer, iPod, digital camera and cellular phone into one device with a touchscreen interface.")

macbook_air = Item(name="MacBook Air M1", serial_number='2232223564', price=1999, 
                                description="MacBook Air is a thin, lightweight laptop from Apple. Because it is a full-sized notebook but only weighs three pounds, the laptop falls into a category that vendors are currently calling 'ultraportable.")


# To filter by 
# for item in Item.query.filter_by(name="Iphone"):
#     item.name

db.session.add(iphone12)
db.session.commit()

db.session.add(macbook_air)
db.session.commit()


