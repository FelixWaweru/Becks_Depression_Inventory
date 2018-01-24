print('\033[1m' + "Beck's Depression inventory")
total = []
category = ['Sadness',
            'Pessimism',
            'Past Failure',
            'Loss of Pleasure',
            'Guilty Feelings',
            'Punishment Feelings',
            'Self Dislike',
            'Self Criticism',
            'Suicidal Thoughts',
            'Crying',
            'Restlessness',
            'Loss of interest',
            'Indecisiveness',
            'Worthlessness',
            'Loss of Energy',
            'Change in sleep patterns',
            'Irritability',
            'Change In Appetite',
            'Ability to concentrate',
            'Tiredness or Fatigue',
            'Loss of sexual Interest']

ans0 = ['I do not feel sad.',
        'I am not discouraged about my future.',
        'I do not feel like a failure.',
        'I get as much pleasure as ever from the things I enjoy.',
        'I don‘t feel particularly guilty.',
        'I don‘t feel I am being punished',
        'I feel the same about myself as ever.',
        'I don’t criticize or blame myself more than usual.',
        'I don’t have any thoughts of killing myself.',
        'I don’t cry anymore than I used to.',
        'I am no more restless or wound up than usual.',
        'I have not lost interest in other people or activities.',
        'I make decisions about as well as ever.',
        'I do not feel I am worthless.',
        'I have as much energy as ever',
        'l have not experienced any change in my sleeping pattern.',
        'I am no more irritable than usual.',
        'I have not experienced any change in my appetite.',
        'I can concentrate as well as ever.',
        'I am no more tired or fatigued than usual.',
        'I have not noticed any recent change in my interest in sex.']

ans1 = ['I feel sad much of the time.',
        'I feel more discouraged about my future than I used to be.',
        'I have failed more than I should have.',
        'I don’t enjoy things as much as I used to.',
        'I feel guilty over many things I have done or should have done.',
        'I feel I may be punished.',
        'I have lost confidence in myself.',
        'I am more critical of myself than I used to be.',
        'I have thoughts of killing myself. but I would not carry them out.',
        'I cry more than I used to.',
        'I feel more restless or wound up than usual.',
        'I am less interested in other people or things than before.',
        'I ﬁnd it more difficult to make decisions than usual.',
        'I don’t consider myself as worthwhile and useful as I used to.',
        'I have less energy than I used to have.',
        'I sleep somewhat more than usual or I sleep somewhat less than usual.',
        'I am more irritable than usual.',
        'My appetite is somewhat less than usual or My appetite is somewhat greater than usual.',
        'I can’t concentrate as well as usual.',
        'I get more tired or fatigued more easily than usual.',
        'I am less interested in sex than l used to be.']

ans2 = ['I am sad all the time.',
        'I do not expect things to work out for me.',
        'As I look back. I see a lot of failures.',
        'I get very little pleasure from the things I used to enjoy.',
        'I feel quite guilty most of the time.',
        ' expect to be punished.',
        'I am disappointed in myself.',
        'I criticize myself for all of my faults.',
        'I would like to kill myself.',
        'I cry over every little thing.',
        'I am so restless or agitated that its hard to stay still.',
        'I have lost most of my interest in other people or things.',
        'I have much greater difficulty in making decisions than I used to.',
        'I feel more worthless as compared to other people.',
        'I don‘t have enough energy to do very much.',
        ' I sleep a lot more than usual or I sleep a lot 1ess than usual.',
        'I am much more irritable than usual.',
        'My appetite is much less than usual or My appetite is much greater than usual.',
        'Its hard to keep my mind on anything for very long.',
        'I am too tired or fatigued to do a lot of the things I used to do.',
        'I am much less interested in sex now.']

ans3 = ['I am so sad or unhappy that l can’t stand it.',
        'I feel my future is hopeless and will only get',
        'I feel l am a total failure as a person.',
        'I can‘t get any pleasure from the things I used to enjoy.',
        'I feel guilty all of the time.',
        'I feel I am being punished.',
        ' I dislike myself.',
        ' I blame myself for everything had that happens.',
        'I would kill myself if I find the chance.',
        'I feel like crying, but I can’t.',
        'I am so restless or agitated that I have to keep moving or doing something.',
        'Its hard to get interested in anything.',
        'I have trouble making any decisions.',
        'I feel utterly worthless.',
        'I dont have enough energy to do anything.',
        'I sleep most of the day or I wake up 1-2 hours early and cant get back to sleep.',
        'I am irritable all the time.',
        'I have no appetite at all or I crave food all the time.',
        'I ﬁnd I cant concentrate on anything.',
        'I am too tired or fatigued to do most of the things I used to do.',
        'I have lost interest in sex completely.']



def questions():
    rounds = 0
    while rounds < 21:
        print('Question ')
        print(rounds + 1)
        print('\033[1m' + category[rounds] + ':')
        print('0 :' + ans0[rounds])
        print('1 :' + ans1[rounds])
        print('2 :' + ans2[rounds])
        print('3 :' + ans3[rounds])
        q1 = input('Answer: \n')
        print(q1)
        # if q1 is not 0 or 1 or 2 or 3:
        #     print('Please select a valid answer')
        #     rounds = rounds
        if q1 is 0 or 1 or 2 or 3:
            total.append(int(q1))
            rounds = rounds + 1
            print('\n')
    else:
        print(total)
        print(sum(total))


questions()
if 1<= sum(total) <= 10:
    print('Normal ups and downs')
elif 11<= sum(total) <= 16:
    print('Mild mood disturbance')
elif 17<= sum(total) <= 20:
    print('Borderline Depression')
elif 21<= sum(total) <= 30:
    print('Moderate Depression')
elif 31<= sum(total) <= 40:
    print('Severe Depression')
elif 40<= sum(total):
    print('Extreme Depression')