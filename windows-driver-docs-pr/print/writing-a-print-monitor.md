---
title: Writing a Print Monitor
description: Writing a Print Monitor
ms.assetid: ca5600fc-9e2c-4735-90c4-9509c31dee29
keywords: ["print spooler customizing WDK , print monitors", "spooler customizing WDK print , print monitors", "customizing print spooler components WDK , print monitors", "print monitors WDK", "writing print monitors", "monitors WDK print", "print monitors WDK , about print monitors"]
---

# Writing a Print Monitor


## <a href="" id="ddk-writing-a-print-monitor-gg"></a>


Print monitors are responsible for directing a print data stream from the print spooler to an appropriate port driver. Two types of print monitors are defined -- [language monitors](language-monitors.md) and [port monitors](port-monitors.md). This section describes both monitor types, and provides design and implementation guidelines.

The following topics are provided:

[Language Monitors](language-monitors.md)

[Port Monitors](port-monitors.md)

[Language and Port Monitor Interaction](language-and-port-monitor-interaction.md)

[Functions Defined by Print Monitors](functions-defined-by-print-monitors.md)

[Initializing a Print Monitor](initializing-a-print-monitor.md)

[Opening and Closing a Port](opening-and-closing-a-port.md)

[Printing a Print Job](printing-a-print-job.md)

[Managing a Port](managing-a-port.md)

[TCPMON Xcv Interface](tcpmon-xcv-interface.md)

[WSDMON Port Monitor](wsdmon-port-monitor.md)

[Converting Print Monitors for Use with Clustered Print Servers](converting-print-monitors-for-use-with-clustered-print-servers.md)

[Installing a Print Monitor](installing-a-print-monitor.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Writing%20a%20Print%20Monitor%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




