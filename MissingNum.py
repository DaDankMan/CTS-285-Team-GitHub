
# By Damian
import random

def get_difficulty_range():
    print("Select difficulty level:")
    print("1. Easy (0 to 10)")
    print("2. Medium (0 to 30)")
    print("3. Hard (0 to 100)")
    print("4. EXTREME (-500 to 500)")
    print("5. IMPOSSIBLE (Good luck, chump!)")

    while True:
        choice = input("Enter 1-5: ")
        if choice == '1':
            return 0, 10, False
        elif choice == '2':
            return 0, 30, False
        elif choice == '3':
            return 0, 100, False
        elif choice == '4':
            return -500, 500, False
        elif choice == '5':
            return 0, 5, True
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

def generate_missing_number_problem(min_val, max_val, impossible=False):
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    # Generate operands
    if operation == '+':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a + b
    elif operation == '-':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a - b
    elif operation == '*':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a * b
    elif operation == '/':
        # Avoid zero division and keep integer result when possible
        b = random.randint(min_val if min_val != 0 else 1, max_val or 1)
        # Ensure b != 0
        if b == 0:
            b = 1
        result = random.randint(min_val, max_val)
        a = b * result
    else:
        return None, None

    if impossible:
        # All blanks shown to the player
        problem = f"_ {operation} _ = _"
        # Return the full answer triple
        correct_answer = (a, b, result)
    else:
        # Randomly choose position to hide (left, right, result)
        missing_position = random.choice(['left', 'right', 'result'])

        if missing_position == 'left':
            problem = f"_ {operation} {b} = {result}"
            correct_answer = a
        elif missing_position == 'right':
            problem = f"{a} {operation} _ = {result}"
            correct_answer = b
        else:  # result
            problem = f"{a} {operation} {b} = _"
            correct_answer = result

    return problem, correct_answer

# Main loop for user interaction
if __name__ == "__main__":
    print("🔢 Welcome to the Missing Number Box Game!")
    print("Fill in the blank (_) to complete the equation.\n")

    min_val, max_val, impossible_mode = get_difficulty_range()

    fails = 0
    question_number = 1

    while True:  # infinite until 3 fails
        problem, correct_answer = generate_missing_number_problem(min_val, max_val, impossible=impossible_mode)
        if problem is None:
            continue

        print(f"Problem {question_number}: {problem}")
        user_input = input("Your answer: ")

        # Handle Impossible mode expecting three numbers
        if impossible_mode:
            # Accept comma- or space-separated three numbers
            cleaned = user_input.replace(',', ' ').strip()
            parts = cleaned.split()
            if len(parts) != 3:
                print("Invalid input! Please enter three numbers separated by commas or spaces (e.g. 3,4,12).\n")
                continue
            try:
                user_answers = []
                for p in parts:
                    if '.' in p:
                        user_answers.append(float(p))
                    else:
                        user_answers.append(int(p))
                # Compare each of the three answers
                a_corr, b_corr, res_corr = correct_answer
                ok = True
                for ua, ca in zip(user_answers, (a_corr, b_corr, res_corr)):
                    if abs(ua - ca) >= 0.001:
                        ok = False
                        break
                if ok:
                    print("✅ Correct!\n")
                else:
                    print(f"❌ Incorrect. The correct answers were {a_corr}, {b_corr}, {res_corr}.\n")
                    fails += 1
                    if fails >= 3:
                        print("💀 Game Over! You reached 3 incorrect answers.")
                        break
            except ValueError:
                print("Invalid input! Please enter numbers only.\n")
                continue
        else:
            # Try to convert input to float or int
            try:
                if '.' in user_input:
                    user_answer = float(user_input)
                else:
                    user_answer = int(user_input)
            except ValueError:
                print("Invalid input! Please enter a number.\n")
                continue

            if abs(user_answer - correct_answer) < 0.001:  # account for float precision
                print("✅ Correct!\n")
            else:
                print(f"❌ Incorrect. The correct answer was {correct_answer}.\n")
                fails += 1
                if fails >= 3:
                    print('''        GAME OVER< YOU SUK!!                                                                                                                 
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                    HAAAAAAAAAAAAAAF                                                    
                                             AAAAE                    KAAAA                                             
                                         AAA                                AAA                                         
                                      AAV                                       AAU                                     
                                   AA                                              AA                                   
                                NAO                                                   AA                                
                               A                                                        AB                              
                             A                                                            CF                            
                           AR                                                               A                           
                          C           AAAAAAAAAAA                      AAAAAAAAAAK           BJ                         
                        RB        UAAAAAAAAALACAAA                   GAAAAAAAAAAAAAAA          A                        
                       FV       AAAAN                                              OAAAL        N                       
                      A        AA                                                      AA        A                      
                     A                                                                            A                     
                    K                                                                              A                    
                    U              V               A                A              I                E                   
                   G              AAAA           AAAAA            AADAA          AAAAA               X                  
                  P                ADAAA       AADGA               WASIAL       ALHR                 N                  
                  J                  DALAA   AAUGA                   LALAA    AAAFA                   B                 
                 C                     AGEAAALLA                       IBJAAAAJCA                     A                 
                 A                       Z J E                             ZX                         W                 
                 A                      AA WROA                         IA R OAA                      US                
                 L                    AAFIH AC AA                      AWMA  AOEAA                     L                
                 X                  AAINA     ADIAA                  AAMAN     AWCA                    A                
                 W                AADTA         AFOAA              AAUAE        RARAAE                 A                
                 U                AAA             AAA              AAA            AAAU                 G                
                 P                                                                                     J                
                 D                                                                                    X                 
                 A                                                                                    D                 
                  Y                                                                                   N                 
                  O                                   GAAAAAAAAAA                                    M                  
                   V                               RAAA         VAAA                                N                   
                                                  AAW  Z  Z        EAA                              A                   
                    R                           FAV  ZYZZ      YYZ   AA                                                 
                     A                          AP Z             Y W  AA                          A                     
                      A                        AO  W             X  X  A                         O                      
                       W                       A  T                 YZ IA                       W                       
                        J                      A                  U Z  JG                      A                        
                         AU                    HA X                 NXTA                     VA                         
                           L                    TA X              X  SA                     H                           
                            WD                    AQ                LA                     E                            
                              MI                   AAFSYZ   ZX   MAAK                   TI                              
                                BF                    AAAAAADAAAAH                    RA                                
                                   AN                                              SAH                                  
                                     LAT                                        XAS                                     
                                         AA                                 PAAQ                                        
                                            HAAAR                       NBAD                                            
                                                  OHMGAAADAAAAAAAAACEV                                                  
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        






''')
                    break

        question_number += 1
