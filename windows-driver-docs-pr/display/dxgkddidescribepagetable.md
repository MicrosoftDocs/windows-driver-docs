---
title: DXGKDDI\_DESCRIBEPAGETABLE callback function
description: The DxgkDdiDescribePageTable function is reserved for system use. Do not implement it in your driver.
ms.assetid: af9c9515-0225-4a97-bb8e-8ff9b57ac1a9
keywords: ["DxgkDdiDescribePageTable callback function Display Devices", "DXGKDDI_DESCRIBEPAGETABLE"]
topic_type:
- apiref
api_name:
- DxgkDdiDescribePageTable
api_location:
- Dispmprt.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGKDDI\_DESCRIBEPAGETABLE callback function


\[Reserved for system use.\]

The *DxgkDdiDescribePageTable* function is reserved for system use. Do not implement it in your driver.

Syntax
------

```ManagedCPlusPlus
DXGKDDI_DESCRIBEPAGETABLE DxgkDdiDescribePageTable;

NTSTATUS DxgkDdiDescribePageTable(
   IN_CONST_HANDLE                  hDevice,
   INOUT_PDXGKARG_DESCRIBEPAGETABLE pDescribePageTable
)
{ ... }
```

Parameters
----------

*hDevice*
This parameter is reserved for system use.

*pDescribePageTable*
This parameter is reserved for system use.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Dispmprt.h (include Dispmprt.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





