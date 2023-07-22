import logging

class Publisher:
    def __init__(self):
        self.subscribers = {} 
        self.channels = {"ONE": {"messages": []}, "TWO": {"messages": []}, "THREE": {"messages": []}}
        self.subscriber_channels = {
        }

    def make_subsciption(self, subscriber, callback, channel):
        if subscriber not in self.subscribers:
            self.subscribers[subscriber] = callback
            self.subscriber_channels[subscriber] = channel
        else:
            logging.info(f"{subscriber} already subscribed")

    def publish(self, channel, message):
      
        self.channels[channel]["messages"].append(message)
  
        for subscriber in self.subscribers:
            self.subscribers[subscriber](message)

class Subscriber:
    def __init__(self):
        self.messages = []
        self.channels = []
        self.id = "!@£$"
    
    def getMessages(self):
        return self.messages

    def getChannels(self):
        return self.channels

    def processMessage(self, message):
        self.messages.append(message)

sub = Subscriber()
sub2 = Subscriber()

pub = Publisher()
pub.make_subsciption(sub.id, sub.processMessage, "ONE")
sub2.make_subsciption(sub2.processMessage, "THREE")

pub.publish("ONE", "Hello Mubi")
pub.publish("THREE", "GIVE ME MY MONEY!!")

print(pub.channels)
print(sub.messages)