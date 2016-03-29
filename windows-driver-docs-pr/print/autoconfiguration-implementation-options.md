---
title: Autoconfiguration Implementation Options
description: Autoconfiguration Implementation Options
ms.assetid: 78a4e11c-ee6e-4306-b787-2ff7889ff877
keywords: ["autoconfiguration WDK printer , implementation options", "printer autoconfiguration WDK printer , implementation options"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguration%20Implementation%20Options%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




