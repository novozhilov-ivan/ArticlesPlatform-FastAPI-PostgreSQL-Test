
- [ ] Пользователь: User
  - [ ] Создать статью
  - [ ] Получить список статей
  - [ ] Получить статью полностью
  - [ ] Удалить статью
  - [ ] Добавить комментарий к статье

- [ ] Пользователь: Admin
  - [ ] Все что и User
  - [ ] Удаление комментариев к любой статье
  - [ ] Назначение пользователя User администратором

- [ ] Репозитории
  - [ ] IArticlesRepo и реализация
    - [ ] create
    - [ ] get_by_oid
    - [ ] get_all_titles
    - [ ] delete
  - [ ] ICategoriesRepo
    - [ ] create
    - [ ] create_many
    - [ ] get_all
  - [ ] IUsersRepo
    - [ ] get_by_nickname
    - [ ] create
  - [ ] ICommentsRepo
    - [ ] get_all_article_comments_by_article_oid
    - [ ] create
    - [ ] delete_by_oid

- [ ] Аутентификация пользователей
  - [ ] Регистрация
  - [ ] Вход в систему