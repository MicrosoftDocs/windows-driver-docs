---
title: GUID_DEVINTERFACE_MOUSE
description: GUID_DEVINTERFACE_MOUSE
keywords: ["GUID_DEVINTERFACE_MOUSE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_MOUSE
api_location:
- Ntddmou.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_DEVINTERFACE_MOUSE


The GUID_DEVINTERFACE_MOUSE [device interface class](./overview-of-device-interface-classes.md) is defined for mouse devices.

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
<td align="left"><p>GUID_DEVINTERFACE_MOUSE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{378DE44C-56EF-11D1-BC8C-00A0C91405DD}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for mouse devices register instances of this device interface class to notify the operating system and applications of the presence of mouse devices.

The system-supplied [mouse class driver](../hid/keyboard-and-mouse-class-drivers.md) registers an instance of this device interface class for a mouse device. Access an instance of this device interface class by using the I/O interface supported by the mouse class driver.

For general information about supporting mouse devices, see [HID Architecture](../hid/hid-architecture.md) and [Features of the Kbdclass and Mouclass Drivers](../hid/keyboard-and-mouse-class-drivers.md).

The WDK includes sample code for the system-supplied mouse class driver. The mouse class driver uses the obsolete identifier [**GUID_CLASS_MOUSE**](guid-class-mouse.md) to register an instance of this [device setup class](./overview-of-device-setup-classes.md).

For information about the device interface class for keyboard devices, see [**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddmou.h (include Ntddmou.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_CLASS_MOUSE**](guid-class-mouse.md)

[**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md)

 

