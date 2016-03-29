---
title: Web Services Device Installation
description: Web Services Device Installation
ms.assetid: fb5f043b-bae5-4cb6-95c0-e4e6b9e9d187
keywords: ["Web Services Device Monitor WDK printer"]
---

# Web Services Device Installation


Networked printers that are enabled for Web Services for Devices (WSD) can be discovered and installed by using the [WSDMON Port Monitor](wsdmon-port-monitor.md). This port monitor is new for Windows Vista.

The WSD Port Monitor automatically discovers WSD printers based on Function Discovery notifications. Options for using WSD to install printers include:

-   Provide standard PnP drivers. The PnP discovery provider that Function Discovery provides will expose WSD devices through the Function Discovery API.

-   Create a service provider to expose new functionality for function instances through the Function Discovery API.

For more information about installing and configuring WSD-enabled devices, see the Microsoft Windows SDK documentation for the [Function Discovery API](http://go.microsoft.com/fwlink/p/?linkid=195380).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Web%20Services%20Device%20Installation%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




