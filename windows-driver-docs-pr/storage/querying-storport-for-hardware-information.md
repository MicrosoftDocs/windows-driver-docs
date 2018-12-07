---
title: Querying Storport for Hardware Information
description: Querying Storport for Hardware Information
ms.assetid: 1e807e42-d03f-44be-a0a4-8187e2d5667a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying Storport for Hardware Information


Storage class drivers and other higher-level drivers can query Storport for information about the capabilities of devices and host bus adapters by means of a query-property request ([**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590)). The query-property request is the PnP equivalent of the inquiry and capabilities requests in legacy systems ([**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff560509) and [**IOCTL\_SCSI\_GET\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff560502)). For storage devices, Storport returns a storage device descriptor ([**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971)) containing SCSI inquiry data or the non-SCSI equivalent, and for host adapters Storport returns a storage adapter descriptor ([**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346)) containing capabilities and limitations data.

Higher-level drivers must pass a [**STORAGE\_PROPERTY\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff566997) structure to Storport with the query property request. If a higher-level driver has set the **PropertyId** member of **STORAGE\_PROPERTY\_QUERY** to **StorageAdapterProperty**, Storport returns a storage adapter descriptor. If the higher-level driver has set the **PropertyId** member to **StorageDeviceProperty**, Storport returns a storage device descriptor.

If a higher-level driver sends a query property request IRP to the FDO of the adapter with **PropertyId** set to **StorageDeviceProperty**, Storport fails the IRP. If the class driver sends this IRP to the PDO of a device with **PropertyId** set to **StorageAdapterProperty**, Storport forwards the IRP down to the adapter FDO.

For a detailed explanation of storage device descriptors and storage adapter descriptors, see [Storage Class Driver's GetDescriptor Routine](storage-class-driver-s-getdescriptor-routine.md), and the reference pages for [**STORAGE\_PROPERTY\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff566997), [**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971), and [**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346).

 

 




