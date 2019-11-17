class Matrix:

    letters_to_coords = {}

    def __init__(self, letters_matrix):
        self.letters_matrix = letters_matrix
        for row in range(len(letters_matrix)):
            for col in range(len(letters_matrix[row])):
                self.letters_to_coords[letters_matrix[row][col]] = (row, col)

    def coords(self, letter):
        return self.letters_to_coords[letter]

    def letter(self, coords):
        return self.letters_matrix[coords[0]][coords[1]]
