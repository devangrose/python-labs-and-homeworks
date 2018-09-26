def kwargosaurus (**kwargs):
    for key, value in kwargs.items():
        if value is 'smaller':
            print('{} is small! Mighty Kwargosaurus will fight you!'.format(key))
        else: 
            print('{} is big! Whimpering Kwargosaurus cries and runs away!'.format(key))
            
kwargosaurus(Velociraptor="smaller", Stegosaurus="smaller", Triceratops="smaller", Trex="bigger")
