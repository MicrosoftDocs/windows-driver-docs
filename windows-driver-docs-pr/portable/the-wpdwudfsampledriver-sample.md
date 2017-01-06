---
Description: The WpdWudfSampleDriver Sample
MS-HAID: 'wpddk.the\_wpdwudfsampledriver\_sample'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The WpdWudfSampleDriver Sample
---

# The WpdWudfSampleDriver Sample


This section of the WPD driver documentation describes a comprehensive sample driver, WpdWudfSampleDriver, that is included with the Windows Driver Kit (WDK).

The comprehensive WPD sample driver (WpdWudfSampleDriver) demonstrates virtually all aspects of the Microsoft Windows Portable Devides (WPD) device driver interface (DDI). This driver is built as a normal User-Mode Driver Framework (UMDF) driver that also processes the WPD command set. Although this driver does not interact with actual hardware, it simulates communicating with a device that supports phone contacts, pictures, music, and video.

This driver was written in the simplest way to demonstrate concepts. Therefore, the sample driver might perform operations or be structured in a way that are inefficient in a production driver. Additionally, this sample does not use real hardware. Instead, it simulates a device by using data structures in memory. Therefore, the driver might be implemented in a way that is unrealistic for production hardware.

Some of the tasks that are accomplished by the WpdWudfSampleDriver are written for the advanced Windows Portable Devices (WPD) driver developer. These tasks are described in topics later in this section.

## <span id="related_topics"></span>Related topics


[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20WpdWudfSampleDriver%20Sample%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




