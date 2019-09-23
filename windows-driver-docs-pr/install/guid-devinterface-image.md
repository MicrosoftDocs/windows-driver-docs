---
title: GUID_DEVINTERFACE_IMAGE
description: GUID_DEVINTERFACE_IMAGE
ms.assetid: 2768f0ef-3765-4a66-b480-0f75a7c49c3c
keywords: ["GUID_DEVINTERFACE_IMAGE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_IMAGE
api_location:
- Wiaintfc.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_IMAGE


The GUID_DEVINTERFACE_IMAGE [device interface class](https://docs.microsoft.com/windows-hardware/drivers/install/device-interface-classes) is defined for [WIA devices and Still Image (STI) devices](https://docs.microsoft.com/windows-hardware/drivers/image/index), including digital cameras and scanners.

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
<td align="left"><p>GUID_DEVINTERFACE_IMAGE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{6BDD1FC6-810F-11D0-BEC7-08002BE2092F}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied kernel-mode drivers for WIA devices register an instance of this device interface class to notify the operating system and applications of the presence of WIA devices.

For information about WIA drivers and STI drivers, see [Windows Image Acquisition Drivers](https://docs.microsoft.com/windows-hardware/drivers/image/windows-image-acquisition-drivers).

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
<td align="left"><p>Available in Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Wiaintfc.h (include Wiaintfc.h)</td>
</tr>
</tbody>
</table>

 

 





