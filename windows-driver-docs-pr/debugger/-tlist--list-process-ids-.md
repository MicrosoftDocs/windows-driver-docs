---
title: .tlist (List Process IDs)
description: The .tlist command lists all processes running on the system.
ms.assetid: 44d46b74-5cf1-4384-b468-baec5a87eaed
keywords: ["List Process IDs (.tlist) command", "process, List Process IDs (.tlist) command", ".tlist (List Process IDs) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .tlist (List Process IDs)
api_type:
- NA
ms.localizationpriority: medium
---

# .tlist (List Process IDs)


The **.tlist** command lists all processes running on the system.

```dbgcmd
.tlist [Options][FileNamePattern]
```

## <span id="ddk_meta_list_process_ids_dbg"></span><span id="DDK_META_LIST_PROCESS_IDS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any number of the following options:

<span id="-v"></span><span id="-V"></span>**-v**  
Causes the display to be verbose. This includes the session number, the process user name, and the command-line used to start the process.

<span id="-c"></span><span id="-C"></span>**-c**  
Limits the display to just the current process.

<span id="_______FileNamePattern______"></span><span id="_______filenamepattern______"></span><span id="_______FILENAMEPATTERN______"></span> *FileNamePattern*   
Specifies the file name to be displayed, or a pattern that the file name of the process must match. Only those processes whose file names match this pattern will be displayed. *FileNamePattern* may contain a variety of wildcards and specifiers; see [String Wildcard Syntax](string-wildcard-syntax.md) for details. This match is made only against the actual file name, not the path.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For other methods of displaying processes, see [Finding the Process ID](finding-the-process-id.md).

Remarks
-------

Each process ID is displayed with an **0n** prefix, to emphasize that the PID is a decimal number.

 

 





