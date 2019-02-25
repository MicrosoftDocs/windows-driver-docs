---
title: Identifiers for IDE Devices
description: Identifiers for IDE Devices
ms.assetid: b1624eb9-afa7-49ce-9db1-b0eab466ddcd
keywords:
- device identification strings WDK , IDE devices
- identification strings WDK device , IDE devices
- identifiers WDK device , IDE devices
- IDE device identifiers WDK device installations
- device IDs WDK device installations
- hardware IDs WDK device installations
- compatible IDs WDK device installations
- integrated device electronics identifiers WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifiers for IDE Devices





Identifiers for integrated device electronics (IDE) devices resemble SCSI identifiers. The device ID format is as follows:

IDE\\t\*v(40)r(8)

Where:

- *t\** is a device-type code of variable length.

- *v(40)* is a string that contains the vendor name, an underscore, vendor's product name, and enough underscores to bring the total to 40 characters.

- *r(8)* is an 8-character revision number.

There are three hardware IDs, in addition to the device ID:

IDE\\v(40)r(8)

IDE\\t\*v(40)

V(40)r(8)

As in the SCSI case, there is only one compatible ID, a generic type name similar to the standard SCSI type names supplied by the SCSI Port driver, but having only eleven entries instead of eighteen. The generic device-type names for IDE devices are as follows:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IDE Type Code</th>
<th align="left">Device Type</th>
<th align="left">Generic Type</th>
<th align="left">Peripheral ID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DIRECT_ACCESS_DEVICE (0)</p></td>
<td align="left"><p>Disk</p></td>
<td align="left"><p>GenDisk</p></td>
<td align="left"><p>DiskPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>SEQUENTIAL_ACCESS_DEVICE (1)</p></td>
<td align="left"><p>Sequential</p></td>
<td align="left"><p>GenSequential</p></td>
<td align="left"><p>TapePeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PRINTER_DEVICE (2)</p></td>
<td align="left"><p>Printer</p></td>
<td align="left"><p>GenPrinter</p></td>
<td align="left"><p>PrinterPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>PROCESSOR_DEVICE (3)</p></td>
<td align="left"><p>Processor</p></td>
<td align="left"><p>GenProcessor</p></td>
<td align="left"><p>OtherPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WRITE_ONCE_READ_MULTIPLE_DEVICE (4)</p></td>
<td align="left"><p>Worm</p></td>
<td align="left"><p>GenWorm</p></td>
<td align="left"><p>WormPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>READ_ONLY_DIRECT_ACCESS_DEVICE (5)</p></td>
<td align="left"><p>CdRom</p></td>
<td align="left"><p>GenCdRom</p></td>
<td align="left"><p>CdRomPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCANNER_DEVICE (6)</p></td>
<td align="left"><p>Scanner</p></td>
<td align="left"><p>GenScanner</p></td>
<td align="left"><p>ScannerPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>OPTICAL_DEVICE (7)</p></td>
<td align="left"><p>Optical</p></td>
<td align="left"><p>GenOptical</p></td>
<td align="left"><p>OpticalDiskPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MEDIUM_CHANGER (8)</p></td>
<td align="left"><p>Changer</p></td>
<td align="left"><p>GenChanger</p></td>
<td align="left"><p>MediumChangerPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>COMMUNICATION_DEVICE (9)</p></td>
<td align="left"><p>Net</p></td>
<td align="left"><p>GenNet</p></td>
<td align="left"><p>CommunicationsPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>Other</p></td>
<td align="left"><p>GenOther</p></td>
<td align="left"><p>OtherPeripheral</p></td>
</tr>
</tbody>
</table>

 

For IDE changer devices, the generic type name is **GenChanger** instead of **ScsiChanger** and for communication devices the generic type name is **GenNet** instead of **ScsiNet**. The SCSI Port driver returns no generic name at all for sequential access and "processor" devices, whereas the IDE bus driver returns **GenSequential** and **GenProcessor**. Also, the IDE bus driver returns only ten generic types, whereas the SCSI Port driver currently returns eighteen. In other respects, the generic names returned by the IDE bus driver are the same as those returned by the SCSI Port driver.

The compatible ID for an IDE tape drive is as follows:

GenSequential

In the special case of an LS-120 device, the IDE bus driver returns the following compatible ID:

GenSFloppy

The following shows the kind of identifiers that can be generated for an IDE hard disk drive:

IDE\\DiskMaxtor_91000D8_____________________SASX1B18

IDE\\Maxtor_91000D8___________________________SASX1B18

IDE\\DiskMaxtor_91000D8________________________

Maxtor_91000D8__________________________SASX1B18

GenDisk

 

 





