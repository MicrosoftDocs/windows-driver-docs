---
title: Debug Port Table 2 (DBG2)
description: The Debug Port ACPI Table is used in platform firmware to describe the debug ports available on the system.
keywords:
- DBG2
- DBGP
- KDCOM
- Serial
- UART
ms.date: 03/22/2023
---

# Microsoft Debug Port Table 2 (DBG2)

This specification defines the format of the Debug Port Table 2 (DBG2), used in platform firmware to describe the debug ports available on the system.
This information applies to the following operating systems: Windows 8 and newer.

References and resources discussed here are listed at the end of this paper.

> Patent Notice:
> Microsoft is making certain patent rights available for implementations of this specification under two options:
>
> 1. Microsoft's Community Promise, available at `https://www.microsoft.com/openspecifications/en/us/programs/community-promise/default.aspx`
> 2. The Open Web Foundation Final Specification Agreement Version 1.0 ("OWF 1.0") as of October 1, 2012, available at `http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0`.

## Document History

| Date | Change |
|------|--------|
| November 29, 2011 | First publication. |
| May 22, 2012 | Updates to Table 3 per final supported platforms for Windows 8. |
| August 10, 2015 | Updated patent notice. |
| October 6, 2015 | Added new serial debugging subtypes (Arm SBSA UART, Arm DCC) |
| December 10, 2015 | Added new serial debugging subtype (BCM2835) |
| May 31, 2017 | Added new serial debugging subtype (i.MX6, Generic Address Structure 16550-compatible) |
| June 11, 2020 | Added new serial debugging subtype (SDM845v2) |
| September 1, 2020 | Converted document to Markdown syntax and formatting changes. |
| September 21, 2020 | Added new serial debugging subtype (IALPSS) |
| February 17, 2021 | Document all known serial debugging subtypes |
| April 10, 2023 | Added new serial debugging subtype (RISC-V) and added clarifying information on 16550-compatible subtypes |

## Introduction

Microsoft requires a debug port on all systems. To describe the debug port(s) available on a platform, Microsoft defines an operating system–specific table (DBG2). This table specifies one or more independent ports for debugging purposes. The presence of a debug port table indicates that the system includes a debug port. The table contains information about the configuration of the debug port. The table is located in system memory with other Advanced Configuration and Power Interface (ACPI) tables, and must be referenced in the ACPI Root System Description Table (RSDT).

The DBG2 table replaces the ACPI Debug Port Table (DBGP) on platforms whose debug port implementations cannot be described using DBGP.

## Debug Port Table 2 (DBG2)

### Table 1. Debug Port Table 2 format

Table 1 defines the fields in DBG2.

| Field | Byte length | Byte offset | Description |
|-------|-------------|-------------|-------------|
| Header |  |  |  |
| Signature | 4 | 0 | 'DBG2'. Signature for Debug Port Table 2. |
| Length | 4 | 4 | Length, in bytes, of the entire Debug Port Table 2. |
| Revision | 1 | 8 | For this version of the specification, this value is 0. |
| Checksum | 1 | 9 | Entire table must sum to zero. |
| OEM ID | 6 | 10 | Original equipment manufacturer (OEM) ID. |
| OEM Table ID | 8 | 16 | For Debug Port Table 2, the table ID is the manufacturer model ID. |
| OEM Revision | 4 | 24 | OEM revision of Debug Port Table 2 for the supplied OEM Table ID. |
| Creator ID | 4 | 28 | Vendor ID of utility that created the table. |
| Creator Revision | 4 | 32 | Revision of utility that created the table. |
| OffsetDbgDeviceInfo | 4 | 36 | Offset, in bytes, from the beginning of this table to the first Debug Device Information structure entry. |
| NumberDbgDeviceInfo | 4 | 40 | Indicates the number of Debug Device Information structure entries. |
| Debug Device Information Structure[NumberDbgDeviceInfo] | Variable | OffsetDbgDeviceInfo | A list of Debug Device Information structures for this platform.  The structure format is defined in the Debug Device Information structure section, later in this document. |

## Debug Device Information structure

### Table 2. Debug Device Information structure format

| Field | Byte length | Byte offset | Description |
|-------|-------------|-------------|-------------|
| Revision | 1 | 0 | Revision of the Debug Device Information structure. For this version of the specification, this must be 0. |
| Length | 2 | 1 | Length, in bytes, of this structure, including NamespaceString and OEMData. |
| NumberofGenericAddressRegisters | 1 | 3 | Number of generic address registers in use. |
| NamespaceStringLength | 2 | 4 | Length, in bytes, of NamespaceString, including NUL characters. |
| NamespaceStringOffset | 2 | 6 | Offset, in bytes, from the beginning of this structure to the field NamespaceString[]. This value must be valid because this string must be present. |
| OemDataLength | 2 | 8 | Length, in bytes, of the OEM data block. |
| OemDataOffset | 2 | 10 | Offset, in bytes, to the field OemData[] from the beginning of this structure. This value will be 0 if no OEM data is present. |
| Port Type | 2 | 12 | Debug port type for this debug device. Each of these values will have a corresponding subtype value as shown in Table 3. |
| Port Subtype | 2 | 14 | Debug port subtype for this debug device.  See Table 3. |
| Reserved | 2 | 16 | Reserved, must be 0. |
| BaseAddressRegisterOffset | 2 | 18 | Offset, in bytes, from beginning of this structure to the field BaseaddressRegister[]. |
| AddressSizeOffset | 2 | 20 | Offset, in bytes, from beginning of this structure to the field AddressSize[]. |
| BaseAddressRegister[] | (NumberofGenericAddressRegisters) * 12 | BaseAddressRegisterOffset | Array of generic addresses. |
| AddressSize[] | (NumberofGenericAddressRegisters) * 4 | AddressSizeOffset | Array of address sizes corresponding to each generic address above. |
| NamespaceString[] | NamespaceStringLength | NamespaceStringOffset | NUL-terminated ASCII string to uniquely identify this device. This string consists of a fully qualified reference to the object that represents this device in the ACPI namespace. If no namespace device exists, NamespaceString[] must only contain a single '.' (ASCII period) character. |
| OemData[] | OemDataLength | OemDataOffset | Optional, variable-length OEM-specific data. |

### Table 3. Debug port types and subtypes

| Port | Type | Subtype | Description |
|------|------|---------|-------------|
| Reserved | 0x0000 – 0x7FFF and 0xFFFF | All | Reserved (Do Not Use) |
| Serial | 0x8000 | 0x0000 | Fully 16550-compatible |
|  |  | 0x0001 | 16550 subset compatible with DBGP Revision 1 |
|  |  | 0x0002 | MAX311xE SPI UART |
|  |  | 0x0003 | Arm PL011 UART |
|  |  | 0x0004 | MSM8x60 (e.g. 8960) |
|  |  | 0x0005 | Nvidia 16550 |
|  |  | 0x0006 | TI OMAP |
|  |  | 0x0007 | Reserved (Do Not Use) |
|  |  | 0x0008 | APM88xxxx |
|  |  | 0x0009 | MSM8974 |
|  |  | 0x000A | SAM5250 |
|  |  | 0x000B | Intel USIF |
|  |  | 0x000C | i.MX 6 |
|  |  | 0x000D | (deprecated) Arm SBSA (2.x only) Generic UART supporting only 32-bit accesses |
|  |  | 0x000E | Arm SBSA Generic UART |
|  |  | 0x000F | Arm DCC |
|  |  | 0x0010 | BCM2835 |
|  |  | 0x0011 | SDM845 with clock rate of 1.8432 MHz |
|  |  | 0x0012 | 16550-compatible with parameters defined in Generic Address Structure |
|  |  | 0x0013 | SDM845 with clock rate of 7.372 MHz |
|  |  | 0x0014 | Intel LPSS |
|  |  | 0x0015 | RISC-V SBI console (any supported SBI mechanism) |
|  |  | 0x0016 – 0xFFFF | Reserved (For Future Use) |
| 1394 | 0x8001 | 0x0000 | IEEE1394 Standard Host Controller Interface |
|  |  | 0x0001 – 0xFFFF | Reserved (For Future Use) |
| USB | 0x8002 | 0x0000 | XHCI-compliant controller with debug interface |
|  |  | 0x0001 | EHCI-compliant controller with debug interface |
|  |  | 0x0002 – 0x0006 | Reserved (Do Not Use) |
|  |  | 0x0007 – 0xFFFF | Reserved (For Future Use) |
| Net | 0x8003 | NNNN | NNNN must be a valid PCI-assigned Vendor ID |
|  | 0x8004 | All | Reserved (Do Not Use) |
| Reserved | 0x8005 – 0xFFFE | All | Reserved (For Future Use) |

### Note on the fields of the Generic Address Structure

- The Generic Address Structure in BaseAddressRegister[0] is used to specify the register bit width and access size used by some serial subtypes.

- The Address Space ID and Register Bit Offset fields must be 0.

- The Register Bit Width field contains the register stride and must be a power of 2 that is at least as large as the access size. On 32-bit platforms this value cannot exceed 32. On 64-bit platforms this value cannot exceed 64.

- The Access Size field is used to determine whether byte, WORD, DWORD, or QWORD accesses are to be used. QWORD accesses are only valid on 64-bit architectures.

### Note on 16550-based UARTs

There are three interface subtypes which can be used for 16550-based UARTs. The differences between them are subtle yet important.

- Interface subtype 0x0 refers to a "legacy" port I/O as seen on x86-based platforms. This type should be avoided on platforms that use memory-mapped I/O, such as ARM or RISC-V.

- Interface subtype 0x1 supports memory mapped UARTs, but only ones that are describable in the DBGP ACPI table. OS implementations may treat this as equivalent to a DBGP-provided debug port and not honor all the fields in the Generic Address Structure.

- Interface subtype 0x12 is the most flexible choice and is recommended when running compatible operating systems on new platforms. This subtype supports all scenarios covered by the subtypes 0x0 and 0x1 as well as new ones, such as those using nontraditional access sizes and bit widths, which can be described in the Generic Address Structure.

## Resources

[ACPI Specification](https://uefi.org/specifications)
