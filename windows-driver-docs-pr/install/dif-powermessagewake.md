---
title: DIF\_POWERMESSAGEWAKE
description: DIF\_POWERMESSAGEWAKE
ms.assetid: 73f6e763-0900-4297-ac88-20bbb3ac424d
keywords: ["DIF_POWERMESSAGEWAKE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_POWERMESSAGEWAKE
api_location:
- Setupapi.h
api_type:
- HeaderDef
---

# DIF\_POWERMESSAGEWAKE


A DIF\_POWERMESSAGEWAKE request allows an installer to supply custom text that Windows displays on the power management properties page of the device properties.

### When Sent

When a user clicks on a menu item or tab to display the properties of a device.

Windows only sends this DIF request if the drivers for the device support power management. Otherwise, Windows does not display any power properties for the device.

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
Supplies a pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP\_POWERMESSAGEWAKE\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553311) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the [**SP\_POWERMESSAGEWAKE\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553311) to supply custom text for a device's power properties page.

### Installer Return Value

A co-installer typically returns NO\_ERROR, ERROR\_DI\_POSTPROCESSING\_REQUIRED, or a Win32 error code.

A class installer returns NO\_ERROR if it successfully supplies power properties text. Otherwise, a class installer returns ERROR\_DI\_DO\_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

A DIF\_POWERMESSAGEWAKE request allows an installer to supply text that Windows displays on the power properties page for a device.

If a co-installer supplies power-properties text, it should do so in its postprocessing phase. A co-installer should be careful when overwriting any power-properties text supplied by an installer that handled the request before the co-installer.

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


[**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP\_POWERMESSAGEWAKE\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553311)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_POWERMESSAGEWAKE%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





