---
title: GUID_DEVINTERFACE_WPD
description: GUID_DEVINTERFACE_WPD
ms.assetid: 611d1866-2530-4acb-8c83-77c29bdd128c
keywords: ["GUID_DEVINTERFACE_WPD Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_WPD
api_location:
- Portabledevice.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_WPD


The GUID_DEVINTERFACE_WPD [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [Windows Portable Devices](http://go.microsoft.com/fwlink/p/?linkid=106527) (WPD).

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
<td align="left"><p>GUID_DEVINTERFACE_WPD</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{6AC27878-A6FA-4155-BA85-F98F491D4F33}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for devices that support the WPD device-driver interface (DDI) register instances of GUID_DEVINTERFACE_WPD to notify the operating system and applications that WPD devices are present.

The WPD class extension component registers an instance of this device interface for a WPD driver that uses the WPD class extension.

Clients that use WPD devices should register to be notified of the arrival of instances of this device interface class.

Clients can enumerate WPD devices that register this interface by calling **IPortableDeviceManager::GetDevices** (documented in Windows SDK).

For information about the device interface class for private WPD devices, see [**GUID_DEVINTERFACE_WPD_PRIVATE**](guid-devinterface-wpd-private.md).

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
<td align="left"><p>Available in Windows Vista, Windows XP, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Portabledevice.h (include Portabledevice.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_WPD_PRIVATE**](guid-devinterface-wpd-private.md)

 

 






