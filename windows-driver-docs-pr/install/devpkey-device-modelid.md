---
title: DEVPKEY_Device_ModelId
description: DEVPKEY_Device_ModelId
ms.assetid: 6066f18b-40bf-4b36-9821-5e886e166256
keywords: ["DEVPKEY_Device_ModelId Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ModelId
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_ModelId


The DEVPKEY_Device_ModelId device property matches a device to a [device metadata package](https://msdn.microsoft.com/library/windows/hardware/ff541439).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_ModelId</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><a href="devprop-type-guid.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_GUID&lt;/strong&gt;](devprop-type-guid.md)"><strong>DEVPROP_TYPE_GUID</strong></a></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The DEVPKEY_Device_ModelId device property provides support for IHVs and OEMs to uniquely identify devices that share the same manufacturer and model. By using a model identifier (ModelID), OEMs and IHVs can match the device model that they distribute to their own branded device metadata package.

The DEVPKEY_Device_ModelId device property contains the value of the [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) XML element from the device's metadata package. When the device is installed, this PKEY is populated with the ModelID GUID value as reported by the device.

For more information, see [Device Metadata Packages](https://msdn.microsoft.com/library/windows/hardware/ff541439).

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
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[Device Metadata Packages](https://msdn.microsoft.com/library/windows/hardware/ff541439)

[**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






