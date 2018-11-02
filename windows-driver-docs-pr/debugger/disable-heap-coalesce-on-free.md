---
title: Disable heap coalesce on free
description: Disable heap coalesce on free
ms.assetid: 64a68fa2-9270-4b2d-9edc-d54370191dcb
keywords: ["Disable heap coalesce on free (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Disable heap coalesce on free


## <span id="ddk_disable_heap_coalesce_on_free_dtools"></span><span id="DDK_DISABLE_HEAP_COALESCE_ON_FREE_DTOOLS"></span>


The **Disable heap coalesce on free** flag leaves adjacent blocks of heap memory separate when they are freed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>dhc</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x00200000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_DISABLE_COALESCING</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

By default, Windows combines ("coalesces") newly-freed adjacent blocks into a single block. Combining the blocks takes time, but reduces fragmentation that might force the heap to allocate additional memory when it cannot find contiguous memory.

This flag is used for maintaining compatibility with old applications.

 

 





