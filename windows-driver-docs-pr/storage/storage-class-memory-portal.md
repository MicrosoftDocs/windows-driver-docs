---
title: Using _DSM for storage class memory
description: To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (_DSM) that can be used with storage drivers.
ms.date: 11/18/2022
---

# Using _DSM for storage class memory

To support device class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines [Device-Specific Methods (_DSM)](../bringup/acpi-device-specific-methods.md) that can be used with storage drivers.

The [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) is designed to map to the [JEDEC Byte Addressable Energy Backed Interface standard](https://www.jedec.org/document_search?search_api_views_fulltext=jesd245) in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers. An NVDIMM-N that supports the JEDEC Byte Addressable Energy Backed Interface standard has a function class of Byte Addressable Energy Backed (0x1) and a function interface value of 0x1.
