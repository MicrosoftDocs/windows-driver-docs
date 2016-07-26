---
title: Physical Configuration of Devices Attached to a Parallel Port
author: windows-driver-content
description: Physical Configuration of Devices Attached to a Parallel Port
MS-HAID:
- 'pcppd\_f41f7a80-ebf1-423d-b29c-a773c8037e3d.xml'
- 'parports.physical\_configuration\_of\_devices\_attached\_to\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ae90fcc6-7ea8-4cb1-89a1-1fbf1ad5c05e
keywords: ["IEEE 1284 WDK", "parallel ports WDK , device configurations", "daisy chain devices WDK", "parallel devices WDK , physical configurations"]
---

# Physical Configuration of Devices Attached to a Parallel Port


## <a href="" id="ddk-physical-configuration-of-devices-attached-to-a-parallel-port-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Physical%20Configuration%20of%20Devices%20Attached%20to%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


