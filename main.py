from classes import HeadHunter, Superjob, Connector
from pprint import pprint

def main():
    """
    Функция для взаимодействия с пользователем.
    """
    vacancies_json = []
    keyword = input("Введите ключевое слово для поиска\n")

    hh = HeadHunter(keyword)
    sj = Superjob(keyword)
    for api in (hh, sj):
        api.get_vacancies(pages_count=2)
        vacancies_json.extend(api.get_formatted_vacancies())

    connector = Connector(keyword=keyword, vacancies_json=vacancies_json)

    while True:
        command = input(
            "1 - Вывести список вакансий;\n"
            "2 - Отсоритровать по минимальной зарплате;\n"
            "3 - Отсоритровать по минимальной зарплате (DESK);\n"
            "4 - Отсоритровать по максимальной зарплате;\n"
            "exit - для выхода.\n"
        )
        if command.lower() == 'exit':
            break
        elif command == "1":
            vacancies = connector.select()
        elif command == "2":
            vacancies = connector.sorted_vacancies_by_salary_from_asc()
        elif command == "3":
            vacancies = connector.sorted_vacancies_by_salary_from_desc()
        elif command == "4":
            vacancies = connector.sorted_vacancies_by_salary_to_asc()


        for vacancy in vacancies:
            print(vacancy, end='\n\n')


if __name__ == "__main__":
    main()