---
title: ".ignore_missing_pages (Suppress Missing Page Errors)"
description: "The .ignore_missing_pages command suppresses the error messages when a Kernel Memory Dump has missing pages."
keywords: ["Suppress Missing Page Errors (.ignore_missing_pages) command", ".ignore_missing_pages (Suppress Missing Page Errors) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .ignore_missing_pages (Suppress Missing Page Errors)
api_type:
- NA
---

# .ignore\_missing\_pages (Suppress Missing Page Errors)


The **.ignore\_missing\_pages** command suppresses the error messages when a Kernel Memory Dump has missing pages.

```dbgcmd
.ignore_missing_pages 0
.ignore_missing_pages 1
.ignore_missing_pages 
```

## <span id="ddk_meta_suppress_missing_page_errors_dbg"></span><span id="DDK_META_SUPPRESS_MISSING_PAGE_ERRORS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Displays all missing page errors while debugging a Kernel Memory Dump. This is the default behavoir of the debugger.

<span id="_______1"></span> **1**  
Suppresses the display of missing page errors while debugging a Kernel Memory Dump.

## Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Dump file debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For more information about how to debug these dump files, see [Kernel Memory Dump](../debugger/kernel-memory-dump.md).

## Remarks

Without parameters, **.ignore\_missing\_pages** displays the current status of this setting.

