---
title: Error Source Control
author: windows-driver-content
description: Error Source Control
MS-HAID:
- 'whea\_675d7659-b616-4163-a450-48ea93f8fb14.xml'
- 'whea.error\_source\_control'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f73d9006-a7e7-4a0d-9654-004f53286743
keywords: ["Windows Hardware Error Architecture WDK , error source control", "WHEA WDK , error source control", "hardware errors WDK WHEA , error source control", "errors WDK WHEA , error source control", "platform-specific hardware error driver plug-ins WDK WHEA , error source control", "PSHED plug-ins WDK WHEA , error source control", "error source control WDK WHEA"]
---

# Error Source Control


The PSHED exposes an interface to the operating system that allows the Windows kernel to control each of the error sources that are implemented by the hardware platform. Error source control operations include the following:

-   Enabling or disabling an error source.

-   Setting or clearing mask bits that are associated with an error source. These mask bits enable or disable specific behaviors of the error source.

-   Setting severity bits that are associated with an error source. These severity bits control the severity level at which particular hardware errors are reported to the operating system.

-   Setting threshold parameters that are associated with an error source.

The Windows kernel calls into the PSHED to configure an error source in response to an error source control request by a WHEA management application. The PSHED supports error source control operations for the standard error sources that the PSHED discovers. If a PSHED plug-in is implemented that participates in [error source discovery](error-source-discovery.md) and reports additional error sources to the operating system that the PSHED does not support, the PSHED plug-in must also participate in error source control to support the error source control operations for these additional error sources. A PSHED plug-in can also optionally participate in error source control to override the way that the PSHED controls one or more of the standard error sources.

For more information about how to implement a PSHED plug-in that participates in error source control, see [Participating in Error Source Control](participating-in-error-source-control.md).

User-mode management applications control the error sources by calling the [WHEA Management API](https://msdn.microsoft.com/library/windows/hardware/ff560556). For more information about how to implement WHEA management applications, see [WHEA Management Applications](whea-management-applications.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Error%20Source%20Control%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


