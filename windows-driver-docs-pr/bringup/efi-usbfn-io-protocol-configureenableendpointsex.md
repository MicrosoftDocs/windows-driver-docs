---
title: EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpointsEx
description: EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpointsEx
ms.assetid: 54DE0D7F-788F-49C3-AF5C-7EDAA0D09D20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpointsEx


Configures endpoints based on supplied list of device and configuration descriptors. The class driver may call this method in substitution of [EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpoints](efi-usbfn-io-protocolconfigureenableendpoints.md).

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS_EX) (
  IN EFI_USBFN_IO_PROTOCOL           *This,
  IN EFI_USB_DEVICE_INFO             *DeviceInfo,
  IN EFI_USB_SUPERSPEED_DEVICE_INFO  *SSDeviceInfo
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="deviceinfo"></a>*DeviceInfo*  
A pointer to an [EFI\_USB\_DEVICE\_INFO](efi-usb-device-info.md) structure.

<a href="" id="ssdeviceinfo"></a>*SSDeviceInfo*  
A pointer to an [EFI\_USB\_SUPERSPEED\_DEVICE\_INFO](efi-usb-superspeed-device-info.md) structure.

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
<td><p><strong>EFI_UNSUPPORTED</strong></p></td>
<td><p>This operation is not supported.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


This function is available starting in revision 0x00010002 of the **EFI\_USBFN\_IO\_PROTOCOL**.

Assuming that the hardware has already been initialized, this function configures the endpoints using the supplied *DeviceInfo*, activates the port, and starts receiving USB events. This function accepts *DeviceInfo* and *SSDeviceInfo* objects and configures the endpoint with the information from the object that supports the highest speed allowed by the underlying hardware. The high speed and super speed *DeviceInfo* objects passed in must have the same DeviceClass in the EFI\_USB\_DEVICE\_DESCRIPTOR. Otherwise, this function will return EFI\_UNSUPPORTED.

This function must ignore the *bMaxPacketSize0* field of the Standard Device Descriptor and *wMaxPacketSize* field of Standard Endpoint Descriptor that are made available through supplied *DeviceInfo*.

## Requirements


**Header:** User generated

 

 




