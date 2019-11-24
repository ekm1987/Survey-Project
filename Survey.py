from Section import Section
from Question import Question

class Survey:

    def __init__(self):
        pass

    def start_survey(self):
        pass

# Welcome message
print('\nWelcome to the Best Pets Survey!\nPlease answer honestly.')

# Here are the first three qualifying questions
question_prompts = [
    '\n---------- Question 1 ----------\nWhat is your favourite pet?\n(a) Dogs of course!\n(b) Cats will rule the world!\n\n',
    '\n---------- Question 2 ----------\nHow many pets do you have?\n(a) 3 or more :)\n(b) 2 or less.\n\n',
    '\n---------- Question 3 ----------\nWould you adopt your next pet\n(a) A thousand times YES!\n(b) Probably not, no.\n\n',
]
qualifying_questions = [
    Question(question_prompts[0], ' '),
    Question(question_prompts[1], ' '),
    Question(question_prompts[2], ' '),
]

# Here is the first section - title, description and questions
# Section 1 title and descripion
section1 = Section('\n\n*****************************\n     About Dogs...\n*****************************', '\nThis round of questions is all about dogs, what else!.')
# Section 1 questions
section1_question_prompts = [
   '\n---------- Dog Question 1 ----------\nWhich is your favourite of the following breeds?\n(a) Staffies.\n(b) German Shepherds.\n(c) Chihuahuas.\n\n',
   '\n---------- Dog Question 2 ----------\nLong fur or short?\n(a) Long.\n(b) Short.\n(c) I don\'t mind, I will love them all :)\n\n',
   '\n---------- Dog Question 3 ----------\nHow often do you take your dog/dog\'s for walks?\n(a) Every day!\n(b) A few times a week.\n(c) Not as often as I would like.\n\n',
]
section1_questions = [
    Question(section1_question_prompts[0], ' '),
    Question(section1_question_prompts[1], ' '),
    Question(section1_question_prompts[2], ' '),
]



# Here is the second section - title, description and questions
# Section 2 title and descripion
section2 = Section('\n\n*****************************\n      About Your Pets...\n*****************************', '\nThis round of questions is all about your pets.')
# Section 2 questions
section2_question_prompts = [
   '\n---------- Pets Question 1 ----------\nWhat kind of pets do you have?\n(a) Dogs\n(b) Cats.\n(c) Both or Something Else!\n\n',
   '\n---------- Pets Question 2 ----------\nDo your pets all get along?\n(a) Yes, they all love each other.\n(b) Mostly, but not all of the time.\n(c) No :(\n\n',
   '\n---------- Pets Question 3 ----------\nWhat do you do with your pets when you go on holidays?\n(a) They come with me of course!\n(b) My family look after them.\n(c) They love staying at the kennels\n\n',
]
section2_questions = [
    Question(section2_question_prompts[0], ' '),
    Question(section2_question_prompts[1], ' '),
    Question(section2_question_prompts[2], ' '),
]

# Here is the third section - title, description and questions
# Section 3 title and descripion
section3 = Section('\n\n*****************************\n    About pet adoption...\n*****************************', '\nWe\'d like to hear your thoughts on Pet Adoption.')
# Section 3 questions
section3_question_prompts = [
   '\n---------- Adoption Question 1 ----------\nWhich Pet Rescue\'s have you heard the most about?\n(a) RSPCA.\n(b) Pet Rescue WA.\n(c) Something else...\n\n',
   '\n---------- Adoption Question 2 ----------\nAre you currently looking to adopt a pet?\n(a) Yes!\n(b) No\n(c) Not yet, but soon\n\n',
   '\n---------- Adoption Question 3 ----------\nHave you ever volunteered with animals?\n(a) Yes, all the time.\n(b) I have in the past.\n(c) I would love to in the future...\n\n',
]
section3_questions = [
    Question(section3_question_prompts[0], ' '),
    Question(section3_question_prompts[1], ' '),
    Question(section3_question_prompts[2], ' '),
]

# Section 1 Function
def run_section1(section1_questions):
    print(section1.section_title)
    print(section1.description)
    for question in section1_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'c']:
                print('***** Great, you answered ' + answer)
                break
            else:
                print('***** Nope, not valid. Try that again. I\'m only accepting a, b or c.')
# Section 2 Function
def run_section2(section2_questions):
    print(section2.section_title)
    print(section2.description)
    for question in section2_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'c']:
                print('***** Great, you answered ' + answer)
                break
            else:
                print('***** Nope, not valid. Try that again. I\'m only accepting a, b or c.')
# Section 3 Function
def run_section3(section3_questions):
    print(section3.section_title)
    print(section3.description)
    for question in section3_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'c']:
                print('***** Great, you answered ' + answer)
                break
            else:
                print('***** Nope, not valid. Try that again. I\'m only accepting a, b or c.')


#this is the start of the survey qualifying questions, but it isn't executed until the bottom
def run_survey(qualifying_questions):
    sections_to_show = []
    for question in qualifying_questions:
        while True:
            answer = input(question.prompt)
            if answer.lower() in ['a', 'b', 'yes', 'no']:
                # if the answer is valid then process it
                print('***** Awesome, you answered ' + answer)
                if answer.lower() in ['a', 'yes']:
                    # if the answer is yes, then save this section for later
                    sections_to_show.append('a')
                else:
                    sections_to_show.append('b')
                break
            else:
                print('***** Hmmmmmmm, that\'s not quite right...Please try again.')
    if sections_to_show[0] == 'a':
        run_section1(section1_questions)
    if sections_to_show[1] == 'a':
        run_section2(section2_questions)
    if sections_to_show[2] == 'a':
        run_section3(section3_questions)

# This starts the survey
run_survey(qualifying_questions)

# This is the end message
print('\nThanks so much for taking the survey. Have a great day!\n\n')
