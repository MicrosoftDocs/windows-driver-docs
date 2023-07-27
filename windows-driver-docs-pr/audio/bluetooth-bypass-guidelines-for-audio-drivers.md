---
title: Bluetooth bypass guidelines for audio drivers
description: Learn how to reroute audio data past the Bluetooth host controller interface (HCI) for processing in system-on-a-chip (SoC) solutions.
ms.date: 07/27/2023
---

# Bluetooth bypass guidelines for audio drivers

This article presents Bluetooth bypass design guidelines for audio driver developers, demonstrating how to reroute audio data past the Bluetooth host controller interface (HCI) for processing in system-on-a-chip (SoC) solutions.

Bluetooth bypass audio data streaming support was introduced in Windows 8.1.

Windows is compatible with low-power Intel-based and Arm-based SoC designs, optimized for "always on" scenarios where low battery consumption is crucial.

SoC architectures use the Universal Asynchronous Receiver/Transmitter (UART) transport mode to transmit data to and from the Bluetooth host controller. Since UARTs can't provide time-sensitive data transmission, a synchronous connection-oriented (SCO) bypass channel must be implemented alongside a UART. The SCO bypass channel transfers audio data via I2S or another connection between the audio codec and the Bluetooth radio, bypassing the Bluetooth HCI typically used to transmit audio data on PCs.

This feature offloads functionality present in Windows versions prior to 8.1. From a user perspective, there are no use case differences between Bluetooth hands-free profile (HFP) on SoC and Bluetooth HFP in Windows.

The following diagram illustrates the software and hardware components that work together to provide this support.

:::image type="content" source="images/btth-bypass-arch.png" alt-text="Diagram showing the software and hardware components that work together to provide Windows support for Bluetooth bypass audio streaming.":::

This Windows feature doesn't support bypass audio streaming using advanced audio distribution profile (A2DP). Windows 8 provides a separate A2DP profile driver that fully supports audio functionality through the standard Bluetooth HCI without requiring additional audio drivers.

## Bluetooth bypass DDI reference

The Bluetooth bypass device driver interface (DDI) reference is a set of topics that detail the structures and IOCTLs introduced in Windows 8.1 to provide support for a Bluetooth Hands-free profile (HFP) driver.

For detailed information about the DDI members, see [Bluetooth HFP DDI Reference](./bluetooth-hfp-ddi-reference.md).

## Related topics

- [Bluetooth bypass guidelines for audio drivers](bluetooth-bypass-guidelines-for-audio-drivers.md)
- [Theory of Bluetooth bypass audio streaming](theory-of-operation.md)
- [Bluetooth Low Energy (LE) Audio](../bluetooth/bluetooth-low-energy-audio.md)
