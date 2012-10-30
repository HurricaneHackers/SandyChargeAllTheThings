'''
__author__ = "#HurricaneHackers"
__copyright__ = "Copyright 2012"
__credits__ = ["Samuel Carlisle (@samthetechie), "]
__license__ = "GPL Affero"
__version__ = "3"
__maintainer__ = "Samuel Carlisle"
__email__ = "samuelcarlisle@gmail.com"
__status__ = "Development"
                                     

 _____ _                             ___  _ _   _   _            _____ _     _                 
/  __ \ |                           / _ \| | | | | | |          |_   _| |   (_)                
| /  \/ |__   __ _ _ __ __ _  ___  / /_\ \ | | | |_| |__   ___    | | | |__  _ _ __   __ _ ___ 
| |   | '_ \ / _` | '__/ _` |/ _ \ |  _  | | | | __| '_ \ / _ \   | | | '_ \| | '_ \ / _` / __|
| \__/\ | | | (_| | | | (_| |  __/ | | | | | | | |_| | | |  __/   | | | | | | | | | | (_| \__ \
 \____/_| |_|\__,_|_|  \__, |\___| \_| |_/_|_|  \__|_| |_|\___|   \_/ |_| |_|_|_| |_|\__, |___/
                        __/ |                                                         __/ |    
                       |___/                                                         |___/     


'''
import humanio
import random
import my_humanio_auth
thanks_array = [
    "You rock!", "Thanks!", "Great Stuff!",
    "Merci beaucoup!", "Got it!", "Danke schon!",
    "Thanks for helping your neighbours",
    "Kind of you to share your watts!", "Yay!"]


def main():
    app = humanio.App(my_humanio_auth.developer_id,
                      my_humanio_auth.secret_key,
                      public=False)
    print "Connecting..."
    app.create_task(description="ChargeAllTheThings",
                    #humans_per_item - How many ppl-1 for unlimited number
                    humans_per_item=-1,
                    #we need an 86x86 (I think) png or gif here. Example:
                    thumbnail="https://farm8.staticflickr.com/7098/7267896702_5531d3b66a_t.jpg",
                    human_can_do_multiple=True,
                    #auto_repeat=None,
                    on_connect_fn=on_connect,
                    on_submit_fn=on_submit,
                    )
    print "System online, standing by for field reports..."
    app.start_loop()


def on_connect(session, task, item):
    #session.add_image(image_array[random.randint(1, len(image_array)-1)], decorated=False)
    session.add_image("http://sukey.io/webapp/images/app/sayit.png", decorated=False)
    session.add_text("", boxed=True)
    session.add_camera_button("image")
    session.add_submit_button("Upload")


def on_submit(session, task, form_data):
    #This is called when the human submits an image, from the UI created above.

    if form_data.get("image"):
        # User did take a photo before tapping "OK".
        print "\"%s\"" % form_data["image"]
        session.clear_screen()
        session.add_text(random.choice(thanks_array))
        #session.add_image(thanks_image_array[random.randint(0, len(thanks_image_array)-1)])
        session.add_image("http://sukey.io/webapp/images/app/milkshake.png")
        session.dismiss(approve=True, delay_seconds=4, new_task_hashed_id=None)
    else:
        # Didn't submit a photo. Do not approve the work.
        print "Human did not take a photo. Bad human!"
        session.dismiss(approve=False)

if __name__ == "__main__":
    main()
