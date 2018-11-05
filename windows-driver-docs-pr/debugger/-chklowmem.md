---
title: chklowmem
description: The chklowmem extension determines whether physical memory pages below 4 GB are filled with the required fill pattern on a computer that was booted with the /pae and /nolowmem options.
ms.assetid: cc1054e2-b824-4fcf-b353-9ee8c0d3dbf3
keywords: ["PAE (physical address extension)", "chklowmem Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- chklowmem
api_type:
- NA
ms.localizationpriority: medium
---

# !chklowmem


The **!chklowmem** extension determines whether physical memory pages below 4 GB are filled with the required fill pattern on a computer that was booted with the [**/pae**](https://msdn.microsoft.com/library/windows/hardware/ff557168) and [**/nolowmem**](https://msdn.microsoft.com/library/windows/hardware/ff557144) options.

```dbgsyntax
!chklowmem
```

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This extension is useful when you are verifying that kernel-mode drivers operate properly with physical memory above the 4 GB boundary. Typically, drivers fail by truncating a physical address to 32 bits and then in writing below the 4 GB boundary. The **!chklowmem** extension will detect any writes below the 4 GB boundary.

 

 





