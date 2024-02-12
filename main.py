import numpy as np

class SuccessiveEstimation:
  def __init__(self):
    print("""⢀⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡟⣿⣿⢀⣶⣶⣴⣶⣶⠀⣠⣶⣶⣦⡄⢀⣴⣶⣶⣦⡀⣠⣴⣶⣶⣄⠀⣤⣶⣶⣦⡀⣠⣶⣶⣦⣄⢺⣿⣿⣶⣶⡄⣴⣶⣆⣤⣶⣶⣦⡀
⢿⣿⣿⣦⣄⠈⣿⣿⣿⣿⣿⢸⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣏⣿⣿⡾⣿⣿⣼⠿⠇⣿⣿⣽⠿⠿⢸⣿⣿⢻⣿⣷⣿⣿⣿⣿⣿⣹⣿⣷
⣤⣽⡿⣿⣿⣤⣿⣿⣿⣿⣿⢸⣿⣿⢠⣤⣄⣿⣿⣿⣤⣤⣬⣿⣿⡟⣿⣿⣧⣙⣿⣿⣷⣆⣙⣿⣿⣿⣦⢸⣿⣿⠸⣿⣿⣿⣿⢸⣿⣿⢻⣿⣿
⢿⣿⣧⣿⣿⠟⣿⣿⣿⣿⣿⠘⣿⣿⣼⣿⡿⢻⣿⣿⣿⣿⠏⣿⣿⣧⣿⣿⠋⣿⣿⣼⣿⡟⢿⣿⣮⣿⣿⢸⣿⣿⠀⣿⣿⣿⡏⢸⣿⣿⣼⣿⡟
⠈⠙⠛⠛⠉⠀⠉⠛⠉⠉⠙⠀⠈⠙⠛⠋⠀⠀⠉⠛⠛⠉⠀⠈⠉⠛⠋⠁⠀⠈⠙⠛⠋⠀⠈⠙⠛⠋⠁⠈⠉⠉⠀⠉⠉⠉⠁⠀⠉⠙⠛⠉⠀
⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⠇⣀⣠⣀⣀⢀⣶⣶⣇⢸⣿⣿⢀⣀⣀⣀⣀⡀⣀⣀⡀⠀⣀⣤⣀⣀⢀⣷⣶⣆⣼⣿⣿⠀⢀⣠⣄⣀⠀⢀⣠⣄⣀⣀⡀⠀⠀
⠀⠀⣿⣿⣷⣤⢸⣿⣿⢻⣿⡟⣿⣿⡿⢻⣿⣿⢸⣿⣿⢻⣿⣿⢻⣿⡇⣼⣿⡟⣿⣿⡾⣿⣿⡿⢻⣿⣿⢰⣿⣿⢻⣿⣧⢸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⣿⣿⡿⠿⠈⢿⣿⣿⣦⡀⣿⣿⡇⢸⣿⣿⢸⣿⣿⢸⣿⣿⢸⣿⡇⢉⣽⣿⣿⣿⡇⣿⣿⡇⢸⣿⣿⢸⣿⣿⢸⣿⣿⢸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⣿⣿⣧⣤⣴⣶⣿⣻⣿⡇⣿⣿⣇⣸⣿⣿⢸⣿⣿⢸⣿⣿⢸⣿⡇⣿⣿⣇⣿⣿⡇⣿⣿⣇⣸⣿⣿⢸⣿⣿⣸⣿⡿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠿⠿⠿⠿⠇⠛⠿⠿⠟⠁⠙⠻⠿⠿⠿⠿⠸⠿⠿⠸⠿⠿⠸⠿⠇⠙⠿⠟⠿⠿⠇⠙⠻⠿⠻⠿⠿⠀⠛⠿⠿⠟⠁⠸⠿⠟⠿⠿⠇⠀⠀


Welcome to Successive Estimation Solver!

Explanation:
To use this program, please provide the factors of the equations you want to solve.
Enter each equation's coefficients separated by spaces, and press Enter after each equation.
For example, 
if you have the equation '5x - y = 3', enter '5 -1 3'.
If the equation is '5x - y + z = 3', enter '5 -1 1 3'.
          
You can enter as many equations as you need.
!! Note that it is recommended that the user gives the equations organized howerver the program may handle it
""")
    while True:
      print("First give the factors of the Equations you want to solve")
      self.get_factors()
      self.print_matrix()
      print("Checking if the matrix is diagonally dominant")
      if self.is_diagonally_dominant():
        print("The matrix is diagonally dominant and can be used with the Jacobi method.")
        break
      else:
        print("The matrix is not diagonally dominant\nTrying to sort the matrix...")
        self.matrix = self.sort_matrix()
        if self.is_diagonally_dominant():
          print("The Matrix is now organized and here is it")
          self.print_matrix()
          break
        else:
          print("The matrix may not converge with the Jacobi method.")
    
    print("Now enter the initial guess (press enter for zeroes)")
    self.initial_guess = input()
    if self.initial_guess:
      self.initial_guess = list(map(lambda x: int(x), self.initial_guess.split()))
    else:
      self.initial_guess = [0] * len(self.matrix)

    print(self.initial_guess)
    self.sep = "="*50
    #now startting the real part of the program : successive estimation
    print(self.sep)
    print("The right solution of these equations is:")
    self.right_solution = self.get_right_solution()
    self.print_values(self.right_solution)


    print(self.sep, self.sep, sep="\n")
    print("Jacobi First iteration gives:")
    self.current_jacobi_guess = self.get_jacobi_iteration(self.initial_guess)
    self.print_values(self.current_jacobi_guess)
    self.jacobi_efficeincy = self.calculate_efficiency(self.current_jacobi_guess, self.right_solution)
    print("The efficiency of the Jacobi method is:", self.jacobi_efficeincy, end="\n\n")

    self.current_gauss_guess = self.get_gauss_iteration(self.initial_guess)
    print("Gauss-Siedle First iteration gives:")
    self.print_values(self.current_gauss_guess)
    self.gauss_efficiency = self.calculate_efficiency(self.current_gauss_guess, self.right_solution)
    print("The efficiency of Gauss-Siedle Method:", self.gauss_efficiency)
    print(self.sep)
    num = 2
    while True:
      print("Enter the number of steps to show next or leave it empty for 1 iteration(exit or e to exit program)")
      self.steps = input("steps: ")
      if not self.steps:
        self.print_report(num)
        num += 1
      else:
        if self.steps.lower() in ['e', "exit"]:
          print("Thank you for using our program")
          break
        else:
          try:
            self.steps = int(self.steps)
            for i in range(self.steps):
              self.print_report(num)
              num += 1
          except ValueError:
            print("Invalid input.")



  def get_factors(self):
    self.matrix = list()
    input_data = input("Equation 1: ")
    factors = list(map(lambda x: int(x), input_data.split()))
    self.matrix.append(factors)
    for i in range(2, len(factors)):
      input_data = input(f"Equation {i}: ")
      factors = list(map(lambda x: int(x), input_data.split()))
      self.matrix.append(factors)

  def print_matrix(self):
    for listy in self.matrix:
      for element in listy[:-1]:
        print(element,end=" ")
      print("|", listy[-1])

  def is_diagonally_dominant(self):
    n = len(self.matrix)
    for i in range(n):
        diagonal = abs(self.matrix[i][i])
        other_elements_sum = sum(abs(self.matrix[i][j]) for j in range(n) if j != i)
        if diagonal <= other_elements_sum:
            return False
    return True
  
  def sort_matrix(self):
    rows = len(self.matrix)
    cols = len(self.matrix[0])

    sorted_matrix = [[0] * cols for _ in range(rows)]

    for row in self.matrix:
        real_row = row[:-1]
        maximum = real_row[0]
        row_number = 0
        for pos, element in enumerate(real_row[1:]):
            if abs(element) > abs(maximum):
                maximum = element
                row_number = pos + 1
        sorted_matrix[row_number] = row

    return sorted_matrix
  
  def get_jacobi_iteration(self, guess):
    n = len(self.matrix)
    x = guess
    self.current_jacobi_guess = [0] * n
    for i in range(n):
        sum_ = sum(self.matrix[i][j] * x[j] for j in range(n) if j != i)
        self.current_jacobi_guess[i] = (self.matrix[i][-1] - sum_) / self.matrix[i][i]
    return self.current_jacobi_guess
  
  def get_right_solution(self, tolerance=1e-10):
    A = np.array([row[:-1] for row in self.matrix])  # Extract the coefficient matrix
    b = np.array([row[-1] for row in self.matrix])   # Extract the constant terms
    solution = np.linalg.solve(A, b)
    self.right_solution = [round(x, -int(np.floor(np.log10(tolerance)))) for x in solution]
    return self.right_solution
  
  def calculate_efficiency(self, actual_solution, target_solution):
      num_variables = len(actual_solution)
      errors = [abs(actual_solution[i] - target_solution[i]) / max(abs(target_solution[i]), 1) for i in range(num_variables)]
      average_relative_error = sum(errors) / num_variables
      efficiency = 100 - average_relative_error * 100
      return round(efficiency, 4)

  def get_gauss_iteration(self, guess):
    num_variables = len(self.matrix)
    gauss_guess = guess.copy()
    for i in range(num_variables):
        sum_ = sum(self.matrix[i][j] * gauss_guess[j] for j in range(num_variables) if j != i)
        gauss_guess[i] = (self.matrix[i][-1] - sum_) / self.matrix[i][i]
    return gauss_guess
  
  def print_report(self, num):
    self.current_jacobi_guess = self.get_jacobi_iteration(self.current_jacobi_guess)
    self.jacobi_efficeincy = self.calculate_efficiency(self.current_jacobi_guess, self.right_solution)
    self.current_gauss_guess = self.get_gauss_iteration(self.current_gauss_guess)
    self.gauss_efficiency = self.calculate_efficiency(self.current_gauss_guess, self.right_solution)

    print(self.sep, sep="\n")
    print("Iteration number:", num)
    print("Jacobiiteration gives:")
    self.print_values(self.current_jacobi_guess)
    print("The efficiency of the Jacobi method is:", self.jacobi_efficeincy)
    if self.jacobi_efficeincy == 100:
      print("The jacobi Method has reached the right soluiton perfectly")
    print()

    print("Gauss-Siedle iteration gives:")
    self.print_values(self.current_gauss_guess)
    print("The efficiency of Gauss-Siedle Method:", self.gauss_efficiency)
    if self.gauss_efficiency == 100:
      print("The Gauss-Siedld Method has reached the right soluiton perfectly")
    print(self.sep)


  def print_values(self,listy):
    for i in range(1, len(listy)+1):
      print(f"x{i} = {listy[i-1]}")



if __name__ =="__main__":
  SuccessiveEstimation()