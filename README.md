#Vimix

REALLY JUST make minimum environment for Vim script.

#Require

`vimix` requires python3.3+

#Install

`pip install vimix`

#Usage

Now, you are provided `vimix` command.

Try `vimix {project name}`.

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
