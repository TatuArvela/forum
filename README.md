# Forum

Forum is a sample message board web application. This repository contains
multiple implementations with identical features built with different frameworks.
The UI for all of them is built with Bootstrap.

## Features

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

The following users are created automatically:

* admin (password `admin`)
* user (password `user`)

## Versions

### Django / Python

Reference implementation, which is based on the tutorial
[A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).

See [./django/README.md](./django/README.md) for more information
