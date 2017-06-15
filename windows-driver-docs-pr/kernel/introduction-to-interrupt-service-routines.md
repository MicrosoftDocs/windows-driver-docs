---
title: Introduction to Interrupt Service Routines
author: windows-driver-content
description: Introduction to Interrupt Service Routines
MS-HAID:
- 'Intrupts\_d0016a3a-c3e2-4856-b31e-99c68dafd72a.xml'
- 'kernel.introduction\_to\_interrupt\_service\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e83eb873-7cdf-4faf-9a6e-cc5954ebf1d6
keywords: ["interrupt service routines WDK kernel , about ISRs", "ISRs WDK kernel , about interrupt service routines", "InterruptService", "line-based interrupts WDK kernel", "interrupt lines WDK kernel", "message-signaled interrupts WDK kernel", "InterruptMessageService"]
---

# Introduction to Interrupt Service Routines


A driver of a physical device that receives interrupts registers one or more interrupt service routines (ISR) to service the interrupts. The system calls the ISR each time it receives that interrupt.

Devices for ports and buses prior to PCI 2.2 generate *line-based interrupts*. A device generates the interrupt by sending an electrical signal on a dedicated pin known as an *interrupt line*. Versions of Microsoft Windows prior to Windows Vista only support line-based interrupts.

Beginning with PCI 2.2, PCI devices can generate *message-signaled interrupts*. A device generates a message-signaled interrupt by writing a data value to a particular address. Windows Vista and later operating systems support both line-based and message-signaled interrupts.

The system supports two different types of ISRs:

-   The driver can register an [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine to handle line-based or message-signaled interrupts. (This is the only type available prior to Windows Vista.) The system passes a driver-supplied context value.

-   The driver can register an [*InterruptMessageService*](https://msdn.microsoft.com/library/windows/hardware/ff547940) routine to handle message-signaled interrupts. The system passes both a driver-supplied context value and the message ID of the interrupt message.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Interrupt%20Service%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


