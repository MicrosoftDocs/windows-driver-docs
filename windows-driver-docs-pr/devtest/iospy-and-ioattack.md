---
title: IoSpy and IoAttack
description: IoSpy and IoAttack
ms.assetid: 4cc5bf5c-f9e4-43d4-8532-dd7813b6f2a0
---

# IoSpy and IoAttack


IoSpy and IoAttack are tools that perform IOCTL and WMI fuzz tests on kernel-mode drivers. By using these tools, you can ensure that drivers' IOCTL and WMI code validate data buffers and buffer lengths correctly. By doing this, you avoid buffer overruns that can lead to system instability.

*Fuzz testing* presents a driver with random data, referred to as *fuzz*, in order to determine defects within the driver. Fuzz testing over an IOCTL or WMI interface is not new. However, most test suites are either generic *black box* fuzz tests, which only verify the external access to a driver's IOCTL or WMI interfaces, or are written to test the specific IOCTL and WMI paths within a driver.

IoSpy and IoAttack use more of a *white box* approach to fuzz testing. When a device is enabled for fuzz testing, IoSpy captures the IOCTL and WMI requests sent to the driver of the device, and records the attributes of these requests within a data file. IoAttack then reads the attributes from this data file, and uses these attributes to *fuzz*, or randomly change, the IOCTL or WMI requests in various ways before sending them to the driver. This allows further entry into the driver's buffer validation code without writing IOCTL- or WMI-specific tests.

IoSpy and IoAttack are supported on systems that run Windows Vista or later versions of the Windows operating system. These tools are included in the WDK as part of the as part of the [Device Fundamentals Tests](device-fundamentals-tests.md), see [Penetration Tests (Device Fundamentals)](coverage-tests--device-fundamentals-.md). You can select these tests from the **Add or Remove Driver tests** dialog box, under Basic\\Device Fundamentals\\Penetration\\IoSpy & Attack folder.

**Important**   IoSpy and IoAttack should be run on test systems that have been previously prepared for kernel-mode debugging.

 

This section includes the following topics:

[IoSpy](iospy.md)

[IoAttack](ioattack.md)

[How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20IoSpy%20and%20IoAttack%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




