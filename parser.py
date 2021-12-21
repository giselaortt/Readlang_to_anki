import sys
import re

def removeBold( sentence ):

    return re.sub("<b>|</b>","", sentence)


def createBold(sentence):
    sentence = re.sub( "\[\[", "<b>", sentence )
    sentence = re.sub( "]]", "</b>", sentence )

    return sentence


#May cause bug if more than 2 fields are included in the sentence
#TODO: raise an exception if only one sentence is present
def separateFields( card ):

    return card.split(";")


def firstFieldMatches( first, second ):
    print(separateFields( first ))
    first,_ = separateFields( first )
    second,_ = separateFields( second )

    return ( removeBold(first) == removeBold(second) )


def uniteFields( first, second ):

    return first + ";" + second


def transferBoldThroughSentences( first, second ):
    one = first.split(" ")
    two = second.split(" ")
    for word, i in zip(two, range(len(two))):
        if( "<b>" in word ):
            one[i] = word

    return ' '.join(one)


def whoIsBold( sentence ):
    listOfWords = sentence.split(" ")
    for word in listOfWords:
        if("<b>" in word):

            return word


def formatTranslationField( card ):
    sentence, translation = separateFields(card)
    word = whoIsBold(sentence)
    translation = word + "<b>: </b>" + translation

    return uniteFields(sentence,translation)


def mergeCards( firstCard, secondCard ):
    firstSentence, firstTranslation =  separateFields( firstCard )
    secondSentence, secondTranslation = separateFields( secondCard )
    newSentence = transferBoldThroughSentences( firstSentence, secondSentence )
    newTranslation = firstTranslation+", "+secondTranslation

    return uniteFields( newSentence, newTranslation )


def shortenFirstField( sentence ):
    subsentences = re.split("–|;|!|\.|'|\"|«|:|»|,", sentence)
    for subsentence in subsentences :
        if '[[' in subsentence :
            #line = subsentence + ";" + subsentences[-1]

            return subsentence.strip(" ") + ";" + subsentences[-1]


def removeRepetitions( cards ):
    for i in range( len(cards)-1, 0, -1 ):
            for j in range( len(cards)-1, i+1, -1 ):
                if( firstFieldMatches( cards[i], cards[j] ) ):
                    cards[i] = mergeCards( cards[i], cards[j] )
                    cards.pop(j)

    return cards


if __name__ == "__main__":
    fptr = open(sys.argv[1],'r')
    ans = open("parsed.txt", 'w+')
    otherfptr = open("no_repetition.txt", "w")
    otherfptr.write("\n")

    for line in fptr.readlines():
        line = shortenFirstField(line)
        line = createBold(line)
        line = formatTranslationField(line)
        ans.write(line)

    ans.seek(0)
    cards = ans.readlines()
    print(cards)
    cards = removeRepetitions(cards)
    for card in cards:
        otherfptr.write(card)

    otherfptr.close()
    ans.close()
    fptr.close()
