# 0x00-shell_basics

This repository contains scripts and files created as part of the ALX Software Engineering program's 0x00-shell_basics project. The project focuses on fundamental shell commands and operations, including navigating the filesystem, listing files, creating directories, and manipulating files.

## Project Description

This project introduces basic shell commands and concepts, essential for system administration and software development in a Unix-like environment. The tasks cover a range of shell operations, from simple navigation to more complex file manipulation and scripting.

## Tasks

### 0. Where am I?

* **File:** `0-current_working_directory`
* **Description:** A script that prints the absolute path name of the current working directory.
* **Example:**
    ```bash
    $ ./0-current_working_directory
    /root/alx-system_engineering-devops/0x00-shell_basics
    $
    ```

### 1. What’s in there?

* **File:** `1-listit`
* **Description:** A script that displays the contents list of the current directory.
* **Example:**
    ```bash
    $ ./1-listit
    Applications    Documents   Dropbox Movies Pictures
    Desktop Downloads   Library Music Public
    $
    ```

### 2. There is no place like home

* **File:** `2-bring_me_home`
* **Description:** A script that changes the working directory to the user’s home directory.
* **Note:** No shell variables are used.
* **Example:**
    ```bash
    $ pwd
    /tmp
    $ echo $HOME
    /home/julien
    $ source ./2-bring_me_home
    $ pwd
    /home/julien
    $
    ```

### 3. The long format

* **File:** `3-listfiles`
* **Description:** A script that displays the current directory contents in long format.
* **Example:**
    ```bash
    $ ./3-listfiles
    total 32
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
    -rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
    $
    ```

### 4. Hidden files

* **File:** `4-listmorefiles`
* **Description:** A script that displays current directory contents, including hidden files (starting with `.`), in long format.
* **Example:**
    ```bash
    $ ./4-listmorefiles
    total 32
    drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
    drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
    -rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
    -rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
    $
    ```

### 5. I love numbers

* **File:** `5-listfilesdigitonly`
* **Description:** A script that displays current directory contents in long format, with user and group IDs displayed numerically, including hidden files.
* **Example:**
    ```bash
    $ ./5-listfilesdigitonly
    total 32
    drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
    drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
    -rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
    -rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
    -rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
    $
    ```

### 6. Welcome

* **File:** `6-firstdirectory`
* **Description:** A script that creates a directory named `my_first_directory` in the `/tmp/` directory.
* **Example:**
    ```bash
    $ ./6-firstdirectory
    $ file /tmp/my_first_directory/
    /tmp/my_first_directory/: directory
    $
    ```

### 7. Betty in my first directory

* **File:** `7-movethatfile`
* **Description:** A script that moves the file `betty` from `/tmp/` to `/tmp/my_first_directory`.
* **Example:**
    ```bash
    $ ./7-movethatfile
    $ ls /tmp/my_first_directory/
    betty
    $
    ```

### 8. Bye bye Betty

* **File:** `8-firstdelete`
* **Description:** A script that deletes the file `betty` from `/tmp/my_first_directory`.
* **Example:**
    ```bash
    $ ./8-firstdelete
    $ ls /tmp/my_first_directory/
    $
    ```

### 9. Bye bye My first directory

* **File:** `9-firstdirdeletion`
* **Description:** A script that deletes the directory `my_first_directory` from `/tmp`.
* **Example:**
    ```bash
    $ ./9-firstdirdeletion
    $ file /tmp/my_first_directory
    /tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
    $
    ```

### 10. Back to the future

* **File:** `10-back`
* **Description:** A script that changes the working directory to the previous one.
* **Example:**
    ```bash
    $ pwd
    /tmp
    $ cd /var
    $ pwd
    /var
    $ source ./10-back
    /tmp
    $ pwd
    /tmp
    ```

### 11. Lists

* **File:** `11-lists`
* **Description:** A script that lists all files (including hidden) in the current directory, parent directory, and `/boot` directory in long format.

### 12. File type

* **File:** `12-file_type`
* **Description:** A script that prints the type of the file named `iamafile` in `/tmp`.
* **Example:**
    ```bash
    $ ./12-file_type
    /tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
    ```

### 13. We are symbols, and inhabit symbols

* **File:** `13-symbolic_link`
* **Description:** A script that creates a symbolic link to `/bin/ls`, named `__ls__`, in the current working directory.
* **Example:**
    ```bash
    $ ls -la
    total 144
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
    $ ./13-symbolic_link
    $ ls -la
    total 144
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
    lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
    ```

### 14. Copy HTML files

* **File:** `14-copy_html`
* **Description:** A script that copies all HTML files from the current working directory to the parent directory, only if they don't exist or are newer.

### 15. Let’s move

* **File:** `100-lets_move`
* **Description:** A script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
* **Example:**
    ```bash
    $ ls -la
    total 148
    drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 My_file
    lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Elif_ym
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
    $ ls -la /tmp/u
    total 8
    drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
    drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
    $ ./100-lets_move
    $ ls -la
    total 148
    drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
    drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
    lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
    -rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
    $ ls -la /tmp/u
    total 8
    drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
    drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
    -rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 My_file
    -rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Elif_ym
    ```

### 16. Clean Emacs

* **File:** `101-clean_emacs`
* **Description:** A script that deletes all files in the current directory that end with the character `~`.
* **Example:**
    ```bash
    $ ls
    main.c  main.c~  Makefile~
    $ ./101-clean_emacs
    $ ls
    main.c
    ```

### 17. Tree

* **File:** `102-tree`
* **Description:** A script that creates the directories `welcome/`, `welcome/to/`, and `welcome/to/school` in the current directory, using only two spaces (and lines).
* **Example:**
    ```bash
    $ ls -l
    total 4
    -rwxrw-r-- 1 julien julien 44 Sep 20 12:09 102-tree
    $ ./102-tree
    $ ls
    102-tree  welcome
    $ ls welcome/
    to
    $ ls -l welcome/to
    total 4
    drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 school
    ```

### 18. Life is a series of commas, not periods

* **File:** `103-commas`
* **Description:** A command that lists all files and directories of the current directory, separated by commas, with specific formatting and sorting rules.
* **Example:**
    ```bash
    $ ls -a
    .  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var
    $ ./103-commas
    ./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var
    ```

### 19. File type: School

* **File:** `school.mgc`
* **Description:** A magic file that can be used with the `file` command to detect `School` data files.
* **Example:**
    ```bash
    $ cp /bin/ls .
    $ ls -la
    total 268
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
    drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
    -rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 school.mgc
    -rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
    -rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisaschoolfile
    -rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
    $ file --mime-type -m school.mgc *
    school.mgc:         application/octet-stream
    ls:                    application/octet-stream
    thisisaschoolfile: School
    thisisatextfile:       text/plain
    $ file -m school.mgc *
    school.mgc:         data
    ls:                    data
    thisisaschoolfile: School data
    thisisatextfile:       ASCII text
    ```

## Author

* Merlyn Zawadi - (https://github.com/Zoe-life)

## Acknowledgments

* ALX Software Engineering program for providing the project guidelines and resources.
* The open-source community for the wealth of knowledge and tools.
