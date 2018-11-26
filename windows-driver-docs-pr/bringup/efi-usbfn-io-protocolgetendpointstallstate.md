---
title: EFI_USBFN_IO_PROTOCOL.GetEndpointStallState
description: EFI_USBFN_IO_PROTOCOL.GetEndpointStallState
ms.assetid: abf53ee7-8460-4861-a82d-827ad1dc6c40
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.GetEndpointStallState


The **GetEndpointStallState** function returns the stall state on the specified endpoint.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN OUT BOOLEAN                  *State
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="endpointindex"></a>*EndpointIndex*  
Indicates the endpoint.

<a href="" id="direction"></a>*Direction*  
Direction of the endpoint. For more information, see [EFI\_USBFN\_ENDPOINT\_DIRECTION](efi-usbfn-endpoint-direction.md).

<a href="" id="state"></a>*State*  
Boolean; **TRUE** value indicates that the endpoint is in a stalled state, **FALSE** otherwise.

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

 

 




