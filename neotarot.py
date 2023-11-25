import random

class TarotCard:
  def __init__(self, name, meaning):
    self.name = name
    self.meaning = meaning

class TarotDeck:
  def __init__(self):
    self.cards = []
    for suit in ["Major Arcana"]:
      for number in range(1, 21):
        card_name = f"{number} of {suit}"
        card_meaning = f"The {card_name} card represents {suit}."
        self.cards.append(TarotCard(card_name, card_meaning))
    for suit in ["Swords", "Cups", "Wands", "Pentacles"]:
      for number in range(1, 15):
        card_name = f"{number} of {suit}"
        card_meaning = f"The {card_name} card represents {suit}."
        self.cards.append(TarotCard(card_name, card_meaning))

  def draw_card(self):
    a = random.choice(self.cards)
    self.cards.remove(a)
    b = random.choice(self.cards)
    self.cards.remove(b)
    c = random.choice(self.cards)
    self.cards.remove(c)
    d = random.choice(self.cards)
    self.cards.remove(d)
    e = random.choice(self.cards)
    self.cards.remove(e)
    f = random.choice(self.cards)
    self.cards.remove(f)
    g = [a, b, c, d, e, f]
    return g

def get_tarot_reading():
  deck = TarotDeck()
  deck2 = TarotDeck()
  deck3 = TarotDeck()
  card = deck.draw_card()
  card2 = deck2.draw_card()
  card3 = deck3.draw_card()
  return card[0], card[1], card[2], card[3] ,card[4], card[5], card2[0], card2[1], card2[2], card2[3] ,card2[4], card2[5], card3[0], card3[1], card3[2], card3[3] ,card3[4], card3[5]

if __name__ == "__main__":
  for k in range(1000000000000000000000000000000000000000000000000000):
    card = get_tarot_reading()
    for h in card:
      print(f"Your tarot reading is: {h.name}")
      print(f"The meaning of the card is: {h.meaning}")
