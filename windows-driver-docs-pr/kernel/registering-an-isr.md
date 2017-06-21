---
title: Registering an ISR
author: windows-driver-content
description: Registering an ISR
ms.assetid: 903e5664-2193-4456-b133-bb979d700bdf
keywords: ["interrupt service routines WDK kernel , registering ISRs", "interrupt objects WDK kernel , registering ISRs", "ISRs WDK kernel , registering ISRs", "registering ISRs WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering an ISR


Drivers use the [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine to register an ISR for an interrupt. **IoConnectInterruptEx** is part of Windows Vista and later operating systems. **IoConnectInterruptEx** takes a single *Parameters* parameter, which is a pointer to an [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550541) structure. For Windows Server 2003, Windows XP, and Windows 2000, drivers can use the Iointex.lib library that is included in the Windows Driver Kit (WDK).

On Windows Vista and later, **IoConnectInterruptEx** provides several different methods for registering an ISR. The value specified for *Parameters*-&gt;**Version** determines the method, as follows:

-   Use CONNECT\_LINE\_BASED to register an [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine for all of a device's line-based interrupts. (Devices usually have at most one line-based interrupt.) The system automatically detects any line-based interrupts assigned to the device. For more information, see [Using the CONNECT\_LINE\_BASED Version of IoConnectInterruptEx](using-the-connect-line-based-version-of-ioconnectinterruptex.md).

-   Use CONNECT\_MESSAGE\_BASED to register an [*InterruptMessageService*](https://msdn.microsoft.com/library/windows/hardware/ff547940) routine for all of a device's message-signaled interrupts. You can also specify a fallback [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine—if the device only has line-based interrupts, **IoConnectInterruptEx** registers the *InterruptService* routine instead. The system automatically detects any message-signaled interrupts assigned to the device. For more information, see [Using the CONNECT\_MESSAGE\_BASED Version of IoConnectInterruptEx](using-the-connect-message-based-version-of-ioconnectinterruptex.md).

-   Use CONNECT\_FULLY\_SPECIFIED to register an *InterruptService* routine for each interrupt separately. You can use this to specify an *InterruptService* routine for either a line-based or a message-signaled interrupt, but you must manually specify the interrupt using information passed by the PnP manager. For more information, see [Using the CONNECT\_FULLY\_SPECIFIED Version of IoConnectInterruptEx](using-the-connect-fully-specified-version-of-ioconnectinterruptex.md).

On operating systems prior to Windows Vista, you can only use CONNECT\_FULLY\_SPECIFIED. If you specify CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED, **IoConnectInterruptEx** returns an error. You can use this behavior to determine if you are running on Windows Vista or an earlier system. For more information, see [Using IoConnectInterruptEx Prior to Windows Vista](using-ioconnectinterruptex-prior-to-windows-vista.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20an%20ISR%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


