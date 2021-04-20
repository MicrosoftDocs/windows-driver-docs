---
title: Providing ISR Context Information
description: Providing ISR Context Information
keywords: ["interrupt service routines WDK kernel , context information", "ISRs WDK kernel , context information", "interrupt objects WDK kernel , context information", "context information WDK interrupts", "pointers WDK interrupts"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Providing ISR Context Information





On entry, an ISR receives a pointer to whatever context area the driver set up when it called [**IoConnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterruptex) to register the routine.

Most drivers set the context pointer to the device object that represents the physical device that generates interrupts, or to that device object's device extension. In the device extension, the driver can store state information for the driver's ISR and [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine, the latter of which usually does almost all of the I/O processing to satisfy each request that caused the device to interrupt.

Typically, drivers use the device extension to store pointers to each of the device's interrupt objects (returned from calls to **IoConnectInterruptEx**). Drivers also typically store information in the device extension that allows an ISR to determine if an interrupt was issued by a device the ISR supports.

(Alternatively, interrupt object pointers can be stored in nonpaged pool that the driver allocates.)

 

