---
title: Audio Helper Object Interfaces
description: Audio Helper Object Interfaces
ms.assetid: 94d3f7f3-7ccc-4f66-b5fa-95f18b8a0f17
---

# Audio Helper Object Interfaces


## <span id="ddk_audio_helper_object_interfaces_ks"></span><span id="DDK_AUDIO_HELPER_OBJECT_INTERFACES_KS"></span>


The Port Class Library (portcls.sys) implements a variety of helper objects that provide functionality that is of general use to adapter drivers. These helper objects provide mechanisms for managing DMA channels, interrupt requests, registry access, resource lists, digital rights, and hardware events. This section provides details on the interfaces that are exposed by those objects.

The following interfaces are described in this section:

[IDmaChannel](https://msdn.microsoft.com/library/windows/hardware/ff536547)

Used to manage a DMA channel for a master or subordinate device. The channel has an associated common buffer and usage parameters.

[IDmaChannelSlave](https://msdn.microsoft.com/library/windows/hardware/ff536548)

A DMA channel with specialized operations for subordinate devices.

[IDmaOperations](https://msdn.microsoft.com/library/windows/hardware/ff536566)

Encapsulates the DMA operations that are accessed through the table of function pointers in a [**DMA\_OPERATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff544071) structure.

[IDrmPort](https://msdn.microsoft.com/library/windows/hardware/ff536571)

Helps a miniport driver keep track of composite DRM rights.

[IDrmPort2](https://msdn.microsoft.com/library/windows/hardware/ff536573)

Helps a miniport driver keep track of composite DRM rights. This is an extended version of **IDrmPort**.

[IInterruptSync](https://msdn.microsoft.com/library/windows/hardware/ff536590)

A synchronization mechanism for coordinating shared access to interrupt service requests.

[IMasterClock](https://msdn.microsoft.com/library/windows/hardware/ff536696)

Provides DirectMusic streams with access to the current reference time from the master clock.

[**IPortClsEtwHelper**](https://msdn.microsoft.com/library/windows/hardware/dn265123)

Used by a miniport driver to access Event Tracing for Windows (ETW) helper functions.
[IPortClsVersion](https://msdn.microsoft.com/library/windows/hardware/ff536877)

Identifies the version of the Microsoft Windows operating system that the driver is running on.

[IPortEvents](https://msdn.microsoft.com/library/windows/hardware/ff536884)

Used by a miniport driver to notify a port driver of hardware events.

[IPreFetchOffset](https://msdn.microsoft.com/library/windows/hardware/ff536951)

Sets the prefetch offset, which is the number of bytes of data separating the write cursor from the play cursor in a Microsoft DirectSound hardware buffer.

[IRegistryKey](https://msdn.microsoft.com/library/windows/hardware/ff536965)

Provides read/write access to a registry key and its subkeys.

[IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976)

Specifies a list of resources such as I/O ports, DMA channels, and interrupts.

[IServiceGroup](https://msdn.microsoft.com/library/windows/hardware/ff536994)

Used to demultiplex interrupt service requests to a list of objects with [IServiceSink](https://msdn.microsoft.com/library/windows/hardware/ff537006) interfaces.

[IServiceSink](https://msdn.microsoft.com/library/windows/hardware/ff537006)

Represents the target of an interrupt service request.

[IUnregisterPhysicalConnection](https://msdn.microsoft.com/library/windows/hardware/ff537022)

Deletes the registration of a physical connection between two subdevices in the same audio adapter or in two different adapters.

[IUnregisterSubdevice](https://msdn.microsoft.com/library/windows/hardware/ff537030)

Deletes the registration of a dynamic subdevice in an audio adapter.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Helper%20Object%20Interfaces%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




