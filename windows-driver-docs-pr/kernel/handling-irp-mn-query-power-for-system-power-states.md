---
title: Handling IRP\_MN\_QUERY\_POWER for System Power States
author: windows-driver-content
description: Handling IRP\_MN\_QUERY\_POWER for System Power States
ms.assetid: 1904a1cb-a220-41cc-8894-5f90919e7383
keywords: ["IRP_MN_QUERY_POWER", "system power states WDK kernel , IRP_MN_QUERY_POWER", "query-power IRPs WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling IRP\_MN\_QUERY\_POWER for System Power States


## <a href="" id="ddk-handling-irp-mn-query-power-for-system-power-states-kg"></a>


The power manager sends a power IRP with the minor IRP code [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) and **SystemPowerState** in **Parameters.Power.Type** to determine whether it can safely change to a specified system power state (S1-S5) and to allow drivers to prepare for such a change.

Whenever possible, the power manager queries before sending an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) that requests a lower (less powered) state. However, in cases of a failing battery or imminent loss of power, the power manager sends the set-power IRP without querying first. The power manager never sends a query before sending an IRP to set the system in the working state (S0).

For information about how a power policy owner for a device handles system query-power requests, see [Handling a System Query-Power IRP in a Device Power Policy Owner](handling-a-system-query-power-irp-in-a-device-power-policy-owner.md).

For information about how drivers (that are not the power policy owner for a device) handle system query-power requests, see the following:

[Handling a System Query-Power IRP in a Filter or Function Driver](handling-a-system-query-power-irp-in-a-filter-or-function-driver.md)

[Failing a System Query-Power IRP in a Filter or Function Driver](failing-a-system-query-power-irp-in-a-filter-or-function-driver.md)

[Handling a System Query-Power IRP in a Bus Driver](handling-a-system-query-power-irp-in-a-bus-driver.md)

Note that a driver must never send a device **IRP\_MN\_SET\_POWER** request in response to a system query; it requests such an IRP only after it receives a system set-power request.

Because the power manager sends the system query IRP to each device stack on the system, it is possible that a driver for one device might fail the query while drivers for other devices complete it successfully. Beginning with Windows Vista, a change to the system power state to a sleep state is a critical power state change. Even if a driver fails a system query-power IRP, the power manager in Windows Vista might still change the system power state to a sleep state. It is also possible that a battery might expire while a query is active, requiring an immediate shutdown. Consequently, after a query IRP, drivers must be prepared to receive any of the following power IRPs:

-   An **IRP\_MN\_SET\_POWER** to the queried state

-   An **IRP\_MN\_SET\_POWER** to a different power state

-   An **IRP\_MN\_SET\_POWER** to the current power state

-   An **IRP\_MN\_QUERY\_POWER** to any state

Usually, however, a driver receives a system set-power IRP following a system query IRP. Regardless, a driver must be ready to change the system power state even if the driver fails a query-power IRP.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20IRP_MN_QUERY_POWER%20for%20System%20Power%20States%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


