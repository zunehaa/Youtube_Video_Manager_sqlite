import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
      
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("------------------------------------------------")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["Name"]}, Duration: {video["Time"]}")

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({"Name": name,"Time": time})
    save_data_helper(videos)
    print("Video added successfully!!\n\n")

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update: "))
    if 1<=index<=len(videos):
        name=input("Enter video name: ")
        time=input("Enter video duration: ")
        videos[index-1]={"Name": name,"Time": time}
        save_data_helper(videos)
        print("Updated successfully!!")
    else:
        print("Invalid index selected.")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Deleted successfully!!")
    else:
        print("Invalid index selected.")


def main():
    videos=load_data()
    while True:
        print("************************")
        print("|    Youtube Manager    |")
        print("************************")
        print("1. List Videos")
        print("2. Add video")
        print("3. Update details of video")
        print("4. Delete video")
        print("5. Exit the app")
        choice=input("Enter your choice: ")
        print("\n\n")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting..")
                break
            case _: #invalid inputs (7,8,9) i.e, default in C++
                print("Invalid choice.")
        

if __name__=="__main__":
    main()