from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Category, Item, Base

engine = create_engine('sqlite:///categorymenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#populate the Category database
Soccer = Category(name="Soccer")
session.add(Soccer)
session.commit()

Basketball = Category(name="Basketball")
session.add(Basketball)
session.commit()

Baseball = Category(name="Baseball")
session.add(Baseball)
session.commit()

Frisbee = Category(name="Frisbee")
session.add(Frisbee)
session.commit()

Snowboarding = Category(name="Snowboarding")
session.add(Snowboarding)
session.commit()

Rock_Climbing = Category(name="Rock Climbing")
session.add(Rock_Climbing)
session.commit()

Foosball = Category(name="Foosball")
session.add(Foosball)
session.commit()

Skating = Category(name="Skating")
session.add(Skating)
session.commit()

Hockey = Category(name="Hockey")
session.add(Hockey)
session.commit()

#populate the item database
Snowboard = Item(name="Snowboard", description="Best for any terrain and conditions. All-mountain snowboards perform "
                                               "anywhere on a mountain-groomed ground, backcountry, even park and pipe",
                 category=Snowboarding,
                 user_id=1,
                 user=User1)
session.add(Snowboard)
session.commit()
