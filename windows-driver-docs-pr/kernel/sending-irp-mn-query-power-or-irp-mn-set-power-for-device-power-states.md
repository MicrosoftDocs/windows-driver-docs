---
title: Sending IRP_MN_QUERY_POWER or IRP_MN_SET_POWER for Device Power States
description: Sending IRP_MN_QUERY_POWER or IRP_MN_SET_POWER for Device Power States
ms.assetid: 58f65138-abb9-4bb8-bf9b-14f17347e309
keywords: ["IRP_MN_SET_POWER", "IRP_MN_QUERY_POWER", "device power states WDK kernel", "query-power IRPs WDK power management", "power IRPs WDK kernel , device queries", "querying power state", "queuing IRPs", "device query power IRPs WDK kernel", "sending power state IRPs", "set-power IRPs WDK kernel", "device set power IRPs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Sending IRP\_MN\_QUERY\_POWER or IRP\_MN\_SET\_POWER for Device Power States





A device power policy owner sends a device query-power IRP ([**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)) to determine whether lower drivers can accommodate a change in device power state, and a device set-power IRP ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)) to change the device power state. (This driver can also send a wait/wake IRP to enable its device to awaken in response to an external signal; see [Supporting Devices that Have Wake-Up Capabilities](supporting-devices-that-have-wake-up-capabilities.md) for details.)

The driver should send an [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) request when either of the following is true:

-   The driver receives a system query-power IRP.

-   The driver is preparing to put an idle device in a sleep state, so must query lower drivers to find out whether doing so is feasible.

The driver should send an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request when any of the following is true:

-   The driver has determined that the device is idle and can be put to sleep.

-   The device is sleeping and must re-enter the working state to handle waiting I/O.

-   The driver receives a system set-power IRP.

A driver must not allocate its own power IRP; the power manager provides the [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) routine for this purpose. As [Rules for Handling Power IRPs](rules-for-handling-power-irps.md) explains, **PoRequestPowerIrp** allocates and sends the IRP, and in combination with **IoCallDriver** (in Windows 7 and Windows Vista), or **PoCallDriver** (in Windows Server 2003, Windows XP, and Windows 2000), ensures that all power requests are properly synchronized. Callers of **PoRequestPowerIrp** must be running at IRQL &lt;= DISPATCH\_LEVEL.

The following is the prototype for this routine:

```cpp
NTSTATUS
PoRequestPowerIrp (
    IN PDEVICE_OBJECT DeviceObject,
    IN UCHAR MinorFunction,
    IN POWER_STATE PowerState,
    IN PREQUEST_POWER_COMPLETE CompletionFunction,
    IN PVOID Context,
    OUT PIRP *Irp OPTIONAL
    );
```

To send the IRP, the driver calls **PoRequestPowerIrp**, specifying a pointer to the target device object in *DeviceObject*, the minor IRP code IRP\_MN\_SET\_POWER or IRP\_MN\_QUERY\_POWER in *MinorFunction*, the value **DevicePowerState** in the <em>PowerState</em>**.Type**, and a device power state in <em>PowerState</em>**.State**. In Windows 98/Me, *DeviceObject* must specify the PDO of the underlying device; in Windows 2000 and later versions of Windows, this value can point to either the PDO or an FDO of a driver in the same device stack.

If the driver must perform additional tasks after all other drivers have completed the IRP, it should pass a pointer to a power completion function in *CompletionFunction*. The I/O manager calls the *CompletionFunction* after calling all the *IoCompletion* routines set by drivers as they passed the IRP down the stack.

Whenever a device power policy owner sends a device power query IRP, it should subsequently send a device set-power IRP from the callback routine (*CompletionFunction*) that it specified in the call to **PoRequestPowerIrp**. If the query succeeded, the set-power IRP specifies the queried power state. If the query failed, the set-power IRP re-asserts the current device power state. Re-asserting the current state is important because drivers queue I/O in response to the query; the policy owner must send the set-power IRP to notify drivers in its device stack to begin processing queued I/O requests.

Keep in mind that the policy owner for a device not only sends the device power IRP but also handles the IRP as it is passed down the device stack. Therefore, such a driver often sets an *IoCompletion* routine (with [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)) as part of its IRP-handling code, particularly when the device is powering up. The *IoCompletion* routine is called in sequence with *IoCompletion* routines set by other drivers and before the *CompletionFunction*. For further information, see [IoCompletion Routines for Device Power IRPs](iocompletion-routines-for-device-power-irps.md).

Because the IRP has been completed by all drivers when the *CompletionFunction* is called, the *CompletionFunction* must not call **IoCallDriver**, **PoCallDriver**, or **PoStartNextPowerIrp** with the IRP it originated. (It might, however, call these routines for a different power IRP.) Instead, this routine performs any additional actions required by the driver that originated the IRP. If the driver sent the device IRP in response to a system IRP, the *CompletionFunction* might complete the system IRP. For further information, see [Handling a System Set-Power IRP in a Device Power Policy Owner](handling-a-system-set-power-irp-in-a-device-power-policy-owner.md).

In response to the call to **PoRequestPowerIrp**, the power manager allocates a power IRP and sends it to the top of the device stack for the device. The power manager returns a pointer to the allocated IRP.

If no errors occur, **PoRequestPowerIrp** returns STATUS\_PENDING. This status means that the IRP has been sent successfully and is pending completion. The call fails if the power manager cannot allocate the IRP or if the caller has specified an invalid minor power IRP code.

Requests to power up a device must be handled first by the underlying bus driver for the device and then by each successively higher driver in the stack. Therefore, when sending a **PowerDeviceD0** request, the driver must ensure that its *CompletionFunction* performs required tasks after the IRP is complete and the device is powered on.

When powering off a device (**PowerDeviceD3**), each driver in the device stack must save all of its necessary context and do any necessary clean-up before sending the IRP to the next-lower driver. The extent of the context information and clean-up depends on the type of driver. A function driver must save hardware context; a filter driver might need to save its own software context. A *CompletionFunction* set in this situation can take actions associated with a completed power IRP, but the driver cannot access the device.

 

 




