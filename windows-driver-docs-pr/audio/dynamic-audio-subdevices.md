---
Description: Dynamic Audio Subdevices
MS-HAID: 'audio.dynamic\_audio\_subdevices'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Dynamic Audio Subdevices
---

# Dynamic Audio Subdevices


Some audio adapters can dynamically change their internal topologies at run time. By using the system-supplied capabilities in the PortCls system driver (Portcls.sys), adapter drivers can provide software support for dynamically configurable audio hardware.

For example, the [Intel High Definition Audio Specification](http://go.microsoft.com/fwlink/p/?linkid=42508) uses the term audio codec to refer to an integrated audio adapter that connects to a High Definition Audio (HD Audio) controller through an HD Audio Link interface. A typical audio codec supports jack-presence detection: when a plug is inserted into or removed from a jack, the hardware generates an interrupt to notify the driver of the change in the hardware configuration. For example, the driver responds to the insertion of a plug into the headphones jack by creating a [KS filter](stream.ks_filters) to represent the audio subdevice for the headphones. The driver assigns hardware resources to the filter (for example, headphones might require a volume control and a digital-to-analog converter, or DAC) and registers the filter as an audio device. When the user unplugs the headphones, the driver responds by freeing the resources, deleting the filter, and removing it from the registry.

This behavior ensures that when an audio application checks to see which audio devices are registered, it finds only the devices that are currently plugged in. If a device is unplugged, it does not appear in the registry.

In Windows Vista, Windows Server 2003 with Service Pack 1 (SP1), and Windows XP with Service Pack 2 (SP2), PortCls supports the [IUnregisterSubdevice](audio.iunregistersubdevice) and [IUnregisterPhysicalConnection](audio.iunregisterphysicalconnection) interfaces. Audio adapter drivers use these two interfaces to delete audio subdevices that are no longer in use. Earlier versions of Windows, including Windows Server 2003 and Windows XP, do not support these interfaces. In these earlier versions of Windows, subdevices can be created but not deleted--once a subdevice is created, it exists for the lifetime of the adapter driver object.

The **IUnregisterSubdevice** interface contains a single method that the adapter driver can use to "unregister" a subdevice that the driver registered through a previous call to the [**PcRegisterSubdevice**](audio.pcregistersubdevice) routine:

[**IUnregisterSubdevice::UnregisterSubdevice**](audio.iunregistersubdevice_unregistersubdevice)

The **IUnregisterPhysicalConnection** interface contains three methods that the adapter driver can use to unregister physical connections between subdevices:

[**IUnregisterPhysicalConnection::UnregisterPhysicalConnection**](audio.iunregisterphysicalconnection_unregisterphysicalconnection)

[**IUnregisterPhysicalConnection::UnregisterPhysicalConnectionFromExternal**](audio.iunregisterphysicalconnection_unregisterphysicalconnectionfromexternal)

[**IUnregisterPhysicalConnection::UnregisterPhysicalConnectionToExternal**](audio.iunregisterphysicalconnection_unregisterphysicalconnectiontoexternal)

These methods remove connections that the driver registered through previous calls to the [**PcRegisterPhysicalConnection**](audio.pcregisterphysicalconnection), [**PcRegisterPhysicalConnectionFromExternal**](audio.pcregisterphysicalconnectionfromexternal), and [**PcRegisterPhysicalConnectionToExternal**](audio.pcregisterphysicalconnectiontoexternal) routines. PortCls stores the information from a PcRegisterPhysicalConnection*Xxx* call so that the port driver can subsequently use the information to respond to the [**KSPROPERTY\_PIN\_PHYSICALCONNECTION**](stream.ksproperty_pin_physicalconnection) property requests. When deleting a subdevice from an adapter's topology, the driver must unregister the subdevice's physical connections to that portion of the topology. Failure to unregister the subdevice's physical connections can cause memory leaks. PortCls supports the PcRegister*Xxx* routines in Windows 2000 and later and in Windows Me/98.

The following topics in this section describe how to implement driver support for adapters with dynamic topologies:

[Managing Dynamic Topologies](managing-dynamic-topologies.md)

[Driver Support for Dynamic Subdevices](driver-support-for-dynamic-subdevices.md)

[Jack Descriptions for Dynamic Audio Subdevices](jack-descriptions-for-dynamic-audio-subdevices.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Dynamic%20Audio%20Subdevices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



