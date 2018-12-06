---
title: PortCls D3 Exit Latency Requirement
description: This topic discusses how the Windows port class driver (PortCls) can use a new Windows 8 interface to manipulate the exit latency requirement for the D3 sleep state.
ms.assetid: 3CEFF85B-5A2E-4F85-BCAC-00F1773A8F4D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PortCls D3 Exit Latency Requirement


This topic discusses how the Windows port class driver (PortCls) can use a new Windows 8 interface to manipulate the exit latency requirement for the D3 sleep state.

When a system enters a platform power state other than fully working (for example, sleep or connected standby), the required exit latency for the audio adapter to return to D0 (fully working) can be relaxed. This makes it possible for the audio adapter to use sleep states deeper than D3, even if these deeper states could result in longer exit latencies (exit times).

PortCls can now use a new power management interface to generate a new D3 exit latency tolerance, and then communicate it dynamically to the audio miniport driver. These tolerances are represented as [**PC\_EXIT\_LATENCY**](https://msdn.microsoft.com/library/windows/hardware/dn265130) enumeration values.

For more information about the new power management interface, see [**IAdapterPowerManagement3**](https://msdn.microsoft.com/library/windows/hardware/jj200330)

 

 




