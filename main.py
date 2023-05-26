import requests

for i in range(1, 494):
    #493 Pokemon
    urlPattern = "https://originalstitch.com/_next/image?url=https%3A%2F%2Fos-cdn.ec-ffmt.com%2Fgl%2Fpokemon%2Fdedicate%2Fpattern-flat%2F" + str(i) + ".jpg&w=3840&q=100" #Need this to request
    urlPhoneWallpaper = "https://os-cdn.ec-ffmt.com/gl/pokemon/dedicate/wallpaper/" + str(i) +".jpg" #Phone Wallpapers?
    reqPattern = requests.get(urlPattern, allow_redirects=True) 
    reqPhoneWallpaper = requests.get(urlPhoneWallpaper, allow_redirects=True) 
    #In the future, hook it up to Bulbapedia and append the appropiate pokemon name.
    open("Pattern_"+ str(i) +".png","wb").write(reqPattern.content)
    open("PhoneWallpaper_"+str(i)+".png","wb").write(reqPhoneWallpaper.content)
