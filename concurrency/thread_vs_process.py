import time
import json
import requests
import concurrent.futures

alphabet = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z'
]


def download_and_write(letter):
    url = "https://www.screener.in/api/company/search/?q={letter}"
    response = requests.get(url.format(letter=letter))
    
    filename = f'{letter}.txt'
    with open(filename, 'w') as f_obj:
        f_obj.write(response.text)
    
    return filename

def load_letters():
    letters_list = []
    for letter in alphabet:
        with open(f'{letter}.txt') as f_obj:
            letters_list += json.loads(f_obj.read())
    
    return letters_list

def process_letters(letter):
    multiplier = 99
    len_name = len(letter['name']) * multiplier
    len_url = len(letter['url']) * multiplier
    result = 0
    for i in range(len_name):
        for j in range(len_url):
            _tmp_result = i * (j / len_name)
            result = _tmp_result if _tmp_result > result else result

    return result



def run_task(tasks_list, func):
    with concurrent.futures.ProcessPoolExecutor() as executor:
    # with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(func, tasks_list)

        for result in results:
            print(result)



if __name__ == '__main__':
    letters_list = load_letters()
    start = time.perf_counter()
    
    # run_task(alphabet, download_and_write)
    
    run_task(letters_list, process_letters)

    end = time.perf_counter()
    time_taken = round(end-start, 5)
    print(time_taken)
