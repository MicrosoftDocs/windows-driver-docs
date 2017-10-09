---
title: DIF\_NEWDEVICEWIZARD\_FINISHINSTALL
description: DIF\_NEWDEVICEWIZARD\_FINISHINSTALL
ms.assetid: 5d27316b-4e47-4e18-95fe-fd4a63a76626
keywords: ["DIF_NEWDEVICEWIZARD_FINISHINSTALL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_NEWDEVICEWIZARD_FINISHINSTALL
api_location:
- Setupapi.h
api_type:
- HeaderDef
---

# DIF\_NEWDEVICEWIZARD\_FINISHINSTALL


A DIF\_NEWDEVICEWIZARD\_FINISHINSTALL request allows an installer to supply finish-install wizard pages that Windows displays to the user after a device is installed but before Windows displays the standard finish page. Windows sends this request when it installs Plug and Play (PnP) devices and when an administrator uses the **Add Hardware Wizard** to install non-PnP devices.

### When Sent

After Windows installs a device (on successful completion of [**DIF\_INSTALLDEVICE**](dif-installdevice.md) processing), but before it displays the Finish wizard page.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
A handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
A pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP\_NEWDEVICEWIZARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the flags in the device installation parameters.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the SP\_NEWDEVICEWIZARD\_DATA structure to supply finish-install wizard pages.

### Installer Return Value

If a co-installer does not handle this DIF request, the co-installer returns NO\_ERROR from its preprocessing pass. If a co-installer handles this request, the co-installer can return NO\_ERROR, ERROR\_DI\_POSTPROCESSING\_REQUIRED, or a Win32 error code.

A class installer returns NO\_ERROR if the installer successfully supplies pages. Otherwise, a class installer returns ERROR\_DI\_DO\_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

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


[**DIF\_FINISHINSTALL\_ACTION**](dif-finishinstall-action.md)

[**DIF\_INSTALLDEVICE**](dif-installdevice.md)

[**SetupDiChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff550930)

[**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP\_NEWDEVICEWIZARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553305)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_NEWDEVICEWIZARD_FINISHINSTALL%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





