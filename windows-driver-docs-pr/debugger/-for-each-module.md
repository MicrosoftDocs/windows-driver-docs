---
title: for_each_module
description: The for_each_module extension executes a debugger command one time for each loaded module.
ms.assetid: 607947d8-be06-4012-8901-13bf27e382b1
keywords: ["for_each_module Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- for_each_module
api_type:
- NA
ms.localizationpriority: medium
---

# !for\_each\_module


The **!for\_each\_module** extension executes a debugger command one time for each loaded module.

```dbgcmd
!for_each_module ["CommandString"]
!for_each_module -?
```

## <span id="ddk__for_each_module_dbg"></span><span id="DDK__FOR_EACH_MODULE_DBG"></span>Parameters


<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to execute one time for each module in the debugger's module list. If *CommandString* includes multiple commands, you must separate them with semicolons and enclose *CommandString* in quotation marks. If you include multiple commands, the individual commands within *CommandString* cannot contain quotation marks.

You can use the following aliases in *CommandString* or in any script that the commands in *CommandString* executes.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Alias</th>
<th align="left">Data type</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>@#FileVersion</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The file version of the module.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#ProductVersion</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The product version of the module.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#ModuleIndex</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The module number. Modules are enumerated consecutively, starting with zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#ModuleName</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The module name. This name is typically the file name without the file name extension. In some situations, the module name differs significantly from the file name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#ImageName</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The name of the executable file, including the file name extension. Typically, the full path is included in user mode but not in kernel mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#LoadedImageName</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Unless Microsoft CodeView symbols are present, this alias is the same as the image name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#MappedImageName</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>In most situations, this alias is <strong>NULL</strong>. If the debugger is mapping an image file (for example, during minidump debugging), this alias is the name of the mapped image.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#SymbolFileName</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The path and name of the symbol file. If you have not loaded any symbols, this alias is the name of the executable file instead.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#ModuleNameSize</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The string length of the module name string, plus one.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#ImageNameSize</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The string length of the image name string, plus one.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#LoadedImageNameSize</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The string length of the loaded image name string, plus one.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#MappedImageNameSize</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The string length of the mapped image name string, plus one.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#SymbolFileNameSize</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The string length of the symbol file name string, plus one.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#Base</p></td>
<td align="left"><p>ULONG64</p></td>
<td align="left"><p>The address of the start of the image.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#Size</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The size of the image, in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#End</p></td>
<td align="left"><p>ULONG64</p></td>
<td align="left"><p>The address of the end of the image.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#TimeDateStamp</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The time and date stamp of the image. If you want to expand this time and date stamp into a readable date, use the <strong><a href="-formats--show-number-formats-.md" data-raw-source="[.formats (Show Number Formats)](-formats--show-number-formats-.md)">.formats (Show Number Formats)</a></strong> command.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>@#Checksum</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The checksum of the module.</p></td>
</tr>
<tr class="even">
<td align="left"><p>@#Flags</p></td>
<td align="left"><p>ULONG</p></td>
<td align="left"><p>The module flags. For a list of the DEBUG_MODULE_<em>Xxx</em> values, see Dbgeng.h.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>@#SymbolType</p></td>
<td align="left"><p>USHORT</p></td>
<td align="left"><p>The symbol type. For a list of the DEBUG_SYMTYPE_<em>Xxx</em> values, see Dbgeng.h.</p></td>
</tr>
</tbody>
</table>

 

These aliases are all replaced before *CommandString* is executed for each module and before any other parsing occurs. These aliases are case sensitive. You must add a space before the alias and a space after it, even if the alias is enclosed in parentheses. If you use C++ expression syntax, you must reference these aliases as @@( @\#*alias*).

These aliases are available only during the lifetime of the call to **!for\_each\_module**. Do not confuse them with pseudo-registers, fixed-name aliases, or user-named aliases.

<span id="_______-_______"></span> -?   
Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to define and use aliases as shortcuts for entering character strings (including use of the ${ } token), see [Using Aliases](using-aliases.md).

Remarks
-------

If you do not specify any arguments, the **!for\_each\_module** extension displays general information about the loaded modules. This information is similar to the information that the following command shows.

```dbgcmd
!for_each_module .echo @#ModuleIndex : @#Base @#End @#ModuleName @#ImageName  @#LoadedImageName
```

For more information about loaded and unloaded modules, use the [**lm (List Loaded Modules)**](lm--list-loaded-modules-.md) command.

If you enable verbose debugger output, the debugger displays the total number of loaded and unloaded modules when the extension is called, and the debugger displays detailed information about each module (including the values of each available alias) before *CommandString* is executed for that module.

The following examples show how to use the **!for\_each\_module** extension. The following commands display the global debug flags.

```dbgcmd
!for_each_module x ${@#ModuleName}!*Debug*Flag*
!for_each_module x ${@#ModuleName}!g*Debug*
```

The following command checks for binary corruption in every loaded module, by using the [**!chkimg**](-chkimg.md) extension:

```dbgcmd
!for_each_module !chkimg @#ModuleName
```

The following command searches for the pattern "MZ" in every loaded image.

```dbgcmd
!for_each_module s-a @#Base @#End "MZ"
```

The following example demonstrates the use of @\#FileVersion and @\#ProductVersion for each module name:

```dbgcmd
0:000> !for_each_module .echo @#ModuleName fver = @#FileVersion pver = @#ProductVersion 
USER32 fver = 6.0.6000.16438 (vista_gdr.070214-1610) pver = 6.0.6000.16438
kernel32 fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
ntdll fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
notepad fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
WINSPOOL fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
COMCTL32 fver = 6.10 (vista_rtm.061101-2205) pver = 6.0.6000.16386
SHLWAPI fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
msvcrt fver = 7.0.6000.16386 (vista_rtm.061101-2205) pver = 7.0.6000.16386
GDI32 fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
RPCRT4 fver = 6.0.6000.16525 (vista_gdr.070716-1600) pver = 6.0.6000.16525
SHELL32 fver = 6.0.6000.16513 (vista_gdr.070626-1505) pver = 6.0.6000.16513
ole32 fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
ADVAPI32 fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
COMDLG32 fver = 6.0.6000.16386 (vista_rtm.061101-2205) pver = 6.0.6000.16386
```

 

 





