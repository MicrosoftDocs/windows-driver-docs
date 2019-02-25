---
title: Autoconfiguration Implementation Options
description: Autoconfiguration Implementation Options
ms.assetid: 78a4e11c-ee6e-4306-b787-2ff7889ff877
keywords:
- autoconfiguration WDK printer , implementation options
- printer autoconfiguration WDK printer , implementation options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfiguration Implementation Options


Printer vendors are not required to provide support for autoconfiguration. Microsoft will not modify existing in-box drivers, but IHVs are encouraged to update their drivers for Windows Vista and to include support for autoconfiguration.

For IHVs who choose to support autoconfiguration, drivers and related software must satisfy specific requirements, whether or not this software ships in-box with Windows.

The requirements for supporting autoconfiguration depend on how the printer driver is implemented--either as a printer minidriver or as a monolithic printer driver--and whether a custom port monitor is included.

<a href="" id="minidriver-implementation--custom-extensions-to-a-microsoft-printer-class-driver-or-a-microsoft-port-monitor-"></a>Minidriver implementation (custom extensions to a Microsoft printer class driver or a Microsoft port monitor)  
See [In-Box Support for Autoconfiguration](in-box-support-for-autoconfiguration.md)

<a href="" id="monolithic-implementation--standalone-printer-driver-"></a>Monolithic implementation (standalone printer driver)  
See [Autoconfiguration in an IHV Driver](autoconfiguration-in-an-ihv-driver.md)

<a href="" id="custom-port-monitor"></a>Custom port monitor  
See [Autoconfiguration in an IHV Port Monitor](autoconfiguration-in-an-ihv-port-monitor.md)

**Note**   "Microsoft printer class driver" refers to the Unidrv-based or Pscript5-based printer driver. "Microsoft port monitor" refers to the standard TCP/IP port monitor or the Web Services for Devices (WSD) port monitor.

 

 

 




