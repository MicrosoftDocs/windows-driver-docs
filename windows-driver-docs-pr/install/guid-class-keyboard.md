---
title: GUID_CLASS_KEYBOARD
description: GUID_CLASS_KEYBOARD
keywords: ["GUID_CLASS_KEYBOARD Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_CLASS_KEYBOARD
api_location:
- Ntddkbd.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_CLASS_KEYBOARD


GUID_CLASS_KEYBOARD is an obsolete identifier for the [device interface class](./overview-of-device-interface-classes.md) for keyboard devices. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md) class identifier for new instances of this class.

## Remarks

The HID samples that are provided in the WDK include the keyboard class driver. The keyboard class driver uses GUID_CLASS_KEYBOARD to register instances of this device interface class.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_KEYBOARD instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddkbd.h (include Ntddkbd.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md)

 

