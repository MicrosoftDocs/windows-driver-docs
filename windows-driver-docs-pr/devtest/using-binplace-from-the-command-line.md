---
title: Using BinPlace from the Command Line
description: Using BinPlace from the Command Line
ms.assetid: ed92fee5-d45c-437a-8c3f-de51b910c2ae
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using BinPlace from the Command Line


**Important**  The examples in this topic discuss the use of the BINPLACE\_PLACEFILE macro and the [BinPlace](binplace.md)[**place file**](place-file-syntax.md). This macro and file are obsolete in the Windows 7 version of the Windows Driver Kit and may not be supported in future versions of the WDK.

 

This topic provides examples of using BinPlace from the command-line.

First, you can set the root destination directory as follows:

```
set _NTTREE=d:\ProjectRoot
```

Then you can set the place file's path and file name in the following way:

```
set BINPLACE_PLACEFILE=d:\mystuff\myplacefile.txt
```

Let the contents of the file d:\\mystuff\\myplacefile.txt be as follows:

```
; This is a simple place file.
commonmodule.dll   retail
application.exe    files\bin
mydriver.sys       *\drivertree
extra.cab          appendix
```

Now you can run BinPlace with the following command:

```
binplace g:\somelocation\extra.cab
```

Because extra.cab is not an executable file, BinPlace will only move it. The root destination directory is d:\\projectroot. The class directory for this file is specified in the place file as **appendix**. The file-type subdirectory is cab (the file name extension of the file being moved). Thus, this file is copied to the location d:\\projectroot\\appendix\\cab\\extra.cab.

Now use BinPlace on the executable file and its symbol file. To do this, you specify the executable file name -- BinPlace will find the associated symbol file.

When you pass an executable file name to BinPlace, it looks for its symbol files in the same directory as the executable file. If it does not find them there, it reads the CodeView record stored in the executable file; if it finds a symbol file path in that record, it looks for symbol files in that path.

**Note**   If you specify a symbol file name explicitly, BinPlace will merely move it, not process it.

 

```
binplace -a -x -s d:\stripped -n g:\full g:\builddir\application.exe
```

The executable file uses the same root destination directory as before. Its class directory is files\\bin. Thus, it is placed in d:\\projectroot\\files\\bin\\application.exe.

The symbol file is placed in two locations. The full symbol file (including both private and public symbols) goes to g:\\full\\files\\bin\\exe\\application.pdb. The stripped symbol file (containing only public symbols) goes to d:\\stripped\\files\\bin\\exe\\application.pdb.

Now, use a similar command on commonmodule.dll:

```
binplace -a -x -s d:\stripped -n g:\full g:\builddir\commonmodule.dll
```

This time, the class subdirectory is **retail**. For the executable file, this directory name is a code for "do not use a class subdirectory," so it is placed in d:\\projectroot\\application.exe. The symbol files are placed in g:\\full\\retail\\dll\\application.pdb and d:\\stripped\\retail\\dll\\application.pdb.

Finally, use BinPlace on mydriver.sys and omit the **-n** switch:

```
binplace -a -x -s d:\stripped g:\builddir\mydriver.sys
```

Here the class subdirectory is **\*/drivertree**. For the executable file, the asterisk (\*) is replaced with the processor type. Assuming you are running on an x86 computer, the executable file is placed in d:\\projectroot\\i386\\drivertree\\application.exe. The stripped symbol file is placed in g:\\full\\drivertree\\sys\\application.pdb, because the asterisk is ignored for a symbol file. Because the **-n** switch was omitted, the full symbol file is not placed anywhere.

 

 





