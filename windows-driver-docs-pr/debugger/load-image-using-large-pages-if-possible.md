---
title: Load image using large pages if possible
description: Load image using large pages if possible
ms.assetid: 7f75b5bd-cc25-4f09-9d60-55b86969d16b
keywords: ["Load image using large pages if possible (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Load image using large pages if possible


## <span id="ddk_load_image_using_large_pages_if_possible_dtools"></span><span id="DDK_LOAD_IMAGE_USING_LARGE_PAGES_IF_POSSIBLE_DTOOLS"></span>


The **Load image using large pages if possible** setting directs the system to use large pages (4 MB) rather than the standard small pages (4 KB) when mapping binaries into the process address space.

This setting is most helpful for large executable files, because it significantly reduces the number of page table entries in physical memory.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>lpg</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>(none)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>Image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This setting is not technically a global flag, because its value is stored in a separate registry entry, not as a value of the GlobalFlag registry entry. As a result, you cannot set it by using a hexadecimal value, and when you select this setting for an image file, it appears in the **Other settings** field of the display.

 

 





