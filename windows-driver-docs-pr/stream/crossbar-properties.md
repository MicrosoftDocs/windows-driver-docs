---
title: Crossbar Properties
author: windows-driver-content
description: Crossbar Properties
MS-HAID:
- 'vidcapds\_f81ee1be-6afb-49ad-8147-152adb383165.xml'
- 'stream.crossbar\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 41e46d45-90f8-4b0c-ab27-1fec4202b711
keywords: ["crossbar properties WDK video capture", "PROPSETID_VIDCAP_CROSSBAR"]
---

# Crossbar Properties


The [PROPSETID\_VIDCAP\_CROSSBAR](https://msdn.microsoft.com/library/windows/hardware/ff567804) property set contains properties related to the routing of data from video input pins (with corresponding audio, if present) to output pins. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_CROSSBAR property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_CROSSBAR KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CROSSBAR_CAN_ROUTE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565117)</p></td>
<td><p>Returns information on whether a specific routing is possible.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CROSSBAR_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565118)</p></td>
<td><p>Returns the capabilities of the crossbar, including the number of input pins and the number of output pins.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CROSSBAR_PININFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565121)</p></td>
<td><p>Returns the pin information, such as the direction of dataflow, pin medium GUIDs, and pin type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CROSSBAR_ROUTE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565126)</p></td>
<td><p>Controls a specific routing, including which input pin to route to which output pin.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Crossbar%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


