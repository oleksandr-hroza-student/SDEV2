from flask_babel import lazy_gettext as _l

# =======================
# ARTISTS
# =======================

artists = {
    'elena-vasquez': {
        'id': 'elena-vasquez',
        'name': 'Elena Vasquez',
        'photo': 'https://placehold.co/300x300/c9b99a/4a3f35?text=EV',
        'bio_short': _l(
            'A Madrid-born painter known for her meditative use of negative space and charcoal.'
        ),
        'bio_full': _l(
            'Elena Vasquez was born in Madrid in 1983 and studied fine arts at the '
            'Universidad Complutense. After a decade working in Berlin, she returned '
            'to Spain where she developed her signature style — vast fields of silence '
            'interrupted by precise, almost calligraphic marks.'
        ),
        'works': [
            'solitude-no3',
            'grey-morning',
            'the-river-speaks'
        ],
    },
}


# =======================
# PAINTINGS
# =======================

paintings = {
    'solitude-no3': {
        'id': 'solitude-no3',
        'title': _l('Solitude No. 3'),
        'artist_id': 'elena-vasquez',
        'year': 2021,
        'material': _l('Charcoal on paper'),
        'thumb': 'https://placehold.co/400x500/e8dfd0/4a3f35?text=Solitude+No.+3',
    },
    'grey-morning': {
        'id': 'grey-morning',
        'title': _l('Grey Morning'),
        'artist_id': 'elena-vasquez',
        'year': 2022,
        'material': _l('Charcoal and chalk on paper'),
        'thumb': 'https://placehold.co/400x500/d8d2c8/3a3530?text=Grey+Morning',
    },
    'the-river-speaks': {
        'id': 'the-river-speaks',
        'title': _l('The River Speaks'),
        'artist_id': 'elena-vasquez',
        'year': 2023,
        'material': _l('Ink and charcoal on canvas'),
        'thumb': 'https://placehold.co/400x500/ddd5c5/2e2a25?text=The+River+Speaks',
    },
}