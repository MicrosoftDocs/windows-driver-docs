---
title: EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpointsEx
description: EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpointsEx
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 54DE0D7F-788F-49C3-AF5C-7EDAA0D09D20
---

# EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpointsEx


Configures endpoints based on supplied list of device and configuration descriptors. The class driver may call this method in substitution of [EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpoints](efi-usbfn-io-protocolconfigureenableendpoints.md).

## Syntax


``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpointsEx%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




