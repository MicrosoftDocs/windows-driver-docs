---
title: Handling a System Set-Power IRP in a Bus Driver
description: Handling a System Set-Power IRP in a Bus Driver
ms.assetid: e88344bd-4223-4cd5-9428-201d46c6dbb4
keywords: ["set-power IRPs WDK power management", "bus drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a System Set-Power IRP in a Bus Driver





When a bus driver receives a system set-power IRP, it must take the following steps:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS. The driver cannot fail a system set-power IRP.

3.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), specifying IO\_NO\_INCREMENT, to complete the IRP.

The bus driver does not change device power settings until it receives a power IRP that requests a device power state.

 

 




