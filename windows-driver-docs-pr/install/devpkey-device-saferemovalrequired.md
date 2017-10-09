---
title: DEVPKEY\_Device\_SafeRemovalRequired
description: DEVPKEY\_Device\_SafeRemovalRequired
ms.assetid: a162e259-21aa-40d9-a65a-af175a59df6a
keywords: ["DEVPKEY_Device_SafeRemovalRequired Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SafeRemovalRequired
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_Device\_SafeRemovalRequired


The DEVPKEY\_Device\_SafeRemovalRequired device property represents a Boolean value that indicates whether a hot-plug device instance requires safe removal from the computer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_SafeRemovalRequired</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_BOOLEAN</strong>](devprop-type-boolean.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If this property for a hot-plug device instance has a value of DEVPROP\_TRUE, the device instance requires safe removal from the computer. In this case, Windows displays the **Safely Remove Hardware** icon in the notification area on the right side of the taskbar. When the user clicks this icon, the system starts the **Safely Remove Hardware** program. By using this program, the user can instruct the system to prepare the device instance for removal before it can be surprise-removed from the computer.

**Note**   If the device instance is a removable media device, such as an optical disk drive, the device instance must have media inserted and must have the DEVPKEY\_Device\_SafeRemovalRequired property value of DEVPROP\_TRUE. If both are true, the device instance is displayed in the **Safely Remove Hardware** program.

 

Windows Plug and Play (PnP) determines that the hot-plug device instance requires safe removal from the system if the following are true:

-   The device instance is currently connected to the system.

-   The device instance is either started or can be ejected automatically by the system.

-   The CM\_DEVCAP\_SURPRISEREMOVALOK device capability bit for the device instance is not set. For more information about device capabilities, see [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967).

-   The device instance does not have the [**DEVPKEY\_Device\_SafeRemovalRequiredOverride**](devpkey-device-saferemovalrequiredoverride.md) device property set to DEVPROP\_FALSE.

    **Note**   PnP unconditionally determines that the hot-plug device requires safe removal if the DEVPKEY\_Device\_SafeRemovalRequiredOverride device property is set to DEVPROP\_TRUE.

     

-   The device instance is either directly removable from its parent device instance or has a removable ancestor in its device tree.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY\_Device\_SafeRemovalRequired.

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
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEVPKEY\_Device\_SafeRemovalRequiredOverride**](devpkey-device-saferemovalrequiredoverride.md)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Device_SafeRemovalRequired%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





