---
title: System-Wide Unique Device IDs
description: System-Wide Unique Device IDs
ms.assetid: 628577b6-05fe-4b63-929f-6d63e93c9266
keywords:
- audio adapters WDK , unique device IDs
- adapter drivers WDK audio , unique device IDs
- Port Class audio adapters WDK , unique device IDs
- MF bus drivers WDK audio
- system-supplied multifunction devices WDK audio
- multifunction audio devices WDK , audio adapters
- unique device IDs WDK audio
- device IDs WDK audio
- identifying device IDs
- subdevices WDK audio
- proprietary bus drivers WDK audio
- device-ID strings WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Wide Unique Device IDs


## <span id="system_wide_unique_device_ids"></span><span id="SYSTEM_WIDE_UNIQUE_DEVICE_IDS"></span>


A driver for a typical audio adapter should easily be able to support several instances of the same audio adapter card in a system. Nearly all the data structures that a driver maintains are stored in the device-extension buffer (see the description of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure's **DeviceExtension** field). If several instances of a driver share any global data, however, those instances should synchronize their access to this data.

One additional requirement is that each subdevice on a particular instance of an adapter card should have a [device-ID string](https://msdn.microsoft.com/library/windows/hardware/ff541224) that uniquely identifies the subdevice across all instances of the same adapter card in the system.

The most straightforward way to accomplish this is to expose each subdevice on the adapter card as a logically distinct device to the Plug and Play manager. This is presented as option (1) in [Multifunction Audio Devices](multifunction-audio-devices.md).

A second approach is to use the system-supplied multifunction bus driver to manage the subdevices on the adapter card. The MF bus driver assigns to each subdevice a device ID that is guaranteed to be unique across the system, even if the system contains several instances of the same adapter card. The MF bus driver accommodates designs in which the subdevices share a common set of configuration registers but each subdevice has its own set of PCI base-address registers. The subdevices should have no hidden dependencies on each other and should be able to operate concurrently without interfering with each other or with other devices in the system. This is option (2) in [Multifunction Audio Devices](multifunction-audio-devices.md).

A third approach is to use a proprietary bus driver to manage the subdevices on an adapter card. This is frequently necessary if the subdevices have mutual dependencies that must be managed centrally. Such dependencies can occur in a couple of ways:

-   The subdevices might share some on-card resource. For example, if the subdevices share a digital signal processor (DSP), the bus driver might need to download the proprietary operating system that runs on the DSP before starting up the first subdevice.

-   A design flaw might cause a dependency among subdevices. For example, a design flaw might require the subdevices to be powered up or down in a particular sequence.

When either type of dependency exists, a proprietary bus driver is nearly always a better solution than presenting the subdevices directly to the Plug and Play manager and attempting to hide the dependency.

If you provide your own bus driver for an adapter card, you should ensure that the device IDs that your bus driver assigns are unique across the system.

A bus driver provides a device ID for one of its children in response to an [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) query from the Plug and Play manager. The ID can be specified in one of two ways, which the bus driver indicates in its response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) query by setting the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure's **UniqueID** field to **TRUE** or **FALSE**:

-   **UniqueID** = **TRUE**

    This means that the name of the child is guaranteed to be unique throughout the system. The device ID string contains a device ID plus an instance ID, which is a serial number that uniquely identifies the hardware instance.

-   **UniqueID** = **FALSE**

    This means that the name of the child is unique only with respect to the parent. Most devices use this means of identification. In this case, the Plug and Play manager extends the device-ID string that it receives to make it unique through the system. The extended string is a function of the parent device's unique ID.

All audio bus drivers should set **UniqueID** = **FALSE** for their children. This causes the Plug and Play manager to extend the child's device ID string by adding information about the device's parent to make the ID unique on the machine.

 

 




