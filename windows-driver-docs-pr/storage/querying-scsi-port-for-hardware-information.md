---
title: Querying SCSI Port for Hardware Information
description: Querying SCSI Port for Hardware Information
ms.assetid: 2f3adc40-6e5a-4a70-8298-60359b77f04f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying SCSI Port for Hardware Information


## <span id="ddk_querying_scsi_port_for_hardware_information_kg"></span><span id="DDK_QUERYING_SCSI_PORT_FOR_HARDWARE_INFORMATION_KG"></span>


Storage class drivers and other higher-level drivers can query SCSI Port for information about the capabilities of devices and host bus adapters by means of a query-property request ([**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590)). The query-property request is the PnP equivalent of the inquiry and capabilities requests in legacy systems ([**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff560509) and [**IOCTL\_SCSI\_GET\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff560502)). For storage devices, SCSI Port returns a storage device descriptor ([**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971)) containing SCSI inquiry data or the non-SCSI equivalent, and for host adapters SCSI Port returns a storage adapter descriptor ([**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346)) containing capabilities and limitations data.

Higher-level drivers must pass a [**STORAGE\_PROPERTY\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff566997) structure to SCSI Port with the query property request. If a higher-level driver has set the **QueryType** member of STORAGE\_PROPERTY\_QUERY to **StorageAdapterProperty**, SCSI Port returns a storage adapter descriptor. If the higher-level driver has set the **QueryType** member to **StorageDeviceProperty**, SCSI Port returns a storage device descriptor.

If a higher-level driver sends a query property request IRP to the FDO of the adapter with **QueryType** set to **StorageDeviceProperty**, SCSI Port fails the IRP. If the class driver sends this IRP to the PDO of a device with **QueryType** set to **StorageAdapterProperty**, SCSI Port forwards the IRP down to the adapter FDO.

For a detailed explanation of storage device descriptors and storage adapter descriptors, see [Storage Class Driver's GetDescriptor Routine](storage-class-driver-s-getdescriptor-routine.md), and the reference pages for [**STORAGE\_PROPERTY\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff566997), [**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971), and [**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346).

 

 




