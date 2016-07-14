---
Description: Resource List Objects
MS-HAID: 'audio.resource\_list\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Resource List Objects
---

# Resource List Objects


## <span id="resource_list_objects"></span><span id="RESOURCE_LIST_OBJECTS"></span>


The PortCls system driver implements the [IResourceList](audio.iresourcelist) interface for the benefit of miniport drivers. An IResourceList object represents a configuration resource list, which is a list of the system hardware resources that the Plug and Play manager assigns to a device at device-startup time. For more information about resource assignment at startup time, see [Starting a Device in a Function Driver](kernel.starting_a_device_in_a_function_driver).

A resource list contains the following types of resources:

-   Interrupt vectors

-   DMA channels

-   I/O port addresses

-   Blocks of bus-relative memory addresses

For information about resource types, see [Hardware Resources](kernel.hardware_resources).

An [IResourceList](audio.iresourcelist) object encapsulates both the translated and untranslated (or "raw") versions of a resource list. For more information about translated and untranslated resources, see [Mapping Bus-Relative Addresses to Virtual Addresses](kernel.mapping_bus_relative_addresses_to_virtual_addresses).

The [IResourceList](audio.iresourcelist) interface supports the following methods:

[**IResourceList::AddEntry**](audio.iresourcelist_addentry)

[**IResourceList::AddEntryFromParent**](audio.iresourcelist_addentryfromparent)

[**IResourceList::FindTranslatedEntry**](audio.iresourcelist_findtranslatedentry)

[**IResourceList::FindUntranslatedEntry**](audio.iresourcelist_finduntranslatedentry)

[**IResourceList::NumberOfEntries**](audio.iresourcelist_numberofentries)

[**IResourceList::NumberOfEntriesOfType**](audio.iresourcelist_numberofentriesoftype)

[**IResourceList::TranslatedList**](audio.iresourcelist_translatedlist)

[**IResourceList::UntranslatedList**](audio.iresourcelist_untranslatedlist)

Header file Portcls.h defines set of macros to simplify the handling of resource-list objects. These macros generate calls to the [IResourceList](audio.iresourcelist) methods. For more information, see IResourceList.

In addition, Portcls.h defines a pair of functions for creating resource lists:

[**PcNewResourceList**](audio.pcnewresourcelist)

[**PcNewResourceSublist**](audio.pcnewresourcesublist)

To start up the devices on an audio adapter card, the operating system calls the adapter driver's start-device routine (see [Startup Sequence](startup-sequence.md)) and passes in a resource list object as an input parameter. This list contains all the system resources that the operating system has assigned to the adapter driver.

In the start-device routine, the adapter driver starts up all of the adapter driver's devices (wave device, MIDI device, and so on). To manage each device, the adapter driver creates a miniport driver object and its associated port driver object. The adapter driver divides up the resources in the resource list among the various devices in the adapter card. For this purpose, the driver typically calls [**PcNewResourceSublist**](audio.pcnewresourcesublist) to create a resource list object for each device. The driver then calls [**IResourceList::AddEntryFromParent**](audio.iresourcelist_addentryfromparent) as many times as necessary to copy selected resources from the parent list into the various child lists. In addition, the adapter driver might assign some resources to itself.

Next, the start-device routine calls each port driver's [**IPort::Init**](audio.iport_init) method and passes in the device's resource list object (containing the child list) as an input parameter. Each port driver's **IPort::Init** method calls the corresponding miniport driver's IMiniport*Xxx*::Init method, which is one of the following:

[**IMiniportDMus::Init**](audio.iminiportdmus_init)

[**IMiniportMidi::Init**](audio.iminiportmidi_init)

[**IMiniportTopology::Init**](audio.iminiporttopology_init)

[**IMiniportWaveCyclic::Init**](audio.iminiportwavecyclic_init)

[**IMiniportWavePci::Init**](audio.iminiportwavepci_init)

The [**IPort::Init**](audio.iport_init) method passes its resource list object to the IMiniport*Xxx*::Init method as an input parameter. The miniport driver can then make use of the DMA channels, interrupts, and other system resources in the resource list.

For a code example, see the Sb16 sample audio driver in the Microsoft Windows Driver Kit (WDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Resource%20List%20Objects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



