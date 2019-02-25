---
title: Using Computer Hardware IDs (CHIDs)
description: Computer Hardware IDs (CHIDs) are defined in the Specifying Hardware IDs for a Computer.
ms.assetid: 45DCAED5-8D20-4A31-B316-0460AB030DAD
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Computer Hardware IDs (CHIDs)


Computer Hardware IDs (CHIDs) are defined in the [Specifying Hardware IDs for a Computer](https://msdn.microsoft.com/windows/hardware/drivers/install/specifying-hardware-ids-for-a-computer).

Windows 10 adds several new CHIDs that incorporate Baseboard Manufacturer and Baseboard Product information. These new CHIDs are included in the CHID hierarchy as shown in the table below. The table shows the hierarchy in descending order of specificity. CHIDs that are new to Windows 10 are highlighted in bold.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>HWID</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HardwareID-0</p></td>
<td><p>Manufacturer + Family + Product Name + SKU Number + BIOS Vendor + BIOS Version + BIOS Major Release + BIOS Minor Release</p></td>
</tr>
<tr class="even">
<td><p>HardwareID-1</p></td>
<td><p>Manufacturer + Family + Product Name + BIOS Vendor + BIOS Version + BIOS Major Release + BIOS Minor Release</p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-2</p></td>
<td><p>Manufacturer + Product Name + BIOS Vendor + BIOS Version + BIOS Major Release + BIOS Minor Release</p></td>
</tr>
<tr class="even">
<td><p>HardwareID-3</p></td>
<td><p><strong>Manufacturer + Family + ProductName + SKU Number + Baseboard_Manufacturer + Baseboard_Product</strong></p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-4</p></td>
<td><p>Manufacturer + Family + ProductName + SKU Number</p></td>
</tr>
<tr class="even">
<td><p>HardwareID-5</p></td>
<td><p>Manufacturer + Family + ProductName</p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-6</p></td>
<td><p><strong>Manufacturer + SKU Number + Baseboard_Manufacturer + Baseboard_Product</strong></p></td>
</tr>
<tr class="even">
<td><p>HardwareID-7</p></td>
<td><p>Manufacturer + SKU Number</p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-8</p></td>
<td><p><strong>Manufacturer + ProductName + Baseboard_Manufacturer + Baseboard_Product</strong></p></td>
</tr>
<tr class="even">
<td><p>HardwareID-9</p></td>
<td><p>Manufacturer + ProductName</p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-10</p></td>
<td><p><strong>Manufacturer + Family + Baseboard_Manufacturer + Baseboard_Product</strong></p></td>
</tr>
<tr class="even">
<td><p>HardwareID-11</p></td>
<td><p>Manufacturer + Family</p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-12</p></td>
<td><p>Manufacturer + Enclosure Type</p></td>
</tr>
<tr class="even">
<td><p>HardwareID-13</p></td>
<td><p><strong>Manufacturer + Baseboard_Manufacturer + Baseboard_Product</strong></p></td>
</tr>
<tr class="odd">
<td><p>HardwareID-14</p></td>
<td><p>Manufacturer</p></td>
</tr>
</tbody>
</table>

 

OEMs must provide the correct CHID information to the driver publisher. The [ComputerHardwareIds](https://msdn.microsoft.com/library/windows/hardware/ff543505) tool, included in the Windows Desktop Tools SDK, can help with reporting CHIDs from a known set of System Management BIOS (SMBIOS) values. ComputerHardwareIds performs two different tasks.

1.  Default behavior: The tool reports the system's SMBIOS values and generated CHIDs.

    By default, the tool displays the system’s SMBIOS values, and the CHIDs that are generated from the SMBIOS values.

2.  Simulation behavior: The tool generates CHIDs from user provided SMBIOS values.

    You can run the tool with simulated SMBIOS values (such as manufacturer, family, and SKU) to get a list of generated CHIDs. This allows you to determine which CHIDs would be generated on a system with specific SMBIOS data values.

## <span id="Tips_for_consistent_CHIDs"></span><span id="tips_for_consistent_chids"></span><span id="TIPS_FOR_CONSISTENT_CHIDS"></span>Tips for consistent CHIDs


CHIDs are generated based on case sensitive SMBIOS values. Care must be taken to ensure that systems do not mix cases in SMBIOS text values. Similarly, UNICODE characters are not specially treated. Upper and lower case versions of special characters, such as the Turkish dotted and un-dotted letter I, are treated uniquely: I, ı, İ and i are not the same.

The ComputerHardwareIds tool only computes CHIDs that have the necessary SMBIOS values available. If an SMBIOS data field is missing (or it is null), then any related CHIDs are not generated. For example, if the SMBIOS SKU field is null, then CHIDs 0, 3, 4 6 and 7 will not be available for that particular system.

For more information about CHIDs, see [Specifying Hardware IDs for a Computer](https://docs.microsoft.com/windows-hardware/drivers/install/specifying-hardware-ids-for-a-computer).

 

 





