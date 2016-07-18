---
title: Architectural Overview
description: This topic presents an architectural overview of the Windows 8.1 support for rerouting audio data to bypass the Bluetooth host controller interface (HCI).
ms.assetid: FC9E5254-B543-4890-811C-1DA5F28E61B9
---

# Architectural Overview


This topic presents an architectural overview of the Windows 8.1 support for rerouting audio data to bypass the Bluetooth host controller interface (HCI).

Starting with Windows 8.1, the Microsoft operating system has been updated to be compatible with low power system-on-a-chip (SoC) design solutions. The new Windows support is compatible with either Intel-based or ARM-based SoC designs. These new low-power devices will be optimized for “always on” scenarios, so low battery consumption will be a key factor for success.

SoC architectures use the Universal Asynchronous Receiver/Transmitter (UART) transport mode to transmit data to and from the Bluetooth host controller.

Because UARTs cannot provide time sensitive data transmission, a synchronous connection oriented (SCO) bypass channel must be implemented in addition to a UART, to transfer audio data via I2S or some other connection between the audio codec and the Bluetooth radio. This means that audio data must be rerouted to bypass the Bluetooth HCI. The Bluetooth HCI which would normally be used on PCs to transmit audio data.

It is important to note that this feature is simply offloading the same functionality that exists in versions of Windows prior to Windows 8.1, so from a user perspective there are no use cases that are different between the Bluetooth hands-free profile (HFP) on SoC and Bluetooth HFP in Windows on a PC or laptop.

The following diagram shows the software and hardware components that work together to provide this new support in Windows 8.1.

![diagram showing the software and hardware components that work together to provide windows support for bluetooth bypass audio streaming.](images/btth-bypass-arch.png)

Note that this Windows feature does not support bypass audio streaming using advanced audio distribution profile (A2DP). Windows 8 provides a separate A2DP profile driver that completely supports audio functionality through the standard Bluetooth HCI without requiring any additional audio drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Architectural%20Overview%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




