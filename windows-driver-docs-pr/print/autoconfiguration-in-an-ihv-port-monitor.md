---
title: Autoconfiguration in an IHV Port Monitor
author: windows-driver-content
description: Autoconfiguration in an IHV Port Monitor
MS-HAID:
- 'autocfg\_99a4d1c6-e6b1-41d3-a270-638deb6666ec.xml'
- 'print.autoconfiguration\_in\_an\_ihv\_port\_monitor'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c41c8502-902a-448c-8f96-fb196e68ee6e
keywords: ["IHV port monitor autoconfiguration WDK printer", "autoconfiguration WDK printer , IHV port monitors", "printer autoconfiguration WDK printer , IHV port monitors"]
---

# Autoconfiguration in an IHV Port Monitor


An IHV who intends to develop a port monitor must design it to support autoconfiguration. To provide support for autoconfiguration in an IHV port monitor, follow these guidelines:

-   Implement the [**SendRecvBidiDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff562071) function and place the address of this function in the **pfnSendRecvBidiDataFromPort** member of the [**MONITOR2**](https://msdn.microsoft.com/library/windows/hardware/ff557532) structure.

-   Support the [bidi communications schema](https://msdn.microsoft.com/library/windows/hardware/ff545175).

-   Support bidi notifications.

An IHV is not required to develop a port monitor if in-box support is sufficient. (For details, see [In-box Support for Autoconfiguration](in-box-support-for-autoconfiguration.md).) Be aware that in-box support is provided only for the standard TCP/IP port monitor and the Web Services for Devices (WSD) port monitor. IHVs who intend to provide autoconfiguration for local printers must provide a port monitor.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguration%20in%20an%20IHV%20Port%20Monitor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


