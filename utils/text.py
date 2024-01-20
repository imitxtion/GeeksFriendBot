greeting = """
👋 Hello, <b>{name}</b>! 
I'm a multifunctional bot, ready to offer you a wide range of capabilities. Here are some of my features:

1. <b>TikTok Helper 🚀</b>
   - Download any TikTok video <u><b>without watermark</b></u> by simply sending a link to me!
   - AI-generated tags for your TikTok videos to boost their visibility and promotion.

2. <b>ChatGPT 💬</b>
   - Engage in a conversation with ChatGPT hassle-free! No need to open a browser or download any apps.

3. <b>To-Do List 📝</b>
   - Write down your tasks, and I'll send you notifications to ensure you never forget anything.

4. <b>Anime Assistant ⛩</b>
   - Stay updated on ongoing anime and create your list of favorite anime titles.

5. <b>Feedback 📬</b>
   - Found a bug or have suggestions? Feel free to send a message to my master.

☕ <b>Support my development:</b>
   If you enjoy my services, consider <a href="example.com">buying a cup of coffee</a> for my master!

Feel free to explore these features \n<b>(っ◔◡◔)っ</b>✨
"""

info = """
<b>(っ◔◡◔)っ</b>✨
   I'm a multifunctional bot, ready to offer you a wide range of capabilities. Here are some of my features:

1. <b>TikTok Helper 🚀</b>
   - Download any TikTok video <u><b>without watermark</b></u> by simply sending a link to me!
   - AI-generated tags for your TikTok videos to boost their visibility and promotion.

2. <b>ChatGPT 💬</b>
   - Engage in a conversation with ChatGPT hassle-free! No need to open a browser or download any apps.

3. <b>To-Do List 📝</b>
   - Write down your tasks, and I'll send you notifications to ensure you never forget anything.

4. <b>Anime Assistant ⛩</b>
   - Stay updated on ongoing anime and create your list of favorite anime titles.

5. <b>Feedback 📬</b>
   - Found a bug or have suggestions? Feel free to send a message to my master.

☕ <b>Support my development:</b>
   If you enjoy my services, consider <a href="example.com">buying a cup of coffee</a> for my master!

Type /menu or /commands to explore how I can help you.
"""

menu = '''
<b>(っ◔◡◔)っ</b> 📃 
   Here\'s my menu
'''

tt_assistant_menu = """
<b>Welcome to the TikTok Assistant!</b> 
Here are the functions:

<b>1. Video Downloader 🎥</b>
   Send me a TikTok video link, and I'll provide you with the downloadable file, <u>without any watermarks</u>.

<b>2. Tags Generator 🏷️</b>
   Generate tags for your TikTok video to boost its visibility and promote it effectively.
"""

tt_video_download = """
Ok, let's do it!
Send me the link to a video that you want to download.
"""

tt_wrong_format = """
<b>(っ◔_◔)っ</b> ❌
   Message that you sent to me is not a link or has a wrong format.
It should look like ⬇
<b><u>https://www.tiktok.com/@username/video/12345...</u></b>
"""

tt_sending_video = """
⏳ Sending the video... 
This process takes more time if the video is long or high quality.
"""

tt_generate_tags = """
   Ok! Let\'s generate tags for your TikTok video.
Send me the main theme of your video.
<b>Example:</b> Sport, workout
"""

tt_generate_tags_prompt = """
Can you please generate for me the best hashtags for my TikTok video?
Theme of it: {vid_theme}
Send the group of them without anything but spaces between. I'll just copy-paste. Thanks.
"""

talk_chatgpt = """
<b>(っ◔◡◔)っ</b> ✅
   ChatGPT connected. You can chat with it now.
<u><i>Use any other command or button to exit this mode</i></u>
"""

todo_info = """
You want to add a new task or check your created tasks?
"""

add_task = """
Let's do it!
Use "/newtask YOUR TASK # TIME" to add a new task.
<b>Example:</b> /newtask Add a new feature to my bot # 2024-01-10 12:00
"""

adding_task_success = """
<b>(っ◔◡◔)っ</b> ✅
   New task added succesfully!

Task: {task}
Time: {time}

<b>I'll send you a notification at the set time.</b>
"""

adding_task_error = """
<b>(っ◔_◔)っ</b> ❌
   An error occured while adding a new task.
<u>Make sure format of the command is correct and try again ⬇</u>
/newtask <i>YOUR TASK</i> <u><b>#</b></u> <i>TIME</i>
"""

task_remind = """
<b>(っ◔◡◔)っ</b> ✉
   <b>Hey, you asked me to remind:</b>
<b>Task:</b> {task}
<b>Set time:</b> {time}
"""

browse_todos = """
<b>(っ◔◡◔)っ</b> 📃 
   Here's a list of your tasks:
"""

anime_assistant_menu = """
<b>Welcome to the Anime Assistant!</b>
Here are the functions:

<b>1) News ⛩</b>
   Stay updated with the latest news from the anime world.

<b>2) Find Anime by Screenshot 🔎</b>
   Send me a screenshot from any anime episode, and I'll identify its title, episode number, and timestamp for you.

<b>3) List of Favorite Anime 📌</b>
   Create and manage your list of favorite anime.
"""

find_sauce = """
Ok. Let's do it!
Send me a moment from any anime and I'll try to find it's timecode and name.
<u>❗ <b>Please note that I could be wrong ❗</b></u>
"""

sauce_not_found = """
<b>(っ◔_◔)っ</b> ❌
   I don't know from where this picture is. 
<b>Let's try another one?</b>
"""

sauce_wrong_format = """
<b>(っ◔_◔)っ</b> ❌
   Message you sent to me is not a screenshot!
<b>Please, try again.</b>
"""

sauce_server_error = """
<b>(っ◔_◔)っ</b> ❌
   Server error occured. 
<b>Please, try again.</b>
"""

send_feedback = """
📬 <b>Your feedback is important for my improvement!</b>
I'll pass on your next message to my master.
"""

send_feedback_success = """
<b>(っ◔◡◔)っ</b> ✅
   Message sent successfully. Thank you!
"""

send_feedback_error = """
<b>(っ◔_◔)っ</b> ❌
   An error occurred while sending your message. 
Try again later or contact my master directly: <b><u>@alex_develor</u></b>
"""

admin_new_message = """
<b>(っ◔◡◔)っ</b> ✉
   Master, you've received a new message! 
From: @{username}, id: {user_id}
   
{user_feedback}
"""

wrong_message = """
<b>(っ◔_◔)っ</b> ❌ 
   Sorry, I don\'t understand you. 
Use "/commands" to see the list of available commands.
"""

bot_start = """
<b>(っ◔◡◔)っ</b> ✅ 
   <b>Bot launched!</b>
"""

bot_stop = """
<b>(っ◔_◔)っ</b> ❌
   <b>Bot stopped!</b>
"""

buy_coffee = """
   If you want to support my development, you can do it here:
<b>(っ◔◡◔)っ <u>https://www.buymeacoffee.com/develor</u></b> 
"""

see_commands = """
<b>(っ◔◡◔)っ</b> 📃
   Here's the list of available commands:

/info - general info
/menu - main menu
/commands - available commands

/video - download video from TikTok w/o watermark
/tags - generate tags for your TikTok video

/chatgpt - talk with ChatGPT

/todo - create a notification for a certain time

/animenews - check the state of anime ongoings
/sauce - find anime by screenshot
/favanime - edit the list of your favourite anime

/feedback - send a message to my master

/coffee - support my development
"""

function_unavailable = """
<b>(っ◔_◔)っ</b> ❌
   I'm sorry, this function is unavailable right now.
"""

processing_info = '⏳ Processing...'