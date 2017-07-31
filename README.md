### /game/ 
shows all the targets and images

### /game/entrance

**GET method**  
randomly choose 2 pairs of target and image
the format is shown below:

```
{"imageUser": "static/game/images/003_5JcHWYV.jpeg",  

"imageOpponent": "static/game/images/001_8m38uYl.jpeg",  

"targetOpponent": "duck",  

"targetUser": "fan"}

```

**POST method**  
returns the array containing the coordinates representing a stroke  

```
{"stroke": [0, 1, 2, 3, 4]}
```

### /game/over
Redirects to /game/entrance

### /game/admin
The administrator page provided by Django.   
Provides a view of all available target texts and images.  

login with  
UserName:admin  
Password:default1234  
