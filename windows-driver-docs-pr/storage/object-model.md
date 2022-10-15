---
title: Object Model (Windows Drivers)
description: Learn more about the Object Model.
ms.date: 10/14/2022
---

# Object Model

## High-Level Object Definition

The table below describes the objects exposed by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal) and their respective definitions. It includes objects that are visible to both Windows hosts and Storage Management Providers (SMPs), as well as objects that are “host-side only”.

<table>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Storage Provider</td>
<td>A Storage Provider enables administration of Storage Subsystems through a common management API by using a Storage Management Provider (SMP). Examples of Storage Providers include the Storage Spaces SMP, a third-party SMP, or a third-party SMI-S provider.</td>
</tr>
<tr class="even">
<td>Storage subsystem</td>
<td>A Storage Subsystem exposes Virtual Disks to Windows. Storage Subsystems respond to administrative commands through corresponding Storage Providers.</td>
</tr>
<tr class="odd">
<td>Masking set</td>
<td>A Masking Set contains Virtual Disks, Target Ports, and Initiator Ports, and is used for bulk mask/unmask operations.</td>
</tr>
<tr class="even">
<td>Target port</td>
<td>A Target Port represents an instance of an endpoint in a Storage Subsystem with associated properties for Show/Hide (Mask/Unmask) and Masking Set usage. Examples of Target Ports are FC, SAS, or iSCSI ports on corresponding controllers, present in Storage Subsystems.</td>
</tr>
<tr class="odd">
<td>Target portal</td>
<td>TargetPortal is an endpoint used by IP based storage networks (such as iSCSI). It provides initiators the IP address for which they should discover target portals on.</td>
</tr>
<tr class="even">
<td>Physical disk</td>
<td>Physical Disks are units of usable storage with a basic set of attributes. Physical Disks do not have any resiliency, and have a fixed capacity. Physical Disks essentially represent physical spindles or equivalent.</td>
</tr>
<tr class="odd">
<td>Storage Pool</td>
<td><p>Storage pool Storage Pools are composed of Physical Disks. Storage Pools are units of administration (e.g. for multi-tenancy) and associated isolation.</p>
<p>All storage subsystems that support Storage Pools must expose a Primordial Pool (refer to “Primordial Pool”).</p></td>
</tr>
<tr class="even">
<td>Virtual disk</td>
<td>Virtual Disks are units of usable storage with an expanded set of attributes as compared to Physical Disks. Examples of the expanded set of attributes include resiliency, dynamic capacity extension, or others. Examples of Virtual Disks are LUNs or Storage Spaces. Virtual Disks, when exposed to Windows, show up as (Windows) Disks to the rest of the Windows stack.</td>
</tr>
<tr class="odd">
<td>(Windows) disk</td>
<td>The (Windows) Disk object is a representation within Windows of usable storage. A Disk is instantiated either from a Physical Disk (e.g. a USB disk connected to Windows directly via a USB cable), or from a Virtual Disk (e.g. an EMC LUN that was unmasked to a particular Windows instance, OR a new Storage Space that has been activated on the Windows instance).</td>
</tr>
<tr class="even">
<td>Partition</td>
<td>A windows partition on a (Windows) Disk.</td>
</tr>
<tr class="odd">
<td>Volume</td>
<td>A volume on a (Windows) partition.</td>
</tr>
<tr class="even">
<td>Initiator port</td>
<td>An Initiator Port represents an instance of an Initiator end point in the Windows host. This is a host side only object and is not visible to SMPs. It is a common object representing a port independent of the connection type (example - one instance of Initiator port could be representing a SAS port on SAS HBA, while another instance could be representing the iSCSI initiator).</td>
</tr>
<tr class="odd">
<td>Initiator Id</td>
<td>Initiator Id This object represents a unique identifier for an Initiator Port. It is an array-side representation of InitiatorPort and is managed by SMPs. The InitiatorPort it is representing need not be instantiated on the machine InitiatorId is being used. This is used in conjunction with TargetPort to establish which InitiatorPort is allowed to access VirtualDisks from which TargetPort through the MaskingSet operations.</td>
</tr>
<tr class="even">
<td>Resiliency setting</td>
<td>Resiliency setting This describes the virtual disk redundancy capabilities supported by a particular Storage Pool. On the primordial pool, these settings represent capabilities supported by the Storage Subsystem. Examples of supported capabilities include resiliency modes (e.g. RAID Type) or others.</td>
</tr>
<tr class="odd">
<td>Offload Data Transfer setting</td>
<td>This describes the offload data transfer (ODX) settings for storage subsystem.</td>
</tr>
</tbody>
</table>

## Windows Storage Management Object Model

The following diagram illustrates the relationships between the main objects exposed by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).

![Windows Storage Management Object Model](images/storage-management-object-model.png "Windows Storage Management Object Model")

## Mapping Between VDS and SMP Objects

The table below illustrates the mapping between VDS hardware objects and SMP objects.

<table>
<thead>
<tr class="header">
<th>VDS Object Name</th>
<th>SMP Object Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Provider</td>
<td>StorageProvider</td>
</tr>
<tr class="even">
<td>SubSystem</td>
<td>StorageSubsystem</td>
</tr>
<tr class="odd">
<td>StoragePool</td>
<td>StoragePool</td>
</tr>
<tr class="even">
<td>VDS_RAID_TYPE</td>
<td>ResiliencySetting</td>
</tr>
<tr class="odd">
<td>Drive</td>
<td>PhysicalDisk</td>
</tr>
<tr class="even">
<td>LUN</td>
<td>VirtualDisk</td>
</tr>
<tr class="odd">
<td>Controller/ControllerPort</td>
<td>TargetPort</td>
</tr>
<tr class="even">
<td>--</td>
<td>TargetPortal</td>
</tr>
<tr class="odd">
<td>HBAPort</td>
<td>InitiatorPort (Host-side only entity)</td>
</tr>
<tr class="even">
<td>--</td>
<td>InitatorPort (Array-side representation of InitiatorPort)</td>
</tr>
<tr class="odd">
<td>--</td>
<td>MaskingSet</td>
</tr>
<tr class="even">
<td>IVdsAsync</td>
<td>StorageJob</td>
</tr>
<tr class="odd">
<td>--</td>
<td>OffloadDataTransferSetting</td>
</tr>
</tbody>
</table>
