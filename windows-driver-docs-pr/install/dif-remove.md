---
title: DIF_REMOVE
description: DIF_REMOVE
ms.assetid: 14429756-c059-46d7-bd1c-0ae57d1ec8b5
keywords: ["DIF_REMOVE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_REMOVE
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_REMOVE


A DIF_REMOVE request notifies an installer that Windows is about to remove a device and gives the installer an opportunity to prepare for the removal.

### When Sent

When a user removes a device in Device Manager.

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
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device to be removed.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_REMOVEDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553323) structure might be associated with the *DeviceInfoData*.

There are no class installation parameters for the request if the DI_CLASSINSTALLPARAMS flag is clear in the [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346). In this case, no hardware profile is specified and the device is to be removed from the system as a whole.

### Installer Output

<a href="" id="none"></a>None  

### Installer Return Value

A co-installer can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**   The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF Code Handler

[**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097)

### Installer Operation

In response to a DIF_REMOVE request, an installer typically performs some clean-up operations. In this case, a co-installer returns NO_ERROR and a class installer returns ERROR_DI_DO_DEFAULT.

If an installer determines that the device should not be removed, the installer fails the DIF request by returning a Win32 error code. If the DI_QUIETINSTALL flag is clear, the installer should display a message to the user explaining why the device is not being removed.

Co-installers must not attempt to remove the device themselves by calling **SetupDiRemoveDevice**. Co-installers typically handle this request in postprocessing, after the device is successfully removed.

If a co-installer has to delete information in the registry, for example, the co-installer should do so in postprocessing and only if the previous installers succeeded the removal request. In its preprocessing pass, the co-installer should store the registry information in its context parameter and return ERROR_DI_POSTPROCESSING_REQUIRED to request postprocessing. When Windows calls the co-installer for postprocessing of this DIF request, the co-installer should check that the DIF status is NO_ERROR and then delete the registry information. If a co-installer deletes registry information in its preprocessing pass and the class installer (or another co-installer) fails the DIF_REMOVE, the co-installer could leave the device in an unpredictable state.

Installers should not delete files when handling this DIF request, in case the files are in use by another device.

Windows sends this DIF request before it initiates PnP query-remove and remove processing.

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


[**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP_REMOVEDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553323)

 

 






