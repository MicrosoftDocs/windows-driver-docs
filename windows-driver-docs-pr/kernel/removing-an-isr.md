---
title: Removing an ISR
description: Removing an ISR
keywords: ["interrupt service routines WDK kernel , removing ISRs", "interrupt objects WDK kernel , removing ISRs", "ISRs WDK kernel , removing ISRs", "removing ISRs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Removing an ISR


Drivers can remove an ISR that is registered with [**IoConnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterruptex) by calling [**IoDisconnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterruptex). **IoDisconectInterruptEx** takes a single *Parameters* parameter, which is a pointer to an [**IO\_DISCONNECT\_INTERRUPT\_PARAMETERS**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_disconnect_interrupt_parameters) structure. The values that are used for the members of the structure depend on the version that is used to register the ISR.

The driver must save certain information when it registers the ISR to later remove it. For the CONNECT\_LINE\_BASED and CONNECT\_FULLY\_SPECIFIED versions, the driver must save the value that is supplied in the **LineBased.InterruptObject** or **FullySpecified.InterruptObject** member of [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_connect_interrupt_parameters). For the CONNECT\_MESSAGE\_BASED version, the driver must save the values supplied in the **Version** and **MessageBased.ConnectionContext** members of **IO\_CONNECT\_INTERRUPT\_PARAMETERS**.

 

