---
title: Monitoring Driver Verifier
description: Monitoring Driver Verifier
ms.assetid: 58b672b8-66f3-436b-900b-11bb94575fb6
keywords:
- Driver Verifier WDK , monitoring
- Driver Verifier Manager
- Verifier utility
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitoring Driver Verifier


## <span id="ddk_monitoring_driver_verifier_tools"></span><span id="DDK_MONITORING_DRIVER_VERIFIER_TOOLS"></span>


The Verifier utility has several ways to monitor the actions of Driver Verifier and of the drivers being verified.

The kernel debugger extension **!verifier** can also be used to monitor and report on a number of statistics related to Driver Verifier's activities. When verifying graphics drivers, the **!gdikdx.verifier** extension should be used instead. For information about debugger extensions, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

This section includes:

[Monitoring Global Counters](monitoring-global-counters.md)

[Monitoring Individual Counters](monitoring-individual-counters.md)

[Creating Log Files](creating-log-files.md)

 

 





