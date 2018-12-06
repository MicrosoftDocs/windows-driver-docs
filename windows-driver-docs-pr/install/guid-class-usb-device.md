---
title: GUID_CLASS_USB_DEVICE
description: GUID_CLASS_USB_DEVICE
ms.assetid: e014f3d5-541d-4e86-a572-b110ec5a822d
keywords: ["GUID_CLASS_USB_DEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_CLASS_USB_DEVICE
api_location:
- Usbiodef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_CLASS_USB_DEVICE


GUID_CLASS_USB_DEVICE is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for [USB](https://msdn.microsoft.com/library/windows/hardware/ff538930) devices that are attached to a USB hub. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_USB_DEVICE**](guid-devinterface-usb-device.md) class identifier for new instances of this class.

Remarks
-------

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](http://go.microsoft.com/fwlink/p/?linkid=256205). The USBVIEW sample uses GUID_CLASS_USB_DEVICE to register to be notified if instances of the GUID_CLASS_USB_DEVICE interface class are present.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_USB_DEVICE instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Usbiodef.h (include Usbiodef.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_USB_DEVICE**](guid-devinterface-usb-device.md)

 

 






