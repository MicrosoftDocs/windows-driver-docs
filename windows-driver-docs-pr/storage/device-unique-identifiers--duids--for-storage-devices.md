---
title: Device Unique Identifiers (DUIDs) for Storage Devices
description: Device Unique Identifiers (DUIDs) for Storage Devices
keywords:
- storage drivers WDK , DUIDs
- DUIDs WDK storage
- device unique IDs WDK storage
- device IDs WDK storage
- identifiers WDK storage
- serial numbers WDK storage
- device layout signatures WDK storage
- signatures WDK , storage
ms.date: 12/18/2024
ms.topic: concept-article
---

# Device Unique Identifiers (DUIDs) for Storage Devices

This article discusses the challenges and solutions related to uniquely identifying storage devices across various environments, particularly in complex file system architectures and storage area networks (SANs).

## Overview

Techniques to identify storage devices became inadequate for various reasons, including:

* File system architecture is increasingly complex.
* The number of operating system components multiplied.
* Initiators accessing storage targets do so through increasingly diverse hardware and software paths.

For example, the PnP manager generates an [instance identifier (ID)](../install/instance-ids.md) for each device in the computer. Each instance ID corresponds to a single device node in the [device tree](../kernel/device-tree.md) and uniquely identifies a device, if the device remains in the same location. Instance IDs persist when a computer is restarted, but they don't remain the same if you move the device to a different bus or a different computer. As a result, instance IDs are inadequate for applications in SANs and for some system components such as the Windows Diagnostics service, that operate in environments with distributed storage. When a hard disk drive predicts a SMART failure, it generates an event for the diagnostic service. This event must contain an identifier that uniquely identifies the failing hard disk on all computers that the disk might physically be in and on all buses that it could be attached to. Instance IDs and any of the other [device identification strings](../install/device-identification-strings.md) are inadequate for this purpose.

Some applications and system services, such as the Microsoft Cluster Service (MSCS) and the Partition Manager, use the device layout signature ([**STORAGE_DEVICE_LAYOUT_SIGNATURE**](/windows-hardware/drivers/ddi/storduid/ns-storduid-_storage_device_layout_signature)) to uniquely identify a storage device in a cluster. But the device layout signature is inadequate for this purpose, under certain circumstances, and includes the following limitations:

* The signature might change or be cleared.

* The signature might be unavailable if the device isn't spinning or has problems accessing the sectors where the signature resides.

* The signature is unavailable if another cluster node has reserved the disk. MSCS can read the drive layout of only disks that are associated with the node that MSCS is running on. Software that must access disks in different cluster nodes must use an alternative to the disk layout signature.

* Drive layout signatures can't help distinguish between a logical unit number (LUN) and its snapshot. Because a LUN and its snapshot have identical content, their drive layout signatures are the same.

A serial number is sometimes a reliable technique of uniquely identifying a storage device that doesn't depend on the location of the device. The serial number is often available as a part of a device's inquiry data. Initiators can query for the inquiry data with a [**IOCTL_STORAGE_QUERY_PROPERTY**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) request, and the port driver reports the results of the query in a [**STORAGE_DEVICE_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_descriptor) structure. However, this technique doesn't help identify devices that don't report inquiry data.

## Device Unique Identifiers (DUIDs)

Because techniques for uniquely identifying devices often become obsolete as technology evolves, Microsoft developed a device ID format called the device unique ID (DUID) that is extensible and that can incorporate new techniques to identify devices as they become available.

A DUID is defined by a [**STORAGE_DEVICE_UNIQUE_IDENTIFIER**](/windows-hardware/drivers/ddi/storduid/ns-storduid-_storage_device_unique_identifier) structure, and the first version of this structure (DUID_VERSION_1) includes a combination of the following identifiers:

* A [**STORAGE_DEVICE_ID_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_id_descriptor) structure, which contains identifiers that are extracted from page 0x83 of the device's vital product data (VPD). Typically, only SCSI and Fibre Channel devices support this page. Integrated drive electronics (IDE) and Universal Serial Bus (USB) devices, IEEE 1394 drives, and RAID controllers don't provide page 0x83.

* A [**STORAGE_DEVICE_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_descriptor) structure, which contains other inquiry data, including an offset to the unit serial number in the **SerialNumberOffset** member. The serial number is formatted as a variable-length, NULL-terminated string. If the storage device is SCSI-compliant, the port driver attempts to extract the serial number from the optional Unit Serial Number page (page 0x80) of the VPD. If the storage device is an IDE device, the port driver generates a serial number from the device's identify data.

* A [**STORAGE_DEVICE_LAYOUT_SIGNATURE**](/windows-hardware/drivers/ddi/storduid/ns-storduid-_storage_device_layout_signature) structure, which contains the device layout signature.

More data can be added to DUIDs in future versions.

DUIDs don't have a fixed size, so software that makes use of DUIDs (known as the DUID consumer) must obtain the size of the DUID from the **Size** member of the **STORAGE_DEVICE_UNIQUE_IDENTIFIER** structure. The version of the DUID is available in this structure's **Version** member.

Some devices don't provide enough information for the system to guarantee that the device's DUID will be sufficiently unique for all uses and all DUID consumers. If the operating system can retrieve unique IDs from the VPD of the device, it can create a DUID that is sufficiently unique for all DUID consumers. But if the system must create a DUID from the device layout signature alone, the DUID is sufficiently unique for some DUID consumers but not for others.

The system attempts to create a DUID that has the following characteristics:

* The DUID remains the same when the operating system restarts.

* The DUID remains the same, even when the device is moved from one computer to another, one adapter to another, or one channel to another.

* The DUID identifies the device and not the media. This distinction is important for drives that have removable media.

* The DUID is the same for all I/O paths on multipath systems.

DUIDs have the following limitations:

* DUIDs often contain binary contents that can't be displayed.

* DUIDs aren't always **null**-terminated. DUID consumers must check the **Size** member of the [**STORAGE_DEVICE_LAYOUT_SIGNATURE**](/windows-hardware/drivers/ddi/storduid/ns-storduid-_storage_device_layout_signature) structure to determine the length of the DUID.

* DUID consumers must use [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) to compare DUIDs instead of comparing them byte by byte.

* *Enumerators* must not attempt to use DUIDs to identify device objects for Plug and Play (PnP) purposes. Multipath systems can have more than one device that share the same DUID. But for PnP, device IDs must be unique.

Initiators can query for the DUID information data using a [**IOCTL_STORAGE_QUERY_PROPERTY**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) request with a property ID of **StorageDeviceUniqueIdProperty**.

### How to Compare DUIDs

DUID consumers must use the [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) routine to compare two DUIDs. **CompareStorageDuids** returns a [**DUID_MATCH_STATUS**](/windows-hardware/drivers/ddi/storduid/ne-storduid-_duid_match_status) value that indicates whether the two DUIDs match. If the operation succeeds, **CompareStorageDuids** returns one of the following values:

* **DuidExactMatch**: All fields in the two DUIDs match exactly.

* **DuidSubIdMatch**: A DUID is made up of several sub-IDs. At least one of the sub-IDs matches, and the two DUIDs probably represent the same device. When device firmware is updated, it might acquire new identifiers, which will change the composition of the device's DUID. If a DUID consumer compares an old DUID for the device with the new DUID, [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) might return **DuidSubIdMatch** instead of **DuidExactMatch**. This example of a valid match is based on a sub-ID. A DUID consumer must choose whether it will accept the **DuidSubIdMatch** return value as a match or a mismatch, depending on the requirements of the DUID consumer.

* **DuidNoMatch**: The serial numbers don't match, and none of the unique sub-IDs from page 83h of the vital product data (VPD) match.

In addition to the preceding values, [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) might return various error codes.

The [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) routine uses the following algorithm to compare two DUIDs:

1. Check for an exact match. If all of the data in the DUIDs match, the DUIDs match exactly and [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) returns **DuidExactMatch**. If not, continue with the next check.

2. Check the VPD identifiers. If any unique sub-IDs match, the DUIDs match and [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) returns **DuidSubIdMatch**. If no sub-IDs match or the device doesn't provide unique VPD identifiers, continue with the next check.

3. Check the unit serial number. If the vendor ID, the product ID, and the serial number are the same, the DUIDs match and [**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) returns **DuidSubIdMatch**. If none of these values match or the device doesn't provide these values, continue with the next check.

4. Check the drive layout signature. If the drive layout signatures of the two DUIDs match, the DUIDs match and[**CompareStorageDuids**](/windows-hardware/drivers/ddi/storduid/nf-storduid-comparestorageduids) returns **DuidSubIdMatch**. If the drive signatures don't match or the system can't read the device's drive layout signature, the DUIDs don't match and **CompareStorageDuids** returns **DuidNoMatch**.
