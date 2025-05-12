class Products: 
    def __init__(self):
        pass

class Opinions:
    def __init__(self, opinion_id, author, recommendation, stars, content, pros, cons, vote_yes, vote_no, publish_date, purchased_date):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.vote_yes = vote_yes
        self.vote_no = vote_no
        self.publish_date = publish_date
        self.purchased_date = purchased_date
            
    def __str__(self):
        return f""