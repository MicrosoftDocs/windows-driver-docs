---
title: No Valid Drivers found after Scan Stage
description: No Valid Drivers found after Scan Stage
ms.assetid: aaf4f39b-82ab-40c3-ac49-5a20c8796051
---

# No Valid Drivers found after Scan Stage


This error indicates a general failure to verify the driver. SDV reports this error in the following situations:

-   SDV reports this error when it cannot interpret the driver code, typically because a driver is not WDM-compliant or KMDF-compliant or it is not written in C. For more information, see [Supported Drivers](supported-drivers.md).

-   SDV reports this error when it is not run in the correct build configuration or platform, or if, for some other reason, SDV did not find or did not compile and build the driver's source files.

-   SDV reports this error when it cannot detect any entry points in the driver. To verify that SDV found the entry points that the driver supports, see the [Sdv-map.h](sdv-map-h.md). For information, see [Scanning the Driver](scanning-the-driver.md).

To identify the problem, verify that you have selected the correct build configuration and platform for your driver.

Next, to confirm that the driver compiles and builds correctly. Next, correct any compiler errors and run SDV again.

For information about the Build and Scan steps, see [Verification Process](verification-process.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20No%20Valid%20Drivers%20found%20after%20Scan%20Stage%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




