---
title: Query Implemented Functions (Function Index 0)
description: This function returns the functions supported by this interface version.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Query Implemented Functions (Function Index 0)


This function returns the functions supported by this interface version. Function 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For the definition of Function 0, see section 9.14.1, "\_DSM (Device Specific Method)" in the [ACPI 6.0 specification](https://uefi.org/specifications).

## Arguments (ARG 3)


None.

## Returns


This function returns an ACPI Buffer containing the following byte values in order: 0xFF, 0xFF, 0xFF, & 0xFF.

## Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

