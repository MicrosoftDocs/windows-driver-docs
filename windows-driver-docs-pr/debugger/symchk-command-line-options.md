---
title: SymChk Command-Line Options
description: SymChk uses the following syntax
ms.assetid: e17dd001-2830-49bd-b727-fcd772ee23b4
keywords: ["SymChk Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 06/28/2017
topic_type:
- apiref
api_name:
- SymChk Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# SymChk Command-Line Options


SymChk uses the following syntax:

```dbgcmd
symchk [/r] [/v | /q ] FileNames /s[Opts] SymbolPath Options

symchk [/r] [/v | /q ] /ie ExeFile /s[Opts] SymbolPath Options

symchk [/r] [/v | /q ] /id DumpFile /s[Opts] SymbolPath Options

symchk [/r] [/v | /q ] /ih HotFixFile /s[Opts] SymbolPath Options

symchk [/r] [/v | /q ] /ip ProcessID /s[Opts] SymbolPath Options

symchk [/r] [/v | /q ] /it TextFileList /s[Opts] SymbolPath Options

symchk [/r] [/v | /q ] /om Manifest FileNames

symchk [/v | /q ] /im ManifestList /s[Opts] SymbolPath Options

symchk [/v | /q ] /om Manifest /ie ExeFile

symchk [/v | /q ] /om Manifest /id DumpFile

symchk [/v | /q ] /om Manifest /ih HotFixFile

symchk [/v | /q ] /om Manifest /ip ProcessFile

symchk [/v | /q ] /om Manifest /it TextFileList
```

## <span id="ddk_symchk_command_line_options_dtoolq"></span><span id="DDK_SYMCHK_COMMAND_LINE_OPTIONS_DTOOLQ"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
If *Files* specifies a directory, the **/r** option causes SymChk to recursively search all subdirectories under this directory for program files.

<span id="________v______"></span><span id="________V______"></span> **/v**   
Displays verbose information. This includes the file name of every program file whose symbols were investigated and whether it passed, failed, or was ignored.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Enables quiet mode. All output will be suppressed (unless the **/ot** option is included).

<span id="_______FileNames______"></span><span id="_______filenames______"></span><span id="_______FILENAMES______"></span> *FileNames*   
Specifies the program files whose symbols are to be checked. Absolute paths, relative paths, and UNC paths are permitted. An asterisk (**\\**<em>) wildcard is permitted. If *FileNames</em> ends in a slash, it is taken to be a directory name, and all files within that directory are checked. If *FileNames* contains spaces, it must be enclosed in quotation marks.

<span id="________ie_______ExeFile______"></span><span id="________ie_______exefile______"></span><span id="________IE_______EXEFILE______"></span> **/ie** *ExeFile*   
Specifies the name of a program that is currently executing. The symbols for this program will be checked. *ExeFile* must include the name of the file and file extension (usually .exe), but no path information. If there are two different executables with the same name, this option is not recommended. *ExeFile* can specify any program, including a kernel-mode driver. If *ExeFile* is a single asterisk ( **\\*** ), SymChk will check the symbols for all running processes, including drivers.

<span id="________id_______DumpFile______"></span><span id="________id_______dumpfile______"></span><span id="________ID_______DUMPFILE______"></span> **/id** *DumpFile*   
Specifies a memory dump file. The symbols for this dump file will be checked.

<span id="________ih_______HotFixFile______"></span><span id="________ih_______hotfixfile______"></span><span id="________IH_______HOTFIXFILE______"></span> **/ih** *HotFixFile*   
Specifies a self-extracting Hotfix CAB file.

<span id="________ip_______ProcessID______"></span><span id="________ip_______processid______"></span><span id="________IP_______PROCESSID______"></span> **/ip** *ProcessID*   
Specifies the process ID of a program that is currently executing. The symbols for this program will be checked. *ProcessID* must be specified as a decimal number. There are two special wildcards supported:

- If *ProcessID* is zero ( **0** ), SymChk will check the symbols for all running drivers.

- If *ProcessID* is a single asterisk ( **\\*** ), SymChk will check the symbols for all running processes, including drivers.

<span id="________it_______TextFileList______"></span><span id="________it_______textfilelist______"></span><span id="________IT_______TEXTFILELIST______"></span> **/it** *TextFileList*   
Specifies a text file that contains a list of program files. The symbols for all these programs will be checked. *TextFileList* must specify exactly one file (by relative, absolute, or UNC path, but with no wildcards); if it contains spaces it should be enclosed in quotation marks. Within this file, each line indicates a program file (by relative, absolute, or UNC paths), and an asterisk wildcard (**\\***) is permitted. However, any line using this wildcard must use a relative path.

If a line in this file contains spaces, it should be enclosed in quotation marks. A semicolon within this file is a comment character -- everything between a semicolon and the end of the line will be ignored.

<span id="________im_______ManifestList______"></span><span id="________im_______manifestlist______"></span><span id="________IM_______MANIFESTLIST______"></span> **/im** *ManifestList*   
Specifies that the input to the command is a manifest file previously created by using the **/om** parameter. The manifest file contains information about the files for which symbols are retrieved. For more information about using a manifest file, see [Using a Manifest File with SymChk](using-a-manifest-file-with-symchk.md).

<span id="________om_______Manifest______"></span><span id="________om_______manifest______"></span><span id="________OM_______MANIFEST______"></span> **/om** *Manifest*   
Specifies that a manifest file is created. The manifest file contains information about a set of files for which symbols will be retrieved, by using the **/im** parameter, at a later time.

<span id="________s_Opts__SymbolPath"></span><span id="________s_opts__symbolpath"></span><span id="________S_OPTS__SYMBOLPATH"></span> **/s**\[*Opts*\] *SymbolPath*  
Specifies the directories containing symbols. Absolute paths, relative paths, and UNC paths are permitted. Any number of directories can be specified -- multiple directories should be separated with semicolons. If *SymbolPath* contains spaces, it must be enclosed in quotation marks. If you wish to specify a symbol server within this path, you should use one of the following syntaxes:

```dbgcmd
srv*DownstreamStore*\\Server\Share
srv*\\Server\Share
```

It is not recommended that you omit the **/s**\[*Opts*\] *SymbolPath* parameter, but if it is omitted, SymChk will point to the public symbol store by using the following default path:

```dbgcmd
srv*%SystemRoot%\symbols*https://msdl.microsoft.com/download/symbols
```

Any number of the following options can follow **/s**. There can be no space between the **/s** and these options:

<span id="e"></span><span id="E"></span>**e**  
SymChk will check each path individually instead of checking all paths at once.

<span id="u"></span><span id="U"></span>**u**  
Downstream stores will be updated. If the symbol path includes a downstream store, the symbol store will be searched for the symbol files. Only symbol stores that are being checked by SymChk will be updated.

<span id="p"></span><span id="P"></span>**p**  
Force checking for private symbols. Public symbols will be treated as not matching. The **p** option implies **e** and **u**, and cannot be used with **s**.

<span id="s"></span><span id="S"></span>**s**  
Force checking for public (split) symbols. Private symbols will be treated as not matching. The **s** option implies **e** and **u**, and cannot be used with **p**.

<span id="r"></span><span id="R"></span>**r**  
Expand all non-symbol server elements in the specified path in order to do a deep search of the path. NOTE: This option may produce matches that will not occur inside the debugger since it modifies the symbol path specified.


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
The available options are divided into several classes. Each class of options controls a different set of features.

**Output options.** Any number of the following options can be specified. These options can be abbreviated by using **/o** only once -- for example, **/oi /oe** can be written as **/oie**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/oe</strong></p></td>
<td align="left"><p>Output will include individual errors. This option is only useful if <strong>/q</strong> is used, because individual errors are automatically displayed if quiet mode hasn&#39;t been activated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/op</strong></p></td>
<td align="left"><p>Output will list each file that passes. (By default, SymChk only displays files that fail testing.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/oi</strong></p></td>
<td align="left"><p>Output will list each file that was ignored. (By default, SymChk only displays files that fail testing.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/od</strong></p></td>
<td align="left"><p>Output will include full details. Same as <strong>/oe /op /oi</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/ot</strong></p></td>
<td align="left"><p>Output will include result totals. This option is only useful if <strong>/q</strong> is used, because these totals are automatically displayed if quiet mode hasn&#39;t been activated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/ob</strong></p></td>
<td align="left"><p>The full path for binaries will be included in all output messages.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/os</strong></p></td>
<td align="left"><p>The full path for symbols will be included in all output messages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/oc</strong> <em>Dir</em></p></td>
<td align="left"><p>SymChk will create a traditional symbol tree in the directory <em>Dir</em> that contains a list of all the symbol files checked.</p></td>
</tr>
</tbody>
</table>

 

**DBG file options.** These options control how SymChk checks *.dbg* symbol files. Only one of the following options can be specified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/ds</strong></p></td>
<td align="left"><p>SymChk will verify that .dbg information was stripped from the executable and only appears in the .dbg file, and that the executable points to the .dbg file. If the program was built without .dbg symbol files, this option has no effect. This is the default.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/de</strong></p></td>
<td align="left"><p>SymChk will verify that .dbg information was not stripped from the executable and that the executable does not point to a .dbg file. If the program was built without .dbg symbol files, this option has no effect.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/dn</strong></p></td>
<td align="left"><p>SymChk will verify that .dbg information is not present in the image, and that the image does not point to a .dbg file.</p></td>
</tr>
</tbody>
</table>

 

**PDB file options.** These options control how SymChk checks .pdb symbol files. Only one of the following options can be specified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/pf</strong></p></td>
<td align="left"><p>SymChk performs no checking on the contents of the .pdb file -- it just verifies that the files exist and match the binary. This is the default.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/ps</strong></p></td>
<td align="left"><p>SymChk will verify that the .pdb files have been stripped of source line, data type, and global information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/pt</strong></p></td>
<td align="left"><p>SymChk will verify that the .pdb files contain data type information.</p></td>
</tr>
</tbody>
</table>

 

**Filtering options.** These options control how module filtering is performed when SymChk is checking processes or dump files. Only one of the following options can be specified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/fm</strong> <em>Module</em></p></td>
<td align="left"><p>SymChk will only check dump files or processes associated with the specified module. <em>Module</em> must include the full filename, but must not include any part of the directory path.</p></td>
</tr>
</tbody>
</table>

 

**Symbol checking options.** Any number of the following options can be specified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>/cs</strong></p></td>
<td align="left"><p>SymChk won&#39;t verify that CodeView data is present. (By default, the presence of CodeView data is verified.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/cc</strong></p></td>
<td align="left"><p>When SymChk is checking a hotfix CAB file, it will not look for symbols inside the cab. (By default, SymChk will look for symbols in the cab as well as in the provided symbol path.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>/ea</strong> <em>File</em></p></td>
<td align="left"><p>SymChk won&#39;t verify symbols for the programs listed in the specified file. This allows you to veto certain programs that would otherwise be verified. <em>File</em> must specify exactly one file (by relative, absolute, or UNC path, but without wildcards); if it contains spaces it should be enclosed in quotation marks. Within <em>File</em>, each line indicates a program file (by relative, absolute, or UNC paths); no wildcards are permitted. If a line in this file contains spaces it should be enclosed in quotation marks. A semicolon within this file is a comment character -- everything between a semicolon and the end of the line will be ignored. If a symbol server is being used, symbols for these programs will not be copied to the downstream store.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>/ee</strong> <em>File</em></p></td>
<td align="left"><p>Error messages for those programs listed in the specified file are suppressed. &quot;Success&quot; and &quot;ignore&quot; messages will appear as usual, and symbol files will be copied to the downstream store as usual. The format of <em>File</em> and the format of its contents are the same as that for <strong>/ea</strong> <em>File</em>.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about SymChk, see [Using SymChk](using-symchk.md).

 

 





