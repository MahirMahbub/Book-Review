TRUNCATE TABLE public.book;

INSERT INTO public.book(id, name, author_name, isbn)
VALUES (1, 'NoWhere','MM', '4453252532'),
       (2, 'Anywhere','NoWhere', '5352525535');

TRUNCATE TABLE public.user;

INSERT INTO public.user(id, first_name, last_name)
VALUES (1, 'A', 'User B'),
       (2, 'C', 'User D');

TRUNCATE TABLE public.user_review;
INSERT INTO public.user_review(id, review, rating, user_id, book_id)
VALUES (1, 'A Good Book', 5, 1, 1),
       (2, 'A Great Book', 5, 1, 1),
       (3, 'A Bad Book', 2, 2, 1),
       (4, 'A Worst Book', 1, 2, 1),
       (5, 'A Good Book', 5, 2, 2);