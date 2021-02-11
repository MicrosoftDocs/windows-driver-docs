---
title: Querying Storport for Hardware Information
description: Querying Storport for Hardware Information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying Storport for Hardware Information


Storage class drivers and other higher-level drivers can query Storport for information about the capabilities of devices and host bus adapters by means of a query-property request ([**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property)). The query-property request is the PnP equivalent of the inquiry and capabilities requests in legacy systems ([**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_inquiry_data) and [**IOCTL\_SCSI\_GET\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_capabilities)). For storage devices, Storport returns a storage device descriptor ([**STORAGE\_DEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_descriptor)) containing SCSI inquiry data or the non-SCSI equivalent, and for host adapters Storport returns a storage adapter descriptor ([**STORAGE\_ADAPTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_adapter_descriptor)) containing capabilities and limitations data.

Higher-level drivers must pass a [**STORAGE\_PROPERTY\_QUERY**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_property_query) structure to Storport with the query property request. If a higher-level driver has set the **PropertyId** member of **STORAGE\_PROPERTY\_QUERY** to **StorageAdapterProperty**, Storport returns a storage adapter descriptor. If the higher-level driver has set the **PropertyId** member to **StorageDeviceProperty**, Storport returns a storage device descriptor.

If a higher-level driver sends a query property request IRP to the FDO of the adapter with **PropertyId** set to **StorageDeviceProperty**, Storport fails the IRP. If the class driver sends this IRP to the PDO of a device with **PropertyId** set to **StorageAdapterProperty**, Storport forwards the IRP down to the adapter FDO.

For a detailed explanation of storage device descriptors and storage adapter descriptors, see [Storage Class Driver's GetDescriptor Routine](storage-class-driver-s-getdescriptor-routine.md), and the reference pages for [**STORAGE\_PROPERTY\_QUERY**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_property_query), [**STORAGE\_DEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_device_descriptor), and [**STORAGE\_ADAPTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddstor/ns-ntddstor-_storage_adapter_descriptor).

 

