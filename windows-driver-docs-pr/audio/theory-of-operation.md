---
title: Theory of Operation
description: This theory of operation topic explains the theory behind the inner working of the new Windows 8.1.
ms.assetid: 5897946A-5319-404B-BE9E-91FF8801652F
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Theory of Operation


This theory of operation topic explains the theory behind the inner working of the new Windows 8.1 support for Bluetooth bypass audio streaming.

When Bluetooth audio is in bypass mode, the audio control path flows through some other hardware connection to the Bluetooth controller, rather than through the host controller interface (HCI). This other hardware connection is often I2S, but can be any interface determined by the Bluetooth host controller. This set of topics refers to this connection as a “bypass” or “sideband” connection.

While audio I/O occurs through the bypass connection, the over-the-air synchronous connection oriented (SCO) audio stream is still managed through the HCI. Windows 8 provides a Bluetooth Hands-Free profile (HFP) driver to hide most of the complexities of managing the SCO connection and other aspects of the Hands-Free profile. However a custom audio driver controls audio data I/O between Windows and the bypass connection.

The separation of roles between the HFP driver and the custom control driver for audio I/O data, means that efficient communication must be established between the Windows HFP driver and the custom audio driver. This communication is handled by a set of IOCTLs that are passed from the custom audio driver to the Windows HFP driver.

Typically the bypass connection itself is always present. The PnP service always enumerates the hardware that includes this connection, and then loads the required audio driver. However, the audio system may or may not have any HFP headsets paired and the bypass connection is only useful if at least one HFP headset is paired.

For each paired HFP device, the Windows HFP driver registers and enables a device interface in the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS interface class. So the following conditions are true for HFP devices:

-   When Windows activates the HFP driver (normally during boot up), the HFP driver registers and enables an interface for each paired HFP device.

-   When an HFP device is first paired, with Windows already up and running, the HFP driver registers and enables an interface for the device.

-   If there are n paired HFP devices, the Windows HFP driver registers n instances of the device interface.

-   When a paired HFP device is removed, the Windows HFP driver disables the device interface.

-   When Windows stops the HFP driver (normally during shutdown or reboot), the HFP driver disables the interface for each paired HFP device.

-   The audio driver must handle multiple arrivals and removals of interfaces at any time, not just during startup or shutdown.

The following topics provide more information about the connection life cycle and some design features of an HFP device and its audio driver.

[HFP Device Startup](startup.md)

[HFP Device Connection](hfp-device-connection.md)

[HFP Device Removal](removal.md)

[Kernel Streaming Considerations](kernel-streaming-considerations.md)

[Audio Endpoint Container ID](audio-endpoint-container-id.md)

[Management of I2S and SCO Resources](management-of-i2s-and-sco-resources.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Theory%20of%20Operation%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


