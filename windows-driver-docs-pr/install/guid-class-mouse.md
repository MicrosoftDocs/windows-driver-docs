---
title: GUID_CLASS_MOUSE
description: GUID_CLASS_MOUSE
ms.assetid: 3b6578c7-0462-4fff-bd09-b9c768676ceb
keywords: ["GUID_CLASS_MOUSE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_CLASS_MOUSE
api_location:
- Ntddmou.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_CLASS_MOUSE


GUID_CLASS_MOUSE is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for mouse devices. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_MOUSE**](guid-devinterface-mouse.md) class identifier for new instances of this class.

Remarks
-------

The HID samples that are provided in the WDK include the mouse class driver. The mouse class driver uses GUID_CLASS_MOUSE to register instances of this device interface class.

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
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_MOUSE instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddmou.h (include Ntddmou.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_MOUSE**](guid-devinterface-mouse.md)

 

 






