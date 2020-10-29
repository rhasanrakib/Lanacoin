from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home_view,name="home"),
    path('politics/',views.politics_view,name="politics"),
    path('transit/',views.last_news_transit_view,name="transit"),
    path('data/',views.last_news_data_view,name="data"),
    path('dollar-today/',views.economy_dollar_today_view,name="dollar_today"),
    path('properties/',views.economy_properties_view,name="properties"),
    path('foregin-trade/',views.economy_foregin_trade_view,name="foregin_trade"),
    path('autos/',views.economy_autos_view,name="autos"),
    path('world/',views.the_world_view,name="world"),
    path('buenos-aires/',views.society_buenos_aires_view,name="buenos_aires"),
    path('security/',views.society_security_view,name="security"),
    path('education/',views.society_education_view,name="education"),
    path('culture/',views.society_culture_view,name="culture"),
    path('health/',views.society_health_view,name="health"),
    path('science/',views.society_science_view,name="science"),
    path('editorial/',views.opinion_editorial_view,name="editorial"),
    path('football/',views.sports_football_view,name="football"),
    path('rugby/',views.sports_rugby_view,name="rugby"),
    path('tennis/',views.sports_tennis_view,name="tennis"),
    path('fashion/',views.lifestyle_fashion_view,name="fashion"),
    path('tourism/',views.lifestyle_tourism_view,name="tourism"),
    path('technology/',views.lifestyle_technology_view,name="technology"),
    path('magazine/',views.print_edition_magazine_view,name="magazine"),
    path('saturday/',views.print_edition_saturday_view,name="saturday"),
    path('ideas/',views.print_edition_ideas_view,name="ideas"),
    path('readers-letter/',views.print_edition_readers_letter_view,name="readers_letter"),
    
    path('article/',views.article_view,name="article"),
]
