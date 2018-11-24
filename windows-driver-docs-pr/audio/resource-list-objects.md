---
title: Resource List Objects
description: Resource List Objects
ms.assetid: a7f18d28-b78f-4b00-8cbb-9f62f5e88dfd
keywords:
- helper objects WDK audio , resource list objects
- resource list objects WDK audio
- IResourceList
- configuration resource lists WDK audio
- startup time resource assignments WDK audio
- hardware resource assignments WDK audio
- start up resource assignments WDK audio
- start-device routines WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




