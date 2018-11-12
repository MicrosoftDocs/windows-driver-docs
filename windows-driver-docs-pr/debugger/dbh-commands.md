---
title: DBH Commands
description: DBH Commands
ms.assetid: 124e8be9-1b1a-4498-84a4-5dbb6b5b9026
keywords: ["DBH, commands"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# DBH Commands


From the DBH command line, you can use a variety of commands to analyze symbols and symbol files.

The following table lists the commands that control the DBH options and perform other basic tasks.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>verbose</strong> [<strong>on</strong>|<strong>off</strong>]</p></td>
<td align="left"><p>Turns verbose mode on or off. With no parameter, displays the current verbose mode setting.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sympath</strong> [<em>Path</em>]</p></td>
<td align="left"><p>Sets the symbol search path. With no parameter, displays the current symbol search path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>symopt</strong> <em>Options</em></p>
<p><strong>symopt +</strong><em>Options</em></p>
<p><strong>symopt -</strong><em>Options</em></p>
<p><strong>symopt</strong></p></td>
<td align="left"><p>Sets the symbol options. With no <strong>+</strong> or <strong>-</strong>, the value of <em>Options</em> replaces the current symbol options. If <strong>+</strong> or <strong>-</strong> is used, <em>Options</em> specifies the options to be added or removed; there must be a space before the <strong>+</strong> or <strong>-</strong> but no space after it. With no parameter, the current symbol options are displayed. When DBH is launched, the default value of all the symbol options is 0x10C13. For a list of available options, see <a href="symbol-options.md" data-raw-source="[Setting Symbol Options](symbol-options.md)">Setting Symbol Options</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>help</strong></p></td>
<td align="left"><p>Displays help text for the DBH commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>quit</strong></p></td>
<td align="left"><p>Quits the DBH program.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the commands that load, unload, and rebase the target module. These commands cannot be used if DBH was started by specifying a process ID on the command line.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>load</strong> <em>File</em></p></td>
<td align="left"><p>Loads the specified module. <em>File</em> should specify the path, file name, and file name extension of either the executable file or the symbol file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>unload</strong></p></td>
<td align="left"><p>Unloads the current module.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>base</strong> <em>Address</em></p></td>
<td align="left"><p>Sets the default base address to the specified value. All symbol addresses will be determined relative to this base address.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the commands that search for files and display directory information.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>findexe</strong> <em>File Path</em></p></td>
<td align="left"><p>Locates the specified executable file in the specified path, using the <strong>FindExecutableImage</strong> routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>finddbg</strong> <em>File Path</em></p></td>
<td align="left"><p>Locates the specified .dbg file in the specified path. Including the .dbg extension is optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dir</strong> <em>File Path</em></p></td>
<td align="left"><p>Locates the specified file in the specified path or in any subdirectory under this path, using the <strong>EnumDirTree</strong> routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>srchtree</strong> <em>Path File</em></p></td>
<td align="left"><p>Locates the specified file in the specified path or in any subdirectory under this path, using the <strong>SearchTreeForFile</strong> routine. This command is the same as <strong>dir</strong>, except that the parameters are reversed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ffpath</strong> <em>File</em></p></td>
<td align="left"><p>Finds the specified file in the current symbol path.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the commands that parse the module list and control the default module. The default module and its base address are displayed on the DBH prompt.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>mod</strong> <em>Address</em></p></td>
<td align="left"><p>Changes the default module to the module with the specified base address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>refresh</strong></p></td>
<td align="left"><p>Refreshes the module list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>omap</strong></p></td>
<td align="left"><p>Displays the module OMAP structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>epmod</strong> <em>PID</em></p></td>
<td align="left"><p>Enumerates all the modules loaded for the specified process. <em>PID</em> specifies the process ID of the desired process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>info</strong></p></td>
<td align="left"><p>Displays information about the currently loaded module.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>obj</strong> <em>Mask</em></p></td>
<td align="left"><p>Lists all object files associated with the default module that match the specified pattern. <em>Mask</em> may contain a variety of wildcard characters and specifiers; see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a> for details.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>src</strong> <em>Mask</em></p></td>
<td align="left"><p>Lists all source files associated with the default module that match the specified pattern. <em>Mask</em> may contain a variety of wildcard characters and specifiers; see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a> for details.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>enummod</strong></p></td>
<td align="left"><p>Enumerates all loaded modules. There is always at least one module, unless DBH is running without a target, in which case there are none.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the commands that display and search for symbols.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>enum</strong> <em>Module</em><strong>!</strong><em>Symbol</em></p></td>
<td align="left"><p>Enumerates all symbols matching the specified module and symbol. <em>Module</em> specifies the module to search (without the file name extension). <em>Symbol</em> specifies a pattern that the symbol must contain. Both <em>Module</em> and <em>Symbol</em> may contain a variety of wildcard characters and specifiers; see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a> for details.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>enumaddr</strong> <em>Address</em></p></td>
<td align="left"><p>Enumerates all symbols associated with the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>addr</strong> <em>Address</em></p></td>
<td align="left"><p>Displays detailed information about the symbols associated with the specified address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>name</strong> [<em>Module</em><strong>!</strong>]<em>Symbol</em></p></td>
<td align="left"><p>Displays detailed information about the specified symbol. An optional <em>Module</em> specifier may be included. Wildcards should not be used, because if multiple symbols match the pattern, <strong>name</strong> only displays the first of them.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>next</strong> [<em>Module</em><strong>!</strong>]<em>Symbol</em></p>
<p><strong>next</strong> <em>Address</em></p></td>
<td align="left"><p>Displays detailed information about the next symbol after the specified symbol or address. If a symbol is specified by name, an optional <em>Module</em> specifier may be included, but wildcards should not be used.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>prev</strong> [<em>Module</em><strong>!</strong>]<em>Symbol</em></p>
<p><strong>prev</strong> <em>Address</em></p></td>
<td align="left"><p>Displays detailed information about the first symbol previous to the specified symbol or address. If a symbol is specified by name, an optional <em>Module</em> specifier may be included, but wildcards should not be used.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>line</strong> <em>File</em><strong>#</strong><em>LineNum</em></p></td>
<td align="left"><p>Displays the hexadecimal address of the binary instruction associated with the specified source line, and any symbols associated with this line. Also sets the current line number equal to the specified line number. <em>File</em> specifies the name of the source file, and <em>LineNum</em> specifies the line number within that file; these should be separated with a number sign ( <strong>#</strong> ).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>srclines</strong> <em>File LineNum</em></p></td>
<td align="left"><p>Displays the object files associated with the specified source line, and the hexadecimal address of the binary instruction associated with this line. Does not change the current line number. <em>File</em> specifies the name of the source file, and <em>LineNum</em> specifies the line number within that file; these should be separated with a space.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>laddr</strong> <em>Address</em></p></td>
<td align="left"><p>Displays the source file and line number corresponding to the symbol located at the specified address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>linenext</strong></p></td>
<td align="left"><p>Increments the current line number, and displays information about the new line number.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lineprev</strong></p></td>
<td align="left"><p>Decrements the current line number, and displays information about the new line number.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>locals</strong> <em>Function</em> [<em>Mask</em>]</p></td>
<td align="left"><p>Displays all local variables contained within the specified function. If <em>Mask</em> is included, only those locals matching the specified pattern are displayed; see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a> for details.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>type</strong> <em>TypeName</em></p></td>
<td align="left"><p>Displays detailed information about the specified data type. <em>TypeName</em> specifies the name of the data type (for example, WSTRING). If no type name matches this value, any matching symbol will be displayed. Unlike most DBH command parameters, <em>TypeName</em> is case-sensitive.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>elines</strong> [<em>Source</em> [<em>Obj</em>]]</p></td>
<td align="left"><p>Enumerates all source lines matching the specified source mask and object mask. <em>Source</em> specifies the name of the source file, including the absolute path and file name extension. <em>Obj</em> specifies the name of the object file, including the relative path and file name extension. Both <em>Source</em> and <em>Obj</em> may contain a variety of wildcard characters and specifiers; see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a> for details. If a parameter is omitted this is equivalent to using the asterisk (<strong><em></strong>) wildcard. If you do not wish to specify path information, prefix the file name with <strong></em>&lt;/strong&gt; to indicate a wildcard path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>index</strong> <em>Value</em></p></td>
<td align="left"><p>Displays detailed information about the symbol with the specified index value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>scope</strong> <em>Address</em></p>
<p><strong>scope</strong> [<em>Module</em><strong>!</strong>]<em>Symbol</em></p></td>
<td align="left"><p>Displays detailed information about the parent of the specified symbol. The symbol may be specified by address or by name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>srch</strong> [<strong>mask=</strong><em>Symbol</em>] [<strong>index=</strong><em>Index</em>] [<strong>tag=</strong><em>Tag</em>] [<strong>addr=</strong><em>Address</em>] [<strong>globals</strong>]</p></td>
<td align="left"><p>Searches for all symbols that match the specified masks. <em>Symbol</em> specifies the symbol name. It should not include the module name, but it may contain wildcard characters and specifiers; see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a> for details. <em>Index</em> specifies the hexadecimal address of a symbol to be used as the parent for the search. <em>Tag</em> specifies the hexadecimal symbol type classifier (<strong>SymTag</strong><em>Xxx</em>) value that must match the symbol. <em>Address</em> specifies the address of the symbol. If <strong>globals</strong> is included, only global symbols will be displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>uw</strong> <em>Address</em></p></td>
<td align="left"><p>Displays the unwind information for the function at the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dtag</strong></p></td>
<td align="left"><p>Displays all the symbol type classifier (<strong>SymTag</strong><em>Xxx</em>) values.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>etypes</strong></p></td>
<td align="left"><p>Enumerates all data types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dump</strong></p></td>
<td align="left"><p>Displays a complete list of all symbol information in the target file.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the commands that relate to symbol servers and symbol stores.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>home</strong> [<em>Path</em>]</p></td>
<td align="left"><p>Sets the home directory used by SymSrv and SrcSrv for the default downstream store. If the symbol path contains a reference to a symbol server that uses a default downstream store, then the <strong>sym</strong> subdirectory of the home directory will be used for the downstream store. With no parameter, <strong>home</strong> displays the current home directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>srvpath</strong> <em>Path</em></p></td>
<td align="left"><p>Tests whether the specified path is the path of a symbol store.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>srvind</strong> <em>File</em></p></td>
<td align="left"><p>Finds the symbol server index that corresponds to the specified file. The symbol server index is a unique value based on the contents of the file, regardless of whether it actually has been added to any symbol store. <em>File</em> should specify the file name and absolute path of the desired file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>fii</strong> <em>File</em></p></td>
<td align="left"><p>Displays the symbol server indexes for the specified binary file and its associated files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>getfile</strong> <em>File Index</em></p></td>
<td align="left"><p>Displays the file with the specified name and symbol server index. <em>File</em> specifies the name of the desired file; this should not include its path. <em>Index</em> specifies the symbol server index of the desired file. DBH uses the <strong>SymFindFileInPath</strong> routine to search the tree under the current symbol path for a file with this name and this index.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sup</strong> <em>Path File1 File2</em></p></td>
<td align="left"><p>Stores a file in a symbol store, based on the values of the parameters. <em>Path</em> specifies the directory path of the symbol store. <em>File1</em> and <em>File2</em> are used to create a delta value, which is in turn used to determine the file being stored.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>storeadd</strong> <em>File Store</em></p></td>
<td align="left"><p>Adds the specified file to the specified symbol store. <em>Store</em> should be the root path of the symbol store.</p></td>
</tr>
</tbody>
</table>

 

The following table lists the DBH commands that apply to real and imaginary symbols.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>undec</strong> <em>Name</em></p></td>
<td align="left"><p>Reveals the meaning of the decorations attached to the specified symbol name. <em>Name</em> can be any string; it need not correspond to a currently loaded symbol. If <em>Name</em> contains C++ decorations, the meaning of these decorations is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>add</strong> <em>Name Address Size</em></p></td>
<td align="left"><p>Adds the specified imaginary symbol to the list of symbols loaded in DBH. <em>Name</em> specifies the name of the symbol to be added, <em>Address</em> specifies its hexadecimal address, and <em>Size</em> its hexadecimal size in bytes. This is treated like any other symbol in later DBH commands, until the DBH session is ended with <strong>quit</strong> or <strong>unload</strong>, or until the imaginary symbol is deleted with <strong>del</strong>. The actual target symbol file is not altered.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>del</strong> <em>Name</em></p>
<p><strong>del</strong> <em>Address</em></p></td>
<td align="left"><p>Deletes an imaginary symbol previously added with the <strong>add</strong> command. The symbol can be specified either by name or by address. This cannot be used to delete real symbols.</p></td>
</tr>
</tbody>
</table>

 

 

 





