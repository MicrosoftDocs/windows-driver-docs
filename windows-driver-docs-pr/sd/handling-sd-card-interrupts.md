---
title: Handling SD Card Interrupts
description: Handling SD Card Interrupts
keywords:
- SD WDK buses , interrupts
- interrupts WDK SD bus
- IRQLs WDK SD bus
- hardware interrupts WDK SD bus
- interrupt notifications WDK SD bus
ms.date: 03/03/2023
---

# Handling SD Card Interrupts


Secure Digital (SD) card drivers do not have interrupt service routines (ISRs) and they do not acquire interrupt request (IRQ) resources. The SD bus driver detects and intercepts hardware interrupts, and then reports them to the device driver by means of the interrupt notification callback routine [**PSDBUS\_CALLBACK\_ROUTINE**](/windows-hardware/drivers/ddi/ntddsd/nc-ntddsd-sdbus_callback_routine), as explained in sections [Secure Digital (SD) Driver Stack](./sd-card-driver-stack.md) and [Opening and Initializing an SD Bus Interface](./opening--initializing-and-closing-an-sd-card-bus-interface.md).

The device driver does not have to complete interrupt processing in the context of the interrupt notification callback routine. The driver can return from the callback routine and complete interrupt processing in its own context. When the driver finishes processing the interrupt, it informs the bus driver by an explicit call to an interrupt acknowledgment routine supplied with the SD bus interface. For more information about the interrupt acknowledgment routine, see [**PSDBUS\_ACKNOWLEDGE\_INT\_ROUTINE**](/windows-hardware/drivers/ddi/ntddsd/nc-ntddsd-psdbus_acknowledge_int_routine). When the bus driver receives this call, it re-enables the interrupt.

SD device drivers have two options with respect to the IRQ levels (IRQLs) at which they run. An SD driver can run exclusively at PASSIVE\_LEVEL, or it can run at DISPATCH\_LEVEL while in the context of the interrupt notification callback routine and at PASSIVE\_LEVEL the rest of the time. When an SD device driver runs exclusively at PASSIVE\_LEVEL, the bus driver assumes responsibility for synchronizing interrupts. Choose this option if your device can operate without strict limits on interrupt latency because it will simplify the design of your driver. In addition to offloading the task of interrupt synchronization onto the bus driver, there are other benefits. For instance, drivers must frequently transfer data in response to an interrupt. If the driver's callback routine is running at PASSIVE\_LEVEL, it is free to do a synchronous I/O operation rather than an asynchronous one. If the callback routine runs at DISPATCH\_LEVEL, the driver must wait until it is running at a lower IRQL before doing synchronous I/O.

An SD device driver specifies the IRQL at which it will run when it initializes the SD bus interface. To run at DISPATCH\_LEVEL in the interrupt notification callback routine, the driver must set the **CallbackAtDpcLevel** member of the [**SDBUS\_INTERFACE\_PARAMETERS**](/previous-versions/windows/hardware/drivers/ff537919(v=vs.85)) structure to **TRUE** and pass this structure to the interface initialization routine. For a description of the interface routine, see [**PSDBUS\_INITIALIZE\_INTERFACE\_ROUTINE**](/windows-hardware/drivers/ddi/ntddsd/nc-ntddsd-psdbus_initialize_interface_routine). To run exclusively at PASSIVE\_LEVEL, the driver must set **CallbackAtDpcLevel** to **FALSE**.

 

