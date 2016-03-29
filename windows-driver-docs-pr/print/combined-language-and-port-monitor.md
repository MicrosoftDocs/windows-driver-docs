---
title: Combined Language and Port Monitor
description: Combined Language and Port Monitor
ms.assetid: 5da362cf-92b8-4c78-80b2-57106b978600
keywords: ["print monitors WDK , language monitors", "print monitors WDK , port monitors", "language monitors WDK print , port monitor interaction", "port monitors WDK print , language monitor interaction", "combined language and port monitors WDK"]
---

# Combined Language and Port Monitor


## <a href="" id="ddk-combined-language-and-port-monitor-gg"></a>


Specialized printer hardware can be supported by a single customized print monitor that acts as a combined language and port monitor. If such a monitor requires user interaction to obtain configuration parameters, it must be divided into a UI DLL and a server DLL, following the model for [port monitors](port-monitors.md). Language-related functionality belongs in the server DLL.

A combined monitor's UI DLL must define [port monitor client DLL functions](port-monitor-client-dll-functions.md). Its server DLL must define both [port monitor server DLL functions](port-monitor-server-dll-functions.md) and [language monitor functions](language-monitor-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Combined%20Language%20and%20Port%20Monitor%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




