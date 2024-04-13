---
title: Reporting Device Power Capabilities
description: Reporting Device Power Capabilities
keywords: ["reporting device power capabilities", "device power capabilities WDK kernel", "DEVICE_CAPABILITIES structure", "query-capabilities IRPs WDK power management", "IRPs WDK power management", "I/O request packets WDK power management"]
ms.date: 06/16/2017
---

# Reporting Device Power Capabilities





During enumeration, drivers report device-specific information in response to a PnP [**IRP\_MN\_QUERY\_CAPABILITIES**](./irp-mn-query-capabilities.md) request. Along with other such information, drivers report a device's power management capabilities in the [**DEVICE\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure. Typically, the bus driver fills in this structure.

Higher-level drivers should set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for the query-capabilities IRP so that they can make a local copy of the structure and ensure that it contains appropriate values. As a general rule, higher-level drivers should not change these values. However, if a change is necessary, a driver can further restrict device capabilities but cannot add to them. In other words, a driver can make the rules more restrictive but cannot loosen them.

After the IRP is complete and all drivers' completion routines have been run, the structure is cached and a driver cannot change its contents.

The following members of the **DEVICE\_CAPABILITIES** structure pertain to power management:

[DeviceD1 and DeviceD2](deviced1-and-deviced2.md)

[WakeFromD0, WakeFromD1, WakeFromD2, and WakeFromD3](wakefromd0--wakefromd1--wakefromd2--and-wakefromd3.md)

[DeviceState](devicestate.md)

[SystemWake](systemwake.md)

[DeviceWake](devicewake.md)

[D1Latency, D2Latency, and D3Latency](d1latency--d2latency--and-d3latency.md)

 

