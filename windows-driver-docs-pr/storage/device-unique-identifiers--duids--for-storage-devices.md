---
title: Device Unique Identifiers (DUIDs) for Storage Devices
description: Device Unique Identifiers (DUIDs) for Storage Devices
ms.assetid: 3846961c-5b75-4a1b-bced-601fc25bf071
keywords:
- storage drivers WDK , DUIDs
- DUIDs WDK storage
- device unique IDs WDK storage
- device IDs WDK storage
- identifiers WDK storage
- serial numbers WDK storage
- device layout signatures WDK storage
- signatures WDK , storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Unique Identifiers (DUIDs) for Storage Devices


Techniques to identify storage devices become inadequate as file system architecture becomes more complex, the number of operating system components multiplies, and initiators access storage targets through increasingly diverse hardware and software paths.

For example, the Plug and Play (PnP) manager generates an [instance identifier (ID)](https://msdn.microsoft.com/library/windows/hardware/ff547656) for each device in the computer. Each instance ID corresponds to a single device node in the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194) and uniquely identifies a device, if the device remains in the same location. Instance IDs persist when a computer is restarted, but they do not remain the same if you move the device to a different bus or a different computer. As a result, instance IDs are inadequate for applications in storage area networks (SANs) and for some newer system components, such as the Windows Vista Diagnostic Service, that operate in environments with distributed storage. When a hard disk drive predicts a SMART failure, it generates an event for the diagnostic service. This event must contain an identifier that uniquely identifies the failing hard disk on all computers that the disk could be in and on all buses that it could be attached to. Instance IDs and any of the other [device identification strings](https://msdn.microsoft.com/library/windows/hardware/ff541224) are inadequate for this purpose.

Some applications and system services, such as the Microsoft Cluster Service (MSCS) and the Partition Manager, use the device layout signature ([**STORAGE\_DEVICE\_LAYOUT\_SIGNATURE**](https://msdn.microsoft.com/library/windows/hardware/ff566973)) to uniquely identify a storage device in a cluster. But the device layout signature is inadequate for this purpose, under certain circumstances, and includes the following limitations:

-   The signature might change or be cleared.

-   The signature might be unavailable if the device is not spinning or has problems accessing the sectors where the signature resides.

-   The signature is unavailable if the disk is reserved by another cluster node. MSCS can read the drive layout of only disks that are associated with the node that MSCS is running on. Software that must access disks in different cluster nodes must use an alternative to the disk layout signature.

-   Drive layout signatures cannot help distinguish between a logical unit number (LUN) and its snapshot. Because a LUN and its snapshot have identical content, their drive layout signatures will be the same.

A serial number is sometimes a reliable technique of uniquely identifying a storage device that does not depend on the location of the device. The serial number is often available as a part of a device's inquiry data. Initiators can query for the inquiry data with a [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) request, and the port driver reports the results of the query in a [**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971) structure. However, this technique does not help identify devices, such as tape drives, that do not report inquiry data.

### <span id="device_unique_identifiers__duids_"></span><span id="DEVICE_UNIQUE_IDENTIFIERS__DUIDS_"></span>Device Unique Identifiers (DUIDs)

Because techniques for uniquely identifying devices often become obsolete as technology evolves, Microsoft has developed a device ID format called the device unique ID (DUID) that is extensible and that can incorporate new techniques to identify devices as they become available.

A DUID is defined by a [**STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER**](https://msdn.microsoft.com/library/windows/hardware/ff566975) structure, and the first version of this structure (DUID\_VERSION\_1) includes a combination of the following identifiers:

<span id="STORAGE_DEVICE_ID_DESCRIPTOR"></span><span id="storage_device_id_descriptor"></span>[**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566972)  
The STORAGE\_DEVICE\_ID\_DESCRIPTOR structure contains identifiers that are extracted from page 0x83 of the device's vital product data (VPD). Typically, only SCSI and Fibre Channel devices support this page. Integrated drive electronics (IDE) and Universal Serial Bus (USB) devices, IEEE 1394 drives, and RAID controllers do not provide page 0x83.

<span id="STORAGE_DEVICE_DESCRIPTOR"></span><span id="storage_device_descriptor"></span>[**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971)  
The STORAGE\_DEVICE\_DESCRIPTOR structure contains other inquiry data, including an offset to the unit serial number in the **SerialNumberOffset** member. The serial number is formatted as a variable-length, **NULL**-terminated string. If the storage device is SCSI-compliant, the port driver attempts to extract the serial number from the optional Unit Serial Number page (page 0x80) of the VPD. If the storage device is an IDE device, the port driver generates a serial number from the device's identify data.

<span id="STORAGE_DEVICE_LAYOUT_SIGNATURE"></span><span id="storage_device_layout_signature"></span>[**STORAGE\_DEVICE\_LAYOUT\_SIGNATURE**](https://msdn.microsoft.com/library/windows/hardware/ff566973)  
The STORAGE\_DEVICE\_LAYOUT\_SIGNATURE contains the device layout signature.

More data will be added to DUIDs in future versions.

DUIDs do not have a fixed size, so software that makes use of DUIDs (known as the DUID consumer) must obtain the size of the DUID from the **Size** member of the STORAGE\_DEVICE\_UNIQUE\_IDENTIFIER structure. The version of the DUID is available in the Vers****ion member of this same structure.

Some devices do not provide enough information for the system to guarantee that the device's DUID will be sufficiently unique for all uses and all DUID consumers. If the operating system can retrieve unique IDs from the VPD of the device, it can create a DUID that is sufficiently unique for all DUID consumers. But if the system must create a DUID from the device layout signature alone, the DUID will be sufficiently unique for some DUID consumers but not for others.

The system attempts to create a DUID that has the following characteristics:

-   The DUID remains the same when the operating system restarts.

-   The DUID remains the same, even when the device is moved from one computer to another, one adapter to another, or one channel to another.

-   The DUID identifies the device and not the media. This distinction is important for drives that have removable media.

-   On multipath systems, the DUID is the same for all I/O paths.

DUIDs have the following limitations:

-   DUIDs often contain binary contents that cannot be displayed.

-   DUIDs are not always **null**-terminated. DUID consumers must check the **Size** member of the [**STORAGE\_DEVICE\_LAYOUT\_SIGNATURE**](https://msdn.microsoft.com/library/windows/hardware/ff566973) structure to determine the length of the DUID.

-   DUID consumers must use [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) to compare DUIDs instead of comparing them byte by byte.

-   [*Enumerators*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator) must not attempt to use DUIDs to identify device objects for Plug and Play (PnP) purposes. Multipath systems can have more than one device that share the same DUID. But for PnP, device IDs must be unique.

Initiators can query for the DUID information data using a [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) request with a property ID of **StorageDeviceUniqueIdProperty**.

### <span id="how_to_compare_duids"></span><span id="HOW_TO_COMPARE_DUIDS"></span>How to Compare DUIDs

DUID consumers must use the [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) routine, which is defined in Storduids.h, to compare two DUIDs. **CompareStorageDuids** returns a [**DUID\_MATCH\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff552760) value that indicates whether the two DUIDs match. If the operation succeeds, **CompareStorageDuids** returns one of the following values:

<span id="DuidExactMatch"></span><span id="duidexactmatch"></span><span id="DUIDEXACTMATCH"></span>**DuidExactMatch**  
All fields in the two DUIDs match exactly.

<span id="DuidSubIdMatch"></span><span id="duidsubidmatch"></span><span id="DUIDSUBIDMATCH"></span>**DuidSubIdMatch**  
A DUID is made up of several sub-IDs. At least one of the sub-IDs matches, and the two DUIDs probably represent the same device. When device firmware is updated, it might acquire new identifiers, which will change the composition of the device's DUID. If a DUID consumer compares an old DUID for the device with the new DUID, [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) might return **DuidSubIdMatch** instead of **DuidExactMatch**. This is an example of a valid match based on a sub-ID. A DUID consumer must choose whether it will accept the **DuidSubIdMatch** return value as a match or a mismatch, depending on the requirements of the DUID consumer.

<span id="DuidNoMatch"></span><span id="duidnomatch"></span><span id="DUIDNOMATCH"></span>**DuidNoMatch**  
The serial numbers do not match, and none of the unique sub-IDs from page 83h of the vital product data (VPD) match.

In addition to the preceding values, [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) might return various error codes.

The [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) routine uses the following algorithm to compare two DUIDs:

1.  Check for an exact match. If all of the data in the DUIDs match, the DUIDs match exactly and [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) returns **DuidExactMatch**. If not, continue with the next check.

2.  Check the VPD identifiers. If any unique sub-IDs match, the DUIDs match and [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) returns **DuidSubIdMatch**. If no sub-IDs match or the device does not provide unique VPD identifiers, continue with the next check.

3.  Check the unit serial number. If the vendor ID, the product ID, and the serial number are the same, the DUIDs match and [**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) returns **DuidSubIdMatch**. If none of these values match or the device does not provide these values, continue with the next check.

4.  Check the drive layout signature. If the drive layout signatures of the two DUIDs match, the DUIDs match and[**CompareStorageDuids**](https://msdn.microsoft.com/library/windows/hardware/ff552464) returns **DuidSubIdMatch**. If the drive signatures do not match or the system cannot read the device's drive layout signature, the DUIDs do not match and **CompareStorageDuids** returns **DuidNoMatch**.

 

 




