labels = ['WK', 'WQ', 'WR', 'WB', 'WN', 'WP',
          'BK', 'BQ', 'BR', 'BB', 'BN', 'BP',
          '_']

label_lib = {
                'WK':'K',
                'WQ':'Q',
                'WR':'R',
                'WB':'B',
                'WN':'N',
                'WP':'P',
                'BK':'k',
                'BQ':'q',
                'BR':'r',
                'BB':'b',
                'BN':'n',
                'BP':'p',
                '_' :'_'
            }
            
            
def _trans_rank(rank):
    new_rank = ''
    empty_counter = 0
    for ch in rank:
        if ch == '_':
            empty_counter+=1
        else:
            if empty_counter>0:
                new_rank += str(empty_counter)
                empty_counter = 0
            new_rank += ch
    if empty_counter > 0:
        new_rank += str(empty_counter)
    return new_rank


def label2fen(label):
    ranks = [_trans_rank(label[i:i+8]) for i in range(0, 64, 8)]
    return '/'.join(ranks)


def fen2label(fen):
    fen = fen.split()[0]
    fen = fen.replace('/', '')
    label = ''
    for ch in fen:
        if ch.isnumeric():
            label += '_' * int(ch)
        else:
            label += ch
    return label


def empty(dir):
    for path in dir.ls(): path.unlink()
        
        
def show(img):
    plt.imshow(img, cmap='gray')