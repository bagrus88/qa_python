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

        # проверяем, что добавилось именно две книги
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # тестируем метод set_book_genre - добавление жанра Мультфильмы книге Винни-Пух
    def test_set_book_genre_vinni_cartoons(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Винни-Пух')
        # устанавливаем книге жанр
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        # проверяем корректно ли установлен жанр книги методом get_book_genre
        assert collector.get_book_genre('Винни-Пух') == 'Мультфильмы'

    # тестируем метод get_book_genre - получение жанра книги по ее названию
    def test_get_book_genre_by_name(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Восточный экспресс')
        # устанавливаем книге жанр
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        # проверяем корректно ли работает метод получения жанра книги по ее названию
        assert collector.get_book_genre('Восточный экспресс') == 'Детективы'

    # тестируем метод get_books_with_specific_genre - получение названий книг по жанру
    def test_get_books_with_specific_genre_by_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        collector.add_new_book('Ниро Вульф')
        collector.set_book_genre('Ниро Вульф', 'Детективы')
        assert 'Ниро Вульф' in collector.get_books_with_specific_genre('Детективы')

    # тестируем метод получения словаря books_genre
    def test_get_books_genre_by_self(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Восточный экспресс')
        # устанавливаем книге жанр
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        # добавляем книгу
        collector.add_new_book('Ниро Вульф')
        # устанавливаем книге жанр
        collector.set_book_genre('Ниро Вульф', 'Детективы')
        assert collector.get_books_genre() == {'Восточный экспресс': 'Детективы', 'Ниро Вульф': 'Детективы'}

    # тестируем метод возвращая книги, подходящие детям, используя параметризацию
    import pytest
    @pytest.mark.parametrize('book,genre', [['Винни-Пух','Мультфильмы'], ['Звездный десант', 'Фантастика']])
    def test_get_books_for_children_by_self(self, book, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book(book)
        # устанавливаем книге жанр
        collector.set_book_genre(book, genre)
        #проверяем метод
        assert book in collector.get_books_for_children()

        #тестируем метод добавления книги в Избранное
    def test_add_book_in_favorites_by_add_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Винни-Пух')
        # устанавливаем книге жанр
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.add_book_in_favorites('Винни-Пух')
        assert collector.get_list_of_favorites_books() == collector.favorites

        #тестируем метод удаления книги из Избранного
    def test_delete_book_from_favorites_delete_book_by_name(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Винни-Пух')
        # устанавливаем книге жанр
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.add_book_in_favorites('Винни-Пух')
        collector.favorites.remove('Винни-Пух')
        assert collector.get_list_of_favorites_books() not in collector.favorites

    # тестируем получение списка Избранных книг
    import pytest
    @pytest.mark.parametrize('book', ['Винни-Пух', 'Восточный экспресс'])
    def test_get_list_of_favorites_books_from_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == collector.favorites

