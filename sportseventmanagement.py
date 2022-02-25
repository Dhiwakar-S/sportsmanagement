#import sqllite 3
j=5
while (j==5):
    print("WELCOME TO SPORTS EVENT MANAGEMENT")
    print('''press 1 for BATMINTION
         press 2 for BASKETBALL
         press 3 for tennis''')
    evi=int(input())
    if (evi==1):
        tms=[]
        for i in range(1,6):
            name=input("Enter your Name: ")
            tms.append(name)

        print(tms)
        print("                                *** WELCOME TO BATMINTION TOURNAMENT ***                       ")
        print('''Mixed Team Event
        A team consists of a minimum of two men and two women and a maximum of five men and five women. With the larger teams, substitutions and changes to the selection of players for ties during the tournament are allowed.

        The Team Event is conducted in two stages: a round-robin group stage followed by a knockout phase (quarter-finals, semi-finals, a bronze medal final and a gold medal final). The event will comprise of 16 team slots allocated in accordance with BWF World Rankings. Teams are divided in the group stage of the competition into four groups of four teams.  All teams in the designated group play each other to establish a final ranking order, based on the total number of matches won. The top two teams from each group progress into the knockout stage, with a draw conducted to decide the quarter-final ties.

        A tie consists of five matches: Men’s and Women’s Singles, Men’s and Women’s Doubles, and Mixed Doubles. No player may play in more than two matches in a tie. A team must win three matches in a tie to be successful. Each match is the best of three games.

        INDIVIDUAL EVENTS
        The individual events are straight knockout competitions, with the number of rounds depending on the number of entries, with options to have a round of 128, 64, 32 and 16 prior to quarter-finals, semi-finals, a bronze medal final and a gold medal final. Each match is the best of three games.

        The match order for the first round of individual events is determined by a competition draw and takes into account event seedings based on BWF World Rankings.

        RULES
        Field of Play

        The court is a 13.40m x 5.18m rectangle for singles and a 13.40m x 6.10m rectangle for doubles. The same court is used for Singles and Doubles contests; only the line marks differ. The court is divided into two equal parts by a net attached to the posts at a height of 1.55m.

        THE CONTEST

        An umpire, aided by a service judge and line judges, presides over a Badminton contest. Before the beginning of the contest, the umpire flips a coin. The winning athlete or pair can choose to serve or receive first or choose its side of the court.

        To score a point, athletes have to hit the shuttlecock over the net with their rackets so that it lands on the opponent’s side. An athlete or pair loses the point if the shuttlecock hits the net, lands outside the court or if he or she commits a fault. The most common faults occur when:

        The shuttlecock hits the athlete
        The athlete’s racket or body touches the net
        The shuttlecock hits the ground before passing over the net
        The shuttlecock is hit twice.


        SERVICE

        Serves must be diagonal
        The server’s feet must be touching the ground
        The serve must be made from below the waist
        Players change ends after each game and in the third game when a side first scores 11 points
        During service in doubles, the partners can take up any position on their respective courts which do not unsight the opposing server or receiver
        During service in singles, the players serve from and receive in their respective right service courts when the server has not scored or has scored an even number of points in that game. Players serve from and receive in their respective left service courts when the server has scored an odd number of points in that game.


        SCORING

        A match is the best of three games.
        The winner of each game is the first player(s) to reach 21, by two clear points.
        At 20-all, the side which scores two consecutive points shall win that game.
        At 29-all, the side scoring the 30th point shall win that game.
        A point is scored by winning a rally. Points are scored regardless of who is serving and the side who wins the point serves the next point.
        The side winning a game serves first in the next game.
        Equipment
        Racket

        A racket has the following parts: handle (known as the grip), shaft, throat and head, which is the stringed area. It weighs between 85g and 100g. Its length and width must not exceed 68cm and 23cm respectively.

        SHUTTLECOCK

        The shuttlecock is made of a semi-spherical piece of cork coated with leather. On it are attached 16 real goose feathers forming a cone. A shuttlecock must weigh between 4.74g and 5.5g.

        UNIFORM

        Badminton athletes wear shorts/skirts and short sleeved shirts and any combination of colours is permissible. In doubles both players must wear the same clothing, which has their name and country on the back of the shirts. Shoes are usually flat but there are no official standards or specifications.

        SPORTS JARGON
        ACE: An outright point from a serve that is not even touched by the receiver.

        LIFT: A shot played from beneath the height of the net, normally played high to the back of the court.

        SMASH: A hard, overhead shot, hit directly down into the opposition’s court.

        CLEAR: A shot hit deep into the opponent’s court.''')
        print('''***NOTE:The Regisition open on 03 march 2022,Time:6:00AM
        and close on 13 march 2022,Time:11:59PM.The Team information will
        be get stored.please don't forgot your USER ID and PASSWORD.
        The Entre Fess will be informed by 11th Evening 6:00 PM.''')
    elif (evi==2):
        tms=[]
        for i in range(1,9):
            name=input("Enter your Name: ")
            tms.append(name)

        print(tms)
        print("                       ***WELCOME TO BASKETBALL TOURNMENT***                        ")
        print('''RULES:
                      Each team shall consist of:
                        • No more than 12 team members entitled to play, including a captain.
                        • A head coach.
                        • A maximum of 8 accompanying delegation members, including a maximum of 2
                        assistant coaches who may sit on the team bench. In case a team has assistant
                        coaches, the first assistant coach shall be entered on the scoresheet.
                        During playing time 5 team members from each team shall be on the playing court
                          and may be substituted.
                  UNIFORMS:
                         The uniform of all team members shall consist of:
                                • Shirts of the same dominant colour front and back as the shorts. If shirts have
                                sleeves they must end above the elbow. Long sleeved shirts are not permitted.
                                All players must tuck their shirts into their playing shorts. 'All-in-ones' are
                                permitted.
                                • T-shirts, regardless of the style, are not permitted to be worn under the shirts.
                                • Shorts of the same dominant colour front and back as the shirts. The shorts must
                                end above the knee.
                                • Socks of the same dominant colour for all team members. Socks need to be
                                visible.
                  OTHER_EQUIPMENT:
                                  All equipment used by players must be appropriate for the game. Any equipment that
                                  is designed to increase a player's height or reach or in any other way give an unfair
                                  advantage is not permitted.
                                  Players shall not wear equipment (objects) that may cause injury to other players.
                                • The following are not permitted:
                                ▬ Finger, hand, wrist, elbow or forearm guards, helmets, casts or braces made
                                of leather, plastic, pliable (soft) plastic, metal or any other hard substance,
                                even if covered with soft padding.
                                ▬ Objects that could cut or cause abrasions (fingernails must be closely cut).
                                ▬ Hair accessories and jewellery.
                                • The following are permitted:
                                ▬ Shoulder, upper arm, thigh or lower leg protective equipment if sufficiently
                                padded.
                                ▬ Arm and leg compression sleeves.
                                ▬ Headgear. It shall not cover any part of the face entirely or partially (eyes,
                                nose, lips etc.) and shall not be dangerous to the player wearing it and/or to
                                other players. The headgear shall not have opening/closing elements around
                                the face and/or neck and shall not have any parts extruding from its surface.
                                ▬ Knee braces.
                                ▬ Protector for an injured nose, even if made of a hard material.
                                ▬ Non-coloured transparent mouth guard.
                                ▬ Spectacles, if they do not pose a danger to other players.
                                ▬ Wristbands and headbands, maximum of 10 cm wide textile material.
                                ▬ Taping of arms, shoulders, legs etc.
                                ▬ Ankle braces.
                                All players on the team must have all their arm and leg compression sleeves,
                                headgear, wristbands, headbands and tapings of the same solid colour.
                  PLAYER_INJURIES:
                             1. In the event of injury to a player(s), the referees may stop the game.
                             2.If the ball is live when an injury occurs, the referee shall not blow his whistle until the
                               team in control of the ball has shot for a field goal, lost control of the ball, withheld
                               the ball from play or the ball has become dead. If it is necessary to protect an injured
                               player, the referees may stop the game immediately.''')
        print('''***NOTE:The Regisition open on 03 march 2022,Time:6:00AM
        and close on 13 march 2022,Time:11:59PM.The Team information will
        be get stored.please don't forgot your USER ID and PASSWORD.
        The Entre Fess will be informed by 11th Evening 6:00 PM.''')
    elif (evi==3):
         tms=[]
         for i in range(1,5):
             name=input("Enter your Name: ")
             tms.append(name)

         print(tms)
         print("                              ***WELCOME TO TENNIS TOURNMENT***                    ")
         print('''Each player or team has a maximum of one bounce after the ball has been hit by their opponent to return the ball over the net and within the boundaries of the court. In wheelchair tennis, players get a maximum of two bounces. When a player then fails to return the ball into the correct court, the opponent wins a point.
                   The aim of tennis is to win enough points to win a game, enough games to win a set, and enough sets to win a match.
                   STARTING THE MATCH
                    Before warming up with your opponent, either player or team will spin their racquet and the winner of the spin will have some options to choose from. They can choose one of these 3 options:
                   To serve or receive
                    The side of the court
                    Or defer their choice to their opponent --but the opponent cannot defer back
                    Once the winner of the toss chooses one of the options above, the opponent has the remaining choice.
                    POINT SYSTEM
                    Tennis has a different point system than most sports. Before we go into detail, here is your guide to scoring a game:
                    0 points= Love
                    1 point = 15
                    2 points= 30
                    3 points= 40
                    Tied score= All
                    40-40 = Deuce
                    Server wins deuce point = Ad-In
                    Receiver wins deuce point = Ad-Out''')
         print('''***NOTE:The Regisition open on 03 march 2022,Time:6:00AM
         and close on 13 march 2022,Time:11:59PM.The Team information will
         be get stored.please don't forgot your USER ID and PASSWORD.
         The Entre Fess will be informed by 11th Evening 6:00 PM.''')
    print("To continue press 5 or press 6")
    j=int(input())
