---
title: CompatibleID Registry Subkey
description: CompatibleID Registry Subkey
ms.assetid: 0111b013-d559-47bb-9cc8-d3930661a0a3
---

# CompatibleID Registry Subkey


Beginning with Windows 7, the **CompatibleID** registry subkey specifies a removable device capability override for a device installed in the computer. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The name of the **CompatibleID** registry subkey specifies the [compatible ID](compatible-ids.md) of the device, and is formatted based on the requirements described below.

The following table defines the format and requirements of the **CompatibleID** registry subkey.

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
<th align="left">Parent key</th>
<th align="left">Child subkeys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Valid [compatible ID](compatible-ids.md) value</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Must include the compatible ID's bus prefix.</p>
<p>All slash () path separator characters within the compatible ID must be replaced with number (#) characters.</p></td>
<td align="left">[DeviceOverrides](deviceoverrides-registry-key.md)</td>
<td align="left"><p>[LocationPaths](locationpaths-registry-subkey.md) and/or [ChildLocationPaths](childlocationpaths-registry-subkey.md)</p></td>
</tr>
</tbody>
</table>

 

The compatible ID value must follow the format requirements described in this table. Each **CompatibleID** subkey must contain either the **LocationPaths** or **ChildLocationPaths** subkeys. Both subkeys could be specified within the **CompatbleID** subkey if necessary.

Because the slash character is not a valid character in a registry subkey name, you must replace it with the number character when specifying a bus prefix for the **CompatibleID** registry subkey name. For example, if a removable device capability override is specified for the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) with a [hardware ID](hardware-ids.md) of PCI\\VEN\_ABCD&DEV\_1234&SUBSYS\_000, you must create a **CompatibleID** registry subkey with a name of PCI\#VEN\_ABCD&DEV\_1234&SUBSYS\_000.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CompatibleID%20Registry%20Subkey%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




