---
title: EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer
description: EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer
ms.assetid: dbaa4f18-97b5-4867-9e03-de19b2253722
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.AllocateTransferBuffer


The **AllocateTransferBuffer** function allocates a transfer buffer of the specified size that satisfies controller requirements.

The allocated transfer buffer must be freed using a matching call to the **FreeTransferBuffer** function.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER) (
  IN EFI_USBFN_IO_PROTOCOL    *This,
  IN UINTN                    Size,
  OUT VOID                    **Buffer
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="size"></a>*Size*  
The number of bytes to allocate for the transfer buffer.

<a href="" id="buffer"></a>*Buffer*  
A pointer to a pointer to the allocated buffer if the call succeeds; undefined otherwise.

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
<tr class="odd">
<td><p><strong>EFI_OUT_OF_RESOURCES</strong></p></td>
<td><p>The requested transfer buffer could not be allocated.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


## Requirements


**Header:** User generated

 

 




