---
title: GUID_DEVINTERFACE_USB_DEVICE
description: GUID_DEVINTERFACE_USB_DEVICE
ms.assetid: 9a771eca-8ec5-4c69-8b1e-f01f548b5041
keywords: ["GUID_DEVINTERFACE_USB_DEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_USB_DEVICE
api_location:
- Usbiodef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_USB_DEVICE


The GUID_DEVINTERFACE_USB_DEVICE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [USB devices](https://msdn.microsoft.com/library/windows/hardware/ff538930) that are attached to a USB hub.

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
<td align="left"><p>GUID_DEVINTERFACE_USB_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{A5DCBF10-6530-11D2-901F-00C04FB951ED}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied USB hub driver registers instances of GUID_DEVINTERFACE_USB_DEVICE to notify the system and applications of the presence of USB devices that are attached to a USB hub.

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](http://go.microsoft.com/fwlink/p/?linkid=256205). The USBVIEW sample uses the obsolete identifier [**GUID_CLASS_USB_DEVICE**](guid-class-usb-device.md) to register to be notified of the arrival of instances of this device interface class.

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


[**GUID_CLASS_USB_DEVICE**](guid-class-usb-device.md)

[**GUID_DEVINTERFACE_USB_HOST_CONTROLLER**](guid-devinterface-usb-host-controller.md)

[**GUID_DEVINTERFACE_USB_HUB**](guid-devinterface-usb-hub.md)

 

 






