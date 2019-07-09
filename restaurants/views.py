from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" :[
   		#Restaurant 1
    	{
    	  "restaurant_name" : "Wahid Falafel",
    	  "food_type" : "Middle Eastern cuisine"
    	},
		#Restaurant 2
    	{
    	  "restaurant_name" : "Katsuya",
    	  "food_type" : "Asian Fusion"
    	},
    	#Restaurant 3
    	{
    	  "restaurant_name" : "Pizza Express",
    	  "food_type" : "Italian cuisine"
    	},

    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {
    	#Restaurant Detail
    	  "restaurant_name" : "McDonald's",
    	  "food_type" : "Burgers"
    	
    	}

    }
    return render(request, 'detail.html', context)
