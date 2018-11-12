---
title: Managing Dynamic Topologies
description: Managing Dynamic Topologies
ms.assetid: 324c372b-c8d6-4eed-b4ea-071b3d5412b1
keywords:
- dynamic topologies WDK audio
- jack-presence detection WDK audio
- registering subdevices
- dynamic subdevices WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Dynamic Topologies


An audio adapter contains some number of subdevices for servicing external audio devices, such as speakers and microphones, that the user plugs into the adapter's front- or back-panel audio jacks. Each subdevice services a particular audio jack or group of jacks.

The audio driver describes each subdevice by presenting a topology that is essentially a map of the internal connections and processing elements within the subdevice. System-supplied Windows API modules and vendor-supplied control-panel applications use the topology information to determine the capabilities of the subdevice and to identify its internal points of control. For more information, see [Exposing Filter Topology](exposing-filter-topology.md).

WDM audio drivers that were developed before the [IUnregisterSubdevice](https://msdn.microsoft.com/library/windows/hardware/ff537030) and [IUnregisterPhysicalConnection](https://msdn.microsoft.com/library/windows/hardware/ff537022) interfaces became available have mostly static topologies. For these drivers, after the adapter driver creates a miniport driver object to manage a subdevice, that object and its associated subdevice persist for the lifetime of the adapter driver object.

However, in a dynamically configurable audio adapter, the adapter driver can create and delete subdevices at run time to reflect changes in the hardware configuration as the user plugs external devices into audio jacks and removes them. This behavior allows subdevices to operate as logically independent hardware functions. In other words, each subdevice can be powered up, configured, and shut down independently of the other subdevices.

Each subdevice has an internal topology that consists of the following:

-   The data paths through the subdevice.

-   The topology nodes (for example, volume control) that process the data streams that flow along the data paths.

-   The subdevice's physical connections to other subdevices in the same adapter.

When an adapter driver dynamically removes a subdevice, it frees the hardware resources that are bound to the subdevice's internal topology. The adapter driver can then use these resources to create a new subdevice with a possibly different topology.

When configuring a new audio subdevice, the adapter driver registers the subdevice's driver interface as an instance of one or more [device interface classes](https://msdn.microsoft.com/library/windows/hardware/ff541339), and the I/O manager adds one or more registry entries that contain symbolic links associating the interface classes and interface instances. To access the subdevice, a user-mode client retrieves the symbolic link from the registry and passes it as a call parameter to the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function. Typically, the client is a Windows API module, such as Dsound.dll or Wdmaud.drv, or a vendor-supplied control panel or audio utility program. For more information about **CreateFile**, see the Microsoft Windows SDK documentation.

When the miniport driver calls the [**IUnregisterSubdevice::UnregisterSubdevice**](https://msdn.microsoft.com/library/windows/hardware/ff537032) method to remove a subdevice, the PortCls system driver (Portcls.sys) tells the I/O manager to remove the symbolic link for the associated device interface from the registry. Components that are registered for device interface removal events receive notification when the interface is removed.

The audio adapter can contain jack-presence circuitry to notify the miniport driver when a plug is inserted into or removed from an audio jack. When the user inserts a plug into an audio jack, the adapter driver adds the device interface of the associated subdevice to the registry. When the user removes a plug from an audio jack, the adapter driver removes the corresponding device interface from the registry.

Audio adapters that support dynamic topologies have the following benefits:

-   User friendly

    Unless desktop speakers, headphones, and other external audio devices are actually plugged into audio jacks on the audio adapter's front or rear panels, the system does not present these devices to audio applications as available for use.

-   Power efficient

    When the user removes a plug from an audio jack, the driver can power down the portion of the adapter circuitry that services that jack.

-   Configurable

    After removing a subdevice, the driver can use the hardware resources that were bound to the subdevice's internal topology to create a new subdevice with a possibly different topology.

 

 




