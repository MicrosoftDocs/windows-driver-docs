---
title: Combined Language and Port Monitor
description: Combined Language and Port Monitor
keywords:
- print monitors WDK , language monitors
- print monitors WDK , port monitors
- language monitors WDK print , port monitor interaction
- port monitors WDK print , language monitor interaction
- combined language and port monitors WDK
ms.date: 04/20/2017
---

# Combined Language and Port Monitor





Specialized printer hardware can be supported by a single customized print monitor that acts as a combined language and port monitor. If such a monitor requires user interaction to obtain configuration parameters, it must be divided into a UI DLL and a server DLL, following the model for [port monitors](port-monitors.md). Language-related functionality belongs in the server DLL.

A combined monitor's UI DLL must define [port monitor client DLL functions](port-monitor-client-dll-functions.md). Its server DLL must define both [port monitor server DLL functions](port-monitor-server-dll-functions.md) and [language monitor functions](language-monitor-functions.md).

 

 




