---
title: Using SymChk
description: Using SymChk
ms.assetid: 60c3df99-a842-4e46-a504-8e2b54030eef
keywords: ["SymChk, using"]
---

# Using SymChk


## <span id="ddk_using_symchk_dtoolq"></span><span id="DDK_USING_SYMCHK_DTOOLQ"></span>


The basic syntax for SymChk is as follows:

``` syntax
symchk [/r] FileNames /s SymbolPath 
```

*FileNames* specifies one or more program files whose symbols are needed. If *FileNames* is a directory and the **/r** flag is used, this directory is explored recursively, and SymChk will try to find symbols for all program files in this directory tree. *SymbolPath* specifies where SymChk is to search for symbols.

There are many more command-line options. For a full listing, see [**SymChk Command-Line Options**](symchk-command-line-options.md).

The symbol path specified can include any number of local directories, UNC directories, or symbol servers. Local directories and UNC directories are not searched recursively. Only the specified directory and a subdirectory based on the executable's extension are searched. For example, the query

``` syntax
symchk thisdriver.sys /s g:\symbols 
```

will search g:\\mysymbols and g:\\mysymbols\\sys.

You can specify a symbol server by using either of the following syntaxes as part of your symbol path:

``` syntax
srv*DownstreamStore*\\Server\Share
srv*\\Server\Share
```

This is very similar to using a symbol server in the debugger's symbol path. For details on this, see [Using Symbol Servers and Symbol Stores](symbol-stores-and-symbol-servers.md).

If a downstream store is specified, SymChk will make copies of all valid symbol files found by the symbol server and place them in the downstream store. Only symbol files that are complete matches are copied downstream.

SymChk always searches the downstream store before querying the symbol server. Therefore you should be careful about using a downstream store when someone else is maintaining the symbol store. If you run SymChk once and it finds symbol files, it will copy those to the downstream store. If you then run SymChk again after these files have been altered or deleted on the symbol store, SymChk will not notice this fact, since it will find what it is looking for on the downstream store and look no further.

**Note**   SymChk always uses SymSrv (Symsrv.dll) as its symbol server DLL. On the other hand, the debuggers can choose a symbol server DLL other than SymSrv if one is available. (SymSrv is the symbol server included in the Debugging Tools for Windows package.)

 

### <span id="Using_SymChk_to_determine_whether_symbols_are_private_or_public"></span><span id="using_symchk_to_determine_whether_symbols_are_private_or_public"></span><span id="USING_SYMCHK_TO_DETERMINE_WHETHER_SYMBOLS_ARE_PRIVATE_OR_PUBLIC"></span>Using SymChk to determine whether symbols are private or public

To determine whether a symbol file is private or public, use the **/v** parameter so that SymChk displays verbose output. Suppose MyApp.exe and MyApp.pdb are in the folder c:\\sym. Enter this command.

**symchk /v c:\\sym\\MyApp.exe /s c:\\sym**

If MyApp.pdb contains private symbols, the output of SymChk looks like this.

``` syntax
[SYMCHK] Searching for symbols to c:\sym\MyApp.exe in path c:\sym
...
DBGHELP: MyApp - private symbols & lines
        c:\sym\MyApp.pdb
...
SYMCHK: FAILED files = 0
SYMCHK: PASSED + IGNORED files = 1
```

If MyApp.pdb contains only public symbols, the output of SymChk looks like this.

``` syntax
[SYMCHK] Searching for symbols to c:\sym\MyApp.exe in path c:\sym
...
DBGHELP: MyApp - public symbols
        c:\sym\MyApp.pdb
...
SYMCHK: FAILED files = 0
SYMCHK: PASSED + IGNORED files = 1
```

To limit your search so that it finds only public symbol files, use the **s** option with the **/s** parameter (**/ss**). The following command finds a match if MyApp.pdb contains only public symbols. It does not find a match if MyApp.pdb contains private symbols.

**symchk /v c:\\sym\\MyApp.exe /ss c:\\sym**

For more information, see [Public and Private Symbols](public-and-private-symbols.md).

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

Here are some examples. The following command searches for symbols for the program Myapp.exe:

``` syntax
e:\debuggers> symchk f:\myapp.exe /s f:\symbols\applications 

SYMCHK: Myapp.exe           FAILED  - Myapp.pdb is missing

SYMCHK: FAILED files = 1
SYMCHK: PASSED + IGNORED files = 0
```

You can try again with a different symbol path:

``` syntax
e:\debuggers> symchk f:\myapp.exe /s f:\symbols\newdirectory 

SYMCHK: FAILED files = 0
SYMCHK: PASSED + IGNORED files = 1
```

The search was successful this time. If the verbose option is not used, SymChk will only list files for which it failed to find symbols. So in this example no files were listed. You can tell that the search succeeded because there is now one file listed in the "passed" category and none in the "failed" category.

A program file is ignored if it contains no executable code. Many resource files are of this type.

If you prefer to see the file names of all program files, you can use the **/v** option to generate verbose output:

``` syntax
e:\debuggers> symchk /v f:\myapp.exe /s f:\symbols\newdirectory 

SYMCHK: MyApp.exe           PASSED

SYMCHK: FAILED files = 0
SYMCHK: PASSED + IGNORED files = 1
```

The following command searches for a huge number of Windows symbols in a symbol server. There are a great variety of possible error messages:

``` syntax
e:\debuggers> symchk /r c:\windows\system32 /s srv*\\manysymbols\windows 

SYMCHK: msisam11.dll         FAILED  - MSISAM11.pdb is missing
SYMCHK: msuni11.dll          FAILED  - msuni11link.pdb is missing
SYMCHK: msdxm.ocx            FAILED  - Image is split correctly, but msdxm.dbg i
s missing
SYMCHK: expsrv.dll           FAILED  - Checksum doesn't match with expsrv.DBG
SYMCHK: imeshare.dll         FAILED  - imeshare.opt.pdb is missing
SYMCHK: ir32_32.dll          FAILED  - Built with no debugging information
SYMCHK: author.dll           FAILED  - rpctest.pdb is missing
SYMCHK: msvcrt40.dll         FAILED  - Built with no debugging information
......
SYMCHK: FAILED files = 211
SYMCHK: PASSED + IGNORED files = 4809
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20SymChk%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




