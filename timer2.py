# @author : Jonathan Ingram


# Timer:
#  https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day

from datetime import datetime
from threading import Timer

# x=datetime.today()
# y=x.replace(hour=6, minute=30, second=0, microsecond=0) #set for 06:30 to open door everyday
# delta_t=y-x

# secs=delta_t.seconds+1


def open_door():

    x=datetime.today()
    y=x.replace(hour=6, minute=30, second=0, microsecond=0) #set for 06:30 to open door everyday
    delta_t=y-x

    secs=delta_t.seconds+1
    print("""

                _   _   _   _   _   _   _     _   _   _   _     _   _   _   _   _   
        / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \   / \ / \ / \ / \ / \ / \  / \ 
        ( C | H | I | C | K | E | N ) ( D | O | O | R ) ( O | P | E | N | I | N | G )
        \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
    
                                              _
                                   .-.  .--''` )
                                _ |  |/`   .-'`
                               ( `\      /`
                               _)   _.  -'._
                             /`  .'     .-.-;
                             `).'      /  \  \\
                            (`,        \_o/_o/__
                             /           .-''`  ``'-.
                             {         /` ,___.--''`
                             {   ;     '-. \ \\
           _   _             {   |'-....-`'.\_\\
          / './ '.           \   \          `"`
       _  \   \  |            \   \\
      ( '-.J     \_..----.._ __)   `\--..__
     .-`                    `        `\    ''--...--.
    (_,.--""`/`         .-             `\       .__ _)
            |          (                 }    .__ _)
            \_,         '.               }_  - _.'
               \_,         '.            } `'--'
                  '._.     ,_)          /
                     |    /           .'
                      \   |    _   .-'
                       \__/;--.||-'
                        _||   _||__   __
                 _ __.-` "`)(` `"  ```._)
              (_`,-   ,-'  `''-.   '-._)
               (  (    /          '.__.'
                `"`'--'

        """) 
    #found via http://www.ascii-art.de/ascii/c/chicken.txt



def close_door():

    x=datetime.today()
    y=x.replace(hour=18, minute=30, second=0, microsecond=0) #set for 18:30 to close door everyday
    delta_t=y-x

    secs=delta_t.seconds+1
    print("""

                _   _   _   _   _   _   _     _   _   _   _     _   _   _   _   _   _   _  
        / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
        ( C | H | I | C | K | E | N ) ( D | O | O | R ) ( C | L | O | S | I | N | G )
        \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
    
                                              _
                                   .-.  .--''` )
                                _ |  |/`   .-'`
                               ( `\      /`
                               _)   _.  -'._
                             /`  .'     .-.-;
                             `).'      /  \  \\
                            (`,        \_o/_o/__
                             /           .-''`  ``'-.
                             {         /` ,___.--''`
                             {   ;     '-. \ \\
           _   _             {   |'-....-`'.\_\\
          / './ '.           \   \          `"`
       _  \   \  |            \   \\
      ( '-.J     \_..----.._ __)   `\--..__
     .-`                    `        `\    ''--...--.
    (_,.--""`/`         .-             `\       .__ _)
            |          (                 }    .__ _)
            \_,         '.               }_  - _.'
               \_,         '.            } `'--'
                  '._.     ,_)          /
                     |    /           .'
                      \   |    _   .-'
                       \__/;--.||-'
                        _||   _||__   __
                 _ __.-` "`)(` `"  ```._)
              (_`,-   ,-'  `''-.   '-._)
               (  (    /          '.__.'
                `"`'--'

        """) 
    #found via http://www.ascii-art.de/ascii/c/chicken.txt

    

opening = Timer(secs, open_door)
closing = Timer(secs, close_door)


opening.start()
closing.start()


