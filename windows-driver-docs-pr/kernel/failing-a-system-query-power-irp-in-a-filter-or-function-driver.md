---
title: Failing a System Query-Power IRP in a Filter or Function Driver
description: Failing a System Query-Power IRP in a Filter or Function Driver
ms.assetid: 7c4ceb8e-94f4-4ff7-9d45-1094e9a861fd
keywords: ["query-power IRPs WDK power management", "filter drivers WDK power management", "function drivers WDK power management", "failing query-power IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failing a System Query-Power IRP in a Filter or Function Driver





A filter or function driver (that is not the power policy owner for a device) can fail an [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) request if either of the following is true:

-   The device is enabled for wake-up and the requested system power state is less powered than the value of [**SystemWake**](systemwake.md), which specifies the least-powered state from which the device can wake the system. For example, a device that can wake the system from S2 but not from S3 would fail a query for S3 but succeed a query for S2.

-   Entering a device power state that corresponds to the requested state would force the driver to abandon an operation that would lose data, such as an open modem connection. A driver rarely will fail a query for this reason; under most circumstances, the application handles such cases.

To fail an **IRP\_MN\_QUERY\_POWER** request for a system power state, a driver should take the following steps:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to indicate that the driver is prepared to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only)

2.  Set **Irp-&gt;IoStatus.Status** to a failure status and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), specifying IO\_NO\_INCREMENT. Do not pass the IRP further down the device stack.

3.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) to release the previously acquired lock.

4.  Return a failure status from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

 

 




