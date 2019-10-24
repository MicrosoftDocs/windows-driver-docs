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

-   Implement the [**SendRecvBidiDataFromPort**](https://docs.microsoft.com/previous-versions/ff562071(v=vs.85)) function and place the address of this function in the **pfnSendRecvBidiDataFromPort** member of the [**MONITOR2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/winsplp/ns-winsplp-_monitor2) structure.

-   Support the [bidi communications schema](https://docs.microsoft.com/windows-hardware/drivers/print/bidi-communications-schema-reference).

-   Support bidi notifications.

An IHV is not required to develop a port monitor if in-box support is sufficient. (For details, see [In-box Support for Autoconfiguration](in-box-support-for-autoconfiguration.md).) Be aware that in-box support is provided only for the standard TCP/IP port monitor and the Web Services for Devices (WSD) port monitor. IHVs who intend to provide autoconfiguration for local printers must provide a port monitor.

 

 




