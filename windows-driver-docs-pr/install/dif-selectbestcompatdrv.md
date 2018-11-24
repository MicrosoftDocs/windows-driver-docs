---
title: DIF_SELECTBESTCOMPATDRV
description: DIF_SELECTBESTCOMPATDRV
ms.assetid: aa10f39f-718b-4160-9cfa-668fb0349156
keywords: ["DIF_SELECTBESTCOMPATDRV Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_SELECTBESTCOMPATDRV
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_SELECTBESTCOMPATDRV


A DIF_SELECTBESTCOMPATDRV request allows an installer to select the best driver from the device information element's compatible driver list.

### When Sent

When the operating system is preparing to install a new PnP device or is performing a change-driver operation on a PnP device.

This DIF request is typically used during a PnP configuration. If a device is being manually installed, Windows sends a [**DIF_SELECTDEVICE**](dif-selectdevice.md) request.

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
None

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters. However, they typically do not when handling this DIF request.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
As a side effect, an installer can modify the driver list associated with the *DeviceInfoData*, in particular, the SP_DRVINSTALL_PARAMS.

### Installer Return Value

A co-installer can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**   The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF Code Handler

[**SetupDiSelectBestCompatDrv**](https://msdn.microsoft.com/library/windows/hardware/ff552112)

### Installer Operation

An installer handles this DIF request to participate in selecting a driver for a PnP device. An installer typically responds to this DIF request in one of the following ways:

-   Do nothing.

    If an installer has no special selection requirements, it does nothing in response to this DIF request. A class installer returns ERROR_DI_DO_DEFAULT and a co-installer returns NO_ERROR.

-   Modify the parameters of one or more drivers in the driver list.

    For example, an installer might remove a driver from consideration for the device by marking it DNF_BAD_DRIVER. An installer modifies driver parameters by following these steps:

    1.  Get the information about the first driver in the list by calling [**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018) and [**SetupDiGetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551978). If appropriate, modify the driver parameters and apply the change by calling [**SetupDiSetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552172).

        If a driver is a worst-case choice, set the driver's rank to 0xFFFF or higher in the driver install parameters. See [How Windows Selects Drivers](https://msdn.microsoft.com/library/windows/hardware/ff546228) for more information.

    2.  Repeat the previous step until you have processed all the drivers in the list. Make sure that you increment the *MemberIndex* parameter to [**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018) as described in the reference page for that function.

    After a class installer modifies the driver list, it returns ERROR_DI_DO_DEFAULT. If a co-installer modifies the driver list, it should do so in preprocessing and return NO_ERROR.

-   Select the best driver for the device.

    This action is less common, but an installer might choose the best driver for the device. Such an installer would examine the data for each driver, choose a driver, and call [**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183) to set the driver. After an installer sets the selected driver, it returns NO_ERROR.

    If a co-installer selects a driver, it should do so in postprocessing.

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


[**SetupDiSelectBestCompatDrv**](https://msdn.microsoft.com/library/windows/hardware/ff552112)

[**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






