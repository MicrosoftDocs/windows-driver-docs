---
title: Autoconfiguration in an IHV Port Monitor
description: Autoconfiguration in an IHV Port Monitor
ms.assetid: c41c8502-902a-448c-8f96-fb196e68ee6e
keywords:
- IHV port monitor autoconfiguration WDK printer
- autoconfiguration WDK printer , IHV port monitors
- printer autoconfiguration WDK printer , IHV port monitors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfiguration in an IHV Port Monitor


An IHV who intends to develop a port monitor must design it to support autoconfiguration. To provide support for autoconfiguration in an IHV port monitor, follow these guidelines:

-   Implement the [**SendRecvBidiDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff562071) function and place the address of this function in the **pfnSendRecvBidiDataFromPort** member of the [**MONITOR2**](https://msdn.microsoft.com/library/windows/hardware/ff557532) structure.

-   Support the [bidi communications schema](https://msdn.microsoft.com/library/windows/hardware/ff545175).

-   Support bidi notifications.

An IHV is not required to develop a port monitor if in-box support is sufficient. (For details, see [In-box Support for Autoconfiguration](in-box-support-for-autoconfiguration.md).) Be aware that in-box support is provided only for the standard TCP/IP port monitor and the Web Services for Devices (WSD) port monitor. IHVs who intend to provide autoconfiguration for local printers must provide a port monitor.

 

 




