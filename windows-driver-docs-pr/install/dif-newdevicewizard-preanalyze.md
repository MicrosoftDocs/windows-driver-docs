---
title: DIF\_NEWDEVICEWIZARD\_PREANALYZE
description: DIF\_NEWDEVICEWIZARD\_PREANALYZE
ms.assetid: 6731a916-488a-4fb2-84d9-4b3cb9b8b160
keywords: ["DIF_NEWDEVICEWIZARD_PREANALYZE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_NEWDEVICEWIZARD_PREANALYZE
api_location:
- Setupapi.h
api_type:
- HeaderDef
---

# DIF\_NEWDEVICEWIZARD\_PREANALYZE


A DIF\_NEWDEVICEWIZARD\_PREANALYZE request allows an installer to supply wizard pages that Windows displays to the user before it displays the analyze page. This request is only used during manual installation of non-PnP devices.

### When Sent

After the user has selected a driver, but before Windows registers the device that makes the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) "live."

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
An [**SP\_NEWDEVICEWIZARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the flags in the device installation parameters. Windows does not check the flags upon completion of this DIF request. However, it checks them later in the installation process.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the [**SP\_NEWDEVICEWIZARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305) to supply custom wizard page(s).

### Installer Return Value

If a co-installer does not handle this DIF request it returns NO\_ERROR from its preprocessing pass. If a co-installer handles this request it can return NO\_ERROR, ERROR\_DI\_POSTPROCESSING\_REQUIRED, or a Win32 error code.

A class installer returns NO\_ERROR if it successfully supplies page(s). Otherwise, a class installer returns ERROR\_DI\_DO\_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

A DIF\_NEWDEVICEWIZARD\_PREANALYZE request allows an installer to supply wizard pages that Windows displays to the user before it displays the analyze page. These pages can be thought of as "postselect" pages. This request is only used during manual installation of non-PnP devices.

An installer might use a custom preanalyze page, for example, to choose a COM port after a modem device is selected.

If an installer adds custom preselect page(s), the installer should first check whether **NumDynamicPages** in the class install parameters has reached MAX\_INSTALLWIZARD\_DYNAPAGES.

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


[**DIF\_NEWDEVICEWIZARD\_PRESELECT**](dif-newdevicewizard-preselect.md)

[**DIF\_NEWDEVICEWIZARD\_POSTANALYZE**](dif-newdevicewizard-postanalyze.md)

[**DIF\_NEWDEVICEWIZARD\_SELECT**](dif-newdevicewizard-select.md)

[**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP\_NEWDEVICEWIZARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_NEWDEVICEWIZARD_PREANALYZE%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





