---
title: About Storage Class Memory
description: To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (_DSM) that can be used with storage drivers.
ms.localizationpriority: medium
ms.date: 12/15/2019
---

# About Storage Class Memory

To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (_DSM) that can be used with storage drivers.

The _DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1) is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers. A NVDIMM-N that supports the JEDEC Byte Addressable Energy Backed Interface standard has a function class of Byte Addressable Energy Backed (0x1) and a function interface value of 0x1.

## Related topics

[Storage driver design guide](./index.md)

[_DSM Interface for JEDEC Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)
