title: "Shell scripts 101: day one"
date: 2012-01-01 16:20:00
published: 2012-01-01 16:20:00
subtitle: In which I try to make dealing with other people's shell scripts easier. 
description:
    Why you should use `set -e` and `set -u` at the top of every shell script.
created: !!timestamp 2012-01-01 16:20:00

## tl;dr ##

There are two basic settings I think all shell scripts should be using to prevent potentially perilous execution: the exit on error (`set -e`) and exit on expanding an unset variable (`set -u`) options.

## Why? ##

Consider the following script, perhaps intended to remove an instance of a web site by name passed as an argument, from a base directory stored in a file.

	:::shell
	#!/bin/sh
	
	TMPDIR=`cat /etc/foo`
	INSTANCE=$1
	rm -rf ${TMPDIR}/${INSTANCE}
	01234567890123456789012345678901234567890123456789012345678901234567890123456789

If `/etc/foo` does not exist, and no argument is given to the script, it will delete everything from the root directory down.

Using `set -e` will exit the program if `cat /etc/foo` returns with an error code.  This prevents us from deleting everything, but if the argument isn't given, it will delete all instances in that base directory.

Using `set -u` will exit the program when `$1` is expanded when unset.  This saves us from potentially deleting more than we expected. 

Usually, errors are not this catastrophic, and problems of this magnitude are rarely not caught during self or peer code review by somewhat experienced users of shell scripts. But smaller and more subtle errors happen more often, and these options can help debug these. 

## Downsides and other considerations ##

But what if you expect an error?  Or how do we turn an ugly, harder to understand, error into something useful to the users of the script?

You can use the `||` operator to specify what to do if the command fails.  For example, imagine you want to check a web page to see if you should upgrade

	:::shell
	#!/bin/sh
	
	current_version=`curl http://foo/v` || \
		(echo "Update server down, contact your sysadmin."; exit 1)

It is easy to forget that (well-behaving) command line tools signal their failure to achieve at least some of what they were asked to do via exit codes.  For example, `grep` will return an exit code (and thus exit your shell script unless you catch it) if it does not find any matches.  This includes if you are using the `-c` argument to `grep` to have it count matches.
