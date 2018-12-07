---
title: Improving System Startup Performance
description: Improving System Startup Performance
ms.assetid: 9fce451c-73b3-4e3b-875d-319aaa8765ff
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Improving System Startup Performance


One of the features that computer users most frequently request is fast startup times from power-off, standby, and hibernation states. To reduce the startup time, Windows uses a number of techniques, which include the following:

-   Remove, from the list of startup operations, processes and services that can be deferred until after startup completes.

-   Prefetch memory pages according to the pattern of requests to load these pages in previous system startups.

-   Overlap device initialization with the disk I/O operations that are required to load the operating system.

-   Enable device initializations to be performed in parallel instead of sequentially.

A kernel-mode driver should take the following steps to improve the performance of the startup process:

-   When a computer starts up from a power-off state (cold startup), the device driver should do only what is required to initialize the device and defer all other device operations until startup is complete. Limit your driver's initialization code to the operations that are required to make the device ready to use.

-   When a computer starts up from the standby or hibernation state (warm startup), a driver that must be initialized before startup completes should use high-priority worker threads and critical queue work items to offload any small tasks that it requires. Otherwise, the driver thread might be starved for processor time by unrelated threads, and startup will be delayed.

-   During a warm startup from standby or hibernation, a driver's DPC routine, or initialization code that runs at DISPATCH\_LEVEL, should avoid long execution times that block other drivers from running. For more information, see [Sharing Processor Resources During Startup from a Low-Power State](sharing-processor-resources-during-startup-from-a-low-power-state.md).

-   During a warm startup from standby or hibernation, a functional device driver should complete an S0 set-power IRP immediately, and then request a D0 set-power IRP. If your driver promptly completes the S0 set-power IRP, the operating system can finish startup while your driver reinitializes the device as a background task. For more information, see [Fast Startup from a Low-Power State](fast-startup-from-a-low-power-state.md).

-   A device driver should not hold a spin lock for more than a brief time, especially during a cold startup from a power-off state. Otherwise, other device initializations cannot occur in parallel.

This section includes the following topics:

[Sharing Processor Resources During Startup from a Low-Power State](sharing-processor-resources-during-startup-from-a-low-power-state.md)

[Fast Startup from a Low-Power State](fast-startup-from-a-low-power-state.md)

 

 




