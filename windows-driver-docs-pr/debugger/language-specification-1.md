---
title: Language Specification 1
description: Language Specification 1
ms.assetid: 7c770200-ed2a-47e0-8389-e79a5624a3dd
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Language Specification 1


The first version of SrcSrv works as follows. (This behavior may change in future versions.)

First, the client calls **SrcSrvInit** with the target path to be used as a base for all source file extractions. This path is stored in the special variable TARG.

When DbgHelp loads a module's .pdb file, it extracts the SrcSrv stream from the .pdb file and passes this data block to SrcSrv by calling **SrcSrvLoadModule**.

Then when DbgHelp needs to obtain a source file, it calls **SrcSrvGetFile** to retrieve a specified source file from version control.

SrcSrv reviews all the source file entries in the data block for an entry that matches exactly the requested source specification. This match is found in VAR1.

After SrcSrv finds the entry, it fills in the special variables (VAR1, VAR2, etc.) with the contents of this source file entry. Then the SRCSRVTRG variable is resolved using these special variables.

The following shows how the SRCSRVTRG variable is resolved using the special variables. We assume that the source path is still:

```console
c:\proj\src\file.cpp*TOOLS_PRJ*tools/mytool/src/file.cpp*3 
```

Each line shows the resolution of one more special variable. The resolved variables are bold.

```console
SRCSRVTRG=%sdtrg% 
SDTRG=%targ%\%var2%\%fnbksl%(%var3%)\%var4%\%fnfile%(%var1%)
c:\src\%var2%\%fnbksl%(%var3%)\%var4%\%fnfile%(%var1%)
c:\src\WIN_SDKTOOLS\%fnbksl%(%var3%)\%var4%\%fnfile%(%var1%)
c:\src\WIN_SDKTOOLS\%fnbksl%( sdktools/debuggers/srcsrv/shell.cpp )\%var4%\%fnfile%(%var1%)
c:\src\WIN_SDKTOOLS\ sdktools\debuggers\srcsrv\shell.cpp\%var4%\%fnfile%(%var1%)
c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\%fnfile%(%var1%)
c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\%fnfile%( c:\db\srcsrv\shell.cpp)
c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\shell.cpp
```

Notice how this generated target path is unique and does not allow two versions of the same file to be extracted to the same location.

SrcSrv now looks to see if the file is already there. If it is, SrcSrv returns the location to the caller. Otherwise, SrcSrv builds the execution command to extract the file by resolving SRCSRVCMD.

In the following example, each line shows the resolution of one more special variable. The resolved variables are bold.

```console
DEPOT=//depot 
WIN_SDKTOOLS= sserver.microsoft.com:4444 
SRCSRVCMD=%sdcmd% 
SDCMD=sd.exe -p %fnvar%(%var2%) print -o %srcsrvtrg% -q %depot%/%var3%#%var4% 
sd.exe -p %fnvar%(WIN_SDKTOOLS) print -o %srcsrvtrg% -q %depot%/%var3%#%var4% 
sd.exe -p sserver.microsoft.com:4444  print -o %srcsrvtrg% -q %depot%/%var3%#%var4% 
sd.exe -p sserver.microsoft.com:4444  print -o c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\shell.cpp -q %depot%/%var3%#%var4% 
sd.exe -p sserver.microsoft.com:4444  print -o c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\shell.cpp -q //depot/%var3%#%var4% 
sd.exe -p sserver.microsoft.com:4444  print -o c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\shell.cpp -q //depot/ sdktools/debuggers/srcsrv/shell.cpp#%var4% 
sd.exe -p sserver.microsoft.com:4444  print -o c:\src\WIN_SDKTOOLS\sdktools\debuggers\srcsrv\shell.cpp\3\shell.cpp -q //depot/ sdktools/debuggers/srcsrv/shell.cpp#3 
```

Now SrcSrv executes this command. If the result of this command is a file in the expected location, this path is returned to the caller.

Note that if a variable cannot be resolved, an attempt is made to look it up as an OS environment variable. If that fails, the variable name is deleted from the text being processed.

Two consecutive percent sign characters are interpreted as a single percent sign.

### <span id="source_server_data_blocks"></span><span id="SOURCE_SERVER_DATA_BLOCKS"></span>Source Server Data Blocks

SrcSrv relies on two blocks of data within the .pdb file, the source file list and the data block.

The source file list is created automatically when a module is built. This list contains fully qualified paths to the source files used to build the module.

The data block is created during source indexing. At this time, an alternative stream named "srcsrv" is added to the .pdb file. The script that inserts this data is dependent on the specific build process and source control system in use.

The data block is divided into three sections: ini, variables, and source files. The data block has the following syntax.

```console
SRCSRV: ini ------------------------------------------------ 
VERSION=1
VERCTRL=<source_control_str>
DATETIME=<date_time_str>
SRCSRV: variables ------------------------------------------ 
SRCSRVTRG=%sdtrg% 
SRCSRVCMD=%sdcmd% 
SRCSRVENV=var1=string1\bvar2=string2 
DEPOT=//depot 
SDCMD=sd.exe -p %fnvar%(%var2%) print -o %srcsrvtrg% -q %depot%/%var3%#%var4% 
SDTRG=%targ%\%var2%\%fnbksl%(%var3%)\%var4%\%fnfile%(%var1%) 
WIN_SDKTOOLS= sserver.microsoft.com:4444 
SRCSRV: source files --------------------------------------- 
<path1>*<var2>*<var3>*<var4> 
<path2>*<var2>*<var3>*<var4> 
<path3>*<var2>*<var3>*<var4> 
<path4>*<var2>*<var3>*<var4> 
SRCSRV: end ------------------------------------------------
```

All text is interpreted literally, except for text enclosed in percent signs (%). Text enclosed in percent signs is treated as a variable name to be resolved recursively, unless it is one of the following functions:

<span id="_fnvar___"></span><span id="_FNVAR___"></span>**%fnvar%()**  
The parameter text should be enclosed in percent signs and treated as a variable to be resolved.

<span id="_fnbksl___"></span><span id="_FNBKSL___"></span>**%fnbksl%()**  
All forward slashes (/) in the parameter text should be replaced with backward slashes (\).

<span id="_fnfile___"></span><span id="_FNFILE___"></span>**%fnfile%()**  
All path information in the parameter text should be stripped out, leaving only the file name.

The \[ini\] section of the data block contains variables that describe the requirements. The indexing script can add any number of variables to this section. The following are examples:

<span id="VERSION"></span><span id="version"></span>**VERSION**  
The language specification version. This variable is required. If you develop a script based on the current language specification, set this value to 1. The SrcSrv client code does not attempt to execute any script that has a value greater than its own. Current versions of SrcSrv use a value of 2.

<span id="VERCTL"></span><span id="verctl"></span>**VERCTL**  
A string that describes the source version control system. This variable is optional.

<span id="DATETIME"></span><span id="datetime"></span>**DATETIME**  
A string that indicates the date and time the .pdb file was processed. This variable is optional.

The \[variables\] section of the data block contains variables that describe how to extract a file from source control. It can also be used to define commonly used text as variables to reduce the size of the data block.

<span id="SRCSRV"></span><span id="srcsrv"></span>**SRCSRV**  
Describes how to build the target path for the extracted file. This is a required variable.

<span id="SRCSRVCMD"></span><span id="srcsrvcmd"></span>**SRCSRVCMD**  
Describes how to build the command to extract the file from source control. This includes the name of the executable file and its command-line parameters. This is required if any extraction command must be executed.

<span id="SRCSRVENV"></span><span id="srcsrvenv"></span>**SRCSRVENV**  
Lists environment variables to be created during the file extraction. This is a string. Separate multiple entries with a backspace character (\\b). This is an optional variable.

<span id="SRCSRVVERCTRL"></span><span id="srcsrvverctrl"></span>**SRCSRVVERCTRL**  
Specifies the version control system in use. For Perforce, this is perforce. For Visual SourceSafe, this is vss. For Team Foundation Server, this is tfs. This variable is used to persist server errors. This is an optional variable.

<span id="SRCSRVVERRDESC"></span><span id="srcsrvverrdesc"></span>**SRCSRVVERRDESC**  
Specifies the text to display when the version control client is unable to contact the server that contains the source files to extract. SrcSrv uses this value to check for connection problems. This is an optional variable.

<span id="SRCSRVERRVAR"></span><span id="srcsrverrvar"></span>**SRCSRVERRVAR**  
Indicates which variable in a file entry corresponds to a version control server. It is used by SrcSrv to identify commands that do not work, based on previous failures. The format of the text is **var***X* where *X* is the number of the variable being indicated. This is an optional variable.

The \[source files\] section of the data block contains an entry for each source file that has been indexed. The contents of each line are interpreted as variables with the names VAR1, VAR2, VAR3, and so on until VAR10. The variables are separated by asterisks. VAR1 must specify the fully qualified path to the source file as listed elsewhere in the .pdb file. For example:

```console
c:\proj\src\file.cpp*TOOLS_PRJ*tools/mytool/src/file.cpp*3 
```

is interpreted as follows:

```console
VAR1=c:\proj\src\file.cpp
VAR2=TOOLS_PRJ
VAR3=tools/mytool/src/file.cpp
VAR4=3
```

In this example, VAR4 is a revision number. However, most source control systems support labeling files in such a way that the source state for a given build can be restored. Therefore, you could instead use the label for the build. The sample data block could be modified to contain a variable such as the following:

```console
LABEL=BUILD47 
```

Then, presuming the source control system uses the at sign (@) to indicate a label, you could modify the SRCSRVCMD variable as follows:

```console
sd.exe -p %fnvar%(%var2%) print -o %srcsrvtrg% -q %depot%/%var3%@%label%
```

### <span id="handling_server_errors"></span><span id="HANDLING_SERVER_ERRORS"></span>Handling Server Errors

Sometimes a client is unable to extract any files at all from a single version control server. This can be because the server is down and off the network or because the user does not have appropriate privileges to access the source. However, the time consumed attempting to get this source can slow things down significantly. In this situation, it is best to disable any attempt to extract from a source that has been proven to be unavailable.

Whenever SrcSrv fails to extract a file, it examines the output text produced by the command. If any part of this command contains an exact match for the contents of the SRCSRVERRDESC, all future commands to the same version control server are skipped. Note that you can define multiple error strings by adding numbers or arbitrary text to the end of the SRCSRVERRDESC variable name. Here is an example:

```console
SRCSRVERRDESC=lime: server not found
SRCSRVERRDESC_2=pineapple: network error
```

The identity of the server is acquired from SRCSRVERRVAR. So if SRCSRVERRVAR contains "var2" and the file entry in the .pdb file looks like this:

```console
c:\proj\src\file.cpp*TOOLS_PRJ*tools/mytool/src/file.cpp*3
```

all future attempts to obtain source using a file entry that contains "TOOLS\_PRJ" in variable 2 are bypassed.

You can also add error indicators on the debugger client by editing [Srcsrv.ini](the-srcsrv-ini-file.md). See the included sample version of srcsrv.ini for details.

 

 





