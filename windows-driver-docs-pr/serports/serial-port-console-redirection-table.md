---
title: Serial Port Console Redirection Table (SPCR)
description: The Serial Port Console Redirection Table that is used to indicate whether a serial port or a non-legacy UART interface is available for use with Microsoft® Windows® Emergency Management Services (EMS). 
ms.assetid: cbcd2e71-881a-44f6-b3d8-5d2aadb02b27
keywords:
- SPCR
- EMS UART
ms.date: 07/23/2018
---

# Serial Port Console Redirection Table  (SPCR)

This document defines the content of the Serial Port Console Redirection Table. This table is used to indicate whether a serial port or a non-legacy UART interface is available for use with Microsoft® Windows® Emergency Management Services (EMS).

The table provides information about the configuration and use of the serial port or non-legacy UART interface. On a system where the BIOS or system firmware uses the serial port for console input/output, this table should be used to convey information about the settings, to ensure a seamless transition between the firmware console output and Windows EMS output.

This table must be located in system memory with other ACPI tables, and it must be referenced in the ACPI RSDT table. 

> Patent Notice:
> Microsoft is making certain patent rights available for implementations of this specification under two options:
> 1)  Microsoft’s Community Promise, available at <http://www.microsoft.com/openspecifications/en/us/programs/community-promise/default.aspx>; or
> 2)  The Open Web Foundation Final Specification Agreement Version 1.0 ("OWF 1.0") as of October 1, 2012, available at http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0. 


| **Field** | **Byte Length** | **Byte Offset** | **Description** | 
|:--|:--|:--|:--|
| Header |  |  |  | 
|     Signature | 4 | 0 | ‘SPCR’. Signature for the Serial Port Console Redirection Table. | 
|     Length | 4 | 4 | Length, in bytes, of the entire Serial Port Console Redirection Table. | 
|     Revision | 1 | 8 | 2 | 
|     Checksum | 1 | 9 | Entire table must sum to zero. | 
|     OEMID | 6 | 10 | OEM ID. | 
|     OEM Table ID | 8 | 16 | For the Serial Port Console Redirection Table, the table ID is the manufacturer model ID. | 
|     OEM Revision | 4 | 24 | OEM revision of Serial Port Console Redirection Table for supplied OEM Table ID. | 
|    Creator ID | 4 | 28 | Vendor ID of utility that created the table. For the DSDT, RSDT, SSDT, and PSDT tables, this is the ID for the ASL Compiler. | 
|    Creator Revision | 4 | 32 | Revision of utility that created the table. For the DSDT, RSDT, SSDT, and PSDT tables, this is the revision for the ASL Compiler. | 
| Interface Type | 1 | 36 | Indicates the type of the register interface: <p> For Revision 1: </p> <ul><li>0 = full 16550 interface </li><li>1 = full 16450 interface (must also accept writing to the 16550 FCR register) </li><li>2-255 = reserved </li></ul><p>For Revision 2: </p>See the Serial Port Subtypes in Table 3 of the [DBG2 Specification](http://go.microsoft.com/fwlink/p/?LinkId=234837) </p>| 
| Reserved | 3 | 37 | Must be 0. | 
| Base Address | 12 | 40|<p>The base address of the Serial Port register set described using the ACPI Generic Address Structure.</p>0 = console redirection disabled <p>**Note:** <p>- COM1 (0x3F8) would be: </p><p>Integer Form: 0x 01 08 00 00 00000000000003F8</p><p>Viewed in Memory: 0x01080000F803000000000000</p><p>COM2 (Ox2F8) would be: </p><p>Integer Form: 0x 01 08 00 00 00000000000002F8</p><p>Viewed in Memory: 0x01080000F802000000000000 </p>|
| Interrupt Type | 1 | 52 | Interrupt type(s) used by the UART. <p>Bit[0] PC-AT-compatible dual-8259 IRQ interrupt</p><p>Bit[1] I/O APIC interrupt (Global System Interrupt)</p><p>Bit[2] I/O SAPIC interrupt (Global System Interrupt)</p> (IRQ) <p>Bit[3] ARMH GIC interrupt (Global System Interrupt)</p><p>Bit[4:7] reserved (must be 0)</p><p>0 = not supported</p><p>1 = supported</p><p>Platforms with both a dual-8259 and an I/O APIC or I/O SAPIC must set the IRQ bit (Bit[0]) and the corresponding Global System Interrupt bit.). E.g. an system that supported 8259 and SAPIC would be 5. </p>|
|IRQ|1|53 | The PC-AT-compatible IRQ used by the UART.<p>2-7, 9-12, 14-15 = valid IRQs respectively</p><p>0-1, 8, 13, 16-255 = reserved</p><p>Valid only if Bit[0] of the Interrupt Type field is set.</p> | 
|Global System Interrupt|4| 54| The Global System Interrupt (GSIV) used by the UART. Not valid if Bit[0] is the only bit set in the Interrupt Type field.|
|Baud Rate|1|58|The baud rate the BIOS used for redirection. <ul><li>0 = as is, operating system relies on the current configuration of serial port until the full featured driver will be initialized.</li><li>3 = 9600</li><li>4 = 19200</li><li>6 = 57600</li><li>7 = 115200</li><li>1-2, 5, 8 - 255 = reserved</li></ul>|
| Parity|1 | 59 | <p>0 = No Parity</p><p>1-255 = reserved</p> | 
| Stop Bits|1 | 60 | <p>0 = Stop bit</p><p>1-255 = reserved</p> | 
| Terminal Type|1|62|The terminal protocol the BIOS was using for console redirection:<ul><li>0 = VT100</li><li>1 = VT100+</li><li>2 = VT-UTF8</li><li>3 = ANSI<li>4-255 = reserved </li></ul>| 
| Reserved | 1 | 63 | Must be 0 | 
| PCI Device ID | 2 | 64 | Must be 0xFFFF if it is not a PCI device | 
| PCI Vendor ID | 2 | 66 | Must be 0xFFFF if it is not a PCI device | 
| PCI Bus Number | 1 | 68 | PCI Bus Number if table describes a PCI device<p>Must be 0x00 if it is not a PCI device</p> | 
| PCI Device Number | 1 | 69 | PCI Slot Number if table describes a PCI device<p>Must be 0x00 if it is not a PCI device</p>| 
| PCI Function Number | 1 | 70 | PCI Function Number if table describes a PCI device<p>Must be 0x00 if it is not a PCI device</p> | 
| PCI Flags | 4 | 71 | PCI Compatibility flags bitmask.  Should be zero by default.<ul><li>Bit[0] = Operating System should NOT suppress PNP device enumeration or disable power management for this device. Must be 0 if it is not a PCI device</li><li>Bits 1-31 = RESERVED, must be zero.</li></ul>| 
| PCI Segment | 1 | 75 | PCI segment number. <p>For systems with fewer than 255 PCI buses, this number must be 0. <p>| 
| Reserved | 4 | 76 | Must be 0 | 

## Revision History

| Date      | Rev  | Description                                                                                                                 |
|:----------|:-----|:----------------------------------------------------------------------------------------------------------------------------|
| 2/15/00   | .10  | Created                                                                                                                     |
| 3/1/00    | .50  | ‘SPCR’. Signature Data added                                                                                                |
| 3/20/00   | .55  | Data revised to include port and irq                                                                                        |
| 3/22/00   | .56  | Clarified port identification Added ability to disable redirection. Added pointer to the Generic Register Address Structure |
| 3/23/00   | .56a | Formatting, disclaimer, copy editing                                                                                        |
| 4/24/00   | .6   | Posted on web for WinHEC                                                                                                    |
| 4/24/00   | .6   | Public review draft published                                                                                               |
| 5/25/00   | .61  | Correction to BASE_ADDRESS description                                                                                      |
| 5/25/00   | .61  | Public review draft published                                                                                               |
| 5/31/00   | .7   | Correction to BASE_ADDRESS description examples. Added 16540 interface                                                      |
| 5/31/00   | .71  | Changed the info on the GRAS from a note to a “\*”                                                                          |
| 5/31/00   | .71  | Public review draft published                                                                                               |
| 6/1/00    | .72  | Changed GRAS COM port examples to be little-endian Added text to the end of the line                                        |
| 7/12/00   | .75  | Fixed IRQ Description. Fixed various format issues Added PCI bus information.                                               |
| 7/26/00   | .76  | Update to PCI field name “Device Number”. Changed intro language to include non-legacy UART.                                |
| 8/10/00   | .77  | Changed interrupt information, adding  APIC and SAPIC Added flow control                                                    |
| 9/22/00   | .78  | Added PCI Segment                                                                                                           |
| 10/25/00  | .80  | Fixed PCI Flags section. Added Terminal Types Added 16450 FCR info                                                          |
| 10/1/01   | .95  | Removed language codes                                                                                                      |
| 1/11/02   | 1.00 | adding updated licensing spec to 1.00                                                                                       |
| 3/12/14   | 1.01 | Released under Microsoft Community Promise                                                                                  |
| 6/2/14    | 1.02 | Changed Table Revision to 2 and added support for additional Interface Types, as defined in the DBG2 specification.         |
| 8/10/15   | 1.03 | Updated patent notice.                                                                                                      |
| 7/23/2018 | 1.04 |                                                                                                                             |

