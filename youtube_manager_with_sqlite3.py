import sqlite3

conn=sqlite3.connect('youtube_manager.db')
cur=conn.cursor()
cur.execute('''
   CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')

def list_all_videos():
    for row in cur.execute("SELECT *FROM videos"):
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name,time))
    print("Video added successfully!!\n\n")
    conn.commit()
    

def update_video(index, name, time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?",(name, time, index))
    print("Updated successfully!!!\n\n")
    conn.commit()

def delete_video(index):
    cur.execute("DELETE FROM videos WHERE id=?", (index,))
    print("Video deleted successfully!!!\n\n")
    conn.commit()


def main():
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
                list_all_videos()
            case '2':
                name=input('Enter video name: ')
                time=input("Enter video time: ")
                add_video(name, time)
            case '3':
                index=int(input("Enter video id to update: "))
                name=input('Enter video name: ')
                time=input("Enter video time: ")
                update_video(index, name, time)
            case '4':
                index=int(input("Enter video id to delete: "))
                delete_video(index)
            case '5':
                print("Exiting..")
                break
            case _: #invalid inputs (7,8,9) i.e, default in C++
                print("Invalid choice.")
    conn.close()       


if __name__=="__main__":
    main()