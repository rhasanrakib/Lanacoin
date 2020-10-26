from django.shortcuts import render

def home_view(request):
    top_news = [
        {
            'title': 'Land grab.',
            'sub_title':"Strong march in Entre Ríos after Etchevehere's complaint",
            'details':'''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title':"The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title':"The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/3449885h186.webp',
        },
        
    ]
    top_news_lower=[
        {
            'title': 'Land grab.',
            'sub_title':"Strong march in Entre Ríos after Etchevehere's complaint",
            'details':'''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title':"The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title':"The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/3449885h186.webp',
        },
        {
            'title': 'Land grab.',
            'sub_title':"Strong march in Entre Ríos after Etchevehere's complaint",
            'details':'''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title':"The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title':"The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo':'images/3449885h186.webp',
        },
        
        

    ]
    return render(request,'home_page.html',{'top_news':top_news,'top_news_lower':top_news_lower,'more_news':top_news_lower,'other_theme':top_news_lower,'interest':top_news_lower,'most_read':top_news_lower})

def politics_view(request):
    lst=[
        {
            'category':'news',
            'title':''' The minimum wage will increase by 28%, far from the expectations of the unions ''',
            'topic':'present',
            'date':'october 14,2020',
            'cover_pic':'images/3275561h134.jpg',
        },
        {
            'category':'comment',
            'title':''' Argentina consecrates the myopia of Nodio observers  ''',
            'topic':'present',
            'date':'october 14,2020',
            'reporter':'Diego Cabot',
            'pro_pic':'images/3275561h134.jpg',
        },
        {
            'category':'news',
            'title':''' The minimum wage will increase by 28%, far from the expectations of the unions ''',
            'topic':'present',
            'date':'october 14,2020',
            'cover_pic':'images/3275561h134.jpg',
        },
        {
            'category':'comment',
            'title':''' Argentina consecrates the myopia of Nodio observers  ''',
            'topic':'present',
            'date':'october 14,2020',
            'reporter':'Diego Cabot',
            'pro_pic':'images/3275561h134.jpg',
        },
        {
            'category':'comment',
            'title':''' Argentina consecrates the myopia of Nodio observers  ''',
            'topic':'present',
            'date':'october 14,2020',
            'reporter':'Diego Cabot',
            'pro_pic':'images/3275561h134.jpg',
        },
    ]
    more=[
        {
            'title':'''Argentina consecrates the myopia of Nodio observers''',
            'cover_pic':'images/3275561h134.jpg',
        },
        {
            'title':'''Argentina consecrates the myopia of Nodio observers''',
            'cover_pic':'images/3275561h134.jpg',
        },
        {
            'title':'''Argentina consecrates the myopia of Nodio observers''',
            'cover_pic':'images/3275561h134.jpg',
        },
    ]
    return render(request,'politics.html',{'data':lst,'more':more})