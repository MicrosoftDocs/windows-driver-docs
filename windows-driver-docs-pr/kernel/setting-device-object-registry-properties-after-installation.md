---
title: Setting Device Object Registry Properties After Installation
description: Setting Device Object Registry Properties After Installation
keywords: ["device objects WDK kernel , registry", "registry WDK device objects"]
ms.date: 06/16/2017
---

# Setting Device Object Registry Properties After Installation





A user-mode program can use the [device installation functions](/previous-versions/ff541299(v=vs.85)) to get or set the registry settings for the properties of a driver's device object. Normally these functions are used by installation software, but they can be used by any user-mode program. (The program must be executed by a user that has Administrator access.)

The [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya) and [**SetupDiSetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya) functions get and set the registry key for each specified property. The *Property* parameter specifies the property to get or set. The *PropertyBuffer* points to the destination buffer (when getting the property) or source buffer (when setting the property) for the property.

The correspondence between values for the *Property* parameter and actual properties is as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value for <em>Property</em> parameter</th>
<th>Device object property</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SPDRP_CHARACTERISTICS</p></td>
<td><p>Device characteristics</p></td>
</tr>
<tr class="even">
<td><p>SPDRP_DEVTYPE</p></td>
<td><p>Device type</p></td>
</tr>
<tr class="odd">
<td><p>SPDRP_EXCLUSIVE</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="even">
<td><p>SPDRP_SECURITY</p></td>
<td><p>Security descriptor as a <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_security_descriptor" data-raw-source="[&lt;strong&gt;SECURITY_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_security_descriptor)"><strong>SECURITY_DESCRIPTOR</strong></a> structure</p></td>
</tr>
<tr class="odd">
<td><p>SPDRP_SECURITY_SDS</p></td>
<td><p>Security descriptor as an SDDL string</p></td>
</tr>
</tbody>
</table>

 

Note that two different ways are provided to get or set the security descriptor. You can specify the SPDRP\_SECURITY value to treat the security descriptor as a **SECURITY\_DESCRIPTOR** structure, or SPDRP\_SECURITY\_SDS to treat the security descriptor as an SDDL string. For more information about SDDL strings, see [SDDL for Device Objects](sddl-for-device-objects.md).

For Windows XP and later operating systems, programs can also get and set the property values for a device setup class. Use the [**SetupDiGetClassRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassregistrypropertya) and [**SetupDiSetClassRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclassregistrypropertya) functions to get and set the property values for a device setup class.

For more information about using the **SetupDi*Xxx*** functions, see [Using Device Installation Functions](../install/using-device-installation-functions.md).

