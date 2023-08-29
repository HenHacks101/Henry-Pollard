from Hand import Hand
from Deck2 import Deck
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont






poker_game = []



poker_game.append(Hand())
poker_game.append(Hand())
poker_game.append(Hand())
poker_game.append(Hand())

shoot1=Deck()
shoot1.shuffle()

poker_game[0].add_card(shoot1.deal_card())
poker_game[1].add_card(shoot1.deal_card())
poker_game[2].add_card(shoot1.deal_card())
poker_game[3].add_card(shoot1.deal_card())
poker_game[0].add_card(shoot1.deal_card())
poker_game[1].add_card(shoot1.deal_card())
poker_game[2].add_card(shoot1.deal_card())
poker_game[3].add_card(shoot1.deal_card())
poker_game[0].add_card(shoot1.deal_card())
poker_game[1].add_card(shoot1.deal_card())
poker_game[2].add_card(shoot1.deal_card())
poker_game[3].add_card(shoot1.deal_card())
poker_game[0].add_card(shoot1.deal_card())
poker_game[1].add_card(shoot1.deal_card())
poker_game[2].add_card(shoot1.deal_card())
poker_game[3].add_card(shoot1.deal_card())
poker_game[0].add_card(shoot1.deal_card())
poker_game[1].add_card(shoot1.deal_card())
poker_game[2].add_card(shoot1.deal_card())
poker_game[3].add_card(shoot1.deal_card())

poker_game[0].print_hand()
poker_game[1].print_hand()
poker_game[2].print_hand()
poker_game[3].print_hand()

# Image.open("cards/" + poker_game[0].get_hand()[0])


def make_collum(im1, im2, im3, im4,):
    #this is the code that prints the colom on the images
    column = Image.new('RGB', (im1.width, im1.height * 4))
    column.paste(im1, (0, 0))
    column.paste(im2, (0, im1.height))
    column.paste(im3, (0, 2*im1.height))
    column.paste(im4, (0, 3*im1.height))
    return column


def make_row(im1, im2, im3, im4, im5):
    #this is the code that prints the row on the images

    row = Image.new('RGB', (im1.width * 6, im1.height))
    row.paste(im1, (0, 0))
    row.paste(im2, (im1.width, 0))
    row.paste(im3, (2*im1.width, 0))
    row.paste(im4, (3*im1.width, 0))
    row.paste(im5, (4*im1.width, 0))
    return row

#these makes the rows and collums
hand1 = make_row(Image.open("cards/" + poker_game[0].get_hand()[0].image_file_name()), Image.open("cards/" + poker_game[0].get_hand()[1].image_file_name()),
                 Image.open("cards/" + poker_game[0].get_hand()[2].image_file_name()), Image.open("cards/" + poker_game[0].get_hand()[3].image_file_name()),
                 Image.open("cards/" + poker_game[0].get_hand()[4].image_file_name()))
hand2 = make_row(Image.open("cards/" + poker_game[1].get_hand()[0].image_file_name()), Image.open("cards/" + poker_game[1].get_hand()[1].image_file_name()),
                 Image.open("cards/" + poker_game[1].get_hand()[2].image_file_name()), Image.open("cards/" + poker_game[1].get_hand()[3].image_file_name()),
                 Image.open("cards/" + poker_game[1].get_hand()[4].image_file_name()))
hand3 = make_row(Image.open("cards/" + poker_game[2].get_hand()[0].image_file_name()), Image.open("cards/" + poker_game[2].get_hand()[1].image_file_name()),
                 Image.open("cards/" + poker_game[2].get_hand()[2].image_file_name()), Image.open("cards/" + poker_game[2].get_hand()[3].image_file_name()),
                 Image.open("cards/" + poker_game[2].get_hand()[4].image_file_name()))
hand4 = make_row(Image.open("cards/" + poker_game[3].get_hand()[0].image_file_name()), Image.open("cards/" + poker_game[3].get_hand()[1].image_file_name()),
                 Image.open("cards/" + poker_game[3].get_hand()[2].image_file_name()), Image.open("cards/" + poker_game[3].get_hand()[3].image_file_name()),
                 Image.open("cards/" + poker_game[3].get_hand()[4].image_file_name()))
collum = make_collum(hand1, hand2,hand3,hand4)

collum.show()
