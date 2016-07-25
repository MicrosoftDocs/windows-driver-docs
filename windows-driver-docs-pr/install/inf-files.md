---
title: INF Files
description: INF Files
ms.assetid: 8557a072-1b08-41f9-8c35-976a96ff639c
---

# INF Files


Windows uses setup information (INF) files to install the following components for a device:

-   One or more drivers that support the device.

-   Device-specific configuration or settings to bring the device online.

You can use an *INX* file to automatically create an INF file. An INX file is an INF file that contains string variables that represent version information. The Build utility and the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool replace the string variables in INX files with text strings that represent a specific hardware architecture or framework version. For more information about INX files, see [Using INX Files to Create INF Files](https://msdn.microsoft.com/library/windows/hardware/ff545473).

This section includes the following topics:

-   [Overview of INF Files](overview-of-inf-files.md)
-   [Accessing INF Files from a Device Installation Application](accessing-inf-files-from-a-setup-application.md)
-   [Providing Vendor Icons for the Shell and AutoPlay](providing-vendor-icons-for-the-shell-and-autoplay.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




