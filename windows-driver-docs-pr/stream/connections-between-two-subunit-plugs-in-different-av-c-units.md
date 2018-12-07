---
title: Connections Between Two Subunit Plugs in Different AV/C Units
description: Connections Between Two Subunit Plugs in Different AV/C Units
ms.assetid: 20d209b3-2516-4913-9f31-b14afddb78fb
keywords:
- connections WDK AV/C
- AV/C WDK , connection scenarios
- AVCCONNECTINFO
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




