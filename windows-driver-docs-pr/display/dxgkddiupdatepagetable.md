---
title: DXGKDDI\_UPDATEPAGETABLE callback function
description: The DxgkDdiUpdatePageTable function is reserved for system use. Do not implement it in your driver.
ms.assetid: 08328e82-d1cc-4c50-bc96-7382232676ab
keywords: ["DxgkDdiUpdatePageTable callback function Display Devices", "DXGKDDI_UPDATEPAGETABLE"]
topic_type:
- apiref
api_name:
- DxgkDdiUpdatePageTable
api_location:
- Dispmprt.h
api_type:
- UserDefined
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXGKDDI\_UPDATEPAGETABLE callback function


\[Reserved for system use.\]

The *DxgkDdiUpdatePageTable* function is reserved for system use. Do not implement it in your driver.

Syntax
------

```ManagedCPlusPlus
DXGKDDI_UPDATEPAGETABLE DxgkDdiUpdatePageTable;

NTSTATUS DxgkDdiUpdatePageTable(
   IN_CONST_HANDLE                hDevice,
   INOUT_PDXGKARG_UPDATEPAGETABLE pUpdatePageTable
)
{ ... }
```

Parameters
----------

*hDevice*
This parameter is reserved for system use.

*pUpdatePageTable*
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
<td align="left">Dispmprt.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXGKDDI_UPDATEPAGETABLE%20callback%20function%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




