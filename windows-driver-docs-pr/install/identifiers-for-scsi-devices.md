---
title: Identifiers for SCSI Devices
description: Identifiers for SCSI Devices
ms.assetid: 8bc68813-5096-40b2-bbd1-0aebb5a3326d
keywords:
- device identification strings WDK , SCSI devices
- identification strings WDK device , SCSI devices
- identifiers WDK device , SCSI devices
- SCSI device identifiers WDK device installations
- device IDs WDK device installations
- hardware IDs WDK device installations
- compatible IDs WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifiers for SCSI Devices





The device ID format for a small computer system interface (SCSI) device is as follows:

SCSI\\t\*v(8)p(16)r(4)

Where:

- *t\** is a device type code of variable length.

- *v(8)* is an 8-character vendor identifier.

- *p(16)* is a 16-character product identifier.

- *r(4)* is a 4-character revision level value.

The bus enumerator determines the device type by indexing an internal string table, using a numerically encoded SCSI device type code, obtained by querying the device, as shown in the following table. The remaining components are just strings returned by the device, but with special characters (including space, comma, and any nonprinting graphic) replaced with an underscore.

The SCSI Port driver currently returns the following device type strings, the first nine of which correspond to standard SCSI type codes.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SCSI Type Code</th>
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
<td align="left"></td>
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
<td align="left"></td>
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
<td align="left"><p>ScsiChanger</p></td>
<td align="left"><p>MediumChangerPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>COMMUNICATION_DEVICE (9)</p></td>
<td align="left"><p>Net</p></td>
<td align="left"><p>ScsiNet</p></td>
<td align="left"><p>CommunicationsPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>ASCIT8</p></td>
<td align="left"><p>ScsiASCIT8</p></td>
<td align="left"><p>ASCPrePressGraphicsPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>11</p></td>
<td align="left"><p>ASCIT8</p></td>
<td align="left"><p>ScsiASCIT8</p></td>
<td align="left"><p>ASCPrePressGraphicsPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>12</p></td>
<td align="left"><p>Array</p></td>
<td align="left"><p>ScsiArray</p></td>
<td align="left"><p>ArrayPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>13</p></td>
<td align="left"><p>Enclosure</p></td>
<td align="left"><p>ScsiEnclosure</p></td>
<td align="left"><p>EnclosurePeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>14</p></td>
<td align="left"><p>RBC</p></td>
<td align="left"><p>ScsiRBC</p></td>
<td align="left"><p>RBCPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>15</p></td>
<td align="left"><p>CardReader</p></td>
<td align="left"><p>ScsiCardReader</p></td>
<td align="left"><p>CardReaderPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>Bridge</p></td>
<td align="left"><p>ScsiBridge</p></td>
<td align="left"><p>BridgePeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>17</p></td>
<td align="left"><p>Other</p></td>
<td align="left"><p>ScsiOther</p></td>
<td align="left"><p>OtherPeripheral</p></td>
</tr>
</tbody>
</table>

 

An example of a device ID for a disk drive would be as follows:

SCSI\\DiskSEAGATE_ST39102LW_______0004

There are four hardware IDs in addition to the device ID:

SCSI\\t\*v(8)p(16)

SCSI\\t\*v(8)

SCSI\\v(8)p(16)r(1)

V(8)p(16)r(1)

In the third and fourth of these additional identifiers, *r(1)* represents just the first character of the revision identifier. These hardware IDs are illustrated by the following examples:

SCSI\\DiskSEAGATE_ST39102LW_______

SCSI\\DiskSEAGATE_

SCSI\\DiskSEAGATE_ST39102LW_______0

SEAGATE_ST39102LW_______0

The SCSI Port driver supplies only one compatible ID, one of the variable-sized generic type codes from the previous table.

For example, the compatible ID for a disk drive is as follows:

GenDisk

The generic identifier is used in INF files for SCSI devices more than any other, because SCSI drivers are typically generic. Be aware that the SCSI Port driver returns no generic name at all for sequential access and "processor" devices.

 

 





