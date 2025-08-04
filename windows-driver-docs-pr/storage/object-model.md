---
title: Object Model (Windows Drivers)
description: Learn more about the Object Model.
ms.date: 11/21/2024
ms.topic: concept-article
---

# Object Model

## High-Level Object Definition

The following table describes the objects exposed by the [Windows Storage Management API](windows-storage-management-api-portal.md) and their respective definitions. It includes objects that are visible to both Windows hosts and Storage Management Providers (SMPs), and objects that are host-side only.

| Object | Definition |
| ------ | ---------- |
| StorageProvider  | Enables administration of storage subsystems (StorageSubsystem) through a common management API by using an SMP. Examples of a StorageProvider include the Storage Spaces SMP, a non-Microsoft SMP, or a non-Microsoft SMI-S provider. |
| StorageSubsystem | Exposes VirtualDisks to Windows. A StorageSubsystem responds to administrative commands through a corresponding StorageProvider. |
| MaskingSet       | Contains VirtualDisks, TargetPorts, and InitiatorPorts, and is used for bulk mask/unmask operations. |
| TargetPort       | Represents an instance of an endpoint in a StorageSubsystem with associated properties for Show/Hide (Mask/Unmask) and MaskingSet usage. Examples of TargetPorts are FC, SAS, or iSCSI ports on corresponding controllers, present in StorageSubsystems. |
| TargetPortal     | Endpoint used by IP-based storage networks (such as iSCSI). It provides initiators the IP address for which they should discover target portals on. |
| PhysicalDisk     | A unit of usable storage with a basic set of attributes. PhysicalDisks don't have any resiliency, and have a fixed capacity. PhysicalDisks essentially represent physical spindles or equivalent. |
| StoragePool      | Composed of PhysicalDisks. StoragePools are units of administration (for example, for multi-tenancy) and associated isolation. All storage subsystems that support StoragePools must expose a PrimordialPool. |
| VirtualDisk      | Unit of usable storage with an expanded set of attributes as compared to PhysicalDisks. Examples of the expanded set of attributes include resiliency, dynamic capacity extension, or others. Examples of a VirtualDisk are LUNs or Storage Spaces. When exposed to Windows, a VirtualDisk shows up as a (Windows) Disk to the rest of the Windows stack. |
| (Windows) Disk    | A representation within Windows of usable storage. A Disk is instantiated either from a PhysicalDisk or a VirtualDisk. An example of a PhysicalDisk is a USB disk connected to Windows directly via a USB cable. Examples of a VirtualDisk include an EMC LUN that was unmasked to a particular Windows instance, OR a new Storage Space activated on the Windows instance. |
| Partition         | A Windows partition on a (Windows) Disk. |
| Volume            | A volume on a (Windows) partition. |
| InitiatorPort    | Represents an instance of an Initiator end point in the Windows host. This host side only object isn't visible to SMPs. It's a common object representing a port independent of the connection type. For example, one instance of InitiatorPort could be representing a SAS port on SAS HBA, while another instance could be representing the iSCSI initiator. |
| InitiatorId      | Represents a unique identifier for an InitiatorPort. It's an array-side representation of InitiatorPort and is managed by SMPs. The InitiatorPort that it represents doesn't need to be instantiated on the machine that the InitiatorId is being used. This object is used with TargetPort to establish which InitiatorPort is allowed to access VirtualDisks from which TargetPort through the MaskingSet operations. |
| ResiliencySetting | Describes the virtual disk redundancy capabilities supported by a particular StoragePool. On the primordial pool, these settings represent capabilities supported by the StorageSubsystem. Examples of supported capabilities include resiliency modes (for example, RAID Type) or others. |
| OffloadDataTransferSetting | Describes the offload data transfer (ODX) settings for storage subsystem. |

## Windows Storage Management Object Model

The following diagram illustrates the relationships between the main objects exposed by the [Windows Storage Management API](windows-storage-management-api-portal.md).

![Windows Storage Management Object Model](images/storage-management-object-model.png "Windows Storage Management Object Model")

## Mapping Between VDS and SMP Objects

The following table illustrates the mapping between VDS (Virtual Disk Service) hardware objects and SMP objects.

| VDS Object Name | SMP Object Name |
| --------------- | --------------- |
| Provider        | StorageProvider |
| SubSystem       | StorageSubsystem |
| StoragePool     | StoragePool  |
| VDS_RAID_TYPE   | ResiliencySetting |
| Drive           | PhysicalDisk |
| LUN             | VirtualDisk |
| Controller/ControllerPort | TargetPort |
| --              | TargetPortal |
| HBAPort         | InitiatorPort (Host-side only entity) |
| --              | InitatorPort (Array-side representation of InitiatorPort) |
| --              | MaskingSet |
| IVdsAsync       | StorageJob |
| --              | OffloadDataTransferSetting |
