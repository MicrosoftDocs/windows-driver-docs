---
title: GUID_CLASS_USBHUB
description: GUID_CLASS_USBHUB
keywords: ["GUID_CLASS_USBHUB Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_CLASS_USBHUB
api_location:
- Usbiodef.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_CLASS_USBHUB


GUID_CLASS_USBHUB is an obsolete identifier for the [device interface class](./overview-of-device-interface-classes.md) for [USB](../index.yml) hub devices. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_USB_HUB**](guid-devinterface-usb-hub.md) class identifier for new instances of this class.

## Remarks

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](/samples/browse/). The USBVIEW sample uses GUID_CLASS_USBHUB to be notified if the instances of the GUID_CLASS_USBHUB device interface class are present.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_USB_HUB instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Usbiodef.h (include Usbiodef.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_USB_HUB**](guid-devinterface-usb-hub.md)

