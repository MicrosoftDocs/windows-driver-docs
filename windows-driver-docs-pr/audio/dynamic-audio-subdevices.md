---
title: Dynamic Audio Subdevices
description: Dynamic Audio Subdevices
ms.assetid: d8ebd6d9-37ed-4890-aae1-5ecf58f2e22a
keywords:
- WDM audio drivers WDK , dynamic subdevices
- audio drivers WDK , dynamic subdevices
- dynamic audio subdevices WDK audio
- subdevices WDK audio
- audio codec WDK
- jack-presence detection WDK audio
- removing subdevices
- deleting subdevices
- unregistering subdevices
- dynamic subdevices WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Audio Subdevices


Some audio adapters can dynamically change their internal topologies at run time. By using the system-supplied capabilities in the PortCls system driver (Portcls.sys), adapter drivers can provide software support for dynamically configurable audio hardware.

For example, the [Intel High Definition Audio Specification](https://go.microsoft.com/fwlink/p/?linkid=42508) uses the term audio codec to refer to an integrated audio adapter that connects to a High Definition Audio (HD Audio) controller through an HD Audio Link interface. A typical audio codec supports jack-presence detection: when a plug is inserted into or removed from a jack, the hardware generates an interrupt to notify the driver of the change in the hardware configuration. For example, the driver responds to the insertion of a plug into the headphones jack by creating a [KS filter](https://msdn.microsoft.com/library/windows/hardware/ff567644) to represent the audio subdevice for the headphones. The driver assigns hardware resources to the filter (for example, headphones might require a volume control and a digital-to-analog converter, or DAC) and registers the filter as an audio device. When the user unplugs the headphones, the driver responds by freeing the resources, deleting the filter, and removing it from the registry.

This behavior ensures that when an audio application checks to see which audio devices are registered, it finds only the devices that are currently plugged in. If a device is unplugged, it does not appear in the registry.

In Windows Vista, Windows Server 2003 with Service Pack 1 (SP1), and Windows XP with Service Pack 2 (SP2), PortCls supports the [IUnregisterSubdevice](https://msdn.microsoft.com/library/windows/hardware/ff537030) and [IUnregisterPhysicalConnection](https://msdn.microsoft.com/library/windows/hardware/ff537022) interfaces. Audio adapter drivers use these two interfaces to delete audio subdevices that are no longer in use. Earlier versions of Windows, including Windows Server 2003 and Windows XP, do not support these interfaces. In these earlier versions of Windows, subdevices can be created but not deleted--once a subdevice is created, it exists for the lifetime of the adapter driver object.

The **IUnregisterSubdevice** interface contains a single method that the adapter driver can use to "unregister" a subdevice that the driver registered through a previous call to the [**PcRegisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537731) routine:

[**IUnregisterSubdevice::UnregisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537032)

The **IUnregisterPhysicalConnection** interface contains three methods that the adapter driver can use to unregister physical connections between subdevices:

[**IUnregisterPhysicalConnection::UnregisterPhysicalConnection**](https://msdn.microsoft.com/library/windows/hardware/ff537024)

[**IUnregisterPhysicalConnection::UnregisterPhysicalConnectionFromExternal**](https://msdn.microsoft.com/library/windows/hardware/ff537027)

[**IUnregisterPhysicalConnection::UnregisterPhysicalConnectionToExternal**](https://msdn.microsoft.com/library/windows/hardware/ff537029)

These methods remove connections that the driver registered through previous calls to the [**PcRegisterPhysicalConnection**](https://msdn.microsoft.com/library/windows/hardware/ff537726), [**PcRegisterPhysicalConnectionFromExternal**](https://msdn.microsoft.com/library/windows/hardware/ff537728), and [**PcRegisterPhysicalConnectionToExternal**](https://msdn.microsoft.com/library/windows/hardware/ff537729) routines. PortCls stores the information from a PcRegisterPhysicalConnection*Xxx* call so that the port driver can subsequently use the information to respond to the [**KSPROPERTY\_PIN\_PHYSICALCONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff565205) property requests. When deleting a subdevice from an adapter's topology, the driver must unregister the subdevice's physical connections to that portion of the topology. Failure to unregister the subdevice's physical connections can cause memory leaks. PortCls supports the PcRegister*Xxx* routines in Windows 2000 and later and in Windows Me/98.

The following topics in this section describe how to implement driver support for adapters with dynamic topologies:

[Managing Dynamic Topologies](managing-dynamic-topologies.md)

[Driver Support for Dynamic Subdevices](driver-support-for-dynamic-subdevices.md)

[Jack Descriptions for Dynamic Audio Subdevices](jack-descriptions-for-dynamic-audio-subdevices.md)

 

 




