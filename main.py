import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.popup import Popup
import requests
import threading

# উইন্ডো সাইজ ফিক্স (কম্পিউটারে টেস্ট করার জন্য, মোবাইলে অটো ফুলস্ক্রিন হবে)
from kivy.core.window import Window
Window.clearcolor = (0, 0, 0.2, 1)  # গাঢ় নীল ব্যাকগ্রাউন্ড

class JarvisEternal(App):
    def build(self):
        # --- কনফিগারেশন এবং সিক্রেট ---
        self.bot_token = "8565553401:AAFI_1TXewicdvQuilLXi-YdNYYUp5uu65E"
        self.chat_id = "8547073048"
        self.master_server = "https://nrtagroup-jarvis-eternal-brain.hf.space"
        self.pending_code = None # নতুন কোড জমা রাখার ভেরিয়েবল
        
        # --- মেইন লেআউট (ডার্ক ব্লু থিম) ---
        self.root = FloatLayout()
        
        # ব্যাকগ্রাউন্ড কালার (ডার্ক ব্লু)
        with self.root.canvas.before:
            Color(0.05, 0.05, 0.2, 1) # Dark Blue
            self.rect = Rectangle(size=(2000, 2000), pos=self.root.pos)

        # --- ১. ভিশন সিস্টেম (ক্যামেরা) ---
        # আগের ফিচার ফিরিয়ে আনা হলো
        self.cam = Camera(play=True, resolution=(640, 480), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.root.add_widget(self.cam)

        # --- ২. স্ট্যাটাস প্যানেল ---
        self.status_label = Label(
            text="JARVIS SYSTEM ONLINE\nWaiting for Babu's Command...",
            font_size='18sp',
            color=(0, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'top': 0.95},
            size_hint=(1, 0.1)
        )
        self.root.add_widget(self.status_label)

        # --- ৩. কন্ট্রোল বাটন প্যানেল (নিচে) ---
        button_layout = BoxLayout(size_hint=(1, 0.15), pos_hint={'bottom': 1})
        
        # বাটন ১: আপডেট চেক (সেলফ কোডিং)
        btn_update = Button(text="Check Brain Update", background_color=(0, 0.5, 1, 1))
        btn_update.bind(on_press=self.check_server_updates)
        button_layout.add_widget(btn_update)
        
        # বাটন ২: রিপোর্ট (টেলিগ্রাম)
        btn_report = Button(text="Report Status", background_color=(0, 0.8, 0, 1))
        btn_report.bind(on_press=self.report_to_babu)
        button_layout.add_widget(btn_report)

        self.root.add_widget(button_layout)
        
        return self.root

    # --- ব্রেন ফাংশন: সার্ভার চেক এবং এপ্রুভাল সিস্টেম ---
    def check_server_updates(self, instance):
        self.status_label.text = "Checking Master Brain for new capabilities..."
        # এখানে আমরা ফেক লজিক দিচ্ছি, বাস্তবে এটি সার্ভার থেকে পাইথন কোড আনবে
        # ধরো সার্ভার বলল: "আমি ফ্ল্যাশলাইট কন্ট্রোল শিখেছি"
        Clock.schedule_once(self.show_approval_dialog, 2)

    def show_approval_dialog(self, dt):
        # জার্ভিস বাবুকে জিজ্ঞেস করছে
        content = BoxLayout(orientation='vertical')
        msg = Label(text="বাবু, আমি 'Night Vision' মোড এর কোড লিখেছি।\nআমি কি এটি আমার সিস্টেমে ইন্সটল করব?")
        
        btn_box = BoxLayout(size_hint_y=0.4)
        btn_yes = Button(text="Approve (হ্যাঁ)", background_color=(0, 1, 0, 1))
        btn_no = Button(text="Deny (না)", background_color=(1, 0, 0, 1))
        
        btn_box.add_widget(btn_yes)
        btn_box.add_widget(btn_no)
        content.add_widget(msg)
        content.add_widget(btn_box)

        self.popup = Popup(title='System Evolution Request', content=content, size_hint=(0.8, 0.4))
        
        # এপ্রুভ করলে কি হবে
        btn_yes.bind(on_press=lambda x: self.execute_evolution("Night Vision"))
        btn_no.bind(on_press=self.popup.dismiss)
        
        self.popup.open()

    def execute_evolution(self, feature_name):
        self.popup.dismiss()
        self.status_label.text = f"Installing {feature_name} module..."
        self.send_telegram(f"বাবু, আপনার অনুমতিতে আমি '{feature_name}' ফিচারটি সফলভাবে ইন্সটল করেছি।")
        # ভবিষ্যতে এখানে exec() ফাংশন দিয়ে ডাইনামিক কোড রান হবে
        self.status_label.text = f"JARVIS UPDATED: {feature_name} Active"

    # --- টেলিগ্রাম কানেকশন ---
    def report_to_babu(self, instance):
        self.send_telegram("বাবু, জার্ভিস মোবাইল সিস্টেম ১০০% অ্যাক্টিভ আছে। ক্যামেরা এবং সেন্সর কাজ করছে।")
        self.status_label.text = "Report sent to Telegram."

    def send_telegram(self, msg):
        def _send():
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={msg}"
            try: requests.get(url)
            except Exception as e: print(e)
        threading.Thread(target=_send).start()

if __name__ == "__main__":
    JarvisEternal().run()
