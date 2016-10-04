---
title: Connections Between Two Subunit Plugs in Different AV/C Units
author: windows-driver-content
description: Connections Between Two Subunit Plugs in Different AV/C Units
MS-HAID:
- 'AVCguide\_82d6c1a5-bf64-4de7-8164-dfe063fa7791.xml'
- 'stream.connections\_between\_two\_subunit\_plugs\_in\_different\_av\_c\_units'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 20d209b3-2516-4913-9f31-b14afddb78fb
keywords: ["connections WDK AV/C", "AV/C WDK , connection scenarios", "AVCCONNECTINFO"]
---

# Connections Between Two Subunit Plugs in Different AV/C Units


Scenarios 5 and 6 represent connections between a subunit in one unit to a subunit in a different unit. These types of connections require the **Signal source** and **Input select** CCM commands.

### <a href="" id="scenario-5"></a> Scenario 5

**Signal source**: The target unit connects to a specific subunit source plug (0x0 to 0x1E), or any available subunit source plug (0xFF), to a specific unit isochronous output plug, or any available unit isochronous output plug (and returns the unit's isochronous output plug number).

**Input select**: The local unit connects from the target subunit's source plug to any of the local unit's isochronous input plugs and then connects to any available subunit destination plug.

![scenario 5 subunit connections](images/avc-ccm5.gif)

Scenario 5 describes a connection where the local pin's **DataFlow** member is KSPIN\_DATAFLOW\_IN.

Each column in the following table corresponds to a member of the [**AVCCONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554101) structure and specifies values for these members for the source subunit plug.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>DeviceID</th>
<th>SubunitAddress</th>
<th>SubunitPlugNumber</th>
<th>UnitPlugNumber (for isochronous output)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Target</p></td>
<td><p>Subunit address</p></td>
<td><p>Source plug (0x0 to 0x1E, or 0xFF)</p></td>
<td><p>0x0 to 0x1E, or 0x7F</p></td>
</tr>
</tbody>
</table>

 

Each column in the following table corresponds to a member of the AVCCONNECTINFO structure and specifies values for these members for a destination subunit plug.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>DeviceID</th>
<th>SubunitAddress</th>
<th>SubunitPlugNumber</th>
<th>UnitPlugNumber (for isochronous input)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Self</p></td>
<td><p>Self</p></td>
<td><p>Destination plug (0xFF)</p></td>
<td><p>0x7F</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="scenario-6"></a> Scenario 6

**Signal source**: The local unit connects to any available (0xFF) subunit source plug to any of the local unit's isochronous output plugs (and returns the unit's isochronous output plug number).

**Input select**: The target unit connects from the local unit's specific isochronous output plug (returned in signal source CCM command) to a specific (0x0 to 0x1E) or any available (0x7F) isochronous input plug on the target unit and then connects to a specific (0x0 to 0x1E) or any available (0xFF) subunit destination plug in target unit (this scenario is the opposite of scenario 5).

![scenario 6 subunit connections](images/avc-ccm6.gif)

Scenario 6 describes a connection where the local pin's **DataFlow** member is KSPIN\_DATAFLOW\_OUT.

Each column in the following table corresponds to a member of the AVCCONNECTINFO structure and specifies values for these members for a source subunit plug.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>DeviceID</th>
<th>SubunitAddress</th>
<th>SubunitPlugNumber</th>
<th>UnitPlugNumber (for isochronous output)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Self</p></td>
<td><p>Self</p></td>
<td><p>Source plug (0xFF)</p></td>
<td><p>0x7F</p></td>
</tr>
</tbody>
</table>

 

Each column in the following table corresponds to a member of the AVCCONNECTINFO structure and specifies values for these members for a destination subunit plug.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>DeviceID</th>
<th>SubunitAddress</th>
<th>SubunitPlugNumber</th>
<th>UnitPlugNumber (for isochronous input)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Target</p></td>
<td><p>Subunit Address</p></td>
<td><p>Destination plug (0x0 to 0x1E)</p></td>
<td><p>0x0 to 0x1E, or 0x7F</p></td>
</tr>
</tbody>
</table>

 

The following list describes the meaning of values that appear in the preceding tables :

-   The values 0x0 to 0x1E (30 decimal) represent specific plug numbers.

-   The value 0x7F represents any available isochronous input or output plug number on the AV/C unit.

-   The value 0xFF represents any available subunit source or destination plug address.

-   "Self" contains the pin to which the AVCCONNECTINFO structure is setting. "Target" represents the data that the AVCCONNECTINFO structure is for.

-   The values in the **Device ID** columns (for source and destination subunit plugs) are used to search for the physical device object (PDO) of the target AV/C device to issue AV/C CCM commands to.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Connections%20Between%20Two%20Subunit%20Plugs%20in%20Different%20AV/C%20Units%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


