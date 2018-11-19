---
title: Using Passive-Level Interrupt Service Routines
description: Starting with Windows 8, a driver can use the IoConnectInterruptEx routine to register a passive-level InterruptService routine (ISR).
ms.assetid: 122BDE14-1552-4F7B-88D3-030423713E00
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Using Passive-Level Interrupt Service Routines


Starting with Windows 8, a driver can use the [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine to register a passive-level [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine (ISR). When the associated interrupt occurs, the kernel's interrupt trap handler schedules this routine to run at IRQL = PASSIVE\_LEVEL. An ISR might need to run at passive level if it can access the hardware registers of a device only through I/O requests. A passive-level ISR can synchrononously send an I/O request to a device and block until the request completes.

## Registering a Passive-Level ISR


The input parameter to **IoConnectInterruptEx** is a pointer to an [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550541) structure. To register a passive-level ISR, set the **Version** member of this structure to either CONNECT\_FULLY\_SPECIFIED or CONNECT\_LINE\_BASED. If **Version** = CONNECT\_FULLY\_SPECIFIED, set the **Irql** member to PASSIVE\_LEVEL, the **SynchronizeIrql** member to PASSIVE\_LEVEL, and the **SpinLock** member to **NULL**. If **Version** = CONNECT\_LINE\_BASED, set **SynchronizeIrql** = PASSIVE\_LEVEL and **SpinLock** = **NULL**.

If the interrupt object specifies a passive-level ISR, the [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) routine uses a kernel synchronization event object instead of a spin lock to synchronize execution of the [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine with the ISR.

This event object is allocated by the **IoConnectInterruptEx** routine in the call that registers the passive-level ISR. The caller must not supply a spin lock in this call. (That is, the caller must set the **SpinLock** member of the **IO\_CONNECT\_INTERRUPT\_PARAMETERS** structure to NULL if the ISR is to run at passive level.) Otherwise, **IoConnectInterruptEx** fails and returns error status STATUS\_INVALID\_PARAMETER.

The [**KeAcquireInterruptSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551914) and [**KeReleaseInterruptSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553139) routines cause a bug check if the ISR for the supplied interrupt object runs at IRQL = PASSIVE\_LEVEL.

## Devices that Require Passive-Level Interrupt Handling


For a memory-mapped device that signals a level-triggered interrupt request, the device's ISR is typically called at DIRQL from within the kernel's interrupt trap handler. The ISR manipulates the hardware registers in the device to turn off the interrupt.

However, an ISR might need to run at IRQL = PASSIVE\_LEVEL if the associated device signals a level-triggered interrupt request but the device's hardware registers cannot be accessed directly from an ISR that is called at DIRQL from within the kernel's interrupt trap handler. For example, the device registers might not be memory-mapped, or the ISR might be temporarily blocked during a register access.

Starting with Windows 8, a driver can register a passive-level ISR. When the interrupt occurs, the kernel's interrupt trap handler schedules the ISR to run at IRQL = PASSIVE\_LEVEL. Before the handler returns, it must silence the interrupt in the interrupt controller (or [GPIO controller](https://msdn.microsoft.com/library/windows/hardware/hh439512)). If a device signals an edge-triggered interrupt, the handler clears the interrupt in the interrupt controller. If the device signals a level-triggered interrupt, the handler temporarily masks the interrupt in the interrupt controller; after the ISR runs, the kernel unmasks the interrupt.

## An Example


An example of a device that might require a passive-level ISR is a sensor device that is connected to a low-power serial bus, such as I²C. Starting with Windows 8, support for I²C and for other [simple peripheral buses](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPBs) is provided by the [SPB framework extension](https://msdn.microsoft.com/library/windows/hardware/hh406203) (SpbCx).

To access the registers of the I²C-connected sensor device, the sensor driver sends the sensor device an I/O request, which is jointly handled by SpbCx and by the controller driver for the bus. To perform the requested operation, the SPB controller must transfer data serially over the bus. This transfer is relatively slow and cannot be performed within the time constraints of an ISR that runs at DIRQL. However, a passive-level ISR can send the I/O request synchronously and then block until the request completes.

The passive-level ISR in this example might be blocked for a longer time if the I²C bus controller is turned off when the ISR sends the I/O request to the interrupting device. In this case, the controller must complete the transition to the D0 power state before it can transfer the data over the bus.

In contrast to a bus such as PCI, the I²C bus in this example provides no bus-specific means to convey interrupt requests from peripheral devices to the processor. Instead, the sensor device might signal an interrupt to a pin on a GPIO controller device, which then relays the interrupt request to the processor. For more information, see [GPIO Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh406467).

Typically, the hardware registers of a GPIO controller are memory-mapped and can be accessed at DIRQL by the kernel's interrupt trap handler. When the sensor device causes an interrupt, the handler must silence the interrupt by manipulating the interrupt bits in the GPIO controller's registers.

For a level-triggered interrupt, the kernel's interrupt trap handler masks the interrupt request at the GPIO pin, and then schedules the sensor device's ISR to run at passive level. The ISR must clear the interrupt request from the sensor device. After the ISR returns, the kernel unmasks the interrupt request at the GPIO pin.

For an edge-triggered interrupt, the kernel's trap handler clears the interrupt request at the GPIO pin, and then schedules the sensor device's ISR to run at passive level.

## Worker Routines


In the call to **IoConnectInterruptEx**, a driver has the option to split the processing of the interrupt between a passive-level ISR and a worker routine. As a general rule, the ISR should do the initial processing of the interrupt (for example, silence a level-triggered interrupt), and defer additional processing to the worker. Although both the ISR and worker run at passive level, the ISR runs at a relatively high priority and might delay other high-priority tasks. These tasks might include passive-level ISRs for new interrupts.

In rare cases, an interrupt might require so little processing that the passive-level ISR can perform all of the processing for the interrupt, and no worker routine is required.

For information about using passive-level ISRs in KMDF drivers, see [Supporting Passive-Level Interrupts](https://msdn.microsoft.com/library/windows/hardware/hh451035).

 

 




