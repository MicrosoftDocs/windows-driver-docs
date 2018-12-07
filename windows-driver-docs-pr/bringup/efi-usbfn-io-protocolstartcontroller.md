---
title: EFI_USBFN_IO_PROTOCOL.StartController
description: EFI_USBFN_IO_PROTOCOL.StartController
ms.assetid: 431406c3-6b96-4815-a8a0-01100e8a5a5f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.StartController


The **StartController** function supplies power to the USB controller if needed and initializes hardware and internal data structures. The port must not be activated by this function.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_START_CONTROLLER) (
  IN EFI_USBFN_IO_PROTOCOL        *This
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

## Return values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>EFI_SUCCESS</strong></p></td>
<td><p>The function returned successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_INVALID_PARAMETER</strong></p></td>
<td><p>A parameter is invalid.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_DEVICE_ERROR</strong></p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


This function is available starting in revision 0x00010001 of the **EFI\_USBFN\_IO\_PROTOCOL**.

## Requirements


**Header:** User generated

 

 




