---
title: .writemem (Write Memory to File)
description: The .writemem command writes a section of memory to a file.
ms.assetid: 928e9452-d9b4-49fa-a5fa-cdc3832d7349
keywords: [".writemem (Write Memory to File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .writemem (Write Memory to File)
api_type:
- NA
ms.localizationpriority: medium
---

# .writemem (Write Memory to File)


The **.writemem** command writes a section of memory to a file.

```dbgcmd
.writemem FileName Range 
```

## <span id="ddk_meta_write_memory_to_file_dbg"></span><span id="DDK_META_WRITE_MEMORY_TO_FILE_DBG"></span>Parameters


<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the file to be created. You can specify a full path and file name, or just the file name. If the file name contains spaces, *FileName* should be enclosed in quotation marks. If no path is specified, the current directory is used.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range to be written to the file. For syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The memory is copied literally to the file. It is not parsed in any way.

The **.writemem** command is the opposite of the [**.readmem (Read Memory from File)**](-readmem--read-memory-from-file-.md) command.

 

 





