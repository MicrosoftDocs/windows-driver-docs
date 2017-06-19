---
title: Failing a System Query-Power IRP in a Filter or Function Driver
author: windows-driver-content
description: Failing a System Query-Power IRP in a Filter or Function Driver
ms.assetid: 7c4ceb8e-94f4-4ff7-9d45-1094e9a861fd
keywords: ["query-power IRPs WDK power management", "filter drivers WDK power management", "function drivers WDK power management", "failing query-power IRPs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Failing a System Query-Power IRP in a Filter or Function Driver


## <a href="" id="ddk-failing-a-system-query-power-irp-in-a-filter-or-function-driver-kg"></a>


A filter or function driver (that is not the power policy owner for a device) can fail an [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) request if either of the following is true:

-   The device is enabled for wake-up and the requested system power state is less powered than the value of [**SystemWake**](systemwake.md), which specifies the least-powered state from which the device can wake the system. For example, a device that can wake the system from S2 but not from S3 would fail a query for S3 but succeed a query for S2.

-   Entering a device power state that corresponds to the requested state would force the driver to abandon an operation that would lose data, such as an open modem connection. A driver rarely will fail a query for this reason; under most circumstances, the application handles such cases.

To fail an **IRP\_MN\_QUERY\_POWER** request for a system power state, a driver should take the following steps:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to indicate that the driver is prepared to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only)

2.  Set **Irp-&gt;IoStatus.Status** to a failure status and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), specifying IO\_NO\_INCREMENT. Do not pass the IRP further down the device stack.

3.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) to release the previously acquired lock.

4.  Return a failure status from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Failing%20a%20System%20Query-Power%20IRP%20in%20a%20Filter%20or%20Function%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


