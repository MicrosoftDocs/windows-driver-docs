---
title: DIF_SELECTDEVICE
description: DIF_SELECTDEVICE
ms.assetid: c1266182-b88f-406a-876c-e0f15050fdf3
keywords: ["DIF_SELECTDEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_SELECTDEVICE
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_SELECTDEVICE


A DIF_SELECTDEVICE request allows an installer to participate in selecting the driver for a device.

### When Sent

When choosing a driver for a newly enumerated device or a new driver for an existing device (change driver). For example, when a user selects Add/Remove Hardware and selects the modem class. Or, a user inserts a PnP device and selects "Choose a Driver From a List" in the Found New Hardware Wizard.

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
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device for which a driver is to be selected. There is a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) associated with the *DeviceInfoSet*.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Optionally supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

If *DeviceInfoData* is **NULL**, this request is to select a driver for the [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) associated with the *DeviceInfoSet*.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
If *DeviceInfoData* is not **NULL**, there are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*. If *DeviceInfoData* is **NULL**, there are device installation parameters associated with the *DeviceInfoSet*.

Of particular interest is the **DriverPath**, which contains the location of INF(s) to use when building the driver list.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_SELECTDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553326) structure is associated with the *DeviceInfoData* if *DeviceInfoData* is not **NULL**. Otherwise, the class installation parameters are associated with the device information set as a whole.

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters. However, it should not modify the **DriverPath** field.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the [**SP_SELECTDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553326). For example, an installer might specify a title and/or instructions for Windows to use in the dialog box that asks the user to select a driver.

If an installer sets new select-device parameters, versus modifying parameters set by a previous installer, the installer must zero the fields that it does not set.

### Installer Return Value

If a co-installer does nothing for this DIF code, it returns NO_ERROR from its preprocessing pass. If a co-installer handles this DIF code, it should do so in its preprocessing pass and return NO_ERROR or a Win32 error code. By the time that a co-installer is called for postprocessing, the driver has already been selected.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**   The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

A class installer returns ERROR_DI_BAD_PATH if the **DriverPath** member of the corresponding [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure is not equal to **NULL**, but there are no valid drivers at the specified path location. This can occur if there are no drivers at the path location or if there are drivers, but the **Flags** member of the [**SP_DRVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553290) structure of each driver was set with the DN_BAD_DRIVER flag. In response to this error code, Windows displays an error to the user.

### Default DIF Code Handler

[**SetupDiSelectDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552115)

### Installer Operation

In response to a DIF_SELECTDEVICE request, an installer performs any selection operations required for its device or device class, besides what the default handler does. An installer typically responds to this DIF request in one of the following ways:

-   Do nothing.

    If an installer has no special selection requirements, it does nothing in response to this DIF code. A class installer returns ERROR_DI_DO_DEFAULT and a co-installer returns NO_ERROR.

-   Supply select strings that Windows will display in the selection UI.

    An installer can supply select strings in the class installation parameters ([**SP_SELECTDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553326)). For example, an installer can modify the **Instructions** or the window header **Title**.

    A class installer should not supply select strings if a co-installer already supplied select strings. The co-installer probably has more relevant information.

    If an installer modifies the [**SP_SELECTDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553326), the installer must also set the DI_USECI_SELECTSTRINGS flag in the [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346).

    If an installer successfully supplies select strings, Windows still has to call the default handler. Therefore, in this case, a co-installer returns NO_ERROR and a class installer returns ERROR_DI_DO_DEFAULT.

-   Modify the device installation parameters.

    An installer can modify the device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)). For example, an installer might set the DI_SHOWOEM flag to have Windows display the **Have Disk** button.

    If a class installer successfully modifies the device installation parameters, the class installer returns ERROR_DI_DO_DEFAULT.

-   Modify the list of drivers from which the user can select.

    This action is less common, but possible. An installer that modifies the driver list might, or might not, also supply select strings.

    An installer that modifies the driver list typically marks driver(s) that are inappropriate for the device. An installer marks such drivers with the flag DNF_BAD_DRIVER. Windows omits these drivers from the list it displays to the user.

    An installer marks bad drivers by following these steps:

    1.  Build the driver list by calling [**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917) with a *DriverType* of SPDIT_CLASSDRIVER.
    2.  Get the information about the first driver in the list by calling [**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018) and [**SetupDiGetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551978). If the driver is not appropriate for the device, set the DNF_BAD_DRIVER flag in the **Flags** field of the parameters. Apply the change to the parameters by calling [**SetupDiSetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552172).
    3.  Repeat the previous step until you have processed all the drivers in the list. Make sure that you increment the *MemberIndex* parameter to **SetupDiEnumDriverInfo** as described in the reference page for that function.

    An installer might set the DNF_BAD_DRIVER flag for one or more drivers in the driver list, but an installer must not clear that flag.

    If one or more installers successfully modify the driver list, Windows still has to call the default handler. Therefore, in this case, a co-installer returns NO_ERROR and a class installer returns ERROR_DI_DO_DEFAULT.

-   Display its own driver-selection user interface and set the selected driver.

    Only a class installer can display its own driver-selection user interface; co-installers must not. For example, a class installer might display pictures instead of textual lists.

    If the class installer successfully sets the selected driver, the class installer returns NO_ERROR and Windows does not call the default handler and therefore does not display the default selection interface.

If the DI_ENUMSINGLEINF flag is set in the device installation parameters, the **DriverPath** is a path of a single INF file instead of a path of a directory. An installer must use only that single INF to build the driver list.

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


[**DIF_NEWDEVICEWIZARD_SELECT**](dif-newdevicewizard-select.md)

[**SetupDiSelectDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552115)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP_SELECTDEVICE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553326)

 

 






