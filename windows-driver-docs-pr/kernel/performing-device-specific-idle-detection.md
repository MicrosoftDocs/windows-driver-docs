---
title: Performing Device-Specific Idle Detection
description: Performing Device-Specific Idle Detection
ms.assetid: 1a4e3b66-f1dc-4dc8-af8b-ed8138270c3c
keywords: ["idle detection WDK power management", "device-specific idle detection WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Performing Device-Specific Idle Detection





Instead of using the power manager's idle detection routines, a driver can perform its own idle detection based on device-specific criteria.

Such a driver should put its idle device in the lowest possible sleep state that is valid for the current system power state. To do so, the driver requests a power IRP ([**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)) with minor IRP code [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744), specifying the device power state to which the device should transition.

 

 




