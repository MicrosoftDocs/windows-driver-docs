---
title: LocationPaths Registry Subkey
description: LocationPaths Registry Subkey
ms.assetid: d34ba7f4-97d2-4e63-a820-436c0336c584
---

# LocationPaths Registry Subkey


Beginning with Windows 7, the **LocationPaths** registry subkey is used in the specification of a removable device capability override for a device identified through either the [HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md) registry subkey. The **LocationPaths** registry subkey specifies that only the location path of the device's parent device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) will have the removable device capability override applied. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The **LocationPaths** registry subkey applies to only the parent devnode of the device specified through the name of the **HardwareID** or **CompatibleID** subkeys. As a result, only the parent devnode of the specified device is affected by the removable device capability override value. Child devnodes of the specified device are not affected by the removable device capability override, unless a [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkey is also specified.

The following table defines the format and requirements of the **LocationPaths** registry subkey.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry subkey name</th>
<th align="left">Required/optional</th>
<th align="left">Format requirements</th>
<th align="left">Parent subkey</th>
<th align="left">Child subkeys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>LocationPaths</strong></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>[HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md)</p></td>
<td align="left"><p>[LocationPath](locationpath-registry-subkey.md) or [*](--registry-subkey.md)</p></td>
</tr>
</tbody>
</table>

 

Either the **LocationPaths** or [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkeys must be present to indicate the parent/child relationship to which the removable device capability override applies.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20LocationPaths%20Registry%20Subkey%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




