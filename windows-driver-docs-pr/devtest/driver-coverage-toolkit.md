---
title: Driver Coverage Toolkit
description: The Driver Coverage toolkit monitors and reports on the various I/O request packets (IRPs) that enter or leave a driver stack for specified devices.
ms.assetid: b35ca87e-9ec7-4e25-89ce-0e7c121f6445
---

# Driver Coverage Toolkit


The Driver Coverage toolkit monitors and reports on the various I/O request packets (IRPs) that enter or leave a driver stack for specified devices. The data from the Driver Coverage toolkit can help identify coverage weaknesses during driver test and verification.

**Note**  The Driver Coverage Toolkit is no longer needed in Windows 10 and the installer is no longer included in the WDK. To perform tasks described here in Windows 10, instead use [Driver Verifier](driver-verifier.md) and [IRP Logging](irp-logging.md).

 

The Driver Coverage toolkit is included in the Windows Driver Kit (WDK) and is run from Visual Studio as part of the [Device Fundamentals Tests](device-fundamentals-tests.md).

The Driver Coverage toolkit consists of the following tools:

-   The [Driver Coverage filter driver](driver-coverage-filter-driver.md) (Drvcov.sys), which monitors IRP requests into and out of the driver stack for one or more specified devices.

-   The driver coverage tools are available as part of the [Device Fundamentals Tests](device-fundamentals-tests.md), see [Coverage Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md). You can use these tools to enable or disable IRP coverage on specified devices, as well as produce reports from the coverage data.

You can install and run the Driver Coverage toolkit on a test computer without much impact. These tools do not modify IRP requests or inject additional IRPs into a driver stack for a device. These tools simply collect data on every IRP that enters or leaves a device driver.

The Driver Coverage toolkit is supported on systems that run Windows Vista and later versions of Windows.

This section contains the following topics:

[Overview of the Driver Coverage Toolkit](overview-of-the-driver-coverage-toolkit.md)

[Driver Coverage Filter Driver](driver-coverage-filter-driver.md)

[How to Collect IRP Coverage Data](how-to-collect-irp-coverage-data.md)

[How to Analyze IRP Coverage Data](how-to-analyze-irp-coverage-data.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20Coverage%20Toolkit%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




