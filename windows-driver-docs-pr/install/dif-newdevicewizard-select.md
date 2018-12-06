---
title: DIF_NEWDEVICEWIZARD_SELECT
description: DIF_NEWDEVICEWIZARD_SELECT
ms.assetid: b6b2eaf7-c87f-45d6-8845-6d03bde9a802
keywords: ["DIF_NEWDEVICEWIZARD_SELECT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_NEWDEVICEWIZARD_SELECT
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_NEWDEVICEWIZARD_SELECT


A DIF_NEWDEVICEWIZARD_SELECT request allows an installer to supply custom wizard page(s) that replace the standard select-driver page. This request is only used during manual installation of non-PnP devices.

### When Sent

Immediately before Windows displays the "Select a Device Driver" page.

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
<td align="left"><p>Does not handle</p></td>
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
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_NEWDEVICEWIZARD_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the flags in the device installation parameters. Windows does not check the flags upon completion of this DIF request. However, it checks them later in the installation process.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the [**SP_NEWDEVICEWIZARD_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305) to supply custom page(s).

### Installer Return Value

If a co-installer does not handle this DIF request it returns NO_ERROR from its preprocessing pass. If a co-installer handles this request it can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

A class installer returns NO_ERROR if it successfully supplies page(s). Otherwise, a class installer returns ERROR_DI_DO_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

A DIF_NEWDEVICEWIZARD_SELECT request allows an installer to supply custom wizard page(s) that replace the standard select-driver page. This request is only used during manual installation of non-PnP devices.

An installer responds to this DIF request to completely replace the standard select-driver wizard page. If, instead, the installer only has to modify the standard page or modify the list of drivers from which to choose, the installer should do so in response to the [**DIF_SELECTDEVICE**](dif-selectdevice.md) request.

A co-installer should add custom page(s) in its postprocessing pass and only if the class installer did not add custom page(s). If the class installer added page(s), the co-installer should not. Otherwise, the user might be asked to choose a driver twice.

If an installer supplies a custom select page, the installer must set the selected driver. In the installer's code that supports the wizard page, after the user clicks **Next**, the installer must call [**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183).

An installer should supply a Wizard 97 header title and a header subtitle in the PROPSHEETPAGE structure for a custom wizard page. An installer should not replace the system-supplied wizard title. See the Microsoft Windows SDK for documentation of the PROPSHEETPAGE structure and for more information about property pages.

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


[**DIF_NEWDEVICEWIZARD_PREANALYZE**](dif-newdevicewizard-preanalyze.md)

[**DIF_NEWDEVICEWIZARD_PRESELECT**](dif-newdevicewizard-preselect.md)

[**DIF_NEWDEVICEWIZARD_POSTANALYZE**](dif-newdevicewizard-postanalyze.md)

[**DIF_SELECTDEVICE**](dif-selectdevice.md)

[**SetupDiSetSelectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552176)

[**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP_NEWDEVICEWIZARD_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305)

 

 






