## Guide to Git™ — Common Git Terms

Last modified: *November 13, 2024*

------

## Overview

[Git™](http://git-scm.com/) is a version-control system that tracks and manages changes to files. Whenever content changes, Git records it and stores the content’s history. Because of Git’s complex functionality, it uses many terms that novice users may not immediately understand.

To learn about how these terms work in context, read our [Common Git Commands](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-commands/) documentation.

## Common Git terms

### Archive

[Archives](https://git-scm.com/docs/git-archive) store the contents of the current working [tree](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#_tree_objects), but not the `.git` directory or uncommitted changes, in a `.zip` or `.tar` file. You may wish to create an archive to provide a source download file.

### Branch

Each [branch](https://git-scm.com/docs/gitglossary#def_branch) in a repository represents a separate line of development, and all branches retain their own project history, working directory, and staging area. Each repository can contain as many branches as you wish to create, but you can only work in one branch at any given time. Generally, branches diverge from the original line of development with the intent to merge the branch’s changes at a later time.

### Check out

Git uses this [term](https://git-scm.com/docs/git-checkout) in two contexts:

- Git uses `git checkout` to switch between multiple branches from the command line. When you check out a branch or commit via the `git checkout` command, Git points [`HEAD`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#head) to the specified branch or commit.

- When you check out files via the

   

  ```
  git checkout
  ```

   

  command, Git copies the version of that file from the specified commit or from the index. This allows you to revert committed or uncommitted changes. For example, if you wanted to

   

  delete

   

  your local changes to

   

  ```
  example.js
  ```

   

  in your

   

  ```
  test
  ```

   

  branch, you would run the following commands:

  1. `git checkout test` — This use of `git checkout` switches you from your current Git branch to the `test` branch, where you will copy the `example.js` file.
  2. `git checkout -- example.js` — This use of `git checkout` switches you from your local `test` branch’s version of `example.js` to the [remote](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) `test` branch’s version of `example.js`. This deletes your local changes.

### Cherry-pick

When you [cherry-pick](https://git-scm.com/docs/git-cherry-pick) changes via the `git cherry-pick` command, Git applies the specified changes from a commit and branch to a different branch’s [`HEAD`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#head).

### Clone

When you [clone](https://git-scm.com/docs/git-clone) a public repository via the `git clone` command, Git performs the following actions:

1. Git creates a new local repository in the directory in which you ran the command.

   Note:

   When you clone a repository in cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*), the system creates the repository in the *Repository Path* directory that you specify.

2. Git sets the [remote](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) repository that you wish to clone as the `origin` remote repository.

3. Git fetches all of the commits and branches from the remote repository.

4. Git checks out the default branch. Generally, this branch is named `master` or `main`.

You can then make changes to the local repository and [push](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#push) them to the remote repository, as well as [pull](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#pull) changes.

To clone private repositories, you must perform additional steps. For more information, read our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

### Commit

[Commits](https://git-scm.com/docs/git-commit) represent a point in Git’s history. Git’s entire history for a repository exists as a timeline of individual commits. When you commit changes, you create a new point in the history that represents the current state of the index. [`HEAD`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#head) then points to the new commit.

### Commit Object

[Commit objects](https://git-scm.com/docs/git-commit) represent your committed revisions to a branch. Each commit object contains the commit’s files (the tree object), parent commits, commit metadata (for example, the author and date), and a [SHA-1](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#sha-1-sha-1-sum-hash) value that identifies the object.

### Deployment

[Deployment](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) sends finished code into production. You can use different configurations to automatically or manually deploy changes.

For example, you can configure cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) to automatically deploy changes that a cPanel-managed repository receives.

For more information, read our [Set Up Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-deployment) documentation.

### Fetch

When you [fetch](https://git-scm.com/docs/git-fetch) changes via the `git fetch` command, Git automatically downloads new changes from the [remote](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) repository. However, it does **not** [merge](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#merge) these changes into the [working tree](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#working-tree) for any local branch.

### Fork

When you [fork](https://git-scm.com/search/results?search=fork) a repository, you create a new server-side copy of that repository. You can then experiment with changes to that repository without any impact on the original repository.

### HEAD

[The `HEAD` value](https://git-scm.com/docs/gitglossary#def_HEAD) represents the [SHA-1](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#sha-1-sha-1-sum-hash) identifier for the most-recent commit or active branch. Whenever you commit changes to the active branch, Git automatically updates `HEAD` to that commit’s [SHA-1](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#sha-1-sha-1-sum-hash) identifier. If you use the `git checkout` command to check out a specific commit instead of a branch, Git enters the `detached HEAD` state.

### Head

[Heads](https://git-scm.com/docs/gitglossary#def_head) are the [SHA-1](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#sha-1-sha-1-sum-hash) identifiers for the most-recent commits to each branch. While only one `HEAD` commit exists, a repository generally contains many heads for each branch.

### Hook

[Hooks](https://git-scm.com/docs/githooks) are scripts or other code that you can configure to trigger before or after specific Git actions. You can store these hooks in the `/hooks` directory within the repository directory.

Note:

cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) automatically adds a `post-receive` hook to cPanel-managed repositories.

### Index (Staging Area, Cache)

[Indexes](https://git-scm.com/docs/git-show-index) contain the files from your working tree that you add to a commit to the Git repository. Git also uses the index to store data during failed [merges](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#merge).

### Log

[The log](https://git-scm.com/docs/git-log) contains the commit [hash](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#sha-1-sha-1-sum-hash) and metadata, such as the commit message, for every commit on the current branch. You can access this data via the `git log` command on the command line or via [Gitweb](https://docs.cpanel.net/cpanel/files/gitweb) in cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*).

### Master or main

Generally, the default branch for a repository is the [`master` or `main` branch.](https://git-scm.com/docs/git-branch) When you commit changes to it, Git moves the default branch’s `HEAD` to the most recent commit’s [SHA-1](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#sha-1-sha-1-sum-hash) identifier.

### Merge

When you [merge](https://git-scm.com/docs/git-merge) one or more commits, Git adds changes to the current branch. To perform a merge of this type, run the `git push` command.

You may also need to manually merge specific revisions if they conflict with changes that have already merged into the repository.

- This type of merge uses the `git merge` command.
- The term “merge” may also refer to the commit that this type of merge creates.

### Origin

[Origin](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) is Git’s default name for the [remote](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) repository from which you [cloned](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#clone) a local repository. Most repositories include at least one origin repository. Software development often refers to origin as “upstream”.

### Pull

When you [pull](https://git-scm.com/docs/git-pull) changes from the [remote](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) repository via the `git pull` command, Git fetches remote changes and then [merges](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#merge) them into the current branch.

Note:

You can use the *Pull from Remote* feature in cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) to automatically pull changes for a repository’s active branch.

### Push

When you [push](https://git-scm.com/docs/git-push) changes via the `git push` command, Git sends commits from your local branch to the [remote](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) repository.

### Rebase

[Rebases](https://git-scm.com/docs/git-rebase) reapply changes to the history of the active branch via the `git rebase` command. To do this, rebases **eliminate** merge commits and create a new commit for each commit in the original branch.

### Remote (Remote Repository)

The [remote](https://git-scm.com/docs/git-remote) repository exists on a remote filesystem. When you [fetch](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#fetch), [pull](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#pull), or [push](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#push) code, Git sends changes to or receives changes from the remote repository.

### Repository

[Repositories](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) store all of the data that Git manages for a specific project. It contains [commit objects](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#commit-objects) and [heads](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#head) as well as the [working tree](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#working-tree).

### SHA-1 (SHA-1 sum, Hash)

[The algorithm](https://git-scm.com/docs/git-log) that generates the names for all Git objects, from [commit objects](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#commit-objects) to [stash objects](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#stash-objects). In Git’s vernacular, this term also refers to the 40-character hexidecimal string that the algorithm generates.

### Stash

[An object](https://git-scm.com/docs/git-stash) that stores changes to the working tree and index for future reuse. The stash allows you to set aside changes to a branch and return to the [`HEAD`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#head) state. You can then reapply the stashed changes or apply them to a different branch.

### Version Control

[Version control](https://git-scm.com/) systems track changes in files and allow multiple users to coordinate those changes and view and manipulate the project’s history. Git is a version control system.

### Working Tree

[The working tree](https://git-scm.com/docs/git-ls-tree) contains the checked-out file system for a repository. The working tree includes the files for the [`HEAD`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#head) commit and any local changes to those files.

## Guide to Git™ — Common Git Commands

Last modified: *November 13, 2024*

------

## Overview

You can access all of Git™’s functionality via the command line. This document lists common commands and options that may assist you when you learn Git.

Important:

- This document is **not** comprehensive. It intentionally omits information about intermediate and advanced Git functionality. For more information about additional commands and options, read [Git’s documentation](https://www.git-scm.com/doc).
- The terminology in this document assumes that you are familiar with the command line. If you are not familiar with these terms, read our [Common Git Terms](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/) documentation.

## Common Git commands

Note:

- To resolve Git errors, read our [Advanced Configuration and Troubleshooting](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-advanced-configuration-and-troubleshooting) documentation.
- For general Linux commands, read our [Getting Started with Linux Commands](https://docs.cpanel.net/knowledge-base/general-systems-administration/getting-started-with-linux-commands) documentation.
- For help to access the command line in order to run these commands, read our [How to Access the Command Line](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-access-the-command-line) documentation.
- You can add the `--help` option to any Git command in order to view the manual page for that command.

### git clone

[This command](https://www.git-scm.com/docs/git-clone) clones a repository into a new directory, creates remote-tracking branches, and forks a new working branch from the cloned repository’s active branch.

```perl
git clone repositoryurl
```

In the example above, `repositoryurl` represents the URL of the repository that you wish to clone.

Note:

- Use the `git fetch` command to update the new repository’s remote-tracking branches.
- Use the `git pull` command to merge the remote master branch into the current master branch.
- cPanel’s [*Git™ Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git™ Version Control*) provides the URL to use to clone each of your account’s repositories.
- To clone private repositories, you must perform additional steps. For more information, read our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

### git add

[This command](https://www.git-scm.com/docs/git-add) adds the current version of a file to the index of staged content for the next commit.

```perl
git add [options] filepath
```

In the example above, `filepath` represents the file’s absolute path **or** its path relative to the current working directory.

- To stage uncommitted changes for **all** tracked files, run this command with either of the `-a` or `-u` options (and without a specified file path).
- This command **only** stages the current changes for the current commit. The next time that you create a commit, you **must** run the command for the file again in order to stage any new changes.

### git commit

[This command](https://www.git-scm.com/docs/git-commit) creates a new commit for the [currently-staged](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-commands/#git-add) changes.

```perl
git commit [options]
```

When you run this command (without the `-m` option), Git immediately displays a text file, in which you can enter and save your commit message.

- To automatically stage modified and deleted files before Git creates the commit, run this command with the `-a` option.
- To specify a short commit message directly from the command line, run this command with the `-m` option. For example:

```perl
git commit -m "Commit message here."
```

Note:

To stage changes for inclusion in a commit, use the `git add` or `git rm` commands or provide individual filepaths as arguments to this command.

### git checkout

[This command](https://www.git-scm.com/docs/git-checkout) sets the specified branch as the current working branch.

```perl
git checkout [options] branchname
```

In the example above, `branchname` represents the branch to check out.

- To check out only a specified file, run this command with a file path instead of a branch name.

  ```perl
  git checkout mybranch files/templates/2.html
  ```

  In this example,

   

  ```
  mybranch
  ```

   

  represents the branch that contains the version of the file that you wish to check out and

   

  ```
  files/templates/2.html
  ```

   

  represents the file to check out. If you run this command, the system will replace the

   

  ```
  files/templates/2.html
  ```

   

  file’s contents in the current local working branch with the file’s contents from the

   

  ```
  mybranch
  ```

   

  branch.

  Note:

  If you omit the branch name, Git will check out that file from the `HEAD` of the current branch.

  

- To create a new branch with the specified branch name and then check it out, run this command with the `-b` option.

- To forcibly change branches, run the command with the `-f` option. This option causes Git to overwrite local changes in order to match the working tree to the branch’s `HEAD` commit.

### git rm

[This command](https://www.git-scm.com/docs/git-rm) removes files or directories from Git’s index and working tree.

```perl
git rm [options] files_or_dirs
```

In the example above, `files_or_dirs` represents the paths to the files or directories to remove, relative to the repository’s main directory.

Important:

- To run this command, the specified file **cannot** contain uncommitted changes.
- This command **cannot** retain the file in the index **and** remove the file from the working tree. To do this, use BASH’s `rm` command.
- If you specify a directory name, you **must** also use the `-r` option. This option allows the command to recursively remove the files in that directory.

### git fetch

[This command](https://www.git-scm.com/docs/git-fetch) downloads branches, tags, and their histories from one or more other repositories.

```perl
git fetch [options] remotename
```

In the example above, `remotename` represents the name of the remote repository.

### git pull

[This command](https://www.git-scm.com/docs/git-pull) fetches and merges changes from a local branch or a remote or local repository. With most options, this command combines the `git fetch` and `git merge` commands.

```perl
git pull [options] repo-or-branch
```

In the example above, `repo-or-branch` represents the branch name or the repository name or URL.

### git push

[This command](https://www.git-scm.com/docs/git-push) adds your committed changes to the specified repository and branch.

```perl
git push [options] repository branch
```

In the example above, `repository` represents the repository name or URL and `branch` represents the remote branch on that repository.

- If you do **not** specify a repository, the command performs one of the following actions:

  - If your current branch’s configuration includes a remote repository, the command adds your changes to that repository.

  - If your current branch’s configuration does

     

    not

     

    include a remote repository, the command adds your changes to the

     

    ```
    origin
    ```

     

    repository.

    Important:

    You **must** explicitly specify a repository in order to specify a branch. If you do **not** specify a branch, the command adds your changes to the remote repository’s current branch.

- To push **all** commits from **all** local branches to their upstream repositories, run this command with the `--all` option.

- To add the specified repository to the branch as its upstream repository, run this command with the `--set-upstream` option.

  - This allows you to omit the repository on subsequent pushes to upstream.
  - You must specify a remote repository when you use this option.

Note:

cPanel’s cPanel’s [*Git™ Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git™ Version Control*) automatically adds a `post-receive` hook that each push to cPanel-managed repositories triggers. For more information, read our [Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment) documentation or Git’s [githooks](https://git-scm.com/docs/githooks#post-receive) documentation.

### git branch

[This command](https://www.git-scm.com/docs/git-branch) creates, lists, or deletes branches.

```perl
git branch [options] branchname
```

In the example above, `branchname` represents the branch name.

- To create a new branch, run this command with the desired branch name.

  Important:

  Git does **not** automatically check out new branches when you create them. You **must** also run the `git checkout` command in order to check out your new branch.

  

- To retrieve a list of existing local branches, run this command without a branch name. Use the `-a` option to retrieve a list of both local and remote branches.

- To set the upstream branch for a specified branch, run this command with the `-u` option.

- To rename a specified branch, run this command with the `-m` option and the current and new branch names. For example:

  ```perl
  git branch -m oldbranch newbranch
  ```

  In this example,

   

  ```
  oldbranch
  ```

   

  represents the current branch name and

   

  ```
  newbranch
  ```

   

  represents the new branch name.

  

- To delete a specified branch, run this command with the `-d` option.

### git merge

[This command](https://www.git-scm.com/docs/git-merge) combines the history of one or more commits into the history of the current branch.



```perl
git merge [options]
```

Note:

The [`git pull`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-commands/#git-pull) command automatically performs this action.



### git blame

[This command](https://www.git-scm.com/docs/git-blame) displays the specified file with the author, most-recent change date, and commit SHA-1 for each line of the file.

```perl
git blame [options] filepath
```

In the example above, `filepath` represents the file’s absolute path or its path relative to the current working directory.

When you run this command without additional options, the output will resemble the following example:

| `1 2 3 4 5 6 7 ` | `5f033c48d84a (Jane E. Coder        2017-05-24 18:25:53 -0600  1) <!DOCTYPE HTML> 5f033c48d84a (Jane E. Coder        2017-05-24 18:25:53 -0600  2) <html> 5f033c48d84a (Jane E. Coder        2017-05-24 18:25:53 -0600  3) 5f033c48d84a (Jane E. Coder        2017-05-24 18:25:53 -0600  4) <body> 54222e949682 (John B. Developer    2018-01-08 10:57:07 +0000  5)    <p>Here's some text.</p> 5f033c48d84a (Jane E. Coder        2017-05-24 18:25:53 -0600  6) 5f033c48d84a (Jane E. Coder        2017-05-24 18:25:53 -0600  7) <script>` |
| ---------------- | ------------------------------------------------------------ |
|                  |                                                              |

In this example, on May 24th, 2017, Jane E. Coder committed changes to the file. On January 8th, 2018, John B. Developer committed changes to the file. Because John committed changes after Jane, this output does **not** display any changes that Jane made to line 5 **or** the history of the other lines before Jane’s commit.

### git clean

[This command](https://www.git-scm.com/docs/git-clean) removes untracked files (files that Git does not manage) from the working tree.

```perl
git clean [options]
```

- To display a list of untracked files to remove but **not** remove them, run this command with the `-n` option.
- To also remove untracked directories, run this command with the `-d` option.

### git config

[This command](https://www.git-scm.com/docs/git-config) retrieves or updates Git’s global and repository settings in its configuration files.

```perl
git config [options]
```

Git stores your settings in the following files:

- `/path-to-git/etc/gitconfig` — Global settings.
- `/path-to-git/config` — Repository settings.
- `/home-directory/.gitconfig` — A user configuration file.
- `/home-directory/.config/git/config` — A user configuration file.

Note:

- In the paths above, `path-to-git` represents the Git installation’s absolute path and `home-directory` represents a cPanel account’s home directory (for example, the `/home/user/.gitconfig` file).
- If both user configuration files exist and their values conflict, the system uses the values in the `.gitconfig` file.
- This command accepts many options for each of Git’s configurable settings. To use this command, read Git’s [git config](https://www.git-scm.com/docs/git-config) documentation.

### git diff

[This command](https://www.git-scm.com/docs/git-diff) compares changes between two commits, a commit and the current working tree, two branches or working trees, or two files.

```perl
git diff [options]
```

By default, this command returns a comparison of the working tree and your last commit (the changes that Git would commit if you ran the `git commit -a` command).

You may wish to use the following common options:

- To view a comparison of two branches, run the following command, where `branch1` and `branch2` represent the branches to compare:

  ```perl
  git diff branch1..branch2
  ```

  

- To view a comparison of two commits, run the following command, where `FirstSHA` and `SecondSHA` represent the SHA-1 values for the two commits:

  ```perl
  git diff FirstSHA..SecondSHA
  ```

  

- To only view differences between two versions of one file in a working tree, branch, or commit, specify that filepath as an argument. For example:

  ```perl
  git diff branch1..branch2 filename
  ```

  In the example above,

   

  ```
  branch1
  ```

   

  and

   

  ```
  branch2
  ```

   

  represent the branches from which Git will compare the contents of the

   

  ```
  filename
  ```

   

  file.

  

### git grep

[This command](https://www.git-scm.com/docs/git-grep) searches the current working tree for one or more patterns (generally, strings or regular expressions).

```perl
git grep [options] "pattern"
```

In the example above, `pattern` represents the data to query.

- To perform a case-insensitive search, run this command with the `-i` option.

- To use Perl-Compatible Regular Expressions (PCREs) in your patterns, run this command with the `--perl-regexp` option. cPanel & WHM’s implementation of Git automatically includes the necessary dependencies for this option.

- To return only files that include all of the specified patterns (when you run the command with multiple patterns), run this command with the `--all-match` option. For example:

  ```perl
  git grep --all-match "string one" "string two" "string three"
  ```

  This example would return files that contain

   

  ```
  string one
  ```

  ,

   

  ```
  string two
  ```

  ,

   

  and

   

  ```
  string three
  ```

  , but would

   

  not

   

  return files that only contain

   

  ```
  string two
  ```

  .

  

- To return file paths relative to the repository’s main directory rather than the current directory, run this command with the `--full-name` option.

### git log

[This command](https://www.git-scm.com/docs/git-log) queries the commit logs for your current branch.

```perl
git log [options]
```

- To view only results from a specific range of commits, run the following command:

  ```perl
  git log FirstSHA..SecondSHA
  ```

  In this example,

   

  ```
  FirstSHA
  ```

   

  and

   

  ```
  SecondSHA
  ```

   

  represent the SHA-1 values for the two commits.

  Note:

  If you do not specify a range of commits to query, this command queries all commits between the `origin` commit and `HEAD` for the current branch.

  

- To view only a specific number of the most recent log entries, run the following command, where `num` represents the number of entries to return:

  ```perl
  git log -num
  ```

  

- To view only log entries before or after a specific date, run one of the following commands, where `date` represents the specified date:

  | `1 2 ` | `git log --before=date git log --after=date` |
  | ------ | -------------------------------------------- |
  |        |                                              |

  For date formatting options, read Git’s

   

  git log

   

  documentation.

  

- To view only log entries for commits from a specific author, run the following command, where `authorname` represents the author’s name in their `.gitconfig` file:

  ```perl
  git log --author=authorname
  ```

  

- To view only log entries that contain a specific pattern (generally, a string), run the following command, where `pattern` represents the pattern to query:

  ```perl
  git log --grep=pattern
  ```

  If you include multiple patterns to query, use the

   

  ```
  --all-match
  ```

   

  option to limit output to log entries that match

   

  all

   

  of the specified patterns.

  

Note:

- This command also accepts formatting options from the `git diff` command.
- If you only require summarized commit log information, you may wish to use the `git shortlog` command.

### git revert

[This command](https://www.git-scm.com/docs/git-revert) reverts existing commits within a specified range and then allows you to edit their commit messages.

```perl
git revert [options] commit1..commit2
```

In the example above, `commit1` and `commit2` represent the SHA-1 values for the range of commits to revert.

Important:

To run this command, your working tree **cannot** contain uncommitted changes.

### git shortlog

[This command](https://www.git-scm.com/docs/git-shortlog) produces a shortened version of the output of the `git log` command. You may wish to use this command if, for example, you need to generate a list of changes for release notes or a change log.

```perl
git shortlog [options]
```

### git stash

[This command](https://www.git-scm.com/docs/git-stash) uses several options to create, manage, and retrieve sets of changes (stashes). When you run this command without specified options, it defaults to `git stash` save functionality.

```perl
git stash [options]
```

Use the following options to manage stashes:

- To create a new stash and return the current branch to its state in the

   

  ```
  HEAD
  ```

   

  commit, run this command with the

   

  ```
  save
  ```

   

  option. When you use this option, you can also use the

   

  ```
  -message
  ```

   

  option to add a description to the stash. For example:

  ```perl
  git stash save -message "Description"
  ```

  In the example above,

   

  ```
  Description
  ```

   

  represents the stash description.

- To return a comparison of stashed changes with the `HEAD` commit when you created the stash, run this command with the `show mystash` option.

- To list your current stashes, run this command with the `list` option.

- To apply stashed changes to the current working tree and and remove the stash, run this command with the `pop mystash` option.

- To apply stashed changes to the current working tree but **not** remove the stash, run this command with the `apply mystash` option.

- To remove all stashes, run this command with the `clear` option.

Note:

In the options above, `mystash` represents the reflog entry or stash index for the desired stashed changes.



## Guide to Git™ — Host Git Repositories on a cPanel Account

Last modified: *November 13, 2024*

------

## Overview

Note:

We recommend that you use cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) to perform Git tasks. While many of these tasks require command-line access, this interface automates some parts of the process and allows you to view historical information for your repositories in [Gitweb](https://docs.cpanel.net/cpanel/files/gitweb).

With the appropriate permissions, cPanel accounts can host Git repositories. Git’s version control software tracks changes in a system of files that multiple users can manage simultaneously. This tutorial uses the command line to create or clone a new Git repository, update the repository’s configuration, and clone the repository locally for updates.

- For a list of common Git commands and their options, read our [Common Git Commands](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-commands) documentation.
- For information about how to deploy code from your hosted Git repositories, read our [Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment) and [Set Up Deployment Cron Jobs](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-deployment-cron-jobs) documentation.
- For more information about Git, read [Git’s](https://git-scm.com/) documentation.

### Requirements

To perform the steps in this tutorial, you **must** meet the following requirements:

- You **must** possess an active cPanel account with available disk space.
- Your system administrator **must** enable the *Shell Access* setting for your cPanel account.
- You **must** register your public key in cPanel’s [*SSH Access*](https://docs.cpanel.net/cpanel/security/ssh-access) interface (*cPanel » Home » Security » SSH Access*) and authorize it for SSH access.

Important:

To clone private repositories, you must perform the additional steps in our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

## Host a Git repository on your cPanel account

### Create or clone a repository

You can create a Git repository in any existing directory, or you can create a new, empty directory for your repository. If your project already has a Git repository, you can [clone](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-commands/#git-clone) the repository to your cPanel account instead.

To use cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) to manage your repository, you **must** ensure the repository and directory you place it into meet the following requirements:

- You **cannot** include whitespace or the following characters in the repository name or directory path:

  ```bash
  \\ \* | " ' < > & @ \` $ { } [ ] ( ) ; ? : = % #
  ```

  

- The repository **cannot** be in the following cPanel-controlled directories:

  | ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ` | `.cpanel .trash etc mail ssl tmp logs .cphorde spamassassin .htpasswds var cgi-bin .ssh perl5 access-logs` |
  | --------------------------------------- | ------------------------------------------------------------ |
  |                                         |                                                              |

  

If you use the command line to create a repository in a restricted path, the [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) will **not** display the repository.

#### Create a new repository

To create a new repository, perform the following steps:

1. Use SSH to log in to your cPanel account on the command line.

2. To navigate to the directory that will contain your repository, run the following command, where :

   ```bash
   cd ~/Project/example
   ```

   Note:

   To create a new directory to store your repository, run the following command and then navigate to that directory:

   ```bash
   mkdir -p ~/Project/example
   ```

   

3. To initialize the directory as a Git repository, run the following command:

   ```bash
   git init
   ```

   

#### Clone an existing repository

Important:

To clone private repositories, you must perform additional steps. For more information, read our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

To clone an existing repository, perform the following steps:

1. Use SSH to log in to your cPanel account on the command line.

2. To navigate to the directory that will contain your repository, run the following command:

   ```bash
   cd ~/Project
   ```

   Note:

   To create a new directory to store your repository, run the following command and then navigate to that directory:

   ```bash
   mkdir -p ~/Project
   ```

   

3. To clone the repository, run the following command :

   ```bash
   git clone https://domain.com/Account/example.git example.git
   ```

   In this example,

    

   ```
   https://domain.com/Account/example.git
   ```

    

   represents the repository’s clone URL.

   

Note:

- Many developers host their code repositories on GitHub. GitHub repository URLs generally resemble the following example, where `Account` represents the GitHub account name and `example` represents the repository name:

```bash
https://github.com/Account/example.git
```

- The system may require a large amount of time to clone larger repositories. Until this process finishes, HEAD information will be unavailable in cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*).
- cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) does **not** allow username-and-password pairs in remote repository URLs.

### Update the Git configuration

This optional step configures the Git repository to remain up to date as you push changes from the local branch.

More:

For more information about Git’s configuration file and its options, read Git’s [git-config](https://git-scm.com/docs/git-config/2.13.0) documentation.

To update the configuration, run the following command from within the repository directory:

```bash
git config receive.denyCurrentBranch updateInstead
```

### Clone the repository locally

Important:

- This feature enforces several restrictions on clone URLs. For more information, read our [Git Version Control](https://docs.cpanel.net/cpanel/files/git-version-control) documentation.
- You can use cPanel’s [*SSH Access*](https://docs.cpanel.net/cpanel/security/ssh-access) interface (*cPanel » Home » Security » SSH Access*) to add and manage SSH keys, which you can use to access the cPanel-hosted repository. Because SSH keys allow access to the entire cPanel account, and not just a single repository, exercise caution when you perform this action.

To clone the cPanel-account-hosted repository, access your local computer via the command line and run the following command:

```bash
git clone ssh://username@hostname/home/username/Project/example.git
```

- `username` represents the cPanel account username.
- `hostname` represents the hostname for the server that hosts your cPanel account.

### Push local changes to the hosted repository

After you finish this tutorial, you can make changes to the repository’s files on your local computer. You **must** run the following command in order to push changes that you make on your local computer to the hosted repository:

```bash
git push origin master -u
```

This command pushes your revisions to the copy of the repository that exists on your cPanel account.

Note:

cPanel & WHM’s Git installation will automatically configure some settings.





## Guide to Git™ — Set Up Access to Private Repositories

Last modified: *November 13, 2024*

------

## Overview

This document describes how to set up SSH access so you can clone a local cPanel repository to a remote private repository. You **must** generate and copy SSH keys to the remote repository server before you can clone a local repository to the remote server.

Important:

- This tutorial uses GitHub as an example host for a private repository. However, most of the steps in this tutorial are similar to the steps for any other private repository host.
- The steps in this tutorial require the *SSH Access & Terminal* feature.

## Set up SSH access to private repositories

To set up access to private repositories, perform the following steps.

### Connect to your server via SSH or the cPanel Terminal

For information on how to connect via SSH, review our [*SSH Access*](https://docs.cpanel.net/cpanel/security/ssh-access/) documentation. For information on how to connect to the cPanel Terminal, review our [*Terminal for cPanel*](https://docs.cpanel.net/cpanel/advanced/terminal-in-cpanel/) documentation. Once you’ve successfully connected, continue following this guide, running the commands either in your SSH-connected command line interface or the cPanel Terminal.

### Generate an SSH key

Run the following command to generate an SSH key file:

```perl
ssh-keygen -t rsa -f ~/.ssh/repo -b 4096 -C "username@example.com"
```

Note:

Replace `repo` with the name of the remote repository, `username` with your cPanel username, and `example.com` with your cPanel domain name.

For example, if your repository name is `testing`, your cPanel username is `cptest`, and your cPanel domain name is `cptest.tld`, run this command:

```perl
ssh-keygen -t rsa -f ~/.ssh/testing -b 4096 -C "cptest@cptest.tld"
```



Warning:

This command contains several parts. If you alter any part of the command, you may affect the performance of your SSH key.

- The `-t` flag specifies the type of algorithm for your SSH key.
- The `-f` flag determines the name for your public and private keys. With the `-f` flag, there is no need to specify the public key name as it will always be the same name as the private key, but with `.pub` as the suffix.
- The `-b` flag specifies the size of the SSH key in bits.
- The `-C` flag specifies a comment to add to your public key. This is helpful when identifying which public keys you have authorized in a remote system, so it is common practice to add your email address as the comment.

After you run this command, the system will prompt you to enter a passphrase. Do **not** enter a passphrase, and press *Enter* to continue.

### Create the SSH configuration file

To create the SSH configuration file, perform the following steps:

1. Run the following command to create the SSH configuration file:

   ```perl
   touch ~/.ssh/config
   ```

2. Update the permissions of the

    

   ```
   ~/.ssh/config
   ```

    

   file to

    

   ```
   0600
   ```

   :

   ```perl
   chmod 0600 ~/.ssh/config
   ```

3. Run the following command to verify the cPanel user account:

   ```perl
   chown cpanelusername:cpanelusername ~/.ssh/config
   ```

4. Open

    

   ```
   ~/.ssh/config
   ```

    

   with the text editor of your choice, and add the following lines where

    

   ```
   testing
   ```

    

   is the name of your repository:

   ```perl
   Host remote-git-repo-domain.tld
       IdentityFile ~/.ssh/testing
   ```

   Note:

   - If you want to use this private key when connecting to any remote host via SSH, you may use an asterisk character (`*`) as the host instead of a specific domain name. Otherwise, use the domain name of your remote Git repository provider. You can find this domain name within the SSH repository URL.
   - You **must** use the path to the private key generated above for the `IdentityFile`.

5. Save the file.

### Register your SSH key with the private repository host

Note:

- For information about how to register your SSH key with another private repository host, consult that host’s website or documentation.
- Some repository hosts, such as Bitbucket, do **not** allow you to configure write access for your access keys.

To register an SSH key with GitHub, perform the following steps:

1. Log in to your GitHub account.

2. Navigate to your private repository.

3. In the top right corner of the page, click *Settings*. A new page will appear.

4. In the left side menu, click *Deploy keys*. A new page will appear.

5. In the top right corner of the page, click *Add deploy key*. A new page will appear.

6. In the *Title* text box, enter a display name for the key.

7. In the *Key* text box, paste the entire **public** SSH key from the `~/.ssh/repo.pub` file you created in the previous step. For example, if you created a key with `~/.ssh/testing` as the key file name, the public key would be in `~/.ssh/testing.pub`.

8. If you want to push code from your cPanel account to your GitHub account, select the

    

   Allow write access

    

   checkbox.

   Note:

   If you do **not** select this checkbox, you can only deploy changes from your GitHub repository to the cPanel-hosted repository.

9. Click *Add key*.

### Test the SSH key

To test your SSH key, run the following command:

```perl
ssh -i ~/.ssh/repo -T git@example.com
```

Note:

Replace `repo` with the name of the repository and `example.com` with the private repository’s domain name you input when you created the SSH key.

For example, if you input `testing` as the repo and `github.com` as the repository host’s domain name in the previous step, run this command:

```perl
ssh -i ~/.ssh/testing -T git@github.com
```

### Set up access to multiple repositories

To create an SSH key for each of your repositories, follow the steps outlined above. After you have added the keys to the remote repositories, create a local `~/.ssh/config` file to alias each of the keys to their corresponding repository names.

For example, if you have two repos configured on GitHub, `testing` and `testing2`, and both your cPanel and GitHub usernames are `cptest`, create or modify the `~/.ssh/config` file with these contents:

```perl
Host github.com-testing
        Hostname github.com
        IdentityFile=/home/cptest/.ssh/testing

Host github.com-testing2
        Hostname github.com
        IdentityFile=/home/cptest/.ssh/testing2
```

### Clone a repository: single repository on the remote host

To clone a repository when you have a single repository configured on the remote repository host, run this command:

```perl
git clone git@example.com:username/repo.git
```

Note:

Replace `example.com` with the domain name of the remote private repository, `username` with your username on the remote repository host, and `repo` with the name of the repository.

For example, if your GitHub username is `cptest`, and the repository name is `testing`, run this command:

```perl
git clone git@github.com:cptest/testing.git
```



### Clone a repository: multiple repositories on the remote host

To clone a repository when you have multiple repositories configured on the remote repository host and have created separate SSH keys and the `~/.ssh/config` file as referenced above, run this command:

```perl
git clone git@Host:username/repo.git
```

For example, if your GitHub username is `cptest`, and the repository name is `testing2`, run this command:

```perl
git clone git@github.com-testing2:cptest/testing2.git
```





## Guide to Git™ — Set Up Deployment

Last modified: *November 13, 2024*

------

## Overview

cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*) allows you to configure deployment for your cPanel-managed repositories. While many deployment configurations are possible, this document only outlines two types of deployment that you can configure.

### Push

**Push** deployment first [pulls](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#pull) changes from a [remote repository](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) to your local computer. Then, you can [push](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#push) them to your cPanel-managed repository. The system will automatically [deploy](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#deployment) changes that you push to the cPanel-managed repository.

![Push deployment diagram](https://docs.cpanel.net/img/git-push-deployment-workflow.png)

### Pull

**Pull** deployment [pulls](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#pull) changes from a [remote repository](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#remote-remote-repository) to your local computer and [pushes](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#push) new changes from your local computer to the remote repository. You can then use the [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*) to manually [deploy](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#deployment) changes that you pull from the remote repository.

![Pull deployment diagram](https://docs.cpanel.net/img/git-pull-deployment-workflow.png)

Note:

If you experience issues when you configure Git deployment, read the following documents:

- [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories)
- [Git Version Control Series: Git Problems and How to Fix Them](https://blog.cpanel.com/git-version-control-series-git-problems-and-how-to-fix-them/)

## Set up push deployment

Note:

We recommend that you use this type of deployment.

### Create an empty repository on your cPanel account

If the repository that you wish to deploy does not already exist on your cPanel account, use cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*) to create one.

Note:

For this type of deployment, do **not** clone a remote repository during this step. Instead, create an empty repository.

### Clone the remote repository to your local computer

If you have not already cloned it, clone the remote repository. For example, run the following command to clone a repository, where `URL` represents the remote repository’s clone URL:

```bash
git clone URL
```

Important:

To clone private repositories, you must perform additional steps. If you do not perform these steps, you will experience errors when you attempt to use Git. For more information, read our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

Note:

You can find the repository’s clone URL by performing the following steps:

1. Navigate to cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*)
2. Locate the desired repository in the list of repositories and click *Manage*.
3. The URL appears under the *Clone URL* heading.

### Create the .cpanel.yml file

In order to deploy changes from a cPanel-managed repository, you **must** check a `.cpanel.yml` file in to the top-level directory of your repository. You can create and commit this file to your local computer’s copy of the repository, or you can create and commit it on the remote repository.

- If you use the remote repository, you will require read-write access or can submit a pull request to the remote repository.
- This tutorial uses changes from the local computer rather than the remote repository.

For example, a `.cpanel.yml` file may resemble the following example:

| `1 2 3 4 5 6 ` | `--- deployment: tasks: - export DEPLOYPATH=/home/user/public_html/ - /bin/cp index.html $DEPLOYPATH - /bin/cp style.css $DEPLOYPATH` |
| -------------- | ------------------------------------------------------------ |
|                |                                                              |

More:

For more information about the `.cpanel.yml` file, read our [Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment) documentation.

### Add the cPanel-managed repository as a remote repository

From your local computer, run the following command to add the cPanel-managed repository as the local computer’s remote repository:

```bash
git remote add origin URL
```

In this command, `URL` represents the cPanel-managed repository’s clone URL.

### Push changes to the cPanel-managed repository

From your local computer, run the following command to push the changes from your local computer to the cPanel-managed repository:

```bash
git push -u origin HEAD
```

After the cPanel-managed repository contains the `.cpanel.yml` file, the system will automatically deploy any changes that you push to it.

Important:

If you experience errors when you attempt to push your changes, the repository may be private and require SSH access. For more information, read our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

## Set up pull deployment

### Clone the remote repository to your cPanel account

If the repository that you wish to deploy does not already exist on your cPanel account, use cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*) to clone the desired remote repository.

Note:

This feature enforces several restrictions on clone URLs, and it verifies the remote host’s public SSH keys for `ssh://` clone URLs.

### Clone the remote repository to your local computer

If you have **not** already cloned the remote repository, use the terminal on your local computer to clone the remote repository.

For example, run the following command to clone a repository, where URL represents the remote repository’s clone URL:

```bash
git clone URL
```

### Create the .cpanel.yml file

In order to deploy changes from a cPanel-managed repository, you **must** check a `.cpanel.yml` file in to the top-level directory of your repository. You can create and commit this file to your local computer’s copy of the repository, or you can create and commit it on the remote repository.

If you use the remote repository, you will **require** read-write access or can submit a pull request to the remote repository. This tutorial uses changes from the local computer rather than the remote repository.

| `1 2 3 4 5 6 ` | `--- deployment: tasks: - export DEPLOYPATH=/home/user/public_html/ - /bin/cp index.html $DEPLOYPATH - /bin/cp style.css $DEPLOYPATH` |
| -------------- | ------------------------------------------------------------ |
|                |                                                              |

More:

For more information about the `.cpanel.yml` file, read our [Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment) documentation.

### Push changes to the remote repository

From your local computer, run the following command to push the changes from your local computer to the remote repository:

```bash
git push origin HEAD
```

### Pull and deploy changes from the cPanel interface

To pull the changes from the remote repository and then manually deploy them, perform the following steps:

1. Navigate to cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*).
2. Locate the desired repository in the list of repositories and click *Manage*.
3. Click the *Pull or Deploy* tab.
4. Click *Update from Remote* to pull changes from the remote repository.
5. Click *Deploy HEAD Commit* to deploy your changes.

Repeat these steps each time that you wish to pull and deploy changes. The system will **not** deploy changes for this deployment type automatically.



## Guide to Git™ — Deployment

Last modified: *November 13, 2024*

------

## Overview

The [*Git™ Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) feature allows you to deploy your cPanel-managed repositories. Generally, deployment sends finished code into production. You can use different configurations to automatically (push deployment) or manually (pull deployment) deploy changes.

- For example, you could use deployment to make changes to your website locally. Then, automatically send them to a directory on your cPanel account.
- For more information about how to deploy changes, read our [*Git™ Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) documentation.
- For more information about how to troubleshoot problems with this feature, read our [Advanced Configuration and Troubleshooting](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-advanced-configuration-and-troubleshooting/)documentation.
- For more information about Git commands, such as `git push`, `git pull`, or `git commit`, read our [Common Git Commands](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-commands) documentation.

## Requirements

Before deployment, repositories **must** meet the following requirements:

- A valid checked-in `.cpanel.yml` file in the top-level directory.
- One or more local or remote branches.
- A [clean working tree](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-common-git-terms/#working-tree).

If a repository does **not** meet these requirements, the system will **not** display deployment information. Also, it will disable deployment functionality.

## The deployment YAML file

The `.cpanel.yml` file determines how and where the changed files deploy. You must check a `.cpanel.yml` file in to the top-level directory for each cPanel-managed repository that you deploy. The `.cpanel.yml` files must use the format in the examples below.

Important:

- The files below are only **examples**. You **must** update them to suit your needs. These files will not allow you to deploy a repository successfully.
- **Don’t** use a wildcard character, such as an asterisk, to deploy all files. This could deploy items like the `.git` directory and cause serious problems.
- **Don’t** use characters that are invalid in YAML files. For more information, read the [Escaped Characters section of yaml.org’s YAML Specification](https://yaml.org/spec/1.2/spec.html#id2776092).

### Deploy individual files

The following `.cpanel.yml` file deploys the `index.html` and `style.css` files to the `example` account’s `public_html` directory:

| `1 2 3 4 5 6 ` | `--- deployment:  tasks:    - export DEPLOYPATH=/home/example/public_html/    - /bin/cp index.html $DEPLOYPATH    - /bin/cp style.css $DEPLOYPATH` |
| -------------- | ------------------------------------------------------------ |
|                |                                                              |

- Line 1 is the beginning of a YAML file.
- Lines 2 and 3 add the `deployment` and `tasks` keys, respectively.
- Lines 4 through 6 specify an array of BASH commands to run during deployment. You can add as many commands to this array as you wish.

Note:

To add comments to this file, add a line that begins with the hash character (`#`).

### Deploy an entire directory

The following `.cpanel.yml` file copies the `images` directory and all of its contents to the `example` account’s `public_html` directory:

| `1 2 3 4 5 ` | `--- deployment:  tasks:    - export DEPLOYPATH=/home/example/public_html/    - /bin/cp -R images $DEPLOYPATH` |
| ------------ | ------------------------------------------------------------ |
|              |                                                              |



- Line 1 is the beginning of a YAML file.
- Lines 2 and 3 add the `deployment` and `tasks` keys, respectively.
- Lines 4 and 5 specify an array of BASH commands to run during deployment. You can add as many commands to this array as you wish.

Note:

To add comments to this file, add a line that begins with the hash character (`#`).

## Automatic or push deployment

Important:

cPanel’s [*Git™ Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) automatically adds a post-receive hook to all cPanel-managed repositories.

- When you push changes directly to a cPanel-managed repository that includes a `.cpanel.yml` file, the hook deploys those changes automatically.
- For more information, read Git’s [githooks](https://git-scm.com/docs/githooks) documentation.

![img](https://docs.cpanel.net/img/git-push-deployment-workflow.png)

With push deployment, a single `git push` command sends changes from your local computer to your cPanel-managed repository. The system then automatically runs the commands in your `.cpanel.yml` file. This configuration will send changes from the cPanel-managed repository to a production directory. (For example, to the directory that contains your website’s public files.)

Note:

You can use manual deployment to deploy your repository again without new changes.

## Manual or pull deployment

![img](https://docs.cpanel.net/img/git-pull-deployment-workflow.png)

With pull deployment, the `git push` command sends changes from your local computer to a remote repository.

- When you click *Update from Remote* in the *Pull or Deploy* tab of the *Manage* section of cPanel’s [*Git™ Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*), the system retrieves changes from the remote repository and applies them to the cPanel-managed repository.
- When you click *Deploy HEAD Commit*, the system runs the commands in your `.cpanel.yml` file to send changes from the cPanel-managed repository to a production directory. (For example, to the directory that contains your website’s public files.)

## Guide to Git™ — Set Up Deployment Cron Jobs

Last modified: *November 13, 2024*

------

## Overview

If you wish to deploy the contents of a cPanel-managed repository on a schedule, you can set up deployment cron jobs. Cron jobs allow you to configure the system to run a specified command automatically at a specified interval.

For more information about deployment, read our [Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment/) documentation.

## Find the repository path

In order to configure your deployment cron job, you **must** use the correct repository path.

To locate the desired repository’s directory, navigate to cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control/) interface (*cPanel » Home » Files » Git Version Control*). Then, in the list of repositories, locate the *Repository Path* value for the desired repository.

## Configure your cron job

The [*Cron Jobs*](https://docs.cpanel.net/cpanel/advanced/cron-jobs/) interface (*cPanel » Home » Advanced » Cron Jobs*) allows you to configure cron jobs.

To configure your deployment cron job, perform the following steps:

1. Select the interval at which you wish to run the cron job. You can select a commonly-used interval from the *Common Settings* menu, or select or enter a specific interval for the following values:

   - *Minute* — The number of minutes between each time that the cron job runs or the minute of each hour on which you wish to run the cron job.
   - *Hour* — The number of hours between each time that the cron job runs or the hour of each day on which you wish to run the cron job.
   - *Day* — The number of days between each time that the cron job runs or the day of the month on which you wish to run the cron job.
   - *Month* — The number of months between each time that the cron job runs or the month in which you wish to run the cron job.
   - *Weekday* — The days of the week on which you wish to run the cron job.

2. In the *Command* text box, enter the commands that you wish the system to run. For example, where `/home/user/example` represents the repository’s *Repository Path* value:

   ```perl
   /usr/bin/uapi VersionControlDeployment create repository_root=/home/user/example
   ```

   If your server runs CloudLinux™, begin these commands with the `/usr/local/cpanel/bin/` file path. For example:

   ```perl
   /usr/local/cpanel/bin/uapi VersionControlDeployment create repository_root=/home/user/example 
   ```

   This command calls UAPI’s [`VersionControlDeployment::create`](https://api.docs.cpanel.net/openapi/cpanel/operation/VersionControlDeployment::create/) function, which creates a new deployment task. This task will run the deployment commands that you specified in your [`.cpanel.yml`](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment/#the-deployment-yaml-file) file once.

3. Click *Add New Cron Job*.

## Guide to Git™ — Advanced Configuration and Troubleshooting

Last modified: *November 13, 2024*

------

## Overview

The *Git Version Control* feature includes several changes from the Git™ default configuration. Additionally, we impose certain restrictions on cPanel-hosted repositories. This document is targeted at system administrators, and includes details of these configurations as well as information that may assist you in troubleshooting cPanel users’ issues.

## Restrictions

This feature imposes the following restrictions on cPanel-hosted repositories:

- Currently, we only support a single remote repository for each local repository. To use multiple remote repositories, users must **only** use the command line.
- Users **cannot** include whitespace or the following characters in repository paths: `\ * | " ' < > & @ ` $ { } [ ] ( ) ; ? : = % #`
- Users cannot use this feature to create, delete, or view repositories in the following cPanel-controlled directories:
  - `.cpanel`
  - `.cphorde`
  - `.htpasswds`
  - `.ssh`
  - `.trash`
  - `access-logs`
  - `cgi-bin`
  - `etc`
  - `logs`
  - `perl5`
  - `mail`
  - `spamassassin`
  - `ssl`
  - `tmp`
  - `var`

Note:

cPanel users **cannot** use the `.` or `..` directory references when they enter the repository path in the interface.

## Configuration changes

This feature alters the following configuration settings:

- `gc.auto` — We have disabled Git’s garbage-collection setting for all cPanel-managed repositories.

- ```
  receive.denyCurrentBranch
  ```

   

  — The system automatically sets this setting in each cPanel-managed repository’s configuration file to the

   

  ```
  updateInstead
  ```

   

  option.

  - The system ensures this configuration each time that you create a new repository via the [`VersionControl::create`](https://api.docs.cpanel.net/openapi/cpanel/operation/VersionControl::create/) function.
  - The `updateInstead` option causes Git to automatically update the working tree whenever you push changes into the current branch.

This feature uses a cPanel-provided Git package. The Git package symlinks Git binaries in the `/usr/local/cpanel/3rdparty/bin/` directory to the `/usr/local/cpanel/3rdparty/lib/path-bin/` directory, which causes them to exist in the user’s default path.

## Deployment

Important:

We **strongly** recommend that you only deploy changes from a remote repository or a clone of it on your local computer. You should **not** directly change the cPanel-managed repository’s contents. For more information about our suggested deployment configuration and how to set it up, read our [Set Up Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-deployment) documentation.

Before deployment, repositories **must** meet the following requirements:

- A valid checked-in `.cpanel.yml` file in the top-level directory.
- One or more local or remote branches.
- A clean working tree.

If a repository does **not** meet these requirements, the system will **not** display deployment information. Also, it will disable deployment functionality.

Note:

- The system adds a

   

  ```
  post-receive
  ```

   

  hook to all cPanel-managed repositories.

  - This hook will automatically run any commands in the .cpanel.yml file whenever changes deploy.
  - For more information, read Git’s [githooks](https://git-scm.com/docs/githooks#post-receive) documentation.

- The system stores deployment process-related historical data in an SQLite database within the `/home/user/.cpanel/datastore/vc_deploy.sqlite` file, where `user` represents the cPanel account name.

For instructions to set up deployment, read our [Set Up Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-deployment) documentation.

For more information about deployment, read our [Deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment) documentation.

## SSH host key verification

When users clone a repository via SSH, the system will automatically check for the remote server’s public SSH key in the `/home/user/.ssh/known_hosts` file, where `user` represents the account’s username.

- If the remote host is **not** registered with the system, the system will prompt the user to accept it. Then, it will add it to the `/home/user/.ssh/known_hosts` file, where `user` represents the account’s username.
- If the remote host is already registered, the system will display a confirmation message.
- If the remote host’s public key has changed, the system will display a warning.
  - For third-party remote hosts, check for announcements about public key updates. Most companies that host repositories make announcements about these changes.
  - For remote hosts that you control, consider whether recent events on your system have caused changes to the public key.
  - For any private repositories, make **certain** that you have performed the steps in our [Set Up Access to Private Repositories](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-set-up-access-to-private-repositories) documentation.

The system also performs these checks each time that a user updates the repository’s information or attempts to pull changes from the repository via the cPanel interface.

Warning:

If you cannot verify the validity of the change, exercise caution, especially if the repository includes sensitive content. An altered SSH key may indicate a [Man-in-the-Middle attack](https://docs.cpanel.net/knowledge-base/general-systems-administration/man-in-the-middle-attacks).

In order for users to see these warnings, you **must** enable the *Enable strict SSH host key checking* setting in the *Security* section of WHM’s [*Tweak Settings*](https://docs.cpanel.net/whm/server-configuration/tweak-settings) interface (*WHM » Home » Server Configuration » Tweak Settings*).

## Troubleshooting

If cPanel users experience problems with their repositories, use the following steps to troubleshoot them.

Note:

This feature logs messages and errors to the following locations:

- `/usr/local/cpanel/logs/error_log` — Errors and stack traces.
- `/home/username/.cpanel/logs/user_task_runner.log` — Queue-related items.
- `/home/username/.cpanel/logs/vc_TIMESTAMP_git_create.log` — Creation-related issues, where `TIMESTAMP` represents the time of the operation.
- `/home/username/.cpanel/logs/vc_TIMESTAMP_git_deploy.log` — Deployment-related issues, where `TIMESTAMP` represents the time of the operation.

### Missing repositories

If repositories exist on the command line but do not display in cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*), the issue may occur because the feature ignores repositories that users created on the command line.

### Missing branches

If the expected list of branches does not display in cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*), the issue may be due to the following causes:

- The branches exist in the copies of the repository on your local computer or remote repository host, but do **not** exist within the cPanel-managed repository.
- The repository is a bare repository. Bare repositories do not include branches.

### Cloned repositories

While the system clones the remote repository, cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) will **only** display the repository name and path.

When users clone a repository, the system clones it via a queued process that runs as that cPanel user. Clones can require a large amount of time, which depends on the size of the repository to clone.

- While the clone process runs, cPanel’s [*Git Version Control*](https://docs.cpanel.net/cpanel/files/git-version-control) interface (*cPanel » Home » Files » Git Version Control*) will **only** display the repository name, repository path, and a progress indicator. Additionally, the system will temporarily disable most of the management functionality for that repository.
- The `process_user_tasks` binary runs as the cPanel user to process each clone, and the queue for each user exists in their `.cpanel/user_tasks/` directory. To resolve issues with clones, stop the process and delete the directory.

## SSH access

If users experience problems with SSH access, ensure that the server and the users’ accounts include the following settings and configurations:

- Port 22 is publicly accessible. If the server uses a nonstandard Git port, use the `ssh -p port` command, where `port` represents the port number, to SSH in to the account.
- The *Shell Access* setting is enabled for the account in WHM’s [*Modify an Account*](https://docs.cpanel.net/whm/account-functions/modify-an-account) interface (*WHM » Home » Account Functions » Modify an Account*).
- The *SSH Access & Terminal* feature is enabled for the user’s feature list in WHM’s [*Feature Manager*](https://docs.cpanel.net/whm/packages/feature-manager) interface (*WHM » Home » Packages » Feature Manager*).

If none of these solutions fix the issue, ensure that the user correctly configured their **public** SSH keys in cPanel’s [*SSH Access*](https://docs.cpanel.net/cpanel/security/ssh-access) interface (*cPanel » Home » Security » SSH Access*).

Note:

If a user attempts to clone a remote repository via SSH and receives errors about a refused connection, perform one of the following actions:

- Clone the repository via HTTPS in a read-only configuration.
- Register the cPanel account’s SSH key pair with the remote repository’s host as a deployment key.

