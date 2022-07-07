#!/usr/bin/env python3
""" Module for bot that interacts with Zulip."""
import time


class MyBotHandler:
    """ Bot that interacts with Zuip."""
    def __init__(self):
        self.schedule_state = False
        self.state_time = time.time()

    def usage(self):
        return """I am a bot that matches users in pairs and in rare cases three's.
        """
#"**How to use Pairing Bot:**\n* `subscribe` to start getting matched with other Pairing Bot users for pair programming\n* `schedule monday wednesday friday` to set your weekly pairing schedule\n  * In this example, I've been set to find pairing partners for you on every Monday, Wednesday, and Friday\n  * You can schedule pairing for any combination of days in the week\n* `streams` to select streams/topics of the match and to select the number of pairings per keyword\n  * For example, `streams any 2 pairing 1 math 1` would schedule per day 2 pairings with anyone, 1 pairing with someone interesting in pair programming, and 1 pairing with someone who'd like to talk about math. Of course, they would need to be available on a given day.\n  * At the moment, there's no strict rules for words as topics here except that they have to be one word. I suggest using the stream name without the spaces!\n* `skip tomorrow` to skip pairing tomorrow\n  * This is valid until matches go out at 04:00 UTC\n* `unskip tomorrow` to undo skipping tomorrow\n* `status` to show your current schedule, skip status, and name\n* `unsubscribe` to stop getting matched entirely\n\nIf you've found a bug, please [submit an issue on github](https://github.com/thwidge/pairing-bot/issues)!"
#"You're unsubscribed!\nI won't find pairing partners for you unless you `subscribe`.\n\nBe well :)"
#"You're not subscribed to Pairing Bot <3"

    def handle_message(self, message, bot_handler):
        content = message['content']
        sender = message['sender_email']

        # parse message
        # schedule
        # subscribe
        # unsubscribe
        # skip
        # status

        # reset time if enough time has passed
        if self.schedule_state and time.time() - self.state_time > 300:
            self.schedule_state = False
        self.state_time = time.time()

        content = content.strip()

        # no prior message
        if not self.schedule_state:
            if content == "subscribe":
                # message to confirm subscription
                response = (
                    "Yay! You're now subscribed to Pairing Bot!\nCurrently, I'm set to find pair "
                    "programming partners for you on **Mondays**, **Tuesdays**, **Wednesdays**, "
                    "*Thursdays**, and **Fridaysr*.\nYou can customize your schedule any time with "
                    "`schedule` :)"
                )
            elif content == "unsubscribe":
                # message to confirm usbusvriptio9hn
                # message to confirm usbusvription
                response = "message to confirm unsubscription"
            elif content == "skip":
                response = "message to confirm skip"
            elif content == "status":
                response = "status message"
            elif content == "schedule":
                response = "message to set up next stage"
                self.schedule_state = True
            else:
                response = "error message"
        # prior message was schedule
        elif self.schedule_state:
            # if finished
            if content == "done":
                response = "confirm done"
            # parse for schedule
            # modify schedule
            else:
                response = "ask for more"

        bot_handler.send_message(dict(
            subject=message['sender_email'],
            content=response,
        ))


handler_class = MyBotHandler
