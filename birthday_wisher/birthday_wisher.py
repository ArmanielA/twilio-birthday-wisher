from twilio.rest import Client
from decouple import config
from datetime import datetime
import pandas as pd

account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
sender_number = config('SENDER_NUMBER')
receiver_number = config('RECEIVER_NUMBER')
twilio_client = Client(account_sid, auth_token)


class BirthdayWisher():
    
    def __init__(self):
        self.birthday_df = self.create_birthdays_dataframe()
    
    def send_birthday_message(self, name):
        try:
                      
            message = f"Today is the birthday of {name}. Let's wish them a happy birthday :)"
            message = twilio_client.messages.create(
                                            from_ = sender_number,
                                            body = message,
                                            to = receiver_number)
            print(f'Birthday reminder of {name} is sent to {receiver_number} with id {message.sid}')
            
        except Exception as e:
            print('Something went wrong. No message is sent.')
            print(repr(e))

    def create_birthdays_dataframe(self):
        try:
            dateparse = lambda x: datetime.strptime(x, "%d-%m-%Y")
            birthdays_df = pd.read_csv(
                r"birthday_wisher\birthdays.csv",
                dtype=str,
                parse_dates=['Birth Date'],
                date_parser=dateparse
            )
            return birthdays_df

        except Exception as e:
            print("Something went wrong. Birthdays dataframe not created.")
            print(repr(e))   
    
    def check_matching_dates(self):
        try:
            today = datetime.now()
            for index, row in self.birthday_df.iterrows():
                if today.day == row["Birth Date"].day and today.month == row["Birth Date"].month:
                    self.send_birthday_message(row["Name"])
                    # print("birthday of ", row["Name"])
        except Exception as e:
            print("Something went wrong. Birthday check not successful.")
            print(repr(e))    
            