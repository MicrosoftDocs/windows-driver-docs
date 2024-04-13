---
title: Registering an ISR
description: Registering an ISR
keywords: ["interrupt service routines WDK kernel , registering ISRs", "interrupt objects WDK kernel , registering ISRs", "ISRs WDK kernel , registering ISRs", "registering ISRs WDK kernel"]
ms.date: 06/16/2017
---

# Registering an ISR


Drivers use the [**IoConnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterruptex) routine to register an ISR for an interrupt. **IoConnectInterruptEx** is part of Windows Vista and later operating systems. **IoConnectInterruptEx** takes a single *Parameters* parameter, which is a pointer to an [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_connect_interrupt_parameters) structure. For Windows Server 2003, Windows XP, and Windows 2000, drivers can use the Iointex.lib library that is included in the Windows Driver Kit (WDK).

On Windows Vista and later, **IoConnectInterruptEx** provides several different methods for registering an ISR. The value specified for *Parameters*-&gt;**Version** determines the method, as follows:

-   Use CONNECT\_LINE\_BASED to register an [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine for all of a device's line-based interrupts. (Devices usually have at most one line-based interrupt.) The system automatically detects any line-based interrupts assigned to the device. For more information, see [Using the CONNECT\_LINE\_BASED Version of IoConnectInterruptEx](using-the-connect-line-based-version-of-ioconnectinterruptex.md).

-   Use CONNECT\_MESSAGE\_BASED to register an [*InterruptMessageService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kmessage_service_routine) routine for all of a device's message-signaled interrupts. You can also specify a fallback [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine—if the device only has line-based interrupts, **IoConnectInterruptEx** registers the *InterruptService* routine instead. The system automatically detects any message-signaled interrupts assigned to the device. For more information, see [Using the CONNECT\_MESSAGE\_BASED Version of IoConnectInterruptEx](using-the-connect-message-based-version-of-ioconnectinterruptex.md).

-   Use CONNECT\_FULLY\_SPECIFIED to register an *InterruptService* routine for each interrupt separately. You can use this to specify an *InterruptService* routine for either a line-based or a message-signaled interrupt, but you must manually specify the interrupt using information passed by the PnP manager. For more information, see [Using the CONNECT\_FULLY\_SPECIFIED Version of IoConnectInterruptEx](using-the-connect-fully-specified-version-of-ioconnectinterruptex.md).

On operating systems prior to Windows Vista, you can only use CONNECT\_FULLY\_SPECIFIED. If you specify CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED, **IoConnectInterruptEx** returns an error. You can use this behavior to determine if you are running on Windows Vista or an earlier system. For more information, see [Using IoConnectInterruptEx Prior to Windows Vista](using-ioconnectinterruptex-prior-to-windows-vista.md).

 

