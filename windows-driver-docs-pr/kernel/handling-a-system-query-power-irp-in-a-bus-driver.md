---
title: Handling a System Query-Power IRP in a Bus Driver
description: Handling a System Query-Power IRP in a Bus Driver
ms.assetid: d42c268e-d57d-41a6-8e61-67c651082106
keywords: ["query-power IRPs WDK power management", "bus drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a System Query-Power IRP in a Bus Driver





When a system query-power request reaches a bus driver (that is not the power policy owner for a device), the driver ensures that it can support a device power state that corresponds to the queried system power state and, if wake-up is enabled, that the queried system power state would not prevent its device from waking the system.

In Windows 7 and Windows Vista, the bus driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS if the driver can change to the specified power state or sets a failure status if the driver cannot.

In Windows Server 2003, Windows XP, and Windows 2000, the bus driver first calls [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) and then sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS if the driver can change to the specified power state or sets a failure status if the driver cannot.

After the bus driver completes the IRP, the power manager calls [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines set by other drivers as they passed the IRP down the stack.

 

 




