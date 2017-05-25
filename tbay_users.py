from tbay import User, Item, Bid, session

#add 3 users

frodo = User(username='frodo', password='thinkful')
bilbo = User(username='bilbo', password='thinkful')
gandalf = User(username='gandalf', password='thinkful')

session.add_all([frodo, bilbo, gandalf])
session.commit()

# baseball up for auction
baseball = Item(name="David Ortiz Baseball", description="Signed by David Ortiz", seller=frodo)
session.add(baseball)
session.commit()

#each user bids twice
frodo_bid_1 = Bid(price=150, bidder=frodo, auction_item=baseball)
frodo_bid_2 = Bid(price=250, bidder=frodo, auction_item=baseball)                                                          
bilbo_bid_1 = Bid(price=50, bidder=bilbo, auction_item=baseball)
bilbo_bid_1 = Bid(price=400, bidder=bilbo, auction_item=baseball)
bilbo_bid_2 = Bid(price=600, bidder=bilbo, auction_item=baseball)                                                           
gandalf_bid_1 = Bid(price=10, bidder=gandalf, auction_item=baseball)
gandalf_bid_2 = Bid(price=50, bidder=gandalf, auction_item=baseball)

session.add_all([frodo_bid_1, frodo_bid_2, bilbo_bid_1, bilbo_bid_2, gandalf_bid_1, gandalf_bid_2])
session.commit()

#highest bid query
session.query(Bid.price).order_by(Bid.price).all()