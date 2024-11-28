class TravelBlog:
    total_blogs: int = 0


tb1 = TravelBlog ()
tb1.name = 'Франция'
tb1.days = 6

TravelBlog.total_blogs += 1

tb2 = TravelBlog ()
tb2.name = 'Греция'
tb2.days = 10

TravelBlog.total_blogs += 1

