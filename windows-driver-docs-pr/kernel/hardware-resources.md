---
title: Hardware Resources
description: Hardware Resources
ms.assetid: c7a6997b-34f9-4dd9-b384-2321a8b5ce54
keywords: ["resource descriptors WDK PnP", "PnP WDK kernel , hardware resources", "Plug and Play WDK kernel , hardware resources", "resource requirements lists WDK PnP", "resource lists WDK PnP", "assigned resources WDK PnP", "requirements lists WDK PnP", "registry WDK PnP", "logical configurations WDK PnP", "boot configurations WDK PnP", "forced configurations WDK PnP", "filtered configurations WDK PnP", "override configurations WDK PnP", "configuration types WDK PnP", "allocated configurations WDK PnP", "basic configurations WDK PnP", "Hardware Resources"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Hardware Resources





Hardware resources are the assignable, addressable bus paths that allow peripheral devices and system processors to communicate with each other. Hardware resources typically include I/O port addresses, interrupt vectors, and blocks of bus-relative memory addresses.

Before the system can communicate with a [*device instance*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance), the PnP manager must assign hardware resources to the device instance based on knowledge of which resources are available and which ones the device instance is capable of using. Resources are assigned to each device node in the [device tree](device-tree.md) (assuming that the represented device needs resources and those resources are available). The PnP manager keeps track of hardware resources using lists, which it associates with device nodes. It uses two types of lists:

<a href="" id="resource-requirements-list"></a>*Resource Requirements List*  
Devices are typically designed to operate within ranges of resource assignments. For instance, a device might require only one interrupt vector, but it might be able to use any one of a range of vectors. For each device instance, the PnP manager maintains a *resource requirements list* that specifies all of the ranges of hardware resources in which the device can operate. The list's name stems from the fact that the PnP manager is required to choose resources from this list when assigning them to the device.

Kernel-mode code specifies resource requirements lists using [**IO\_RESOURCE\_REQUIREMENTS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff550609) structures (either as input to system routines or in response to IRPs). User-mode code specifies resource requirements lists using [PnP configuration manager structures](https://msdn.microsoft.com/library/windows/hardware/ff549718) as input to [PnP configuration manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549713).

<a href="" id="resource-list"></a>*Resource List*  
When the PnP manager assigns resources to a device, it keeps track of these assignments by creating a list of assigned resources for each device instance. These lists could be called *resource assignment lists*, but that name is typically shorted to *resource lists*. The PnP manager can change resource list contents as devices are added to or removed from a system and resources are subsequently reallocated. (Resources can also be assigned by a PnP BIOS. Also, installation software—using INF files or user input—can force the PnP manager to assign specific resources to a device.)

Kernel-mode code specifies resource lists by using [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) structures (either as input to system routines or in response to IRPs). User-mode code specifies resource lists using [PnP configuration manager structures](https://msdn.microsoft.com/library/windows/hardware/ff549718) as input to [PnP configuration manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549713).

The PnP manager stores resource requirements lists and resource lists in the registry, where they can be viewed by using Regedit.exe. Drivers can access these lists indirectly through [Plug and Play routines](https://msdn.microsoft.com/library/windows/hardware/ff558809) and [Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807). User-mode applications can use [PnP configuration manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549713). (Drivers and applications must not directly access these lists using registry functions because the storage format is subject to change in a future release.)

### <a href="" id="ddk-logical-configurations-kg"></a>Logical Configurations

Both resource requirements lists and resource lists contain one or more *logical configurations*. Each logical configuration identifies either a range of acceptable resources, or a set of specific resources for a specific [*device instance*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance). Additionally, each logical configuration for a device instance belongs to one of the *logical configuration types*. Configuration types are listed below. Several logical configurations, of the same or different types, might be assigned to each device instance.

### Logical Configuration Types for Resource Requirements Lists

<a href="" id="basic-configuration"></a>*Basic Configuration*  
A resource requirements list identifying resource ranges supplied by a Plug and Play device. A driver should return this list when it receives the [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff551715) IRP. (The basic configuration for a non-PnP device can be described in an INF file. In this case, device installation software reads the INF file and calls [PnP configuration manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549713) to create a requirements list.)

<a href="" id="filtered-configuration"></a>*Filtered Configuration*  
A resource requirements list that has been supplied to a driver stack, possibly modified, then returned by the driver stack, in response to the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874) IRP. The PnP manager uses the resulting filtered configuration as the basis for allocating resources.

<a href="" id="override-configuration"></a>*Override Configuration*  
A resource requirements list that overrides basic configurations. Typically, a device installer creates an override configuration if the device's INF file includes an [**INF DDInstall.LogConfigOverride section**](https://msdn.microsoft.com/library/windows/hardware/ff547339). An override configuration is not removed if its device is physically removed from the system.

### Logical Configuration Types for Resource Lists

<a href="" id="boot-configuration"></a>*Boot Configuration*  
A resource list identifying the resources assigned to a device instance when the system is booted. (For PnP devices, this is the configuration supplied by the BIOS; for non-PnP devices, these resources might be selected by jumpers on the card.) A driver should return this resource list when it receives the [**IRP\_MN\_QUERY\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff551710) IRP. (A boot configuration can be partially empty if the BIOS cannot determine all resources used by a device.) The PnP manager can modify this list if a device is removed or restarted. For non-PnP devices, this configuration type can be used instead of a forced configuration, in which case it has a lower configuration priority than an equivalent forced configuration. Only one boot configuration can exist for each device instance.

<a href="" id="forced-configuration"></a>*Forced Configuration*  
A resource list identifying resources that a device instance must use. A forced configuration prevents the PnP manager from assigning other resources to the device instance. A device installer might create a forced configuration based on information that is either contained in an INF or received from a user. A forced configuration is not removed if its device is physically removed from the system. Only one forced configuration can exist for each device instance.

<a href="" id="allocated-configuration"></a>*Allocated Configuration*  
A resource list identifying resources currently in use by a device instance. Only one allocated configuration can exist for each device instance.

Device drivers are responsible for determining a PnP-compatible device's basic configuration, filtered configuration, and boot configuration, and for returning that information in response to IRPs sent by the PnP manager. (For more information, see [Adding a PnP Device to a Running System](adding-a-pnp-device-to-a-running-system.md).) Driver installation software can create override configurations, forced configurations, and, for non-PnP devices, boot configurations. The PnP manager maintains each device instance's allocated configuration.

A priority is assigned to each configuration when it is created. If the PnP manager finds that a device instance has been assigned several logical configurations of the same type, it attempts to use the one with the highest priority first. If that configuration results in resource conflicts, it tries the configuration with the next lower priority. (For a list of configuration priorities, see [**CM\_Add\_Empty\_Log\_Conf**](https://msdn.microsoft.com/library/windows/hardware/ff537921).)

 

 




