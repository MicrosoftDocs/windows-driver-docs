---
title: .dumpcab (Create Dump File CAB)
description: The .dumpcab command creates a CAB file containing the current dump file.
ms.assetid: 65ed766f-b049-47b0-90d7-e21d510a35ba
keywords: [".dumpcab (Create Dump File CAB) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .dumpcab (Create Dump File CAB)
api_type:
- NA
ms.localizationpriority: medium
---

# .dumpcab (Create Dump File CAB)


The **.dumpcab** command creates a CAB file containing the current dump file.

```dbgcmd
.dumpcab [-a] CabName 
```

## <span id="ddk_meta_create_dump_file_cab_dbg"></span><span id="DDK_META_CREATE_DUMP_FILE_CAB_DBG"></span>Parameters


<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
Causes all currently loaded symbols to be included in the CAB file. For minidumps, all loaded images will be included as well. Use [**lml**](lm--list-loaded-modules-.md) to determine which symbols and images are loaded.

<span id="_______CabName______"></span><span id="_______cabname______"></span><span id="_______CABNAME______"></span> *CabName*   
The CAB file name, including extension. *CabName* can include an absolute or relative path; relative paths are relative to the directory in which the debugger was started. It is recommended that you choose the extension .cab.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more details on crash dumps, see [Crash Dump Files](crash-dump-files.md).

Remarks
-------

This command can only be used if you are already debugging a dump file.

If you are debugging a live target and want to create a dump file and place it in a CAB, you should use the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command. Next, start a new debugging session with the dump file as its target, and use **.dumpcab**.

The **.dumpcab** command cannot be used to place multiple dump files into one CAB file.

 

 





