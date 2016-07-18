---
title: Resource List Objects
description: Resource List Objects
ms.assetid: a7f18d28-b78f-4b00-8cbb-9f62f5e88dfd
keywords: ["helper objects WDK audio , resource list objects", "resource list objects WDK audio", "IResourceList", "configuration resource lists WDK audio", "startup time resource assignments WDK audio", "hardware resource assignments WDK audio", "start up resource assignments WDK audio", "start-device routines WDK audio"]
---

# Resource List Objects


## <span id="resource_list_objects"></span><span id="RESOURCE_LIST_OBJECTS"></span>


The PortCls system driver implements the [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976) interface for the benefit of miniport drivers. An IResourceList object represents a configuration resource list, which is a list of the system hardware resources that the Plug and Play manager assigns to a device at device-startup time. For more information about resource assignment at startup time, see [Starting a Device in a Function Driver](https://msdn.microsoft.com/library/windows/hardware/ff563856).

A resource list contains the following types of resources:

-   Interrupt vectors

-   DMA channels

-   I/O port addresses

-   Blocks of bus-relative memory addresses

For information about resource types, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).

An [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976) object encapsulates both the translated and untranslated (or "raw") versions of a resource list. For more information about translated and untranslated resources, see [Mapping Bus-Relative Addresses to Virtual Addresses](https://msdn.microsoft.com/library/windows/hardware/ff554399).

The [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976) interface supports the following methods:

[**IResourceList::AddEntry**](https://msdn.microsoft.com/library/windows/hardware/ff536978)

[**IResourceList::AddEntryFromParent**](https://msdn.microsoft.com/library/windows/hardware/ff536981)

[**IResourceList::FindTranslatedEntry**](https://msdn.microsoft.com/library/windows/hardware/ff536982)

[**IResourceList::FindUntranslatedEntry**](https://msdn.microsoft.com/library/windows/hardware/ff536984)

[**IResourceList::NumberOfEntries**](https://msdn.microsoft.com/library/windows/hardware/ff536986)

[**IResourceList::NumberOfEntriesOfType**](https://msdn.microsoft.com/library/windows/hardware/ff536988)

[**IResourceList::TranslatedList**](https://msdn.microsoft.com/library/windows/hardware/ff536990)

[**IResourceList::UntranslatedList**](https://msdn.microsoft.com/library/windows/hardware/ff536991)

Header file Portcls.h defines set of macros to simplify the handling of resource-list objects. These macros generate calls to the [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976) methods. For more information, see IResourceList.

In addition, Portcls.h defines a pair of functions for creating resource lists:

[**PcNewResourceList**](https://msdn.microsoft.com/library/windows/hardware/ff537717)

[**PcNewResourceSublist**](https://msdn.microsoft.com/library/windows/hardware/ff537718)

To start up the devices on an audio adapter card, the operating system calls the adapter driver's start-device routine (see [Startup Sequence](startup-sequence.md)) and passes in a resource list object as an input parameter. This list contains all the system resources that the operating system has assigned to the adapter driver.

In the start-device routine, the adapter driver starts up all of the adapter driver's devices (wave device, MIDI device, and so on). To manage each device, the adapter driver creates a miniport driver object and its associated port driver object. The adapter driver divides up the resources in the resource list among the various devices in the adapter card. For this purpose, the driver typically calls [**PcNewResourceSublist**](https://msdn.microsoft.com/library/windows/hardware/ff537718) to create a resource list object for each device. The driver then calls [**IResourceList::AddEntryFromParent**](https://msdn.microsoft.com/library/windows/hardware/ff536981) as many times as necessary to copy selected resources from the parent list into the various child lists. In addition, the adapter driver might assign some resources to itself.

Next, the start-device routine calls each port driver's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method and passes in the device's resource list object (containing the child list) as an input parameter. Each port driver's **IPort::Init** method calls the corresponding miniport driver's IMiniport*Xxx*::Init method, which is one of the following:

[**IMiniportDMus::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536700)

[**IMiniportMidi::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536709)

[**IMiniportTopology::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536713)

[**IMiniportWaveCyclic::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536722)

[**IMiniportWavePci::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536734)

The [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method passes its resource list object to the IMiniport*Xxx*::Init method as an input parameter. The miniport driver can then make use of the DMA channels, interrupts, and other system resources in the resource list.

For a code example, see the Sb16 sample audio driver in the Microsoft Windows Driver Kit (WDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Resource%20List%20Objects%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




