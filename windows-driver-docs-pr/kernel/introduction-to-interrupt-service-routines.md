---
title: Introduction to Interrupt Service Routines
description: Introduction to Interrupt Service Routines
keywords: ["interrupt service routines WDK kernel , about ISRs", "ISRs WDK kernel , about interrupt service routines", "InterruptService", "line-based interrupts WDK kernel", "interrupt lines WDK kernel", "message-signaled interrupts WDK kernel", "InterruptMessageService"]
ms.date: 06/16/2017
---

# Introduction to Interrupt Service Routines


A driver of a physical device that receives interrupts registers one or more interrupt service routines (ISR) to service the interrupts. The system calls the ISR each time it receives that interrupt.

Devices for ports and buses prior to PCI 2.2 generate *line-based interrupts*. A device generates the interrupt by sending an electrical signal on a dedicated pin known as an *interrupt line*. Versions of Microsoft Windows prior to Windows Vista only support line-based interrupts.

Beginning with PCI 2.2, PCI devices can generate *message-signaled interrupts*. A device generates a message-signaled interrupt by writing a data value to a particular address. Windows Vista and later operating systems support both line-based and message-signaled interrupts.

The system supports two different types of ISRs:

-   The driver can register an [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine to handle line-based or message-signaled interrupts. (This is the only type available prior to Windows Vista.) The system passes a driver-supplied context value.

-   The driver can register an [*InterruptMessageService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kmessage_service_routine) routine to handle message-signaled interrupts. The system passes both a driver-supplied context value and the message ID of the interrupt message.

For more information about registering an InterruptService or InterruptMessageService routine to service the device's interrupts, see [Introduction to Message-Signaled Interrupts](./introduction-to-message-signaled-interrupts.md).
 

