---
title: GNSS driver design guide for Windows 10
description: This guide describes the design requirements and architecture of the Universal Windows driver for GNSS (UMDF 2.0), for the converged Windows Location stack in Windows 10.
MS-HAID:
- 'sensors.location\_driver\_design\_guide\_for\_windows\_10'
- 'sensors.gnss\_driver\_design\_guide\_for\_windows\_10'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: FD8503DC-A43F-43B2-A1E9-D80778E326F9
---

# GNSS driver design guide for Windows 10


This guide describes the design requirements and architecture of the Universal Windows driver for GNSS (UMDF 2.0), for the converged Windows Location stack in Windows 10.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[GNSS driver overview](gnss-driver-overview.md)</p></td>
<td><p>Use the GNSS driver design guide to learn how to implement the <strong>DeviceIoControl</strong> APIs with the GNSS driver so that a high level operating system component (HLOS) like the GNSS adapter can access the desired GNSS functionality.</p></td>
</tr>
<tr class="even">
<td><p>[GNSS driver requirements](gnss-driver-requirements.md)</p></td>
<td><p>Describes requirements, assumptions, and constraints to consider when developing a GNSS driver for Windows 10.</p></td>
</tr>
<tr class="odd">
<td><p>[GNSS driver architecture](gnss-driver-architecture.md)</p></td>
<td><p>Provides an overview of GNSS UMDF 2.0 driver architecture, I/O considerations, and discusses several types of tracking and fix sessions.</p></td>
</tr>
<tr class="even">
<td><p>[GNSS driver design](gnss-driver-design.md)</p></td>
<td><p>Discusses design principles to consider when developing a GNSS driver for Windows 10 including data structures, error reporting, and driver versioning.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20GNSS%20driver%20design%20guide%20for%20Windows%2010%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




