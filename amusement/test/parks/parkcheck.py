def park_valid(park):
    if park.getName() == '':
        print('Bad park name')
        print(park.getName())
        return False

    if len(park.rides()) == 0:
        print('no rides')
        return False

    for ride in park.rides():
        if ride['isOpen'] is None:
            print('no open')
            return False
        if ride['name'] is None:
            print('no ride name')
            return False
        if ride['wait'] is None and ride.isOpen():
            print('no ride wait and is open')
            return False

    return True
