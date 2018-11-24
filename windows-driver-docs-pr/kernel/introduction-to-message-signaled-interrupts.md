---
title: Introduction to Message-Signaled Interrupts
description: Introduction to Message-Signaled Interrupts
ms.assetid: 035207a1-762d-463e-822e-64ac4833afa4
keywords: ["message-signaled interrupts WDK kernel", "MSIs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Message-Signaled Interrupts


Message-signaled interrupts (MSIs) were introduced in the PCI 2.2 specification as an alternative to line-based interrupts. Instead of using a dedicated pin to trigger interrupts, devices that use MSIs trigger an interrupt by writing a value to a particular memory address. PCI 3.0 defines an extended form of MSI, called *MSI-X*, that enables greater programmability. Windows Vista and later versions of Windows support MSI and MSI-X. A single device can support both MSI and MSI-X. For such a device, the operating system will automatically use MSI-X.

An *interrupt message* is a particular value that a device writes to a particular address to trigger an interrupt. Unlike line-based interrupts, message-signaled interrupts have edge semantics. The device sends a message but does not receive any hardware acknowledgment that the interrupt was received.

For PCI 2.2, a message consists of an address and a partially opaque 16-bit value. Each device is assigned a single address. To send multiple messages, the device can use the lower 4 bits of the message value to distinguish messages. Therefore, for PCI 2.2, devices can support up to 16 messages.

For PCI 3.0, a message consists of an address and an opaque 32-bit value. Each different message has its own unique address. Unlike for PCI 2.2, the device does not modify the value. For PCI 3.0, a device can support up to 2,048 different messages. Devices that support PCI 3.0 MSI-X feature a dynamically programmable hardware table that contains entries for each of the interrupt sources in the device. Each entry in this table can be programmed with one of the messages that are allocated to a device, and can be independently masked. Drivers can change the programming of an interrupt message into a table entry and whether an entry has been masked. For more information, see [Dynamically Configuring MSI-X](dynamically-configuring-msi-x.md).

Drivers can register a single [*InterruptMessageService*](https://msdn.microsoft.com/library/windows/hardware/ff547940) routine that handles all possible messages or individual [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routines for each message.

Drivers can handle MSIs that a device sends as follows:

1.  During driver installation, enable MSIs in the registry. You can also use the registry to specify the number of messages to allocate for the device. For more information, see [Enabling Message-Signaled Interrupts in the Registry](enabling-message-signaled-interrupts-in-the-registry.md).

2.  Optionally, increase the number of interrupt messages and save some per-message settings by responding to an [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874) request. For more information, see [Using Interrupt Resource Descriptors](using-interrupt-resource-descriptors.md).

3.  In the driver's dispatch routine for [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749), call [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) to register an *InterruptService* or *InterruptMessageService* routine to service the device's interrupts. Use the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx** to register an *InterruptService* routine for a specific message or the CONNECT\_MESSAGE\_BASED version of **IoConnectInterruptEx** to register a single *InterruptMessageService* routine for all messages. For more information, see [Using the CONNECT\_MESSAGE\_BASED Version of IoConnectInterruptEx](using-the-connect-message-based-version-of-ioconnectinterruptex.md) and [Using the CONNECT\_FULLY\_SPECIFIED Version of IoConnectInterruptEx](using-the-connect-fully-specified-version-of-ioconnectinterruptex.md).

4.  After the driver no longer intends to service interrupts from the device, call [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093) (after disabling the device's interrupts) to remove any registered interrupt service routines.

Drivers that are designed to use multiple messages should check that the expected number of messages is allocated. If the Plug and Play (PnP) manager cannot allocate the requested number of messages, it instead allocates exactly one message to the device. Drivers can check the number of messages that are actually allocated in one of the following ways:

-   The PnP manager reports the number of allocated messages in its list of raw resource descriptors. For more information, see [Using Interrupt Resource Descriptors](using-interrupt-resource-descriptors.md).

-   When **IoConnectInterruptEx** returns, it sets *Parameters*-&gt;**MessageBased.ConnectContext.InterruptMessageTable-&gt;MessageCount** to the number of allocated messages.

 

 




