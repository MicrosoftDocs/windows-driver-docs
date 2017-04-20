---
title: Connections Between Two Subunit Plugs Within One AV/C Unit
author: windows-driver-content
description: Provides information about connections between two subunit plugs within one AV/C unit
ms.assetid: 2acd5f23-89b6-40f9-9154-22f1bb51d08c
keywords: ["connections WDK AV/C", "AV/C WDK , connection scenarios", "AVCCONNECTINFO"]
---

# Connections Between Two Subunit Plugs Within One AV/C Unit


Scenarios 3 and 4 represent connections between a subunit and another subunit in the same unit.

### **Scenario 3**

Connect from a specific source plug (0x0 to 0x1E), or any available source plug (0xFF) of another subunit in the same unit, to the local subunit's destination plug, as the following figure shows.

![diagram illustrating a connection where the local pin’s dataflow member is kspin\-dataflow\-in](images/avc-ccm3.gif)

Scenario 3 describes a connection where the local pin's **DataFlow** member is KSPIN\_DATAFLOW\_IN.

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
<td><p>Not used because the source unit's device identifier is the unit that contains the subunit</p></td>
<td><p>Subunit address</p></td>
<td><p>Destination plug (0x0 to 0x1E, or 0xFF)</p></td>
<td><p>N/A</p></td>
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
<td><p>Not used because this scenario does not involve another unit</p></td>
<td><p>Self</p></td>
<td><p>Destination Plug (0xFF)</p></td>
<td><p>N/A</p></td>
</tr>
</tbody>
</table>

 

### **Scenario 4**

Connect from the local subunit's source plug to a specific destination plug (0x0 to 0x1E), or any available (0xFF) destination plug of another subunit, as the following figure shows. Scenario 4 represents the opposite of scenario 3.

![diagram illustrating a connection where the local pin’s dataflow member is kspin\-dataflow\-out](images/avc-ccm4.gif)

Scenario 4 describes a connection where the local pin's **DataFlow** member is KSPIN\_DATAFLOW\_OUT.

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
<td><p>Not used because the source unit's device identifier is the unit that contains the subunit</p></td>
<td><p>Self (same subunit)</p></td>
<td><p>Source plug (0xFF)</p></td>
<td><p>N/A</p></td>
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
<td><p>Not used because this scenario does not involve another unit</p></td>
<td><p>Subunit Address</p></td>
<td><p>Destination plug (0x0 to 0x1E, or 0xFF)</p></td>
<td><p>N/A</p></td>
</tr>
</tbody>
</table>

 

The following list describes the meaning of values that appear in the preceding tables:

-   The values 0x0 to 0x1E (30 decimal) represent specific plug numbers.

-   The value 0xFF represents any available subunit source or destination plug address.

-   "Self" contains the pin to which the AVCCONNECTINFO structure is setting.

-   The values in the **DeviceID** columns (for source and destination subunit plugs) are used to search for the physical device object (PDO) of the target AV/C device to issue AV/C CCM commands to.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Connections%20Between%20Two%20Subunit%20Plugs%20Within%20One%20AV/C%20Unit%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


