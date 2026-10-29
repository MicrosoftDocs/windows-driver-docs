---
title: ACPI RMEM Table
description: Learn about the RMEM Revision 1 ACPI table format, firmware publication, and validation of reserved-memory diagnostic information.
keywords:
- ACPI
- RMEM
- reserved memory
- firmware
ms.date: 10/20/2026
ms.topic: reference
ai-usage: ai-assisted
---

# Reserved-Memory Reporting (RMEM) Table

The Reserved-Memory Reporting (RMEM) table is an Advanced Configuration and Power Interface (ACPI) table published by platform firmware. It describes firmware-reserved physical-memory ranges to help diagnostic applications explain why some installed memory is unavailable to the operating system. Each entry reports the reservation's size, purpose category, attributes, and optional diagnostic label. Firmware can redact a physical address while retaining size and purpose information.

Firmware developers can use the Revision 1 format and producer requirements to construct RMEM tables. Diagnostic application developers can use the retrieval and validation guidance to interpret them. Windows applications retrieve firmware-published tables through the existing [**GetSystemFirmwareTable**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable) API; no RMEM-specific Windows change is required.

## RMEM purpose, scope, and unsupported uses

Firmware can reserve memory for security services, shared buffers, graphics, AI accelerators, firmware runtime functions, and other platform purposes. The Unified Extensible Firmware Interface (UEFI) memory map describes memory types and attributes, but it doesn't provide a uniform purpose category and diagnostic label for each reservation.

RMEM supplements that information so diagnostic tools can:

- Explain differences between physically installed and operating-system-visible memory.
- Attribute reservations to platform functions.
- Investigate unexpectedly large reservations.
- Compare reservation behavior across firmware configurations.

RMEM is diagnostic metadata. Publishing an entry doesn't reserve memory, change the system memory map, transfer ownership, or grant access to a reported range. Existing platform mechanisms remain responsible for reservation and access control.

Only report installed physical memory whose reservation is known from an authoritative platform source. A gap in the UEFI memory map isn't sufficient evidence of a reservation. Don't use RMEM to report device MMIO, uninstalled address space, alignment holes, or ordinary usable memory.

## RMEM table format

Revision 1 consists of a 36-byte standard ACPI description header, a 4-byte RMEM header extension, and a packed array of 48-byte entries. All offsets and lengths in the following tables are in bytes. Multibyte integers use little-endian byte order.

## RMEM Revision 1 table header

| Field | Byte length | Byte offset | Description |
| --- | ---: | ---: | --- |
| Signature | 4 | 0 | ASCII signature `RMEM`. |
| Length | 4 | 4 | Length of the complete table, including all entries. |
| Revision | 1 | 8 | `1` for the format described in this article. |
| Checksum | 1 | 9 | Makes the sum of all bytes in the complete table zero modulo 256. |
| OEM ID | 6 | 10 | OEM identifier, following the standard ACPI header conventions. |
| OEM Table ID | 8 | 16 | OEM table identifier, following the standard ACPI header conventions. |
| OEM Revision | 4 | 24 | OEM revision, following the standard ACPI header conventions. |
| Creator ID | 4 | 28 | Creator identifier, following the standard ACPI header conventions. |
| Creator Revision | 4 | 32 | Creator revision, following the standard ACPI header conventions. |
| EntryCount | 2 | 36 | Number of RMEM entries. |
| EntryOffset | 2 | 38 | Offset from the table start to the first entry. Must be `40` for Revision 1. |
| Entries | 48 * EntryCount | 40 | Packed array of Revision 1 entries. |

For Revision 1, the total length is:

```text
Length = EntryOffset + (48 * EntryCount)
EntryOffset = 40
```

The entry array starts at an 8-byte-aligned offset from the table base. The Project Mu RMEM publisher and its accompanying PowerShell validation example limit the table to 64 entries. Firmware should omit the table when it has no reservations to report.

## RMEM Revision 1 entry format

Offsets in this table are relative to the start of an entry.

| Field | Byte length | Byte offset | Description |
| --- | ---: | ---: | --- |
| Base | 8 | 0 | Physical address of the first byte of the reservation, or zero when Address Hidden is set. |
| Size | 8 | 8 | Reservation size in bytes. Must be nonzero. |
| Category | 2 | 16 | Purpose category from the category table. |
| Flags | 2 | 18 | Entry attributes. |
| Label | 28 | 20 | Optional null-terminated, zero-padded ASCII diagnostic label. |

The actual base address and size must be aligned to 4 KiB. The last byte of the range, `Base + Size - 1`, must be representable in the platform's physical-address space without arithmetic overflow. Firmware validates the actual address before applying address redaction.

The label can contain up to 27 ASCII characters followed by a null terminator. An absent label consists of 28 zero bytes. Set all bytes after the first null terminator to zero. A label is descriptive text, not a stable identifier for ownership, access control, or programmatic policy.

## RMEM Revision 1 categories

| Value | Category | Intended use |
| ---: | --- | --- |
| 0 | Unknown | Invalid sentinel for missing or uninitialized values. Must not appear in a valid entry. |
| 1 | Security | Isolated execution, security processors, or protected services. |
| 2 | SharedMemory | Memory shared across firmware execution environments. |
| 3 | DisplayFramebuffer | Pre-OS or persistent display framebuffer memory. |
| 4 | GpuReserved | Memory reserved for graphics use. |
| 5 | AiAcceleratorReserved | Memory reserved for AI acceleration. |
| 6 | FirmwareRuntime | Runtime data, services, or crash diagnostics. |
| 7 | Other | A reservation that doesn't fit another category. |

The Project Mu RMEM reference implementation accepts categories 1 through 7. Its `RmemCategoryMax` value is an exclusive implementation bound, not a serialized category.

## RMEM Revision 1 flags

| Bits | Attribute | Meaning |
| ---: | --- | --- |
| 0 | Address Hidden | The physical base address is intentionally redacted. |
| 1-15 | Not defined | Must be zero. |

When Address Hidden is clear, `Base` identifies the first physical byte of the range.

When Address Hidden is set:

- The serialized `Base` must be zero.
- `Size`, `Category`, and `Label` remain available for diagnostic reporting.
- Firmware must validate alignment, address limits, arithmetic, and overlap using the actual address.
- Consumers must treat the address as unavailable, not as a reservation beginning at physical address zero.

## Firmware production and publication

Use one owning producer and one reporting path for each reservation. Entries must not overlap, including exact duplicates. Adjacent ranges don't overlap.

The Project Mu reference implementation supports two producer paths:

- **Pre-DXE:** Platform or silicon code creates one `RMEM_HOB_RECORD` GUID HOB for each reservation known before DXE.
- **DXE:** A producer locates `EDKII_RMEM_REGISTRATION_PROTOCOL` and calls `AddReservedRange()` for a reservation allocated, discovered, or finalized during DXE.

Both paths provide the actual physical address, including for address-hidden reservations. The publisher copies the label during registration.

The common `RmemAcpiDxe` driver:

1. Initializes the platform physical-address limit from the CPU HOB.
2. Imports and validates RMEM GUID HOB records.
3. Installs the registration protocol and accepts DXE registrations until `ReadyToBoot`.
4. Applies the same range and conflict validation to both producer paths.
5. Freezes registration at `ReadyToBoot`.
6. Serializes the entries, redacts hidden addresses, calculates the checksum, and installs one RMEM table through the ACPI table protocol.

The publisher rejects invalid registrations and continues publishing accepted entries. It rejects registration after finalization. Missing or invalid CPU address-width information prevents the publisher from starting.

These HOB and protocol interfaces describe the reference firmware implementation; they aren't additional fields in the ACPI table.

## Windows retrieval and consumer validation

Windows desktop applications can retrieve ACPI tables through [**GetSystemFirmwareTable**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable). Use the ACPI provider and the table identifier corresponding to `RMEM`. Follow the API's little-endian table-identifier convention: a C/C++ multicharacter literal for this identifier is `'MEMR'`.

Query the required buffer size, allocate a suitable buffer, retrieve the table, and check the returned size before parsing. Handle a missing table or retrieval failure explicitly. RMEM availability depends on the currently booted firmware publishing the table.

Treat retrieved bytes as untrusted input. For the Revision 1 format and Project Mu RMEM validation policy described here:

1. Require at least 40 bytes before reading the RMEM header extension.
2. Validate the `RMEM` signature, revision 1, and complete-table checksum.
3. Require `EntryOffset` to equal 40 and `EntryCount` to be no greater than 64.
4. Use checked arithmetic to calculate `EntryOffset + (48 * EntryCount)`. Require it to match both the header length and the retrieved table length.
5. Validate category values and reject undefined flag bits.
6. Validate nonzero size, 4-KiB alignment, and visible-address arithmetic. Require a hidden entry's serialized base to be zero.
7. Validate label termination and the ASCII, zero-padding requirements before using labels.
8. Reject overlaps among entries whose actual addresses are available.
9. Reject unsupported table revisions instead of interpreting them as Revision 1.

A consumer can't independently check overlap or actual address-width limits for an entry whose address is hidden. Firmware remains responsible for these checks before redaction. Never read physical memory merely because an RMEM entry describes a range.

The [Project Mu RMEM documentation](https://github.com/microsoft/mu_basecore/blob/587366f707e8a15d4b5bec9aaea759b558486705/MdeModulePkg/Universal/Acpi/RmemAcpiDxe/ReadMe.md#windows-powershell-retrieval) includes a PowerShell retrieval and diagnostic example.

## RMEM security and privacy considerations

RMEM exposes reservation sizes, categories, labels, and, unless hidden, physical addresses to software that can retrieve the table. Address redaction doesn't conceal the reservation's existence, size, category, or label.

Don't put secrets, product codenames, unique device information, or memory contents in a label. Register entries only from authoritative firmware sources. Don't use RMEM as the sole basis for memory ownership or access-control decisions.

## Related topics

- [ACPI system description tables](/windows-hardware/drivers/bringup/acpi-system-description-tables)
- [GetSystemFirmwareTable](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable)
- [Project Mu RMEM structure definitions](https://github.com/microsoft/mu_basecore/blob/587366f707e8a15d4b5bec9aaea759b558486705/MdeModulePkg/Include/Guid/ReservedMemoryReportingTable.h)
