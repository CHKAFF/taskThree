from dialog_bot_sdk.bot import DialogBot
import grpc
from dialog_bot_sdk import interactive_media, messaging

def on_msg(*params):
    print('on msg', params)
    #print(params[0].message.textMessage)
    p = params[0]
    
    if str(params[0].message.textMessage.text) == "/start":
        bot.messaging.send_message(
            params[0].peer,
            "Хочешь узнать что я могу?",
            [interactive_media.InteractiveMediaGroup(
            [
                interactive_media.InteractiveMedia(
                    1,
                    interactive_media.InteractiveMediaButton("Yes", "ДА")
                ),
                interactive_media.InteractiveMedia(
                    2,
                    interactive_media.InteractiveMediaButton("No", "НЕТ")
                ),
            ]
        )])
    else:
        bot.messaging.send_message(
        params[0].peer,
        "Хотите забронировать аудиторию?",
        [interactive_media.InteractiveMediaGroup(
            [
                interactive_media.InteractiveMedia(
                    1,
                    interactive_media.InteractiveMediaButton("Yes", "ДА")
                ),
                interactive_media.InteractiveMedia(
                    2,
                    interactive_media.InteractiveMediaButton("No", "НЕТ")
                ),
                interactive_media.InteractiveMedia(
                    3,
                    interactive_media.InteractiveMediaButton("feedback", "Запросить FEEDBACK")
                ),
            ]
        )]
    )
    

def on_click(*params):
    print(params[0])
    which_button = params[0].value
    if which_button == "Yes":
        print("jopa")
       # bot.messaging.update_message(p, text = "Всё супер")
    #id = params[0].uid
    #peer = {type: PEERTYPE_PRIVATE, id: id, str_id {}}
    #if which_button == "feedback":
    #    bot.messaging.send_message(peer, "Держи")
#print(params.id)
    #if params[0]

if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'hackathon-mob.transmit.im',  # bot endpoint (specify different endpoint if you want to connect to your on-premise environment)
        grpc.ssl_channel_credentials(), # SSL credentials (empty by default!)
        'b120071b560f1ef597b6a56363ee171bbbdd9fc9',  # bot token
        verbose=False # optional parameter, when it's True bot prints info about the called methods, False by default
    )

    bot.messaging.on_message(on_msg, on_click)