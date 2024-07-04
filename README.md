# qa_python

1) добавили 2 книги и проверили что они есть в списке
test_add_new_book_add_two_books

2) добавили книгу длиной больше 41 символа и проверили что записать не смогли
test_add_new_book_more_41_symbo

3) проверка что у книги нет жанра
test_set_book_genre_have_no_genre_true

4) у созданный книги жанр присутствует в списке
test_set_book_genre_have_genre

5) получаем жанр книги по ее названию
test_get_book_genre_exist_in_list_true

6) проверка специфичности жанра
test_get_books_with_specific_genre_true

7) добавили книгу и проверили что список не пустой
test_get_books_genre_not_empty

8) добавили 2 книги с разными жанрами и проверили что одна из них для детей
test_get_books_for_children_true

9) добавили книгу в избранное и убедились что она там
test_add_book_in_favorites_true

10) добавили книгу в избранное, удалили и проверили что удалилась
test_delete_book_from_favorites_true

11) запрашиваем кингу в списке избранных
test_get_list_of_favorites_books_true