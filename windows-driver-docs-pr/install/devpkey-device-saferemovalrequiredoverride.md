---
title: DEVPKEY\_Device\_SafeRemovalRequiredOverride
description: DEVPKEY\_Device\_SafeRemovalRequiredOverride
ms.assetid: 8289effe-3849-41bf-b870-69e3d8cb8850
keywords: ["DEVPKEY_Device_SafeRemovalRequiredOverride Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SafeRemovalRequiredOverride
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_Device\_SafeRemovalRequiredOverride


The DEVPKEY\_Device\_SafeRemovalRequiredOverride device property represents the safe removal override for the device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_SafeRemovalRequiredOverride</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_BOOLEAN</strong>](devprop-type-boolean.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This device property can be used to override the result of the heuristic that Windows Plug and Play (PnP) uses to calculate the value of the [**DEVPKEY\_Device\_SafeRemovalRequired**](devpkey-device-saferemovalrequired.md) device property. This override is performed as follows:

-   If the DEVPKEY\_Device\_SafeRemovalRequiredOverride device property is set to DEVPROP\_TRUE and the device instance is removable or has a removable ancestor, PnP sets the DEVPKEY\_Device\_SafeRemovalRequired device property to DEVPROP\_TRUE and does not use the heuristic.

    **Note**  A device instance is considered removable if its removable device capability is set. For more information, see [Overview of the Removable Device Capability](https://msdn.microsoft.com/library/windows/hardware/ff549564).

     

-   If the DEVPKEY\_Device\_SafeRemovalRequiredOverride device property is set to DEVPROP\_TRUE and the device instance (or an ancestor) is not removable, PnP sets the DEVPKEY\_Device\_SafeRemovalRequired to DEVPROP\_FALSE and does not use the heuristic.

-   If the DEVPKEY\_Device\_SafeRemovalRequiredOverride device property is either not set or set to DEVPROP\_FALSE, PnP sets the DEVPKEY\_Device\_SafeRemovalRequired device property to a value that is determined by using the heuristic.

You can retrieve the value of DEVPKEY\_Device\_SafeRemovalRequiredOverride by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963). You can also set this value by calling [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163).

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


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Device_SafeRemovalRequiredOverride%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





