---
title: Performing Device-Specific Idle Detection
description: Performing Device-Specific Idle Detection
keywords: ["idle detection WDK power management", "device-specific idle detection WDK power management"]
ms.date: 06/16/2017
---

# Performing Device-Specific Idle Detection





Instead of using the power manager's idle detection routines, a driver can perform its own idle detection based on device-specific criteria.

Such a driver should put its idle device in the lowest possible sleep state that is valid for the current system power state. To do so, the driver requests a power IRP ([**PoRequestPowerIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp)) with minor IRP code [**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md), specifying the device power state to which the device should transition.

 

