def read_content_from_file(filepath: str):
    """
    Зчитує вміст файлу і повертає його у вигляді списку рядків.

    Args:
        filepath (str): Шлях до файлу, який потрібно зчитати.

    Returns:
        list: Список, що містить рядки файлу.

    Raises:
        FileNotFoundError: Якщо файл, вказаний за допомогою 'filepath', не існує.
        PermissionError: Якщо у користувача немає прав на читання файлу.
        UnicodeDecodeError: Якщо виникає проблема з декодуванням вмісту файлу.
        OSError: Для будь-яких інших пов'язаних з операційною системою помилок.
    """
    with open(filepath, "r") as f_o:
        return f_o.readlines()
