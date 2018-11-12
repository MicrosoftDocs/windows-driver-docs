---
title: ate
description: The ate extension displays the alternate page table entry (ATE) for the specified address.
ms.assetid: 8ec98fa5-4939-49cb-8678-e412b9cbe7e3
keywords: ["ate Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- ate
api_type:
- NA
ms.localizationpriority: medium
---

# !ate


The **!ate** extension displays the alternate page table entry (ATE) for the specified address.

```dbgcmd
    !ate Address
```    

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the ATE to display.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about page tables and page directories, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

This extension is only available on Itanium-based computers.

The status flags for the ATE are shown in the following table. The **!ate** display indicates these bits with capital letters or dashes and adds additional information as well.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Display when set</th>
<th align="left">Display when clear</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>V</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Commit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>G</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Not accessed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>E</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Execute.</p></td>
</tr>
<tr class="even">
<td align="left"><p>W</p></td>
<td align="left"><p>R</p></td>
<td align="left"><p>Writeable or read-only.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>L</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Locked. The ATE is locked, therefore, any faults on the page that contain the ATE will be retried until the current fault is satisfied. This can happen on multi-processor systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Z</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Fill zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>N</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>No access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>C</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>Copy on Write.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>I</p></td>
<td align="left"><p>-</p></td>
<td align="left"><p>PTE indirect. This ATE indirectly references another physical page. The page that contains the ATE might have two conflicting ATE attributes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>P</p></td>
<td align="left"></td>
<td align="left"><p>Reserved.</p></td>
</tr>
</tbody>
</table>

 

 

 





