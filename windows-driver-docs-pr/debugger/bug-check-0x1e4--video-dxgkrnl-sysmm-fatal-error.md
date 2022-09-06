---
title: Bug Check 0x1E4 VIDEO_DXGKRNL_SYSMM_FATAL_ERROR
description: The VIDEO_DXGKRNL_SYSMM_FATAL_ERROR bug check has a value of 0x000001E4 that indicates that the Microsoft DirectX graphics kernel system memory manager has detected a violation.
keywords: ["Bug Check 0x1E4 VIDEO_DXGKRNL_SYSMM_FATAL_ERROR", "VIDEO_DXGKRNL_SYSMM_FATAL_ERROR"]
ms.date: 08/02/2022
topic_type:
- apiref
api_name:
- VIDEO_DXGKRNL_SYSMM_FATAL_ERROR
api_type:
- NA
---

# Bug Check 0x1E4: VIDEO\_DXGKRNL\_SYSMM\_FATAL\_ERROR

The VIDEO\_DXGKRNL\_SYSMM\_FATAL\_ERROR bug check has a value of 0x000001E4. This indicates that the Microsoft DirectX graphics kernel system memory manager has detected a violation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left">The subcode of the BugCheck</p>
<p>0x1 : Invalid physical object type</p>
<p>0x2 : IOMMU enabled with invalid reason</p>
<p>0x3 : IOMMU disabled with invalid reason</p>
<p>0x4 : ADL is being built against non-locked memory</p>
<p>0x5 : Memory is being unlocked while ADLs exist</p>
<p>0x6 : Adapter objects were leaked</p>
<p>0x7 : ADL leaked</p>
<p>0x8 : Logical Block Pool leaked</p>
<p>0x9 : Logical Block Pool Allocator leaked</p>
<p>0xA : Failed Domain Reattach</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Reserved</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>


> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


 

 




