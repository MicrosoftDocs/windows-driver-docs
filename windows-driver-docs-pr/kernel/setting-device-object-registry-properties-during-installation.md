---
title: Setting Device Object Registry Properties During Installation
author: windows-driver-content
description: Setting Device Object Registry Properties During Installation
MS-HAID:
- 'DevObjts\_1709912f-b4e9-49e7-a140-d3034a345329.xml'
- 'kernel.setting\_device\_object\_registry\_properties\_during\_installation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 29d40398-09b9-4e64-aa47-da229066bffd
keywords: ["device objects WDK kernel , registry", "registry WDK device objects"]
---

# Setting Device Object Registry Properties During Installation


## <a href="" id="ddk-setting-device-object-registry-properties-during-installation-kg"></a>


To set device object properties during installation, you must provide an INF file that specifies the properties. You can specify device object properties for either a device, or a device setup class.

These are specified as follows.

-   For an individual device, properties are set in the *add-registry-section* for the device. The INF **AddReg** directive within the device's *DDInstall*.HW section specifies the *add-registry-section* for the device.

-   For a device setup class, properties are set in the *add-registry-section* for the device setup class. The INF **AddReg** directive within the **ClassInstall32** section for the class specifies the *add-registry-section* for the class.

Within an *add-registry-section*, the following keywords can be used to specify the individual device object property to set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyword</th>
<th>Device object property</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DeviceType</strong></p></td>
<td><p>Device type</p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceCharacteristics</strong></p></td>
<td><p>Device characteristics</p></td>
</tr>
<tr class="odd">
<td><p><strong>Exclusive</strong></p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="even">
<td><p><strong>Security</strong></p></td>
<td><p>Security descriptor</p></td>
</tr>
</tbody>
</table>

 

For more information about using these keywords, see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

The settings can be set by a user-mode component by using the device installation functions. For more information, see [Setting Device Object Registry Properties After Installation](setting-device-object-registry-properties-after-installation.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Device%20Object%20Registry%20Properties%20During%20Installation%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


