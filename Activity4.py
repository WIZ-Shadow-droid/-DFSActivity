from collections import deque

maze = {
    "A": ["B", "C"],   # A = Entrance
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["H"],
    "G": [],
    "H": []            # H = Notebook room
}

def dfs_find_path(maze, start, goal, path=None):
    if path is None:
        path = [start]
    else:
        path = path + [start]

    print ("Visiting", start, " | Path so Far:", path)

    if start == goal:
        return path
    for notebookroom in maze[start]:
        if notebookroom not in path:
            result = dfs_find_path(maze, notebookroom, goal, path)
            if result:
                return result
    return None
print(dfs_find_path(maze, "A", "H"), "NoteBookRoom FInd")

#1.Aliah start at A

#2.DFS visit first at Room A

#3.Aliah follow the path of Room A and use the Element iside it which is B and C and continue to the Elements of B which is D and E
#and continue going to the first element of B since D doesnt have an element she continue to element E and go to G 
#since G doesnt have an element she return to A and go to the next element (C) after that she use the element inside C and continue to F and Find her lost NoteBook

#4. Because DFS wants to check all the elements inside the value so it can properly go through its goal

#5.It Returns automaticaly to the previus value and check the next element inside the value
