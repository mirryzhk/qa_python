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


# Тест №1 Проверка установки жанра для книги
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        new_book_name = 'Диплом'
        collector.add_new_book(new_book_name)
        assert collector.get_book_genre(new_book_name) == ''
        collector.set_book_genre(new_book_name, 'Комиксы')
        assert collector.get_book_genre(new_book_name) == ''
        collector.set_book_genre(new_book_name, 'Мультфильмы')
        assert collector.get_book_genre(new_book_name) == 'Мультфильмы'


# Тест №2 Проверка получения жанра для книги
    def test_get_genre_for_one_book(self):

        collector = BooksCollector()
        new_book_name = 'Диплом'
        collector.add_new_book(new_book_name)
        assert collector.get_book_genre(new_book_name) == ''
        collector.set_book_genre(new_book_name, 'Комиксы')
        assert collector.get_book_genre(new_book_name) == ''
        collector.set_book_genre(new_book_name, 'Мультфильмы')
        assert collector.get_book_genre(new_book_name) == 'Мультфильмы'


# Тест №3 Проверка с помощью параметризации установки жанра для книг
    @pytest.mark.parametrize(
        'book_name,genre',  # Параметры передали в декоратор в виде единой строки
        [
            ['Книга в жанре мультфильма', 'Мультфильмы'],  # Тестовые данные передали вторым аргументом,
            ['Книга в жанре детектива', 'Детективы'],
            ['Книга в жанре комедии', 'Комедии'],
        ]
    )
    def test_set_get_books_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre


# Тест №4 Проверка с помощью параметризации попытки установки неверного жанра
    @pytest.mark.parametrize(
        'book_name,genre',  # Параметры передали в декоратор в виде единой строки
        [
            ['Книга в жанре мультфильма', 'неправильный жанр'],  # Тестовые данные передали вторым аргументом,
            ['Книга в жанре детектива', 'ДетекТивы'],
            ['Книга в жанре комедии', 'Комедии  '],
        ]
    )
    def test_set_get_books_invalid_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == ''


# Тест №5 Проверка вывода книги в специфическом жанре
    def test_get_books_with_specific_genre(self):
        # Тест №
        collector = BooksCollector()
        for i in range(1, 11):
            book_name = f'book_{i}'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name,'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == [f'book_{i}' for i in range(1, 11)]


# Тест №6 Проверка добавления книг и установки жанра
    def test_get_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
        books_name = [f'book_{i}' for i in range(1, 11)]
        for book_name in books_name:
            collector.add_new_book(book_name)
        assert collector.get_books_genre() == {name: '' for name in books_name}

        for book_name in books_name:
            collector.set_book_genre(book_name, 'Детективы')
        assert collector.get_books_genre() == {name: 'Детективы' for name in books_name}


# Тест №7 Проверка добавления книг с недетским жанром
    def test_get_children_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

        book_name_1 = 'Книга для взрослых_1'
        collector.add_new_book(book_name_1)
        assert collector.get_books_for_children() == []
        collector.set_book_genre(book_name_1, 'Детективы')
        assert collector.get_books_for_children() == []

        book_name_2 = 'Книга для взрослых_2'
        collector.add_new_book(book_name_2)
        assert collector.get_books_for_children() == []
        collector.set_book_genre(book_name_2, 'Ужасы')
        assert collector.get_books_for_children() == []

        children_books = []
        for genre in ['Фантастика', 'Мультфильмы', 'Комедии']:
            book_name = f'Детская книга_{genre}'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
            children_books.append(book_name)

        assert collector.get_books_for_children() == children_books

# Тест №8 Проверка получения книг из избранного
    def test_favorite_books(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []

        books_name = [f'book_{i}' for i in range(1, 11)]
        for book_name in books_name:
            collector.add_new_book(book_name)

        favorite_books = books_name[:: 4]
        for name in favorite_books:
            collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == favorite_books

        collector.add_new_book('New book')
        assert collector.get_list_of_favorites_books() == favorite_books

        collector.add_book_in_favorites('New book')
        favorite_books.append('New book')
        assert collector.get_list_of_favorites_books() == favorite_books


# Тест №9 Проверка удаления книг из избранного
    def test_favorite_books_with_remove(self):
        collector = BooksCollector()
        books_name = [f'book_{i}' for i in range(1, 11)]
        for book_name in books_name:
            collector.add_new_book(book_name)

        favorite_books = books_name
        for name in favorite_books:
            collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books() == favorite_books

        while favorite_books:
            name = favorite_books.pop()
            collector.delete_book_from_favorites(name)
            assert collector.get_list_of_favorites_books() == favorite_books

        assert len(collector.get_books_genre()) == 10
