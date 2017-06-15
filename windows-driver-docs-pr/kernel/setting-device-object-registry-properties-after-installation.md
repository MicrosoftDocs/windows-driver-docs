---
title: Setting Device Object Registry Properties After Installation
author: windows-driver-content
description: Setting Device Object Registry Properties After Installation
MS-HAID:
- 'DevObjts\_ba33d246-2931-463e-b595-d547c7a56276.xml'
- 'kernel.setting\_device\_object\_registry\_properties\_after\_installation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e9415497-f61e-49ba-9376-9255e51e72a8
keywords: ["device objects WDK kernel , registry", "registry WDK device objects"]
---

# Setting Device Object Registry Properties After Installation


## <a href="" id="ddk-setting-device-object-registry-properties-after-installation-kg"></a>


A user-mode program can use the [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) to get or set the registry settings for the properties of a driver's device object. Normally these functions are used by installation software, but they can be used by any user-mode program. (The program must be executed by a user that has Administrator access.)

The [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) and [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169) functions get and set the registry key for each specified property. The *Property* parameter specifies the property to get or set. The *PropertyBuffer* points to the destination buffer (when getting the property) or source buffer (when setting the property) for the property.

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
<td><p>Security descriptor as a [<strong>SECURITY_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563689) structure</p></td>
</tr>
<tr class="odd">
<td><p>SPDRP_SECURITY_SDS</p></td>
<td><p>Security descriptor as an SDDL string</p></td>
</tr>
</tbody>
</table>

 

Note that two different ways are provided to get or set the security descriptor. You can specify the SPDRP\_SECURITY value to treat the security descriptor as a **SECURITY\_DESCRIPTOR** structure, or SPDRP\_SECURITY\_SDS to treat the security descriptor as an SDDL string. For more information about SDDL strings, see [SDDL for Device Objects](sddl-for-device-objects.md).

For Windows XP and later operating systems, programs can also get and set the property values for a device setup class. Use the [**SetupDiGetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551097) and [**SetupDiSetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552135) functions to get and set the property values for a device setup class.

For more information about using the **SetupDi*Xxx*** functions, see [Using Device Installation Functions](https://msdn.microsoft.com/library/windows/hardware/ff553567).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Device%20Object%20Registry%20Properties%20After%20Installation%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


