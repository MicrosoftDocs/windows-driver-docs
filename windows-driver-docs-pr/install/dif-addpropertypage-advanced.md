---
title: DIF_ADDPROPERTYPAGE_ADVANCED
description: DIF_ADDPROPERTYPAGE_ADVANCED
ms.assetid: d2b05c45-3536-4997-ac6f-a5b5c95a97da
keywords: ["DIF_ADDPROPERTYPAGE_ADVANCED Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_ADDPROPERTYPAGE_ADVANCED
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_ADDPROPERTYPAGE_ADVANCED


A DIF_ADDPROPERTYPAGE_ADVANCED request allows an installer to supply one or more custom property pages for a device.

### When Sent

When a user clicks on the properties for a device in Device Manager or in Control Panel.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class Co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device Co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Optionally supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set. If *DeviceInfoSet* is **NULL**, Windows is requesting property pages for the [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
Device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) are associated with the *DeviceInfoData*, if specified, or with the *DeviceInfoSet*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_ADDPROPERTYPAGE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552337) structure is associated with the *DeviceInfoData*, if specified, or with the *DeviceInfoSet*.

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the [**SP_ADDPROPERTYPAGE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552337) to supply custom pages.

### Installer Return Value

A co-installer can return NO_ERROR or a Win32 error. A co-installer should not return ERROR_DI_POSTPROCESSING_REQUIRED for this DIF request.

A class installer returns NO_ERROR if it successfully supplies pages. Otherwise, a class installer returns ERROR_DI_DO_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

In response to this DIF request an installer can supply custom property pages. Handling this DIF request allows you to supply property pages from a class installer or co-installer and removes the need for a separate DLL that acts as a property-page provider.

An installer typically handles this DIF request to add a new device-specific or setup-class-specific property page. An installer can also replace the system-supplied driver property page, resource property page, or power property page for a device. If an installer replaces a system-supplied page, the installer must set the appropriate flag in the device installation parameters for the device:

<a href="" id="di-driverpage-added"></a>DI_DRIVERPAGE_ADDED  
The installer supplied a driver property page.

<a href="" id="di-resourcepage-added"></a>DI_RESOURCEPAGE_ADDED  
The installer supplied a resource property page.

<a href="" id="di-flagsex-powerpage-added"></a>DI_FLAGSEX_POWERPAGE_ADDED  
The installer supplied a power property page.

An installer cannot replace the system-supplied general properties page.

Windows only displays one driver page, one resource page, and one power page for a device. An installer should not supply a replacement system page if a previous installer already supplied a page of that type. This constraint does not apply to nonsystem-supplied property pages.

A co-installer should add custom pages in its preprocessing pass.

If an installer allows a user to set a property that requires Windows to remove and restart the device, the installer must set the DI_FLAGSEX_PROPCHANGE_PENDING flag in the device installation parameters from its **DialogProc** routine.

For more information about how to provide device property pages, see [Providing Device Property Pages](https://msdn.microsoft.com/library/windows/hardware/ff549784).

For more information about DIF codes, see [Handling DIF Codes](https://msdn.microsoft.com/library/windows/hardware/ff546094).

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
<td align="left"><p>Supported in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**SP_ADDPROPERTYPAGE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552337)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






