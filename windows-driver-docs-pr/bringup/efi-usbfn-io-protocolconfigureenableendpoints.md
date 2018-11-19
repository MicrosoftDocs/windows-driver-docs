---
title: EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpoints
description: EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpoints
ms.assetid: 31bc58a0-ec2b-4b5e-ad1b-e6107cc083b1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpoints


The **ConfigureEnableEndpoints** function initializes endpoints based on supplied device and configuration descriptors.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS) (
  IN EFI_USBFN_IO_PROTOCOL         *This,
  IN EFI_USB_DEVICE_INFO           *DeviceInfo
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="deviceinfo"></a>*DeviceInfo*  
A pointer to an [EFI\_USB\_DEVICE\_INFO](efi-usb-device-info.md) structure.

## Return values


The function returns the following values:

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
<tr class="odd">
<td><p><strong>EFI_OUT_OF_RESOURCES</strong></p></td>
<td><p>The request could not be completed due to lack of resources.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


Assuming that the hardware has already been initialized, this function configures the endpoints using the supplied *DeviceInfo* , activates the port, and starts receiving USB events.

This function must ignore the *bMaxPacketSize0* field of the Standard Device Descriptor and *wMaxPacketSize* field of Standard Endpoint Descriptor that are made available through supplied *DeviceInfo*.

## Requirements


**Header:** User generated

 

 




