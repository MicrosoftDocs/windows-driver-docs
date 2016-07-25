---
title: Driver Store
description: Driver Store
ms.assetid: 17abe3a4-0663-4b8b-8072-2171b4cedbe4
---

# Driver Store


Starting with Windows Vista, the driver store is a trusted collection of inbox and third-party [driver packages](driver-packages.md). The operating system maintains this collection in a secure location on the local hard disk. Only the driver packages in the driver store can be installed for a device.

When a driver package is copied to the driver store, all of its files are copied. This includes the [INF file](overview-of-inf-files.md) and all files that are referenced by the INF file. All files that are in the driver package are considered critical to the device installation. The INF file must reference all of the required files for device installation so that they are present in the driver store. If the INF file references a file that is not included in the driver package, the driver package is not copied to the store.

The process of copying a driver package to the driver store is called *staging*. A driver package must be *staged* to the driver store before the package can be used to install any devices. As a result, driver staging and device installation are separate operations.

A driver package is staged to the driver store by being verified and validated:

-   Verifying the [driver package](driver-packages.md) integrity.

    Software integrity has become a top priority for IHVs and OEMs. Concerned by the increase in malicious software on the Internet, these customers want to be sure that their software has not been tampered with or corrupted.

    Before a driver package is copied to the driver store, the operating system first verifies that the digital signature is correct. For more information about digital signatures, see [Driver Signing](driver-signing.md).

-   Validating the [driver package](driver-packages.md).

    The operating system validates the driver package in the following ways:

    -   The current user must have permission to install the driver package.
    -   The [INF file](overview-of-inf-files.md) of the driver package is syntactically correct, and all files referenced by the INF files are present in the driver package.

After a driver package has passed integrity and syntax checks, it is copied to the driver store. Afterwards, the operating system uses the driver package to automatically install new devices without requiring user interaction.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Driver%20Store%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




