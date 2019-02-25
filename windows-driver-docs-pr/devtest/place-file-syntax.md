---
title: Place File Syntax
description: The place file is a text file that BinPlace reads to determine the class subdirectories that are associated with a file it is placing.
ms.assetid: 49f58ed1-9a4d-4e3e-9248-eebd95271374
keywords:
- Place File Syntax Driver Development Tools
topic_type:
- apiref
api_name:
- Place File Syntax
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Place File Syntax


**Note**   Place files are now obsolete and should not be used. .



The place file is a text file that BinPlace reads to determine the class subdirectories that are associated with a file it is placing.

The path and name of this file are specified by the -p PlaceFile command-line parameter. If this is not used, the default is \\tools\\placefil.txt. A place file can have any number of lines. Each line lists a file and a class subdirectory. Listing a file does not cause BinPlace to take any action. Rather, whenever BinPlace is supplied a file name on the command line, it will open the place file to see if that file is listed. If it is, BinPlace will use the class subdirectory specified in the place file for that particular file.

Each line of a place file has the same format.

```

     FileName Class[:Class[...]   [ ; Comment ] 
```

Each line in the place file follows these rules:

-   The *FileName* field must begin the line.
-   The *FileName* and *Class* fields must be separated by one or more spaces.
-   If a semicolon appears anywhere on the line, everything to the right of it is treated as a comment.
-   Blank lines and comment lines that begin with semicolons are permitted.

The *FileName* and *Class* fields are explained as follows:

## <span id="ddk_place_file_syntax_tools"></span><span id="DDK_PLACE_FILE_SYNTAX_TOOLS"></span>Parameters


<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
A field that specifies the name of a file that BinPlace can act on. *FileName* must include the file name extension, but it must not include the file path. (File paths will be specified on the BinPlace command line.)

<span id="_______Class______"></span><span id="_______class______"></span><span id="_______CLASS______"></span> *Class*   
A field that specifies the class subdirectory that is used for this file. Unless the **-y** or **-:DEST** command-line switches are used, BinPlace places a file in a directory that is created by taking the root destination directory, appending the class subdirectory, and then appending the file-type subdirectory. See [BinPlace Destination Directories](binplace-destination-directories.md) for full details.

*Class* should neither begin nor end with a backslash. Directory names must not contain spaces. There are special strings that can be used within a *Class* value. The effect of the string is different on the placement of executable files and symbol files. The following tables show the results of these strings.

For all builds:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">String</th>
<th align="left">Effect on executable files</th>
<th align="left">Effect on symbol files</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>retail</strong></p></td>
<td align="left"><p>Ignored. This directory level will be skipped.</p></td>
<td align="left"><p>Treated as a literal directory named <strong>retail</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*</strong></p></td>
<td align="left"><p></p>
On an x86 computer: <strong>i386</strong>.
On an Itanium-based computer: <strong>IA64</strong>.
On an x64-based computer: <strong>AMD64</strong>.</td>
<td align="left"><p>Ignored. This directory level will be skipped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>system</strong></p></td>
<td align="left"><p>Becomes <strong>system32</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>system16</strong></p></td>
<td align="left"><p>Becomes <strong>system</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>windows</strong></p></td>
<td align="left"><p>Becomes &quot;.&quot; Ignored. This directory level will be skipped.</p></td>
<td align="left"><p>Symbol path is <strong>retail</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>drivers</strong></p></td>
<td align="left"><p>Becomes <strong>system32\drivers</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>drvetc</strong></p></td>
<td align="left"><p>Becomes <strong>system32\drivers\etc</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>config</strong></p></td>
<td align="left"><p>Becomes <strong>system32\config</strong>.</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>



For x86 builds:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">String</th>
<th align="left">Effect on executable files</th>
<th align="left">Effect on symbol files</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>hal</strong></p></td>
<td align="left"><p>Becomes <strong>system32</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>printer</strong></p></td>
<td align="left"><p>Becomes <strong>system32\spool\drivers\w32x86</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>prtprocs</strong></p></td>
<td align="left"><p>Becomes <strong>system32\spool\prtprocs\w32x86</strong>.</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>



For AMD64 builds:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">String</th>
<th align="left">Effect on executable files</th>
<th align="left">Effect on symbol files</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>hal</strong></p></td>
<td align="left"><p>Becomes &quot;<strong>..</strong>&quot; For example, if the root destination directory is C:\Binaries\Amd64, the file is placed in C:\Binaries.</p></td>
<td align="left"><p>Symbol path is stripped of one directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>printer</strong></p></td>
<td align="left"><p>Becomes <strong>system32\spool\drivers\w32amd64</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>prtprocs</strong></p></td>
<td align="left"><p>Becomes <strong>system32\spool\prtprocs\w32amd64</strong>.</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>



For IA64 builds:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">String</th>
<th align="left">Effect on executable files</th>
<th align="left">Effect on symbol files</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>hal</strong></p></td>
<td align="left"><p>Becomes &quot;<strong>..</strong>&quot;</p></td>
<td align="left"><p>Symbol path is stripped of one directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>printer</strong></p></td>
<td align="left"><p>Becomes <strong>system32\spool\drivers\w32ia64</strong>.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>prtprocs</strong></p></td>
<td align="left"><p>Becomes <strong>system32\spool\prtprocs\w32ia64</strong>.</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>



Unless otherwise noted, the symbol path is truncated to include only the first directory in the path. For example, if you were using BinPlace to move an x86 file called Build.exe that has the target class of **printer**, you might use the following command syntax:

```
binplace -r BinaryRoot  -xa -s SymbolsDir1 -n SymbolsDir2 SourceFileLocation\build.exe
```

The command would result in the following output tree:

```
<SymbolsDir1>\system32\exe\build.pdb
<SymbolsDir2>\system32\exe\build.pdb 
<BinaryRoot>\system32\spool\drivers\w32x86\build.exe 
```

For AMD64 and IA64 builds, use the **hal** class with caution because the BinPlace results might not be what you expect. For example, if the root destination directory is C:\\Binaries\\Amd64, and you specified the **hal** class, the file is placed in C:\\Binaries and not in the processor-specifc directory that you might have intended.

If you want a file to be placed in multiple locations, you can include multiple instances of *Class*, separated by colons. There must not be spaces between the directories and the colons. For example:

```
someprogram.exe   dir1\dir2\dir3:otherdir1\otherdir2   ; To two locations
```

<span id="_______Comment______"></span><span id="_______comment______"></span><span id="_______COMMENT______"></span> *Comment*   
Any text after a semicolon will be ignored by BinPlace.









