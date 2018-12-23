# AutoTinder <img src="https://user-images.githubusercontent.com/12884292/50386865-98662d80-06f8-11e9-881f-285d04dbeb19.png" width="30" height="30">


Python based Tinder automation script, created to solve mankind's most important need. <br/>
**Includes**: Tinder Data Creation Tool, Automation script.<br/>
## Automation Process Log:
Firstly, I created the tool using the Tinder API, PyQt5 and some other libraries like pandas. The generated data was an actual representation of final test input. However, initially my data was about 500 images and was imbalanced. Roughly 380 likes. So I actually generated about 1500 images and it turned out I had a lot of dislikes in these images ultimately balancing the dataset. Now I connected the Uploaded the Images to Azure's CustomVision platform because right off the bat I can use their transfer learning model (General) and get prediction API URL. I wrote the autotinder.py script to direct the image URL from the Tinder API's recommendation call to CustomVision's Prediction API call and got a like or dislike response. I then used the Tinder API to register the like/dislike call.
But I was not done yet, this could be automated even more. Instead of me running the script manually every 12 hours or so, wouldn't it be great if the script ran automatically after every 12 hours (time taken to regenerate likes). I was able to achieve this through Azure's WebJobs. This was a little bit tricky as I had to bundle the required libraries with the script.
## Azure's CustomVision Results
![image](https://user-images.githubusercontent.com/12884292/50387252-8daf9680-0700-11e9-9eb3-5d52ff8b546e.png)
There were a lot of images where it was borderline like/dislike, on top of that group selfies made it even more problematic and the good old useless images of animals and memes had to be disliked. Their general Model doesn't specifically recognize faces, which in addition to the previously mentioned reasons explains the results.

## Azure Webjobs automation ScreenCaptures
![image](https://user-images.githubusercontent.com/12884292/50387303-5ee5f000-0701-11e9-9caf-4a91c43626f1.png)
![image](https://user-images.githubusercontent.com/12884292/50387305-7329ed00-0701-11e9-9516-170e3d6bb2b7.png)
![image](https://user-images.githubusercontent.com/12884292/50387308-8341cc80-0701-11e9-96cb-c97efd30a916.png)



## Programs Used
> * Azure WebJobs
> * [Azure CustomVision](https://www.customvision.ai)
> * [TinderAPI](https://github.com/fbessez/Tinder)
  I got to know there is another cool API that you can use [Pynder](https://github.com/charliewolf/pynder)

## Dependencies
> * python 3.6
> * requests
> * robobrowser
> * BeautifulSoup4
> * lxml
> * PyQt5 

## Running AutoTinder
```
$ python main.py
```

## Running AutoTinder Data Creation Tool
```
$ python tindertool.py
```
__Instructions__
>  - Login with your Facebook Credentials
>  - Select on Generate Data Tab and select preferences.
>  - Click on Generate Data as many times as you wish before you get rate limited or wipe the data of your locality.
>  - Click on Label Data and have fun labeling 
![image](https://user-images.githubusercontent.com/12884292/50387067-cbaabb80-06fc-11e9-95fc-f87fedc95893.png)
![image](https://user-images.githubusercontent.com/12884292/50387121-9eaad880-06fd-11e9-80d5-0b066fbc9cd2.png)

## Future Work
> Train on VGG-Face Model to get better results.

## Credits
> * https://soundcloud.com/theaipodcast/ai-tinder-dating
> * https://github.com/fbessez/Tinder
> * https://github.com/philipperemy/Deep-Learning-Tinder
