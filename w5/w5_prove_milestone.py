print('Interactive Stories')
print('Do you want to read a history?')
print('please choose one') 
if history == [a = "The Dark Wooden", b = "Maya y el oso", c = "Juanita va al parque", d = "el auto y el arbol"]
if history == 'a':
    print [history[0]]
    print('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.')
    tool = input('Which one do you want to pick up? ')
if tool == 'match':
    print('''You pick up the match and strike it, and for an instant, the forest around you is illuminated.
You see a large grizzly bear, and then the match burns out.''')

    action1 = input('Do you want to RUN, or HIDE behind a tree? ')
    if action1 == 'hide':
        print('Corrieron los minutos más lagos de toda tu vida....')
    
    elif action1 == 'run':
        print('you die')

elif tool == 'flashlight':
    print('''You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought
    you also heard something off to the side.''')

    action2 = input('Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
    if action2 == 'follow':
        print('no haces ruido')
    elif action2 == 'look':
        print('miras alrededor')
