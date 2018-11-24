---
title: GUID_DEVINTERFACE_WPD_PRIVATE
description: GUID_DEVINTERFACE_WPD_PRIVATE
ms.assetid: 50292137-d648-41cf-928e-d72549f6321b
keywords: ["GUID_DEVINTERFACE_WPD_PRIVATE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_WPD_PRIVATE
api_location:
- Portabledevice.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_WPD_PRIVATE


The GUID_DEVINTERFACE_WPD_PRIVATE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for specialized [Windows Portable Devices](http://go.microsoft.com/fwlink/p/?linkid=106527) (WPD).

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
<td align="left"><p>GUID_DEVINTERFACE_WPD_PRIVATE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{BA0C718F-4DED-49B7-BDD3-FABE28661211}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

GUID_DEVINTERFACE_WPD_PRIVATE should be used only for private devices that are used by custom WPD applications. Generic WPD drivers and clients of WPD devices should not use instances of this device interface class.

Custom applications can enumerate private devices that register this interface by calling **IPortableDeviceManager::GetPrivateDevices** (documented in Windows SDK).

For information about the device interface class for generic WPD devices, see [**GUID_DEVINTERFACE_WPD**](guid-devinterface-wpd.md).

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


[**GUID_DEVINTERFACE_WPD**](guid-devinterface-wpd.md)

 

 






