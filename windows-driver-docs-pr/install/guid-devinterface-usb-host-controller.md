---
title: GUID_DEVINTERFACE_USB_HOST_CONTROLLER
description: GUID_DEVINTERFACE_USB_HOST_CONTROLLER
ms.assetid: 4afa1ada-ff57-4585-9117-10595310b976
keywords: ["GUID_DEVINTERFACE_USB_HOST_CONTROLLER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_USB_HOST_CONTROLLER
api_location:
- Usbiodef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_USB_HOST_CONTROLLER


The GUID_DEVINTERFACE_USB_HOST_CONTROLLER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [USB](https://msdn.microsoft.com/library/windows/hardware/ff538930) host controller devices.

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
<td align="left"><p>GUID_DEVINTERFACE_USB_HOST_CONTROLLER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{3ABF6F2D-71C4-462A-8A92-1E6861E6AF27}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied port driver for a USB host controller registers instances of GUID_DEVINTERFACE_USB_HOST_CONTROLLER to notify the operating system and applications of the presence of USB host controllers.

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](http://go.microsoft.com/fwlink/p/?linkid=256205). The USBVIEW uses the obsolete identifier [**GUID_CLASS_USB_HOST_CONTROLLER**](guid-class-usb-host-controller.md) to enumerate instances of this device interface class.

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


[**GUID_CLASS_USB_HOST_CONTROLLER**](guid-class-usb-host-controller.md)

[**GUID_DEVINTERFACE_USB_DEVICE**](guid-devinterface-usb-device.md)

[**GUID_DEVINTERFACE_USB_HUB**](guid-devinterface-usb-hub.md)

 

 






