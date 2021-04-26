---
title: PortCls D3 Exit Latency Requirement
description: This topic discusses how the Windows port class driver (PortCls) can use a new Windows 8 interface to manipulate the exit latency requirement for the D3 sleep state.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PortCls D3 Exit Latency Requirement


This topic discusses how the Windows port class driver (PortCls) can use a new Windows 8 interface to manipulate the exit latency requirement for the D3 sleep state.

When a system enters a platform power state other than fully working (for example, sleep or connected standby), the required exit latency for the audio adapter to return to D0 (fully working) can be relaxed. This makes it possible for the audio adapter to use sleep states deeper than D3, even if these deeper states could result in longer exit latencies (exit times).

PortCls can now use a new power management interface to generate a new D3 exit latency tolerance, and then communicate it dynamically to the audio miniport driver. These tolerances are represented as [**PC\_EXIT\_LATENCY**](/windows-hardware/drivers/ddi/portcls/ne-portcls-_pc_exit_latency) enumeration values.

For more information about the new power management interface, see [**IAdapterPowerManagement3**](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpowermanagement3)

 

