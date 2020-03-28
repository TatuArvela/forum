# Forum

Forum is a sample message board web application. This repository contains
multiple implementations with identical features built with different frameworks.
The UI is built with Bootstrap.

## Features

### Graph

```text
├──⟨ᴜsᴇʀs⟩
│   ├── create (admin)
│   ├── log in
│   └── log out
└──⟨ʙᴏᴀʀᴅs⟩
    ├── index
    ├── create (admin)
    ├── delete (admin)
    └── show
        └──⟨ᴛʜʀᴇᴀᴅs⟩
            ├── create
            ├── delete (admin)
            └── show
                └──⟨ᴘᴏsᴛs⟩
                    ├── create
                    └── delete (admin)
```

### List

- [ ] Create user (admin)
- [ ] Log in
- [ ] Log out
- [ ] List boards
- [ ] Create board (admin)
- [ ] Delete board (admin)
- [ ] List threads in board
- [ ] Create thread
- [ ] Delete thread (admin)
- [ ] List posts in thread
- [ ] Create post
- [ ] Delete post (admin)

## Versions

- [Django / Python](###Django-/-Python)
- [Rails / Ruby](###Rails-/-Ruby)
- [Meteor / TypeScript / Node.js](###Meteor-/-TypeScript-/-Node.js)
- [Laravel / PHP](###Laravel-/-PHP)
- [Spring / Kotlin / JVM](###Spring-/-Kotlin-/-JVM)
- [ASP.NET Core](###ASP.NET-Core)

### Django / Python

Reference implementation, which is based on the tutorial
[A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).

#### Installation and configuration

Run the commands below and follow their instructions:

```bash
pipenv install
pipenv shell
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py runserver
```

The following users are added automatically:

* admin (password `admin`)
* user (password `user`)

Finally, open [http://127.0.0.1:8000](http://127.0.0.1:8000)

#### Tests

> _TODO: Better test coverage_

Run the following command:

```bash
pipenv shell
python manage.py test
```

### Rails / Ruby

#### Installation and configuration

Run the commands below and follow their instructions:

```bash
gem install
rails server
```

Open [http://127.0.0.1:3000](http://127.0.0.1:3000)

#### Features in progress

- [ ] Create user (admin)
- [ ] Log in
- [ ] Log out
- [ ] List boards
- [ ] Create board (admin)
- [ ] Delete board (admin)
- [ ] List threads in board
- [ ] Create thread (authenticated)
- [ ] Delete thread (admin)
- [ ] List posts in thread
- [ ] Create post (authenticated)
- [ ] Delete post (admin)

### Meteor / TypeScript / Node.js

Planned.

### Laravel / PHP

Planned.

### Spring / Kotlin / JVM

Planned.

### ASP.NET Core

Planned.
