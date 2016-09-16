---
title: XPSDrv Driver Requirements
author: windows-driver-content
description: XPSDrv Driver Requirements
MS-HAID:
- 'xpsconfig\_c7e22628-e6ea-416f-8e20-f4cf5df6eef1.xml'
- 'print.xpsdrv\_driver\_requirements'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 382b53eb-a69a-452a-8403-876640a9129e
keywords: ["Version 3 XPS drivers WDK XPSDrv , requirements"]
---

# XPSDrv Driver Requirements


For in-box and the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), the XPSDrv configuration module must meet the following requirements:

-   The XPSDrv printer driver must implement a Version 3 print driver configuration module.

-   The configuration module must support all PrintTicket and PrintCapabilities functionality. The Windows Vista version of the Unidrv and Pscript5 printer drivers provide this support automatically. For more information about how to add this support to monolithic, GDI-based version 3 printer drivers, see [Adding Print Ticket Support to Monolithic Print Drivers](adding-print-ticket-support-to-monolithic-print-drivers.md).

For the complete list of configuration module requirements, see [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Driver%20Requirements%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


