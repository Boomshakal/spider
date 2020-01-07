import itchat, time
def lc():
    print("Finash Login!")
def ec():
    print("exit")

itchat.auto_login(loginCallback=lc, exitCallback=ec)
itchat.send_msg("hello world.")
time.sleep(1)
itchat.logout()