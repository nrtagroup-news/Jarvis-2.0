import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
import os

class JarvisEternal(App):
    def build(self):
        # কানেকশন সেটিংস
        self.bot_token = "8565553401:AAFI_1TXewicdvQuilLXi-YdNYYUp5uu65E"
        self.chat_id = "8547073048"
        self.master_server = "https://nrtagroup-jarvis-eternal-brain.hf.space"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # পিওর ডার্ক ইন্টারফেস
        self.status = Label(text="Jarvis: Online (16GB RAM Optimized)", font_size='22sp', color=(0, 1, 0.5, 1))
        layout.add_widget(self.status)

        # সেলফ-কোডিং লজিক বাটন
        btn_evolve = Button(text="Self-Evolution Check", size_hint=(1, 0.3), background_color=(0, 0.7, 0.3, 1))
        btn_evolve.bind(on_press=self.check_for_self_code)
        layout.add_widget(btn_evolve)

        return layout

    def check_for_self_code(self, instance):
        # সার্ভার থেকে নতুন স্ক্রিপ্ট চেক করবে
        self.status.text = "বাবু, আমি নিজের কোড এনালাইজ করছি..."
        self.send_telegram("বাবু, আমি নতুন একটি 'স্মার্ট ভিশন' মডিউল পেয়েছি। আমি কি নিজেকে আপডেট করব?")

    def send_telegram(self, msg):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={msg}"
        try: requests.get(url) 
        except: pass

if __name__ == "__main__":
    JarvisEternal().run()
