---
title: Transport Bus Driver for Bluetooth Power Control Handling Guidelines
description: IHVs need to implement a transport bus driver in order to support Bluetooth functionality of a multifunction controller often integrated in a System on Chip (SoC) system.
ms.assetid: 00792128-320E-45C1-9F58-343B72565CA7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transport Bus Driver for Bluetooth Power Control Handling Guidelines


IHVs need to implement a transport bus driver in order to support Bluetooth functionality of a multifunction controller often integrated in a System on Chip (SoC) system.

The [Bluetooth Serial HCI Bus Driver](http://go.microsoft.com/fwlink/p/?linkid=256088) sample can help IHVs facilitate the development of the their transport bus driver. The sample illustrates how to handle IOCTL (IO Control) requests from its upper layer and how to deliver HCI packets to its serial controller driver at its lower layer. However, an out-of-band control other than using its own IO transport (UART in the case of the WDK sample) is often used to support idle and wake controls; such a mechanism is required and used to optimize power consumption. The information in this section and its subtopics supplements the bus sample driver by providing guidelines and sample codes for handling power controls.

The information in this section and its subtopics applies to:

-   Windows 8.1

As a short range wireless radio, Bluetooth is often a function within a multifunction controller that is integrated on a System on Chip (SoC) system. Prior versions of Windows, up to Windows 7, provided an inbox class driver for Bluetooth with USB as the only transport option. Windows 8 introduced the [Bluetooth Extensible Transport IOCTLs](https://msdn.microsoft.com/library/windows/hardware/hh450819). USB transport and the extensible transport models will continue to be supported in the Windows 8.1. The extensibility model DDI will remain unchanged in Windows to give a system integrator the flexibility to choose a suitable transport for SoC platforms, e.g. UART (Universal Asynchronous Receiver/Transmitter). In addition, simpler and low power controllers, e.g. GPIOs, can be used as a "sideband" mechanism for handling power control (e.g. enabling the Bluetooth radio and as a sleep/wake signaling).

The information in this section and its subtopics provides guidelines and sample codes for power control handling by such bus drivers and explains the interaction with the Bluetooth core drivers. The controls include: idle capabilities, arming and disarming for wake, idle and wake signaling, and device power state changes. A driver developer can adopt the Bluetooth Serial HCI Bus Driver sample to simplify the development efforts to support Bluetooth over an alternate (non-USB) transport.

While different transports are being used to support Bluetooth, the Bluetooth DDIs remain the same for Bluetooth profile drivers. This means that Bluetooth profile drivers and applications remain agnostic to the transport or power control handling being implemented.

 

 





