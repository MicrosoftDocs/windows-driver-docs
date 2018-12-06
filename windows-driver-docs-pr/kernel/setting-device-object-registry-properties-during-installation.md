---
title: Setting Device Object Registry Properties During Installation
description: Setting Device Object Registry Properties During Installation
ms.assetid: 29d40398-09b9-4e64-aa47-da229066bffd
keywords: ["device objects WDK kernel , registry", "registry WDK device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting Device Object Registry Properties During Installation





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

 

 




