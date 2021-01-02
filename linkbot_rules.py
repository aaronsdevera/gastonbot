'''

##################
(1) STEP ONE!  
##################
add the one-word command to the command palette that starts on line 

'''

COMMAND_PALLETTE = [
    'bark'
]





'''

##################
(2) STEP TWO!  
##################
add the function for the command in the FUNCTION section that starts on line

use this template:

def myCommandFunction(parsedEvent):
    payload = None
    # enter code below
    # payload = doSomething()
    return payload

######################################################################################
'''


def bark(parsedEvent):
    payload = None
    # enter code below
    payload = 'BARK!'
    return payload











'''

##################
(3) STEP THREE!  
##################
add trigger logic

for the incoming message event, assume an event dict with the following structure:
{
    'message_mention' : mention,
    'message_command' : command,
    'message_args' : args,
    'message_id' : message_id,
    'message_body' : message,
    'thread_id': thread_id,
    'thread' : thread,
    'thread_category': thread_category,
    'thread_category_id': thread_category_id,
    'author_id': author_id,
    'author_nick': author_nick,
    'author': author
}


for your function code, use this template:

if COMMAND == 'myCommand':
    # enter code below
    try:
        payload = myCommandFunction(parsedEvent)
        print('[+] command "{}" successfully executed.'.format(COMMAND))
    except:
        print('[!] error executing command "{}".'.format(COMMAND))
    return payload
'''





def linkbot(parsedEvent):

    COMMAND = parsedEvent['message_command']

    if COMMAND in COMMAND_PALLETTE:
        print('[+] command {} confirmed to be valid.'.format(COMMAND))
        print('[+] proceeding to run associated function for {}.'.format(COMMAND))

        '''
######################################################################################
        TRIGGER LOGIC STARTS HERE

        this is (3) STEP THREE!  
        use this template:

        if COMMAND == 'myCommand':
            # enter code below
            try:
                payload = myCommandFunction(parsedEvent)
                print('[+] command "{}" successfully executed.'.format(COMMAND))
            except:
                print('[!] error executing command "{}".'.format(COMMAND))
            return payload

######################################################################################
        '''




        if COMMAND == 'bark':
            # enter code below
            try:
                payload = bark(parsedEvent)
                print('[+] command "{}" successfully executed.'.format(COMMAND))
            except:
                print('[!] error executing command "{}".'.format(COMMAND))
            return payload


















    else:
        print('[+] command {} is not a valid command'.format(COMMAND))