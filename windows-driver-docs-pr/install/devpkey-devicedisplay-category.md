---
title: DEVPKEY_DeviceDisplay_Category
description: DEVPKEY_DeviceDisplay_Category
ms.assetid: 4f1999cd-e3b7-4755-ab48-1feabbc9d245
keywords: ["DEVPKEY_DeviceDisplay_Category Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceDisplay_Category
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceDisplay_Category


The DEVPKEY_DeviceDisplay_Category device property represents one or more functional categories that apply to a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceDisplay_Category</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Device categories for a physical device are specified through the [**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101) XML element in a [device metadata package](https://msdn.microsoft.com/library/windows/hardware/ff541439). Each instance of that device in a system inherits the device categories for that physical device.

Each physical device can have one or more functional categories specified in the [device metadata package](https://msdn.microsoft.com/library/windows/hardware/ff541439). Each category is used by Windows Devices and Printers to group the device instance into one of the recognized device categories.

Multifunction devices would typically identify multiple functional categories for each hardware function that the device supports. For example, a multifunction device could identify functional categories for printer, fax, scanner, and removable storage device functionality.

The first functional category string in the [**DEVPROP_TYPE_STRING_LIST**](devprop-type-string-list.md) specifies the physical device's primary functional category. The primary functional category is defined by the independent hardware vendor (IHV) to specify how the device is advertised, packaged, sold, and ultimately identified by users.

If the DEVPKEY_DeviceDisplay_Category device property specifies more than one functional category string, the remaining strings that follow the first string specifies the physical device's secondary functional categories.

The **Devices and Printers** user interface in Control Panel displays the primary and secondary functional categories of the device instance. These categories are displayed in the order that is specified in the DEVPKEY_DeviceDisplay_Category device property.

You can access the DEVPKEY_DeviceDisplay_Category property by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

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


[**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






