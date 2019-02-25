---
title: GUID_DEVINTERFACE_KEYBOARD
description: GUID_DEVINTERFACE_KEYBOARD
ms.assetid: ae434c45-07f6-4aa1-b9d3-e4ceca8cc81c
keywords: ["GUID_DEVINTERFACE_KEYBOARD Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_KEYBOARD
api_location:
- Ntddkbd.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_KEYBOARD


The GUID_DEVINTERFACE_KEYBOARD [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for keyboard devices.

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
<td align="left"><p>GUID_DEVINTERFACE_KEYBOARD</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{884b96c3-56ef-11d1-bc8c-00a0c91405dd}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for keyboard devices register instances of this device interface class to notify the system and applications of the presence of keyboard devices.

The system-supplied [keyboard class driver](../hid/keyboard-and-mouse-class-drivers.md) registers an instance of this device interface class for a keyboard device. Access an instance of this device interface class by using the I/O interface supported by the keyboard class driver.

For general information about supporting keyboard devices, see [HID Architecture](https://msdn.microsoft.com/library/windows/hardware/jj126193) and [Features of the Kbdclass and Mouclass Drivers](../hid/keyboard-and-mouse-class-drivers.md).

The WDK includes sample code for the system-supplied keyboard class driver. The keyboard class driver uses the obsolete identifier [**GUID_CLASS_KEYBOARD**](guid-class-keyboard.md) to register an instance of this [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

For information about the device interface class for mouse devices, see [**GUID_DEVINTERFACE_MOUSE**](guid-devinterface-mouse.md).

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
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddkbd.h (include Ntddkbd.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_CLASS_KEYBOARD**](guid-class-keyboard.md)

[**GUID_DEVINTERFACE_MOUSE**](guid-devinterface-mouse.md)

 

 






