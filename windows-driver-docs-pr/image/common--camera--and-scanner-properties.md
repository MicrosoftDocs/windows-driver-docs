---
title: Common, Camera, and Scanner Properties
description: Common, Camera, and Scanner Properties
ms.assetid: 7d988a1b-4c2f-43f7-be09-a250d9ede35c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Common, Camera, and Scanner Properties





WIA properties are attributes of either a device (the root) or an item (a child). Device properties contain information about the device, such as the manufacturer's name, a description of the device, and its type (scanner or camera). Item properties contain information about a particular item, such as the item's name, when it was captured, and so on. Device properties are identified by the WIA\_D naming convention; item properties are identified by the WIA\_I naming convention.

The three-letter acronym in the middle of a WIA property name contains information about the type of property: whether it is a generic device information property (DIP), a device property (DPA, DPC, or DPS), or an item property (IPA, IPC, or IPS). Device and item properties can be common to both types of devices (DPA and IPA), can be specific to cameras (DPC or IPC), or can be specific to scanners (DPS and IPS). The following table lists the various WIA property types and gives examples of each type.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_DIP_<em>Xxx</em></p></td>
<td><p>Device Information Property</p>
<p>Setup and installation information common to both scanner and camera devices. The WIA service provides these properties. A minidriver does not provide them.</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPA_<em>Xxx</em></p></td>
<td><p>Device Property, All</p>
<p>Information that is common to both scanner and camera devices, such as connection status and device time.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_<em>Xxx</em></p></td>
<td><p>Item Property, All</p>
<p>Information that is common to both camera and scanner items, such as the item&#39;s name and the type of image.</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPC_<em>Xxx</em></p></td>
<td><p>Device Property, Camera</p>
<p>Information that is specific to camera devices, such as the number of pictures taken.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPC_<em>Xxx</em></p></td>
<td><p>Item Property, Camera</p>
<p>Information that is specific to camera items, such as width and height of thumbnail images.</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_<em>Xxx</em></p></td>
<td><p>Device Property, Scanner</p>
<p>Information that is specific to scanner devices, such as bed size.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_<em>Xxx</em></p></td>
<td><p>Item Property, Scanner</p>
<p>Information that it is specific to scanner items, such as horizontal and vertical resolution.</p></td>
</tr>
</tbody>
</table>

 

See [WIA Properties](https://msdn.microsoft.com/library/windows/hardware/ff552739) for a complete list of WIA common, camera-specific, and scanner-specific properties.

 

 




