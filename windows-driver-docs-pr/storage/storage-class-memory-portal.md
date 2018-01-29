---
title: Storage class memory
description: To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (\_DSM) that can be used with storage drivers.
ms.assetid: e4f354d0-f292-4dc2-a7e3-edd8dfa63b90
---

# Storage class memory


To support device-class-specific communications between the storage driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (\_DSM) that can be used with storage drivers.

The \_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1) is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers.

## <span id="related_topics"></span>Related topics


[Storage driver design guide](http://go.microsoft.com/fwlink/p/?LinkId=798409)

[JEDEC Byte-Addressable Energy-Backed Interface NVDIMM Device-Specific Method (\_DSM)](jedec-byte-addressable-energy-backed-interface-nvdimms-device-specific-method---dsm-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20class%20memory%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





