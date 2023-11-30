#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for proName in dir(hidden_4):
        if proName[0] != '_' and proName[1] != '_':
            print(proName)
