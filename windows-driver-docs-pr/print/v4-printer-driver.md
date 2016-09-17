---
title: V4 Printer Driver
author: windows-driver-content
description: The v4 printer driver model was designed to address known issues with the version 3 driver model, and thus improve the quality of the experience that users have with their printers.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: CB333340-FBA0-4CB4-BAD6-4673B4AC0DF2
---

# V4 Printer Driver


The v4 printer driver model was designed to address known issues with the version 3 driver model, and thus improve the quality of the experience that users have with their printers.

**Note**  To help to better explain some of the concepts in this section, a fictional company called Fabrikam is used.

 

**Introduction**

The v4 printer driver model is a refinement of the existing v3 printer driver model, and it was designed to improve driver development, reduce IT management costs, and support new scenarios. The v4 print driver model continues to support many familiar technologies like [XPSDrv](xpsdrv-printer-driver.md), [GPD](introduction-to-gpd-files.md), [PPD](pscript-minidrivers.md), [Autoconfiguration](printer-autoconfiguration.md), and [Bidi](bidirectional-communication.md). The v4 print driver model also supports several new extensibility points.

The v4 print driver model is also optimized for several new scenarios including the following:

-   Windows 8 scenarios

    Windows Store apps present new design considerations regarding UI behavior and security context. So a printer driver model was needed that would provide deeply integrated support for this new environment. The v4 print driver model provides the only way for printer manufacturers to provide customized Print Preferences experiences or Printer Notification experiences in Windows Store apps.

-   Printer sharing

    Printer sharing is a key value proposition item for Windows servers. The v4 printer driver model was designed to make sharing easier and more efficient by eliminating the need to manage drivers across processor architectures.

-   Ease of driver development

    The v4 driver has to support existing development efforts from the version 3 printer driver model and from the XPSDrv architecture. And also, the v4 driver must be easier to develop and test.

**High-level Architecture**

The following is a high-level representation of a v4 print driver. With the exception of the rendering filters and user interface applications, all the other functional blocks in the diagram are implemented by Microsoft. V4 print drivers rely heavily on data files and JavaScript for extensibility. The blue boxes represent existing files that were used in the v3 driver model, and the green boxes represent new places to plug in.

![high level representation of v4 print driver](images/v4driverarch.png)

This section discusses the following aspects of the v4 printer driver:

[V4 Printer Driver Rendering](v4-driver-rendering.md)

[V4 Printer Driver Configuration](v4-driver-configuration.md)

[V4 Printer Driver Setup](v4-driver-setup.md)

[V4 Printer Driver User Interfaces](v4-printer-driver-user-interfaces.md)

[V4 Printer Driver Connectivity](v4-printer-driver-connectivity.md)

[Build a v4 Printer Driver in Visual Studio](build-a-v4-print-driver-in-visual-studio.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20V4%20Printer%20Driver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


