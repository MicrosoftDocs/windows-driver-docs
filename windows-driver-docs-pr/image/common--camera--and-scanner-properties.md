---
title: Common, Camera, and Scanner Properties
author: windows-driver-content
description: Common, Camera, and Scanner Properties
ms.assetid: 7d988a1b-4c2f-43f7-be09-a250d9ede35c
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Common, Camera, and Scanner Properties


## <a href="" id="ddk-common-camera-and-scanner-properties-si"></a>


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
<p>Information that is common to both camera and scanner items, such as the item's name and the type of image.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Common,%20Camera,%20and%20Scanner%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


