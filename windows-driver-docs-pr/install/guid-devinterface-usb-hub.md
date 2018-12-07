---
title: GUID_DEVINTERFACE_USB_HUB
description: GUID_DEVINTERFACE_USB_HUB
ms.assetid: 899b77ad-fa98-4078-9207-69b422e3d0d0
keywords: ["GUID_DEVINTERFACE_USB_HUB Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_USB_HUB
api_location:
- Usbiodef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_USB_HUB


The GUID_DEVINTERFACE_USB_HUB [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [USB](https://msdn.microsoft.com/library/windows/hardware/ff538930) hub devices.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVINTERFACE_USB_HUB</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{F18A0E88-C30C-11D0-8815-00A0C906BED8}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied USB port driver registers instances of GUID_DEVINTERFACE_USB_HUB to notify the operating system and applications of the presence of the root hub of host controller devices. The system-supplied USB hub driver registers instances of this class for additional hub devices, if any, that are supported by the host controller.

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](http://go.microsoft.com/fwlink/p/?linkid=256205). The USBVIEW sample uses the obsolete identifier [**GUID_CLASS_USBHUB**](guid-class-usbhub.md) to be notified of instances of this device interface class.

You must include initguid.h before including any header that declares a GUID by using the DEFINE_GUID macro.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Usbiodef.h (include Usbiodef.h, initguid.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_CLASS_USBHUB**](guid-class-usbhub.md)

[**GUID_DEVINTERFACE_USB_DEVICE**](guid-devinterface-usb-device.md)

[**GUID_DEVINTERFACE_USB_HOST_CONTROLLER**](guid-devinterface-usb-host-controller.md)

 

 






