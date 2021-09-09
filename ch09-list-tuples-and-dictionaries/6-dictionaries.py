def main():
    print('First point')
    captains = {}
    print(f'Empty dictionary: \n{captains}')

    print('Second point')
    captains['Enterpirse'] = 'Picard'
    captains['Voyager'] = 'Janeway'
    captains['Defiant'] = 'Sisko'
    print(f'dictionary: \n{captains}')

    print('Third point')
    if 'Enterprise' not in captains:
        captains['Enterprise'] = 'unknown'

    if 'Discovery' not in captains:
        captains['Discovery'] = 'unknown'


    print('Fourth point')
    for ship, captain in captains.items():
        print(f'The {ship} is captained by {captain}')
    
    print('Fifth point')
    print(f"Before deletion \n {captains}")
    try:
        del captains['Discovery']
    except KeyError:
        print('That key does not exist')
    print(f"After deletion \n {captains}")


if __name__ == '__main__':
    main()