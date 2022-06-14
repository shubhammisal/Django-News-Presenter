from django.shortcuts import render
from newsapi import NewsApiClient
from datetime import date
from news.forms import newsForm

def index(request):
	newsapi = NewsApiClient(api_key ='API KEY')
	S='NDTV News,India TV News,the-times-of-india,India Today'
    
	if request.method == 'POST':
		form  = newsForm(request.POST)
		from_date=form['from_date'].value()
		to_date=form['to_date'].value()

		top =newsapi.get_everything(
                                sources=S,
                                from_param=from_date,
                                to=to_date,
                                language='en',
                                
                                page=2)
		l = top['articles']
		desc =[]
		news =[]
		img =[]
		publishedAt=[]
		author=[]
		for i in range(len(l)):
			f = l[i]
			news.append(f['title'])
			desc.append(f['description'])
			img.append(f['urlToImage'])
			publishedAt.append(f['publishedAt'])
			author.append(f['author'])
		mylist = zip(news, desc, img, publishedAt,author)

		return render(request, 'news/index.html', context ={"mylist":mylist,'form':form})

	else:
		
		top =newsapi.get_everything(
									sources=S,
									from_param=date.today(),
									to=date.today(),
									language='en',
									sort_by='relevancy',
									page=2)
		l = top['articles']
		desc =[]
		news =[]
		img =[]
		publishedAt=[]
		author=[]
		for i in range(len(l)):
			f = l[i]
			news.append(f['title'])
			desc.append(f['description'])
			img.append(f['urlToImage'])
			publishedAt.append(f['publishedAt'])
			author.append(f['author'])
		mylist = zip(news, desc, img, publishedAt,author)
		form=newsForm()
		return render(request, 'news/index.html', context ={"mylist":mylist,'form':form})
