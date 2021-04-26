---
title: Resource List Objects
description: Resource List Objects
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


The PortCls system driver implements the [IResourceList](/windows-hardware/drivers/ddi/portcls/nn-portcls-iresourcelist) interface for the benefit of miniport drivers. An IResourceList object represents a configuration resource list, which is a list of the system hardware resources that the Plug and Play manager assigns to a device at device-startup time. For more information about resource assignment at startup time, see [Starting a Device in a Function Driver](../kernel/starting-a-device-in-a-function-driver.md).

A resource list contains the following types of resources:

-   Interrupt vectors

-   DMA channels

-   I/O port addresses

-   Blocks of bus-relative memory addresses

For information about resource types, see [Hardware Resources](../kernel/hardware-resources.md).

An [IResourceList](/windows-hardware/drivers/ddi/portcls/nn-portcls-iresourcelist) object encapsulates both the translated and untranslated (or "raw") versions of a resource list. For more information about translated and untranslated resources, see [Mapping Bus-Relative Addresses to Virtual Addresses](../kernel/mapping-bus-relative-addresses-to-virtual-addresses.md).

The [IResourceList](/windows-hardware/drivers/ddi/portcls/nn-portcls-iresourcelist) interface supports the following methods:

[**IResourceList::AddEntry**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-addentry)

[**IResourceList::AddEntryFromParent**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-addentryfromparent)

[**IResourceList::FindTranslatedEntry**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-findtranslatedentry)

[**IResourceList::FindUntranslatedEntry**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-finduntranslatedentry)

[**IResourceList::NumberOfEntries**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-numberofentries)

[**IResourceList::NumberOfEntriesOfType**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-numberofentriesoftype)

[**IResourceList::TranslatedList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-translatedlist)

[**IResourceList::UntranslatedList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-untranslatedlist)

Header file Portcls.h defines set of macros to simplify the handling of resource-list objects. These macros generate calls to the [IResourceList](/windows-hardware/drivers/ddi/portcls/nn-portcls-iresourcelist) methods. For more information, see IResourceList.

In addition, Portcls.h defines a pair of functions for creating resource lists:

[**PcNewResourceList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcelist)

[**PcNewResourceSublist**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcesublist)

To start up the devices on an audio adapter card, the operating system calls the adapter driver's start-device routine (see [Startup Sequence](startup-sequence.md)) and passes in a resource list object as an input parameter. This list contains all the system resources that the operating system has assigned to the adapter driver.

In the start-device routine, the adapter driver starts up all of the adapter driver's devices (wave device, MIDI device, and so on). To manage each device, the adapter driver creates a miniport driver object and its associated port driver object. The adapter driver divides up the resources in the resource list among the various devices in the adapter card. For this purpose, the driver typically calls [**PcNewResourceSublist**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcesublist) to create a resource list object for each device. The driver then calls [**IResourceList::AddEntryFromParent**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iresourcelist-addentryfromparent) as many times as necessary to copy selected resources from the parent list into the various child lists. In addition, the adapter driver might assign some resources to itself.

Next, the start-device routine calls each port driver's [**IPort::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-init) method and passes in the device's resource list object (containing the child list) as an input parameter. Each port driver's **IPort::Init** method calls the corresponding miniport driver's IMiniport*Xxx*::Init method, which is one of the following:

[**IMiniportDMus::Init**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-init)

[**IMiniportMidi::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-init)

[**IMiniportTopology::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiporttopology-init)

[**IMiniportWaveCyclic::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavecyclic-init)

[**IMiniportWavePci::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-init)

The [**IPort::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-init) method passes its resource list object to the IMiniport*Xxx*::Init method as an input parameter. The miniport driver can then make use of the DMA channels, interrupts, and other system resources in the resource list.

For a code example, see the Sb16 sample audio driver in the Microsoft Windows Driver Kit (WDK).

 

