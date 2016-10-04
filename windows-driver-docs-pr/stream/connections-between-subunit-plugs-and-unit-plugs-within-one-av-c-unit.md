---
title: Connections Between Subunit Plugs and Unit Plugs Within One AV/C Unit
author: windows-driver-content
description: Connections Between Subunit Plugs and Unit Plugs Within One AV/C Unit
MS-HAID:
- 'AVCguide\_d4b8b022-b3c0-49cd-8853-eae09b41fe7b.xml'
- 'stream.connections\_between\_subunit\_plugs\_and\_unit\_plugs\_within\_one\_av\_c\_unit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 12132a0c-9657-4cff-a582-8404a103c46a
keywords: ["connections WDK AV/C", "AV/C WDK , connection scenarios", "AVCCONNECTINFO"]
---

# Connections Between Subunit Plugs and Unit Plugs Within One AV/C Unit


Scenarios 1 and 2 represent connections between a subunit and the unit that contains the subunit.

### **Scenario 1**

Connect the local subunit's source plug to the unit's isochronous output plug, as the following figure shows.

This scenario is the type of connection that was originally supported in *Avc.sys*.

![diagram illustrating a connection where the local pin’s dataflow member is kspin\-dataflow\-in](images/avc-ccm1.gif)

Scenario 1 describes a connection where the local pin's **DataFlow** member is KSPIN\_DATAFLOW\_IN.

Each column in the following table corresponds to a member of the [**AVCCONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554101) structure and specifies values for these members for a source subunit plug.

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
<td><p>0xFF (the unit that contains the subunit)</p></td>
<td><p>iPlug (0x0 to 0x1E or 0x7F)</p></td>
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
<td><p>Destination plug (0x0 to 0x1E)</p></td>
<td><p>N/A</p></td>
</tr>
</tbody>
</table>

 

### **Scenario 2**

Connect from the unit's isochronous input plug to the local subunit's destination plug, as the following figure shows.

![diagram illustrating a connection where the local pin’s dataflow member is kspin\-dataflow\-out](images/avc-ccm2.gif)

Scenario 2 describes a connection where the local pin's **DataFlow** member is KSPIN\_DATAFLOW\_OUT.

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
<td><p>Not used because source unit's device identifier is the unit that contains the subunit</p></td>
<td><p>Subunit address</p></td>
<td><p>Source plug (0x0 to 0x1E)</p></td>
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
<td><p>0xFF (the unit containing the subunit)</p></td>
<td><p>oPCR (0x0 to 0x1E, or 0x7F)</p></td>
<td><p>N/A</p></td>
</tr>
</tbody>
</table>

 

The following list describes the meaning of values that appear in the preceding tables:

-   The values 0x0 to 0x1E (30 decimal) represent specific plug numbers.

-   The value 0x7F represents any available isochronous input or output plug number on the AV/C unit.

-   The value 0xFF represents any available subunit source or destination plug address.

-   The values in the **DeviceID** columns (for source and destination subunit plugs) are used to search for the physical device object (PDO) of the target AV/C device to issue AV/C CCM commands to.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Connections%20Between%20Subunit%20Plugs%20and%20Unit%20Plugs%20Within%20One%20AV/C%20Unit%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


