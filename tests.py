import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # 1) пример теста:
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
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 2) проверили что название книги больше 41 символа и добавить не получилось
    def test_add_new_book_more_41_symbol(self):
        collector = BooksCollector()
        book = 'книга с очень длинным названием в 44 символа'
        collector.add_new_book(book)
        result = len(collector.get_books_genre()) == 0
        assert result == False

    # 3) проверили что у книги нет жанра
    def test_set_book_genre_have_no_genre_true(self):
        collector = BooksCollector()
        # добавляем книгу без жанра
        collector.add_new_book('Предубеждение и зомби')
        # проверяем что добавленная кника не имеет жанра
        assert collector.get_books_genre() is not ''

    # 4) Жанр новой книги есть всписке
    @pytest.mark.parametrize('book, genre', [['Убойные каникулы', 'Ужасы']])
    def test_set_book_genre_have_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        # проверяем что добавленная кника не имеет жанра
        assert collector.get_book_genre(book) in collector.genre

    # 5) получаем жанр книги по ее названию
    @pytest.mark.parametrize('book, genre', [['Луна 2112', 'Фантастика']])
    def test_get_book_genre_exist_in_list_true(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    # 6) список книг с определнынм жанром
    @pytest.mark.parametrize('book, genre', [['Лунтики', 'Мультфильмы']])
    def test_get_books_with_specific_genre_true(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        result = collector.get_books_with_specific_genre('Мультфильмы')
        assert len(result) == 1

    # 7) проверяем что в списке не пусто если добавили книгу
    @pytest.mark.parametrize('book, genre', [['Лунтики', 'Детективы']])
    def test_get_books_genre_not_empty(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        result = collector.get_books_genre()
        assert len(result) != 0

    # 8) добавили 2 книги с разными жанрами
    #    и проверили что одна из них подходит для детей
    def test_get_books_for_children_true(self):
        collector = BooksCollector()
        book1 = 'Приключения Тома Сойера'
        genre1 = 'Мультфильмы'
        book2 = 'Техасская резня'
        genre2 = 'Ужасы'
        collector.add_new_book(book1)
        collector.set_book_genre(book1, genre1)
        collector.add_new_book(book2)
        collector.set_book_genre(book2, genre2)

        result = collector.get_books_for_children()
        expected_result = [book1]
        assert result == expected_result

    # 9) добавили книгу в избранное и убедились что она там есть
    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        book = 'Приключения незнайки на луне'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.favorites

    # 10) сначала добавили книгу, потом удалили
    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        book = 'Приключения незнайки на луне2'
        collector.add_new_book(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()

    # 11) добавляем книгу в избранное и проверили что она там
    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        book = 'Приключения незнайки на луне'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert [book] == collector.get_list_of_favorites_books()
