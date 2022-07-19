# task

Hey Maciek! 

During our conversation I somehow was thinking about creating a wrapper - as a decorator - but when I started coding my solution, I thought about much simple idea. I hope below resolution it's still align with what we were discussing, but if you think that I should use different approch here I can probably redo the script. 


task.py is the result of the very first idea on how to identify the correct order. I see now that the variable naming could be better, but I hope that would work for this "small" task and it's not used in the app, but I include it to present the order of thinking here.


In the repo I include, **requirements.txt** so you can use those to install all dependencies in your virual env.


The app is build using Flask and it expose below endpoint: 
/status/<order>/<email>
    
  
This endpoint takes 2 args - "order" and "email".
        
I'm handling the entire script behaviour in just 1 function

    
**Errors handling:**
    
I don't remember how Zowie is handling errors but I have 3 scenarion where only 2 should be true in some case at Zowie level:
1) If the order doesn't exist or if it doesn't match with the customer email address I'm responding with a genering "ValueError" to not give any hints to customer which parametr is exacly incorrect. This can be easily changed if needed but we didn't discuss that in details.

2) If the orgin data API is not responding.

3) If somehow we would try to access non existing endpoint that should be fetched with errorhandler 404. I guess this makes no use when using the Zowie interface as we'll be hardcoding the endpoint but it's there just in case that's not always true.


