---
title: Bluetooth Hands-Free Profile (HFP) Bypass Audio Streaming
description: This article explains the operation and theory of Bluetooth hands-free profile (HFP) bypass audio streaming.
ms.date: 07/27/2023
---

# Bluetooth HFP bypass audio streaming

This article explains the operation and theory of Bluetooth hands-free profile (HFP) bypass audio streaming.

In bypass mode, Bluetooth audio control path flows through a hardware connection other than the host controller interface (HCI), such as I2S, to the Bluetooth controller. This other hardware connection is often I2S, but can be any interface determined by the Bluetooth host controller. This connection is referred to as a "bypass" or "sideband" connection.

While audio I/O occurs through the bypass connection, the over-the-air synchronous connection oriented (SCO) audio stream is still managed through the HCI. Windows 8 provides a Bluetooth Hands-Free Profile (HFP) driver to simplify managing the SCO connection and other aspects of the Hands-Free Profile. However, a custom audio driver controls audio data I/O between Windows and the bypass connection.

The HFP driver and the custom control driver for audio I/O data have separate roles, requiring efficient communication between them. This communication is handled by a set of IOCTLs passed from the custom audio driver to the Windows HFP driver.

Typically, the bypass connection is always present. The Plug and Play (PnP) service enumerates the hardware that includes this connection and loads the required audio driver. However, the audio system may or may not have any HFP headsets paired, and the bypass connection is only useful if at least one HFP headset is paired.

For each paired HFP device, the Windows HFP driver registers and enables a device interface in the GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS interface class. The following conditions apply to HFP devices:

- When Windows activates the HFP driver (usually during boot up), the HFP driver registers and enables an interface for each paired HFP device.
- When an HFP device is first paired with Windows already running, the HFP driver registers and enables an interface for the device.
- If there are n paired HFP devices, the Windows HFP driver registers n instances of the device interface.
- When a paired HFP device is removed, the Windows HFP driver disables the device interface.
- When Windows stops the HFP driver (usually during shutdown or reboot), the HFP driver disables the interface for each paired HFP device.
- The audio driver must handle multiple arrivals and removals of interfaces at any time, not just during startup or shutdown.

## Managing I2S and SCO resources

This section discusses the assumptions made in the design of Bluetooth bypass audio streaming support.

Currently, Windows assumes there's only one Bluetooth host controller. Additionally, the Hands-Free Profile (HFP) synchronous connection-oriented (SCO) bypass support assumes there's only one bypass connection, and any channel opened through the HFP device driver interface is associated with that single connection.

Audio drivers should arbitrate this channel and the single bypass connection for a single consumer on a first-come, first-serve basis. The simplest way to achieve this is for the driver to allow only a single filter to transition its pins to the ACQUIRE state.

## See also

The following topics provide more information about the connection life cycle and some design features of an HFP device and its audio driver:

- [HFP device startup](startup.md)
- [HFP device connection](hfp-device-connection.md)
- [HFP device removal](removal.md)
- [Kernel streaming considerations](kernel-streaming-considerations.md)
- [Audio endpoint container ID](audio-endpoint-container-id.md)
- [Bluetooth Low Energy (LE) Audio](../bluetooth/bluetooth-low-energy-audio.md)
