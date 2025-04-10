def points_mot(mot):
    l = len(mot)
    if l == 3 or l == 4:
        return 1
    elif l == 5:
        return 2
    elif l == 6:
        return 3
    elif l == 7:
        return 5
    elif l >= 8:
        return 11
    return 0

def mot_valide_dans_grille(grille, mot):
    def dfs(i, j, index, visites):
        if index == len(mot):
            return True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) not in visites:
                    if grille[ni][nj] == mot[index]:
                        if dfs(ni, nj, index + 1, visites | {(ni, nj)}):
                            return True
        return False

    mot = mot.upper()
    for i in range(4):
        for j in range(4):
            if grille[i][j] == mot[0]:
                if dfs(i, j, 1, {(i, j)}):
                    return True
    return False
