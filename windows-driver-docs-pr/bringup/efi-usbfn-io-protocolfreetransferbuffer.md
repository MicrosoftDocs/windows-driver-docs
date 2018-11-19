---
title: EFI_USBFN_IO_PROTOCOL.FreeTransferBuffer
description: EFI_USBFN_IO_PROTOCOL.FreeTransferBuffer
ms.assetid: 236b925f-2c7b-4df8-b5c8-e8c2f7b853d2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.FreeTransferBuffer


The **FreeTransferBuffer** function de-allocates the memory allocated for the transfer buffer by the [EFI\_USBFN\_IO\_PROTOCOL.AllocateTransferBuffer](efi-usbfn-io-protocolallocatetransferbuffer.md) function.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_FREE_TRANSFER_BUFFER) (
  IN EFI_USBFN_IO_PROTOCOL    *This,
  IN VOID                     *Buffer
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance

<a href="" id="buffer"></a>*Buffer*  
Pointer to the transfer buffer to de-allocate.

## Return values


This function returns the following values:

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
<td><p>The function returned successfully</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_INVALID_PARAMETER</strong></p></td>
<td><p>A parameter is invalid</p></td>
</tr>
</tbody>
</table>

 

## Remarks


## Requirements


**Header:** User generated

 

 




