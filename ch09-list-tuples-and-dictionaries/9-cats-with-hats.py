cats = ['cat #' + str(x) for x in range(1,101)]
cats_dict = {k:'No hat' for k in cats }
cats_with_hats  = []

def put_hat(cat):
    if cats_dict[cat] == 'No hat':
            cats_dict[cat] = 'Hat'
    else:
        cats_dict[cat] = 'No hat'

def main():
    for i in range(1, 100):
        for j in range(0, len(cats), i):
            put_hat(cats[j])

    for k,v in cats_dict.items():
        if v == 'Hat':
            cats_with_hats.append(k)

    print(cats_with_hats)

if __name__ == '__main__':
    main()