from replit import db
def database():
    choice = input("Do \"set\" or \"get\" >>> ").lower()
    if choice == "set":
        db["leaderboard0"] = "2334245:jeff"
        db["leaderboard1"] = "345:bob"
        db["leaderboard2"] = "345:tim"
        db["leaderboard3"] = "233245442:max"
        database()
    else:
        matches = db.prefix("leaderboard")
        leaderboard = []
        for i in range(len(matches)):
            value = db[matches[i]]
            leaderboard.append(value)
        leaderboard.sort()

        def printlead():
            print("Position".ljust(20) + "Username".center(20) + "Points".rjust(20))
            for i in range(len(leaderboard)):
                for j in range(len(leaderboard[i])):
                    letter = leaderboard[i][j]
                    if letter == ":":
                        points = leaderboard[i][0:j-1]
                        username = leaderboard[i][j+1:]
                        position = str(i+1)
                print(position.ljust(20) + username.center(20) + points.rjust(20))
        printlead()
        database()


database()
