#Vimix

REALLY JUST make minimum environment for Vim script.

#Install
Use `pip`.

`pip install vimix`

#Require

`vimix` requires python3.3+

#Usage

Run `vimix {project name}` command.

```
$vimix hoge
```

Then, made project directory like below.

```
vim-hoge
├── README.md
├── autoload
│   └── hoge.vim
├── doc
│   └── hoge.txt
└── plugin
    └── hoge.vim
```

You can give prefix and suffix for project name with command option.
By default, prefix is 'vim-', suffix is nothing.

```
$vimix hoge -p fuga- -s .piyo
```

Then, makde project directory like below.

```
fuga-hoge-piyo/
├── README.md
├── autoload
│   └── hoge.vim
├── doc
│   └── hoge.txt
└── plugin
    └── hoge.vim
```
