---
title: Identifiers for SCSI Devices
description: Identifiers for SCSI Devices
keywords:
- device identification strings WDK , SCSI devices
- identification strings WDK device , SCSI devices
- identifiers WDK device , SCSI devices
- SCSI device identifiers WDK device installations
- device IDs WDK device installations
- hardware IDs WDK device installations
- compatible IDs WDK device installations
ms.date: 09/01/2020
ms.localizationpriority: medium
---

# Identifiers for SCSI Devices

Starting with Windows 10, Version 2004 (OS build 19041.488 or higher), two additional identifiers are available for NVMe storage disk drives which support the [STOR_RICH_DEVICE_DESCRIPTION](/windows-hardware/drivers/ddi/storport/ns-storport-stor_rich_device_description) structure:

`SCSI\t*v(8)p(40)`

Where:

- t* is a device type code of variable length

- v(8) is an 8-character vendor identifier

- p(40) is a 40-character product identifier

`SCSI\t*v(8)p(40)r(8)`

Where:

- t* is a device type code of variable length

- v(8) is an 8-character vendor identifier

- p(40) is a 40-character product identifier

- r(8) is an 8-character revision level value

In versions of Windows prior to Windows 10, Version 2004 (OS build 19041.488 or higher), the device ID format for a small computer system interface (SCSI) device is as follows:

`SCSI\\t\*v(8)p(16)r(4)`

Where:

- *t\** is a device type code of variable length

- *v(8)* is an 8-character vendor identifier

- *p(16)* is a 16-character product identifier

- *r(4)* is a 4-character revision level value

The bus enumerator determines the device type by indexing an internal string table, using a numerically encoded SCSI device type code, obtained by querying the device, as shown in the following table. The remaining components are just strings returned by the device, but with special characters (including space, comma, and any nonprinting graphic) replaced with an underscore.

The SCSI Port driver currently returns the following device type strings, the first nine of which correspond to standard SCSI type codes.

| SCSI type code | Device type | Generic type | Peripheral ID |
|--|--|--|--|
| DIRECT_ACCESS_DEVICE (0) | Disk | GenDisk | DiskPeripheral |
| SEQUENTIAL_ACCESS_DEVICE (1) | Sequential |  | TapePeripheral |
| PRINTER_DEVICE (2) | Printer | GenPrinter | PrinterPeripheral |
| PROCESSOR_DEVICE (3) | Processor |  | OtherPeripheral |
| WRITE_ONCE_READ_MULTIPLE_DEVICE (4) | Worm | GenWorm | WormPeripheral |
| READ_ONLY_DIRECT_ACCESS_DEVICE (5) | CdRom | GenCdRom | CdRomPeripheral |
| SCANNER_DEVICE (6) | Scanner | GenScanner | ScannerPeripheral |
| OPTICAL_DEVICE (7) | Optical | GenOptical | OpticalDiskPeripheral |
| MEDIUM_CHANGER (8) | Changer | ScsiChanger | MediumChangerPeripheral |
| COMMUNICATION_DEVICE (9) | Net | ScsiNet | CommunicationsPeripheral |
| 10 | ASCIT8 | ScsiASCIT8 | ASCPrePressGraphicsPeripheral |
| 11 | ASCIT8 | ScsiASCIT8 | ASCPrePressGraphicsPeripheral |
| 12 | Array | ScsiArray | ArrayPeripheral |
| 13 | Enclosure | ScsiEnclosure | EnclosurePeripheral |
| 14 | RBC | ScsiRBC | RBCPeripheral |
| 15 | CardReader | ScsiCardReader | CardReaderPeripheral |
| 16 | Bridge | ScsiBridge | BridgePeripheral |
| 17 | Other | ScsiOther | OtherPeripheral |

An example of a device ID for a disk drive would be as follows:

`SCSI\\DiskSEAGATE_ST39102LW_______0004`

There are four hardware IDs in addition to the device ID:

`SCSI\\t\*v(8)p(16)`

`SCSI\\t\*v(8)`

`SCSI\\v(8)p(16)r(1)`

`V(8)p(16)r(1)`

In the third and fourth of these additional identifiers, *r(1)* represents just the first character of the revision identifier. These hardware IDs are illustrated by the following examples:

`SCSI\\DiskSEAGATE_ST39102LW_______`

`SCSI\\DiskSEAGATE_`

`SCSI\\DiskSEAGATE_ST39102LW_______0`

`SEAGATE_ST39102LW_______0`

The SCSI Port driver supplies only one compatible ID, one of the variable-sized generic type codes from the previous table.

For example, the compatible ID for a disk drive is as follows:

`GenDisk`

The generic identifier is used in INF files for SCSI devices more than any other, because SCSI drivers are typically generic.

Be aware that the SCSI Port driver returns no generic name for sequential access and "processor" devices.
