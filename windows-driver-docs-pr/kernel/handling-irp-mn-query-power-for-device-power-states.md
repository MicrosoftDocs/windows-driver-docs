---
title: Handling IRP_MN_QUERY_POWER for Device Power States
description: Handling IRP_MN_QUERY_POWER for Device Power States
ms.assetid: 902619bc-068a-4613-b99d-78a243f7fee6
keywords: ["IRP_MN_QUERY_POWER", "device power states WDK kernel", "query-power IRPs WDK power management", "power IRPs WDK kernel , device queries", "querying power state", "queuing IRPs", "device query power IRPs WDK kernel", "dispatch routines WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling IRP\_MN\_QUERY\_POWER for Device Power States





A device query-power IRP queries about a change of state for a single device and is sent to all of the drivers in the stack for the device. Such an IRP specifies **DevicePowerState** in the **Power.Type** member of the I/O stack location.

Drivers handle query-power IRPs as they travel down the stack.

A function or filter driver can fail an [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) request if any of the following is true:

-   The device is enabled for wake-up and the requested power state is below the state from which the device can wake the system. For example, a device that can wake the system from D2 but not from D3 would fail a query for D3 but succeed a query for D2.

-   Entering the requested state would force the driver to abandon an operation that would lose data, such as an open modem connection. A driver rarely will fail a query for this reason; under most circumstances, the application handles such cases.

To fail an [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) request, a driver takes the following steps:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to indicate that the driver is prepared to handle the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Set **Irp-&gt;IoStatus.Status** to a failure status and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), specifying IO\_NO\_INCREMENT. The driver does not pass the IRP further down the device stack.

3.  Return an error status from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

If the driver succeeds the query-power IRP, it must not start any operations or take any other action that would prevent its successful completion of a subsequent **IRP\_MN\_SET\_POWER** request to the queried power state.

A driver that succeeds the IRP must prepare for a set-power IRP for the queried state and pass down the query IRP, as follows:

1.  Finish any outstanding I/O operations.

2.  Queue incoming I/O requests.

3.  Avoid starting any other new activities that would interfere with a transition to the specified power state. However, the driver should not save device context or take other steps toward shutdown.

4.  Call **IoCopyCurrentIrpStackLocationToNext** to set the IRP stack location for the next-lower driver.

5.  Set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine. In the *IoCompletion* routine, call **PoStartNextPowerIrp** (Windows Server 2003, Windows XP, and Windows 2000 only) to indicate the driver's readiness to handle the next power IRP.

6.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (in Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (in Windows Server 2003, Windows XP, and Windows 2000) to pass the query IRP to the next-lower driver. Do not complete the IRP.

7.  Return STATUS\_PENDING. The driver must not change the value at **Irp-&gt;IoStatus.Status**.

When the query-power IRP reaches the bus driver, the bus driver calls **PoStartNextPowerIrp** (Windows Server 2003, Windows XP, and Windows 2000 only) and sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS if the driver can change to the specified power state or sets a failure status if it cannot. The bus driver then calls **IoCompleteRequest**, specifying IO\_NO\_INCREMENT.

The drivers in a typical device stack handle a device query-power IRP as follows:

-   Most filter drivers should simply pass the IRP to the next-lower driver (see [Passing Power IRPs](passing-power-irps.md)) and return STATUS\_PENDING. Some filter drivers, however, might first need to perform device-specific tasks, such as queuing incoming IRPs or saving device power state.

-   A function driver performs device-specific tasks (such as, completing pending I/O requests, queuing incoming I/O requests, saving device context, or changing device power), sets an *IoCompletion* routine, and passes the device power IRP to the next-lower driver (see [Passing Power IRPs](passing-power-irps.md)). It returns STATUS\_PENDING from its *DispatchPower* routine.

-   The bus driver calls [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) (Windows Server 2003, Windows XP, and Windows 2000 only) to start the next power IRP. It then completes the IRP, specifying IO\_NO\_INCREMENT. If the driver cannot complete the IRP immediately, it calls [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422), returns STATUS\_PENDING from its *DispatchPower* routine, and completes the IRP later.

Even if the target device is already in the queried power state, each function or filter driver must queue I/O and pass the IRP down to the next-lower driver. The IRP must travel all the way down the device stack to the bus driver, which completes it.

While handling an **IRP\_MN\_QUERY\_POWER** request, a driver should return from the *DispatchPower* routine as quickly as possible. A driver must not wait in its *DispatchPower* routine for a kernel event signaled by code that handles the same IRP. Because power IRPs are synchronized throughout the system, a deadlock might occur.

 

 




