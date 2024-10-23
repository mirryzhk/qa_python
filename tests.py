import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Тест №1 Проверка установки и получения жанра для книги
    def test_set_genre_for_book(self, books_collector):
        book_name = 'Книга Тест 1'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Фантастика')
        assert books_collector.get_book_genre(book_name) == 'Фантастика'

    # Тест №2 Проверка установки и получения жанра у несуществующей книги
    def test_get_genre_for_book(self, books_collector):
        book_name = 'Книга Тест 2'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Ужасы')
        assert books_collector.get_book_genre('Неизвестная книга') is None

    # Тест №3 Проверка с помощью параметризации добавления книг с различными названиями
    @pytest.mark.parametrize(
        'book_name,expected',
        [
            ('Книга Тест 3.2', {'Книга Тест 3.2': ''}),
            ('А', {'А': ''}),
            ('А' * 40, {'А' * 40: ''}),
            ('', {}),
            ('А' * 41, {}),
        ]
    )
    def test_add_new_book(self, books_collector, book_name, expected):
        books_collector.add_new_book(book_name)
        assert books_collector.get_books_genre() == expected

    # Тест №4 Проверка установки неверного жанра для книги
    def test_set_fail_genre_for_book(self, books_collector):
        book_name = 'Книга Тест 4'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Несуществующий жанр')
        assert books_collector.get_book_genre(book_name) == ''

    # Тест №5 Проверка вывода книги по жанру
    def test_get_books_with_specific_genre(self, books_collector):
        book_name = 'Книга Тест 5'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Комедии')
        assert books_collector.get_books_with_specific_genre('Комедии') == [book_name]


    # Тест №6 Проверка вывода жанра книги
    def test_get_genre_by_book(self, books_collector):
        book_name = 'Книга Тест 6'
        books_collector.add_new_book(book_name)
        expected_genre = 'Детективы'
        books_collector.set_book_genre(book_name, expected_genre)

        actual_genre = books_collector.get_book_genre(book_name)
        assert actual_genre == expected_genre


    # Тест №7 Проверка наличия книги с одним жанром в детском жанре
    def test_add_horror_book(self, books_collector):
        book_name = 'Книга Тест 7'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Ужасы')

        books_for_children = books_collector.get_books_for_children()
        assert book_name not in books_for_children


    # Тест №8 Проверка добавления книги в избранное
    def test_add_book_to_favorites(self, books_collector):
        book_name = 'Книга Тест 8'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Мультфильмы')
        books_collector.add_book_in_favorites(book_name)

        favorites = books_collector.get_list_of_favorites_books()
        assert book_name in favorites

    # Тест №9 Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self, books_collector):
        book_name = 'Книга Тест 9'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Фантастика')
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)

        favorites = books_collector.get_list_of_favorites_books()
        assert book_name not in favorites