---
title: GUID_CLASS_USB_HOST_CONTROLLER
description: GUID_CLASS_USB_HOST_CONTROLLER
keywords: ["GUID_CLASS_USB_HOST_CONTROLLER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_CLASS_USB_HOST_CONTROLLER
api_location:
- Usbiodef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_CLASS_USB_HOST_CONTROLLER


GUID_CLASS_USB_HOST_CONTROLLER is an obsolete identifier for the [device interface class](./overview-of-device-interface-classes.md) for [USB](../index.yml) host controller devices. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_USB_HOST_CONTROLLER**](guid-devinterface-usb-host-controller.md) class identifier for new instances of this class.

## Remarks

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](/samples/browse/). The USBVIEW sample uses GUID_CLASS_USB_HOST_CONTROLLER to enumerate instances of the GUID_CLASS_USB_HOST_CONTROLLER device interface class.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_USB_HOST_CONTROLLER instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Usbiodef.h (include Usbiodef.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_USB_HOST_CONTROLLER**](guid-devinterface-usb-host-controller.md)

