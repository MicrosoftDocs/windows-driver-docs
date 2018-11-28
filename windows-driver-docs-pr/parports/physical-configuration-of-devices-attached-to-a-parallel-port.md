---
title: Physical Configuration of Devices Attached to a Parallel Port
description: Physical Configuration of Devices Attached to a Parallel Port
ms.assetid: ae90fcc6-7ea8-4cb1-89a1-1fbf1ad5c05e
keywords:
- IEEE 1284 WDK
- parallel ports WDK , device configurations
- daisy chain devices WDK
- parallel devices WDK , physical configurations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Physical Configuration of Devices Attached to a Parallel Port





This section describes the typical physical configurations of devices that are attached to a parallel port.

The following figure shows a parallel device attached a parallel port.

![diagram illustrating a parallel device connected to a parallel port](images/parport2.png)

Microsoft Windows supports one parallel device attached to a parallel port, which can be a legacy device or a Plug and Play device that complies with the IEEE 1284 standard.

The following figure shows IEEE 1284.3 devices and an end-of-chain IEEE 1284 device that are simultaneously attached to a parallel port.

![ieee 1284.3 daisy chain devices connected to a parallel port](images/parport3.png)

The IEEE 1284.3 standard specifies that up to four daisy chain devices and an end-of-chain device can be simultaneously attached to a parallel port.

The following table specifies the number of IEEE 1284.3 devices that are supported by each version of Windows.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Windows version</th>
<th>Maximum number of daisy chain devices</th>
<th>IEEE 1284.3 device IDs</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Windows Me</p></td>
<td><p>zero</p></td>
<td><p>N/A</p></td>
<td><p>Not supported by system-supplied drivers.</p></td>
</tr>
<tr class="even">
<td><p>Windows 2000</p></td>
<td><p>four</p></td>
<td><p>from 0 through 3</p></td>
<td><p>To ensure reliable operation, Microsoft recommends at most two devices.</p></td>
</tr>
<tr class="odd">
<td><p>Windows XP and later</p></td>
<td><p>two</p></td>
<td><p>0 or 1</p></td>
<td></td>
</tr>
</tbody>
</table>

 

For more information about supporting IEEE 1284.3 devices, see:

[Parallel Device Interfaces, Internal Names, and Symbolic Links](parallel-device-interfaces--internal-names--and-symbolic-links.md)

[Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port](selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parallel-p.md)

 

 




