---
title: Handling a System Set-Power IRP in a Bus Driver
description: Handling a System Set-Power IRP in a Bus Driver
keywords: ["set-power IRPs WDK power management", "bus drivers WDK power management"]
ms.date: 06/16/2017
---

# Handling a System Set-Power IRP in a Bus Driver





When a bus driver receives a system set-power IRP, it must take the following steps:

1.  Call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp) to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS. The driver cannot fail a system set-power IRP.

3.  Call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest), specifying IO\_NO\_INCREMENT, to complete the IRP.

The bus driver does not change device power settings until it receives a power IRP that requests a device power state.

 

