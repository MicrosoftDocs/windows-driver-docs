---
title: DeviceD1 and DeviceD2
description: DeviceD1 and DeviceD2
keywords: ["DeviceD1", "DeviceD2"]
ms.date: 06/16/2017
---

# DeviceD1 and DeviceD2





The **DeviceD1** and **DeviceD2** members of [**DEVICE\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) indicate whether the device hardware supports these device power states. Each is a single bit, which is set if the device supports the state and is clear if the device does not support the state. The operating system assumes that all devices support the D0 and D3 [device power states](device-power-states.md).

 

