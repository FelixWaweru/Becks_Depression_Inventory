import time


class InvalidInputException(BaseException):
    pass


_DEFAULT_ERROR_MSG = "ERROR: please enter a number between 0 and 3!"


print("Beck's Depression inventory")
total = []
category = [
        "Sadness",
        "Pessimism",
        "Past Failure",
        "Loss of Pleasure",
        "Guilty Feelings",
        "Punishment Feelings",
        "Self Dislike",
        "Self Criticism",
        "Suicidal Thoughts",
        "Crying",
        "Irritability",
        "Loss of Interest",
        "Indecisiveness",
        "Feeling (Un)Attractive",
        "Loss of Energy",
        "Change in Sleep Patterns",
        "Tiredness or Fatigue",
        "Change In Appetite",
        "Restlessness",
        "Ability to Concentrate",
        "Loss of Sexual Interest",
        ]

ans0 = [
        "I do not feel sad.",
        "I am not particularly discouraged about the future.",
        "I do not feel like a failure.",
        "I get as much satisfaction out of things as I used to.",
        "I don‘t feel particularly guilty.",
        "I don‘t feel I am being punished.",
        "I don't feel disappointed in myself.",
        "I don't feel I am any worse than anybody else.",
        "I don’t have any thoughts of killing myself.",
        "I don’t cry any more than I used to.",
        "I am no more irritated by things than I ever was.",
        "I have not lost interest in other people.",
        "I make decisions about as well as ever.",
        "I don't feel that I look any worse than I used to.",
        "I can work about as well as before.",
        "I can sleep as well as usual.",
        "I am no more tired or fatigued than usual.",
        "I have not experienced any change in my appetite.",
        "I am no more restless or agitated than usual.",
        "I can concentrate as well as ever.",
        "I have not noticed any recent change in my interest in sex.",
        ]

ans1 = [
        "I feel sad.",
        "I feel discouraged about the future.",
        "I feel I have failed more than the average person.",
        "I don’t enjoy things the way I used to.",
        "I feel guilty a good part of the time.",
        "I feel I may be punished.",
        "I am disappointed in myself.",
        "I am critical of myself for my weaknesses or mistakes.",
        "I have thoughts of killing myself, but I would not carry them out.",
        "I cry more than I used to.",
        "I am slightly more irritated now than usual.",
        "I am less interested in other people than before.",
        "I put off making decisions more than I used to.",
        "I am worried that I am looking old or unattractive.",
        "It takes an extra effort to get started at doing something.",
        "I don't sleep as well as I used to.",
        "I get tired or fatigued more easily than usual.",
        "My appetite is somewhat less or somewhat greater than usual.",
        "I feel more restless or agitated than usual.",
        "I can't concentrate as well as usual.",
        "I am less interested in sex than I used to be."
        ]

ans2 = [
        "I am sad all the time and I can't snap out of it.",
        "I feel I have nothing to look forward to.",
        "As I look back on my life, all I can see is a lot of failures.",
        "I don't get real satisfaction out of anything anymore.",
        "I feel quite guilty most of the time.",
        "I expect to be punished.",
        "I am disgusted with myself.",
        "I blame myself all the time for my faults.",
        "I would like to kill myself.",
        "I cry all the time now.",
        "I am quite annoyed or irritated a good deal of the time.",
        "I have lost most of my interest in other people.",
        "I have greater difficulty in making decisions than I used to.",
        "I feel there are permanent changes in my appearance that make me look unattractive",
        "I have to push myself very hard to do anything.",
        "I sleep a lot more than usual or I sleep a lot less than usual. (1-2 hours difference to before)",
        "I get tired or fatigued from doing almost anything.",
        "My appetite is much less or much greater than usual.",
        "I am so restless or agitated that its hard to stay still.",
        "Its hard to keep my mind on anything for very long.",
        "I am much less interested in sex now.",
       ]

ans3 = [
        "I am so sad and unhappy that I can’t stand it.",
        "I feel the future is hopeless and that things cannot improve.",
        "I feel I am a complete failure as a person.",
        "I am dissatisfied or bored with everything.",
        "I feel guilty all of the time.",
        "I feel I am being punished.",
        "I hate myself.",
        "I blame myself for everything bad that happens.",
        "I would kill myself if I had the chance.",
        "I used to be able to cry, but now I can't cry even though I want to.",
        "I feel irritated all the time.",
        "I have lost all of my interest in other people.",
        "I can't make decisions at all anymore.",
        "I believe that I look ugly.",
        "I can't do any work at all.",
        "I wake up several hours earlier than I used to and cannot get back to sleep.",
        "I am too tired or fatigued to do anything.",
        "I have no appetite at all or I crave food all the time.",
        "I am so restless or agitated that I have to keep moving or doing something.",
        "I find I cant concentrate on anything.",
        "I have lost interest in sex completely.",
        ]


def questions():
    rounds = 0
    while rounds < 21:
        print('Question ', rounds + 1)
        print(category[rounds] + ':', end='\n\n')
        print('0: ' + ans0[rounds])
        print('1: ' + ans1[rounds])
        print('2: ' + ans2[rounds])
        print('3: ' + ans3[rounds])

        q1 = input('\nAnswer: \n')

        answer = int(q1)

        if not 0 <= answer <= 3:
            raise InvalidInputException(_DEFAULT_ERROR_MSG)

        total.append(int(q1))
        rounds = rounds + 1
        print('\n')

    else:
        print(total)
        print(sum(total))


def write_progress_file(file_name="progress.txt"):
    """Progress file is OVERWRITTEN, NOT appended!"""

    with open(file_name, "w") as progress_file:

        if 1 <= sum(total) <= 10:
            print('Normal ups and downs')
            progress_file.write(time.ctime() + " SCORE:" + str(sum(total)) + " MOOD: Normal ups and downs" + "\n")

        elif 11 <= sum(total) <= 16:
            print('Mild mood disturbance')
            progress_file.write(time.ctime() + " SCORE:" + str(sum(total)) + " MOOD: Mild mood disturbance" + "\n")

        elif 17 <= sum(total) <= 20:
            print('Borderline Depression')
            progress_file.write(time.ctime() + " SCORE:" + str(sum(total)) + " MOOD: Borderline Depression" + "\n")

        elif 21 <= sum(total) <= 30:
            print('Moderate Depression')
            progress_file.write(time.ctime() + " SCORE:" + str(sum(total)) + " MOOD: Moderate Depression" + "\n")

        elif 31 <= sum(total) <= 40:
            print('Severe Depression')
            progress_file.write(time.ctime() + " SCORE:" + str(sum(total)) + " MOOD: Severe Depression" + "\n")

        elif 40 <= sum(total):
            print('Extreme Depression')
            progress_file.write(time.ctime() + " SCORE:" + str(sum(total)) + " MOOD: Extreme Depression" + "\n")


if __name__ == '__main__':
    questions()
    write_progress_file()

