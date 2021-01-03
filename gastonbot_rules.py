'''
######################################################################################
##################
(1) STEP ONE!  
##################
add the one-word command to the command palette that starts on line 
######################################################################################
'''

COMMAND_PALLETTE = [
    {
        'command' : 'bark',
        'description' : 'gaston will BARK at you or whoever you `@mention`'
    },
    {
        'command' : 'help',
        'description' : 'show list of commands'
    },
    {
        'command' : 'kiss',
        'description' : 'gaston will :tongue: you or whoever you `@mention`'
    }
]



'''
######################################################################################

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

    # are there args?
    if parsedEvent['message_args'] == '' or parsedEvent['message_args'] == ' ':
        payload = 'BARK!'
    else:
        # if args, check to see if there is a mention in there
        split_args = parsedEvent['message_args'].split(' ')
        mention = parsedEvent['message_args']
        payload = 'BARK! {}'.format(mention)
    return payload



def helpme(parsedEvent):
    payload = 'WOOF! I\'m gastonbot. I\'m not that useful, but I still love you!\n'
    payload += 'Here is what you can ask me:\n'
    commands_payload = ''
    for each in COMMAND_PALLETTE:
        commands_payload += '- `{command}` - {description}\n'.format(command=each['command'],description=each['description'])
    payload += commands_payload
    payload += '\ninvoke a command by mentioning me directly `@gastonbot`!'
    return payload




def kiss(parsedEvent):
    payload = None
    # enter code below

    # are there args?
    if parsedEvent['message_args'] == '' or parsedEvent['message_args'] == ' ':
        payload = ':tongue: <@{}>'.format(parsedEvent['author_id'])
    else:
        # if args, check to see if there is a mention in there
        split_args = parsedEvent['message_args'].split(' ')
        mention = parsedEvent['message_args']
        payload = ':tongue: {}'.format(mention)
    return payload









'''
######################################################################################
##################
(3) STEP THREE!      print(payload)


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
        print('[gastonbot] command "{}" successfully executed.'.format(COMMAND))
    except:
        print('[!] error executing command "{}".'.format(COMMAND))
    return payload
######################################################################################
'''





def gastonbot(parsedEvent):

    COMMAND = parsedEvent['message_command']
    valid = False
    for command in COMMAND_PALLETTE:
        if command['command'] == COMMAND:
            valid = True

    if valid == True:
        print('[gastonbot] command {} confirmed to be valid.'.format(COMMAND))
        print('[gastonbot] proceeding to run associated function for {}.'.format(COMMAND))


        ######################################################################################
        ##################
        # (3) STEP THREE!  
        ##################
        # put trigger logic below!
        ######################################################################################

        if COMMAND == 'bark':
            # enter code below
            try:
                payload = bark(parsedEvent)
                print('[gastonbot] command "{}" successfully executed.'.format(COMMAND))
            except:
                print('[gastonbot] error executing command "{}".'.format(COMMAND))
            return payload


        if COMMAND == 'help':
            # enter code below
            try:
                payload = helpme(parsedEvent)
               
            except:
                payload = 'I cannot help you, I\m just a doooooog'
            return payload

        if COMMAND == 'kiss':
            # enter code below
            try:
                payload = kiss(parsedEvent)
                print('[gastonbot] command "{}" successfully executed.'.format(COMMAND))
            except:
                print('[gastonbot] error executing command "{}".'.format(COMMAND))
            return payload










        ######################################################################################
        # end step three
        ######################################################################################





    else:
        print('[gastonbot] command {} is not a valid command'.format(COMMAND))
        print('[gastonbot] initiating conversation sequence')