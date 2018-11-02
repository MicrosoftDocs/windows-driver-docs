---
title: .createdir (Set Created Process Directory)
description: The .createdir command controls the starting directory and handle inheritance for any processes created by the debugger.
ms.assetid: 797f5398-f0b4-48e9-bc5f-eac5a53cad67
keywords: [".createdir (Set Created Process Directory) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .createdir (Set Created Process Directory)
api_type:
- NA
ms.localizationpriority: medium
---

# .createdir (Set Created Process Directory)


The **.createdir** command controls the starting directory and handle inheritance for any processes created by the debugger.

```dbgsyntax
.createdir [-i | -I] [Path] 
```

## <span id="ddk_meta_set_created_process_directory_dbg"></span><span id="DDK_META_SET_CREATED_PROCESS_DIRECTORY_DBG"></span>Parameters


<span id="_______-i______"></span><span id="_______-I______"></span> **-i**   
Causes processes created by the debugger to inherit handles from the debugger. This is the default.

<span id="_______-I______"></span><span id="_______-i______"></span> **-I**   
Prevents processes created by the debugger from inheriting handles from the debugger.

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
Specifies the starting directory for all child processes created by any target process. If *Path* contains spaces, it must be enclosed in quotation marks.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If **.createdir** is used with no parameters, the current starting directory and handle inheritance status are displayed.

If **.createdir** has never been used, any created process will use its usual default directory as its starting directory. If you have already set a path with **.createdir** and want to return to the default status, use **.createdir ""** with nothing inside the quotation marks.

The **.createdir** setting affects all processes created by [**.create (Create Process)**](-create--create-process-.md). It also affects processes created by WinDbg's [File | Open Executable](file---open-executable.md) menu command, unless the **Start directory** text box is used to override this setting.

 

 





