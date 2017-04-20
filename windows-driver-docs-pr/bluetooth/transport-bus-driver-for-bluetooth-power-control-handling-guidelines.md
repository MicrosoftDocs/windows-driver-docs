---
title: Transport Bus Driver for Bluetooth Power Control Handling Guidelines
description: IHVs need to implement a transport bus driver in order to support Bluetooth functionality of a multifunction controller often integrated in a System on Chip (SoC) system.
ms.assetid: 00792128-320E-45C1-9F58-343B72565CA7
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transport Bus Driver for Bluetooth Power Control Handling Guidelines


IHVs need to implement a transport bus driver in order to support Bluetooth functionality of a multifunction controller often integrated in a System on Chip (SoC) system.

The [Bluetooth Serial HCI Bus Driver](http://go.microsoft.com/fwlink/p/?linkid=256088) sample can help IHVs facilitate the development of the their transport bus driver. The sample illustrates how to handle IOCTL (IO Control) requests from its upper layer and how to deliver HCI packets to its serial controller driver at its lower layer. However, an out-of-band control other than using its own IO transport (UART in the case of the WDK sample) is often used to support idle and wake controls; such a mechanism is required and used to optimize power consumption. The information in this section and its subtopics supplements the bus sample driver by providing guidelines and sample codes for handling power controls.

The information in this section and its subtopics applies to:

-   Windows 8.1

As a short range wireless radio, Bluetooth is often a function within a multifunction controller that is integrated on a System on Chip (SoC) system. Prior versions of Windows, up to Windows 7, provided an inbox class driver for Bluetooth with USB as the only transport option. Windows 8 introduced the [Bluetooth Extensible Transport IOCTLs](https://msdn.microsoft.com/library/windows/hardware/hh450819). USB transport and the extensible transport models will continue to be supported in the Windows 8.1. The extensibility model DDI will remain unchanged in Windows to give a system integrator the flexibility to choose a suitable transport for SoC platforms, e.g. UART (Universal Asynchronous Receiver/Transmitter). In addition, simpler and low power controllers, e.g. GPIOs, can be used as a "sideband" mechanism for handling power control (e.g. enabling the Bluetooth radio and as a sleep/wake signaling).

The information in this section and its subtopics provides guidelines and sample codes for power control handling by such bus drivers and explains the interaction with the Bluetooth core drivers. The controls include: idle capabilities, arming and disarming for wake, idle and wake signaling, and device power state changes. A driver developer can adopt the Bluetooth Serial HCI Bus Driver sample to simplify the development efforts to support Bluetooth over an alternate (non-USB) transport.

While different transports are being used to support Bluetooth, the Bluetooth DDIs remain the same for Bluetooth profile drivers. This means that Bluetooth profile drivers and applications remain agnostic to the transport or power control handling being implemented.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Transport%20Bus%20Driver%20for%20Bluetooth%20Power%20Control%20Handling%20Guidelines%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




