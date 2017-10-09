---
title: DIF\_SELECTBESTCOMPATDRV
description: DIF\_SELECTBESTCOMPATDRV
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
---

# DIF\_SELECTBESTCOMPATDRV


A DIF\_SELECTBESTCOMPATDRV request allows an installer to select the best driver from the device information element's compatible driver list.

### When Sent

When the operating system is preparing to install a new PnP device or is performing a change-driver operation on a PnP device.

This DIF request is typically used during a PnP configuration. If a device is being manually installed, Windows sends a [**DIF\_SELECTDEVICE**](dif-selectdevice.md) request.

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
Supplies a pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters. However, they typically do not when handling this DIF request.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
As a side effect, an installer can modify the driver list associated with the *DeviceInfoData*, in particular, the SP\_DRVINSTALL\_PARAMS.

### Installer Return Value

A co-installer can return NO\_ERROR, ERROR\_DI\_POSTPROCESSING\_REQUIRED, or a Win32 error code.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR\_DI\_DO\_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO\_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**   The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF Code Handler

[**SetupDiSelectBestCompatDrv**](https://msdn.microsoft.com/library/windows/hardware/ff552112)

### Installer Operation

An installer handles this DIF request to participate in selecting a driver for a PnP device. An installer typically responds to this DIF request in one of the following ways:

-   Do nothing.

    If an installer has no special selection requirements, it does nothing in response to this DIF request. A class installer returns ERROR\_DI\_DO\_DEFAULT and a co-installer returns NO\_ERROR.

-   Modify the parameters of one or more drivers in the driver list.

    For example, an installer might remove a driver from consideration for the device by marking it DNF\_BAD\_DRIVER. An installer modifies driver parameters by following these steps:

    1.  Get the information about the first driver in the list by calling [**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018) and [**SetupDiGetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551978). If appropriate, modify the driver parameters and apply the change by calling [**SetupDiSetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552172).

        If a driver is a worst-case choice, set the driver's rank to 0xFFFF or higher in the driver install parameters. See [How Windows Selects Drivers](https://msdn.microsoft.com/library/windows/hardware/ff546228) for more information.

    2.  Repeat the previous step until you have processed all the drivers in the list. Make sure that you increment the *MemberIndex* parameter to [**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018) as described in the reference page for that function.

    After a class installer modifies the driver list, it returns ERROR\_DI\_DO\_DEFAULT. If a co-installer modifies the driver list, it should do so in preprocessing and return NO\_ERROR.

-   Select the best driver for the device.

    This action is less common, but an installer might choose the best driver for the device. Such an installer would examine the data for each driver, choose a driver, and call [**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183) to set the driver. After an installer sets the selected driver, it returns NO\_ERROR.

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

[**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_SELECTBESTCOMPATDRV%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





