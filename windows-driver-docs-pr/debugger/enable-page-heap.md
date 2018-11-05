---
title: Enable page heap
description: Enable page heap
ms.assetid: b889b7b7-721c-4ecf-bf59-c1ccc0bc735d
keywords: ["Enable page heap (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable page heap


## <span id="ddk_enable_page_heap_dtools"></span><span id="DDK_ENABLE_PAGE_HEAP_DTOOLS"></span>


The **Enable page heap** flag turns on page heap verification, which monitors dynamic heap memory operations, including allocate and free operations, and causes a debugger break when the verifier detects a heap error.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>hpa</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x02000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_PAGE_ALLOCS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This option enables full page heap verification when set for image files and standard page heap verification when set in the system registry or as a kernel flag.

-   *Full page heap verification* (for **/i**) places a zone of reserved virtual memory at the end of each allocation.

-   *Standard page heap verification* (for **/r** or **/k**) places random patterns at the end of an allocation and examines the patterns when a heap block is freed.

Setting this flag for an image file is the same as typing **gflags /p /enable** *ImageFile* **/full** for the image file at the command line.

 

 





