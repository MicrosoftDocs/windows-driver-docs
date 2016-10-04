---
title: Print Ticket Processing in the Print Driver
author: windows-driver-content
description: Print Ticket Processing in the Print Driver
MS-HAID:
- 'drvarch\_321d29d9-4920-4fa6-a8a7-c150aa143ba4.xml'
- 'print.print\_ticket\_processing\_in\_the\_print\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a7295632-0133-4133-b62e-5526dcc12c7d
keywords: ["Print Tickets WDK , print driver processing", "Print Tickets WDK , XPSDrv", "Print Tickets WDK , GDI-based print drivers"]
---

# Print Ticket Processing in the Print Driver


The validated settings in a PrintTicket object are used to configure the print processing that the XPSDrv print driver performs. The components of the print driver, therefore, must read and interpret the settings in the Print Tickets before the driver performs any processing so the driver can process the document according to these settings.

XPSDrv print drivers perform this processing in the print processing filters of the print driver.

GDI-based print drivers continue to use the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure for the settings because of the compatibility support that is built into the Windows Vista print subsystem. For more information about this support, see [Print Ticket Compatibility with Win 32 Applications](print-ticket-compatibility-with-win-32-applications.md).

For more information about implementing Print Ticket processing in the print driver, see [Print Ticket Support in the XPSDrv Render Module](print-ticket-support-in-the-xpsdrv-render-module.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20Processing%20in%20the%20Print%20Driver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


