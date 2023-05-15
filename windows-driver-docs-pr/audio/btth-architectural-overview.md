---
title: Windows Bluetooth host controller interface (HCI) architectural overview
description: This article presents an architectural overview of the Windows support for rerouting audio data to bypass the Bluetooth host controller interface (HCI).
ms.date: 04/27/2023
---

# Windows Bluetooth host controller interface (HCI) architectural overview

This article presents an architectural overview of the Windows support for rerouting audio data to bypass the Bluetooth host controller interface (HCI).

Starting with Windows 8.1, the Microsoft operating system has been updated to be compatible with low power system-on-a-chip (SoC) design solutions. Windows supports Intel-based and Arm-based SoC designs. These new low-power devices are optimized for "always on" scenarios, so low battery consumption is a key factor for success.

SoC architectures use the Universal Asynchronous Receiver/Transmitter (UART) transport mode to transmit data to and from the Bluetooth host controller.

Because UARTs can't provide time sensitive data transmission, a synchronous connection oriented (SCO) bypass channel must be implemented in addition to a UART. The SCO bypass channel transfers audio data via I2S or some other connection between the audio codec and the Bluetooth radio. Audio data must be rerouted to bypass the Bluetooth HCI, which would normally be used to transmit audio data on PCs.

This feature is offloading the same functionality that exists in versions of Windows prior to Windows 8.1. From a user perspective, there are no use cases that are different between the Bluetooth hands-free profile (HFP) on SoC and Bluetooth HFP in Windows.

The following diagram shows the software and hardware components that work together to provide this new support in Windows 8.1.

:::image type="content" source="images/btth-bypass-arch.png" alt-text="Diagram showing the software and hardware components that work together to provide Windows support for Bluetooth bypass audio streaming.":::

This Windows feature doesn't support bypass audio streaming using advanced audio distribution profile (A2DP). Windows 8 provides a separate A2DP profile driver that completely supports audio functionality through the standard Bluetooth HCI without requiring any other audio drivers.
