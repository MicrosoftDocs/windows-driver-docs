---
title: EFI_USBFN_IO_PROTOCOL.GetEndpointMaxPacketSize
description: EFI_USBFN_IO_PROTOCOL.GetEndpointMaxPacketSize
ms.assetid: 0af72372-7c58-490d-8eec-bd38bce09b0d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.GetEndpointMaxPacketSize


The **GetEndpointMaxPacketSize** function returns the maximum packet size of the specified endpoint type for the supplied bus speed..

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE) (
  IN EFI_USBFN_IO_PROTOCOL      *This,
  IN EFI_USB_ENDPOINT_TYPE      EndpointType,
  IN EFI_USB_BUS_SPEED          BusSpeed,
  OUT UINT16                    *MaxPacketSize
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="endpointtype"></a>*EndpointType*  
Endpoint type as defined in the [EFI\_USB\_ENDPOINT\_TYPE](efi-usb-endpoint-type.md). enumeration

<a href="" id="busspeed"></a>*BusSpeed*  
An [EFI\_USB\_BUS\_SPEED](efi-usb-bus-speed.md) enumeration value that indicates the current bus speed as known to the caller.

<a href="" id="maxpacketsize"></a>*MaxPacketSize*  
The maximum packet size, in bytes, of the specified endpoint type.

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
<td><p><strong>EFI_DEVICE_ERROR</strong></p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_NOT_READY</strong></p></td>
<td><p>The physical device is busy or not ready to process this request</p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

 

 




