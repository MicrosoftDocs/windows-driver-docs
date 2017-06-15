---
title: Improving System Startup Performance
author: windows-driver-content
description: Improving System Startup Performance
MS-HAID:
- 'PwrMgmt\_83e9db69-37fd-40f4-9d1e-fe2de8f40871.xml'
- 'kernel.improving\_system\_startup\_performance'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9fce451c-73b3-4e3b-875d-319aaa8765ff
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Improving%20System%20Startup%20Performance%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


