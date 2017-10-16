---
title: DIF_PROPERTYCHANGE
description: DIF_PROPERTYCHANGE
ms.assetid: 62f3380d-8cd1-4f4c-a727-1285de081b9e
keywords: ["DIF_PROPERTYCHANGE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_PROPERTYCHANGE
api_location:
- Setupapi.h
api_type:
- HeaderDef
---

# DIF_PROPERTYCHANGE


A DIF_PROPERTYCHANGE request notifies the installer that the device's properties are changing. The device is being enabled, disabled, started, stopped, or some item on a property page has changed. This DIF request gives the installer an opportunity to participate in the change.

### When Sent

When a device is being enabled, disabled, restarted, stopped, or its properties have changed.

For example, Windows sends this request when a property-page provider sets the DI_FLAGSEX_PROPCHANGE_PENDING flag in the **FlagsEx** field of the [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure for the device.

For more information about detecting when a device is started for the first time or subsequently restarted, see the Installer Operation section.

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
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_PROPCHANGE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553315) structure is associated with the *DeviceInfoData*.

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

[**SetupDiChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff550930)

### Installer Operation

In response to a DIF_PROPERTYCHANGE request an installer can participate in the property-change operation. The class installation parameters (SP_PROPCHANGE_PARAMS) indicate which change is taking place.

A property change might require a system restart. For information about how to restart the system, see [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922).

When Windows sends a DIF_INSTALLDEVICE request to install a device for the first time, Windows starts the device but does not send a DIF_PROPERTYCHANGE request as part of the installation. If a custom installation operation must be performed when a device is started for the first time and whenever the device is subsequently restarted, an installer or a co-installer should handle the DIF_INSTALLDEVICE request that starts the device for the first time and a DIF_PROPERTYCHANGE request that indicates that the state change action is that the device is being started.

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


[**SetupDiChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff550930)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP_PROPCHANGE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553315)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_PROPERTYCHANGE%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





