---
title: Handling a System Set-Power IRP in a Device Power Policy Owner
description: Handling a System Set-Power IRP in a Device Power Policy Owner
ms.assetid: f6206455-142b-4f3f-ae5a-d8e79386bce3
keywords: ["set-power IRPs WDK power management", "device power policy owners WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a System Set-Power IRP in a Device Power Policy Owner





In response to a system set-power IRP, the [power policy owner](managing-device-power-policy.md) for a device stack is responsible for putting its device stack into an appropriate device power state.

As a general rule, when a device power policy owner receives an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) for a system power state, it should respond by passing the system set-power IRP down the device stack. A device power policy owner should also respond by sending down the device stack **IRP\_MN\_SET\_POWER** for a corresponding device power state in an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine. After all drivers in the stack have completed the device set-power IRP, the device power policy owner completes the system set-power IRP.

However, to improve system resume performance, device power owners for devices that do not have child devices should use a different approach to reduce the time it takes a system to return to [working state S0](system-working-state-s0.md) from a [sleeping state](system-sleeping-states.md). In this case, in response to a system set-power IRP that returns a system to working state S0, device power policy owners should perform the following sequence of operations:

1.  After receiving an **IRP\_MN\_SET\_POWER** IRP for the S0 system power state in the driver's [DispatchPower routine](dispatchpower-routines.md), set an *IoCompletion* routine for the IRP and pass the IRP down the stack.

2.  In the *IoCompletion* routine set in step (1), request an **IRP\_MN\_SET\_POWER** IRP for the corresponding device power state and then immediately complete the system set-power IRP. The driver should not wait for device set-power IRPs to complete before it completes the system set-power IRP. The *IoCompletion* routine is executed after all lower-level drivers have completed the system set-power IRP and the system set-power IRP is passed back to the driver's functional device object (FDO).

3.  Perform any required device-specific initialization.

4.  Complete the device set-power IRP that was sent in step (2).

5.  Process I/O requests that were queued when the device was in a [device sleeping state](device-sleeping-states.md).

The kernel power manager has a limited set of IRP dispatch queues, and must quickly notify all devices in the system of the return to the system working state S0. Drivers that fail to complete the system set-power IRP as quickly as possible prevent other devices from getting their system set-power IRP, which can adversely affect overall system performance during system power-state transitions.

For more detail on handling system set-power IRPs, see the following:

[Determining the Correct Device Power State](determining-the-correct-device-power-state.md)

[Sending a Device Set-Power IRP in Response to a System Set-Power IRP](sending-a-device-set-power-irp-in-response-to-a-system-set-power-irp.md)

 

 




