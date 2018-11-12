---
title: Storage class memory
description: To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (\_DSM) that can be used with storage drivers.
ms.assetid: e4f354d0-f292-4dc2-a7e3-edd8dfa63b90
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Storage class memory


To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (\_DSM) that can be used with storage drivers.

The \_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1) is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers.

## <span id="related_topics"></span>Related topics


[Storage driver design guide](http://go.microsoft.com/fwlink/p/?LinkId=798409)

[JEDEC Byte-Addressable Energy-Backed Interface NVDIMM Device-Specific Method (\_DSM)](jedec-byte-addressable-energy-backed-interface-nvdimms-device-specific-method---dsm-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






