---
title: Storage Filter Driver's Device-Type-Specific Functionality
description: Storage Filter Driver's Device-Type-Specific Functionality
ms.assetid: ecc0d938-e931-46bd-a1e1-0e6da8e149a4
keywords: ["storage filter drivers WDK , device-type-specific functionality", "filter drivers WDK storage , device-type-specific functionality", "SFD WDK storage , device-type-specific functionality", "device-type-specific functionality WDK storage"]
---

# Storage Filter Driver's Device-Type-Specific Functionality


## <span id="ddk_storage_filter_drivers_device_type_specific_functionality_kg"></span><span id="DDK_STORAGE_FILTER_DRIVERS_DEVICE_TYPE_SPECIFIC_FUNCTIONALITY_KG"></span>


Depending on the nature of its device, an storage filter driver (SFD) might be responsible for the following device-type-specific functionality:

-   Translating data from or into a device-specific format before or after sending a transfer request to lower drivers if the device processes data in a nonstandard format

-   Setting up IRPs with SRBs for port-driver-supported I/O control requests, for driver-defined I/O control requests, or for pass-through requests, as necessary for its device, and sending those IRPs to the next-lower driver

-   Modifying class driver-supplied SRBs as necessary for its device

-   Establishing time-out values for requests

-   Supplying one or more [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines and, like the corresponding storage class driver, handling certain error conditions and retries for device-specific requests that require special handling

In general, an SFD has the same responsibilities as a storage class driver for those requests that require device-specific handling. For a discussion of the functionality required of storage class drivers, see [Storage Class Drivers](storage-class-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Filter%20Driver's%20Device-Type-Specific%20Functionality%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




