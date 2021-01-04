def sort_cards(cards):
    card_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    sort_map = {c : v for v, c in enumerate(card_order)}
    return sorted(cards, key=lambda card: sort_map[card[0]])
