---
title: EFI_USBFN_IO_PROTOCOL.AbortTransfer
description: EFI_USBFN_IO_PROTOCOL.AbortTransfer
ms.assetid: 204998d6-7d8d-482b-8d9c-b96d2e2729bf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.AbortTransfer


The **AbortTransfer** function aborts transfer on the specified endpoint.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_ABORT_TRANSFER) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance

<a href="" id="endpointindex"></a>*EndpointIndex*  
Indicates the endpoint on which the ongoing transfer needs to be canceled.

<a href="" id="direction"></a>*Direction*  
Direction of the endpoint. For more information see [EFI\_USBFN\_ENDPOINT\_DIRECTION](efi-usbfn-endpoint-direction.md).

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
<td><p>The function returned successfully</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_INVALID_PARAMETER</strong></p></td>
<td><p>A parameter is invalid</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_DEVICE_ERROR</strong></p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_NOT_READY</strong></p></td>
<td><p>The physical device is busy or not ready to process this request</p></td>
</tr>
</tbody>
</table>

 

## Remarks


This function fails with **EFI\_INVALID\_PARAMETER** if the specified direction is incorrect for the endpoint.

## Requirements


**Header:** User generated

 

 




