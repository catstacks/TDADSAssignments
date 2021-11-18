#madlibs template source: http://unplugtoconnect.org/2020/04/27/unplugged-stories-make-your-own-mad-libs/

animal = input('Enter an animal: ')
country = input('Enter a country: ')
plural_noun = input('Enter a plural noun (a plural name word e.g. berries, cars, people etc.): ')
food = input('Enter a food: ')
screen_device = input('Enter the name of a device with a screen e.g. phone: ')
noun = input('Enter a noun (a name word e.g. house, tree, sun etc.): ')
verb = input('Enter a verb (a doing word e.g. eat, run, smile etc.): ')
adjective = input('Enter an adjective (a decribing word e.g. dark, pleasant, round etc.): ')
whitespace = " "
story_text = "The majestic" + whitespace + animal + whitespace + "has roamed the forests of" + whitespace + country + whitespace + "for thousands of years. Today, she wanders in search of" + whitespace + plural_noun + ". She must find food to survive. While hunting for" + whitespace + food + ", she found a/an" + whitespace + screen_device + whitespace + "hidden behind a" + whitespace + noun + ". She has never seen anything like this before. What will she do? With the device in her teeth, she tries to" + whitespace + verb + ", but nothing happens. She takes it back to her family. When her family sees it, they quickly" + whitespace + verb + ". Soon, the device becomes" + whitespace + adjective + ", and the family decides to put it back where they found it."

print(story_text)