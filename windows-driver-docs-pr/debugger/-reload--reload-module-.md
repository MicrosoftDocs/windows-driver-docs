---
title: .reload (Reload Module)
description: The .reload command deletes all symbol information for the specified module and reloads these symbols as needed. In some cases, this command also reloads or unloads the module itself.
ms.assetid: 750eb1a2-7af9-4f2d-81ca-9ea0fb157961
keywords: ["Reload Module (.reload) command", "symbols, Reload Module (.reload) command", ".reload (Reload Module) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .reload (Reload Module)
api_type:
- NA
ms.localizationpriority: medium
---

# .reload (Reload Module)


The **.reload** command deletes all symbol information for the specified module and reloads these symbols as needed. In some cases, this command also reloads or unloads the module itself.

```dbgcmd
.reload [Options] [Module[=Address[,Size[,Timestamp]]]] 
.reload -?
```

## <span id="ddk_meta_reload_module_dbg"></span><span id="DDK_META_RELOAD_MODULE_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any of the following options:

<span id="_d"></span><span id="_D"></span>**/d**  
Reload all modules in the debugger's module list. (When you omit all parameters, this situation is the default during user-mode debugging.)

<span id="_f"></span><span id="_F"></span>**/f**  
Forces the debugger to immediately load the symbols. This parameter overrides *lazy symbol loading*. For more information, see the following Remarks section.

<span id="_i"></span><span id="_I"></span>**/i**  
Ignores a mismatch in the .pdb file versions. (If you do not include this parameter, the debugger does not load mismatched symbol files.) When you use **/i**, **/f** is used also, even if you do not explicitly specify it.

<span id="_l"></span><span id="_L"></span>**/l**  
Lists the modules but does not reload their symbols. (In kernel mode, this parameter gives the same output as the [**!drivers**](-drivers.md) extension.)

<span id="_n"></span><span id="_N"></span>**/n**  
Reloads kernel symbols only. This parameter does not reload any user symbols. (You can use this option only during kernel-mode debugging.)

<span id="_o"></span><span id="_O"></span>**/o**  
Forces the cached files in a symbol server's downstream store to be overwritten. When you use this flag, you should also include **/f**. By default, the downstream store files are never overwritten.

Because the symbol server uses distinct file names for the symbols of every different build of a binary, you do not have to use this option unless you believe your downstream store has become corrupted.

<span id="_s"></span><span id="_S"></span>**/s**  
Reloads all modules in the system's module image list. (When you omit all parameters, this situation is the default during kernel-mode debugging.)

If you are loading an individual system module by name while you perform user-mode debugging, you must include **/s**.

<span id="_u"></span><span id="_U"></span>**/u**  
Unloads the specified module and all its symbols. The debugger unloads any loaded module whose name matches *Module*, regardless of the full path. Image names are also searched. For more information, see the note in the following Remarks section.

<span id="_unl"></span><span id="_UNL"></span>**/unl**  
Reloads symbols based on the image information in the unloaded module list.

<span id="_user"></span><span id="_USER"></span>**/user**  
Reloads user symbols only. (You can use this option only during kernel-mode debugging.)

<span id="_v"></span><span id="_V"></span>**/v**  
Turns on verbose mode.

<span id="_w"></span><span id="_W"></span>**/w**  
Treats *Module* as a literal string. This treatment prevents the debugger from expanding wildcard characters.

<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the name of an image on the target system for which to reload symbols on the host computer. *Module* should include the name and file name extension of the file. Unless you use the **/w** option, *Module* might contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md). If you omit *Module*, the behavior of the **.reload** command depends on which *Options* you use.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the base address of the module. Typically, you have to have this address only if the image header has been corrupted or is paged out.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Specifies the size of the module image. In many situations, the debugger knows the correct size of the module. When the debugger does not know the correct size, you should specify *Size*. This size can be the actual module size or a larger number, but the size should not be a smaller number. Typically, you have to have this size only if the image header has been corrupted or is paged out.

<span id="_______Timestamp______"></span><span id="_______timestamp______"></span><span id="_______TIMESTAMP______"></span> *Timestamp*   
Specifies the timestamp of the module image. In many situations, the debugger knows the correct timestamp of the module. When the debugger does not know the timestamps, you should specify *Timestamp*. Typically, you have to have this timestamp only if the image header has been corrupted or is paged out.

**Note**   There must be no blank space between the *Address*, *Size*, and *Timestamp* parameters.

 

<span id="_______-_______"></span> **-?**   
Displays a short help text for this command.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about deferred (lazy) symbol loading, see [Deferred Symbol Loading](deferred-symbol-loading.md). For more information about other symbol options, see [Setting Symbol Options](symbol-options.md).

Remarks
-------

The **.reload** command does not cause symbol information to be read. Instead, this command lets the debugger know that the symbol files might have changed or that a new module should be added to the module list. This command causes the debugger to revise its module list and delete its symbol information for the specified modules. The actual symbol information is not read from the individual .pdb files until the information is needed. (This kind of loading is known as *lazy symbol loading* or *deferred symbol loading*.)

You can force symbol loading to occur by using the **/f** option or by issuing an [**ld (Load Symbols)**](ld--load-symbols-.md) command.

The **.reload** command is useful if the system stops responding (that is, crashes), which might cause you to lose symbols for the target computer that is being debugged. The command can also be useful if you have updated the symbol tree.

If the image header is incorrect for some reason, such as the module being unloaded, or is paged out, you can load symbols correctly by using the **/unl** argument, or specifying both *Address* and *Size*.

The **.reload /u** command performs a broad search. The debugger first tries to match *Module* with an exact module name, regardless of path. If the debugger cannot find this match, *Module* is treated as the name of the loaded image. For example, if the HAL that resides in memory has the module name of halacpi.dll, both of the following commands unload its symbols.

```dbgcmd
kd> .reload /u halacpi.dll

kd> .reload /u hal
```

If you are performing user-mode debugging and want to load a module that is not part of the target application's module list, you must include the **/s** option, as the following example shows.

```dbgcmd
0:000> .reload /u ntdll.dll
Unloaded ntdll.dll

0:000> .reload /s /f ntdll.dll
```

 

 





