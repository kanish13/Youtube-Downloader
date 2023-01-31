import pafy
a_v=int(input("You want the video in MP4 or in MP3 format: 1.MP4 2.MP3:"))
if a_v==1:
    s_b=int(input("You want to download the single file or multiple file: 1.SINGLE 2.MULTIPLE:"))
    if s_b==1:
        url=input("Enter the complete URL of the video:")
        video=pafy.new(url)
        best=video.getbest()
        print(video.title)
        best.download()
        print("Video downloaded successfully")
    elif s_b==2:
        file_name=input("Enter the file name:")
        file=open(file_name,"r")
        for line in file:
            url=line
            try:
                video=pafy.new(url)
                best=video.getbest()
                print(video.title)
                best.download()
            except:
                pass
        file.close()
elif a_v==2:
    s_b=int(input("You want to download the single file or multiple file: 1.SINGLE 2.MULTIPLE:"))
    if s_b==1:
        url=input("ENter the complete URL of the video")
        video=pafy.new(url)
        best=video.getbestaudio()
        best.download()
        print("Video downloaded successfully")
    elif s_b==2:
        file_name=input("Enter the file name:")
        file=open(file_name,"r")
        for line in file:
            url=line
            try:
                video=pafy.new(url)
                bestaudio=video.getbestaudio()
                print(video.title)
                bestaudio.download()
            except:
                pass
        file.close()
            
