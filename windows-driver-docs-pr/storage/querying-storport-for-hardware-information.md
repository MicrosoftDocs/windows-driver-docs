---
title: Querying Storport for Hardware Information
description: Querying Storport for Hardware Information
ms.assetid: 1e807e42-d03f-44be-a0a4-8187e2d5667a
---

# Querying Storport for Hardware Information


Storage class drivers and other higher-level drivers can query Storport for information about the capabilities of devices and host bus adapters by means of a query-property request ([**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590)). The query-property request is the PnP equivalent of the inquiry and capabilities requests in legacy systems ([**IOCTL\_SCSI\_GET\_INQUIRY\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff560509) and [**IOCTL\_SCSI\_GET\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff560502)). For storage devices, Storport returns a storage device descriptor ([**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971)) containing SCSI inquiry data or the non-SCSI equivalent, and for host adapters Storport returns a storage adapter descriptor ([**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346)) containing capabilities and limitations data.

Higher-level drivers must pass a [**STORAGE\_PROPERTY\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff566997) structure to Storport with the query property request. If a higher-level driver has set the **PropertyId** member of **STORAGE\_PROPERTY\_QUERY** to **StorageAdapterProperty**, Storport returns a storage adapter descriptor. If the higher-level driver has set the **PropertyId** member to **StorageDeviceProperty**, Storport returns a storage device descriptor.

If a higher-level driver sends a query property request IRP to the FDO of the adapter with **PropertyId** set to **StorageDeviceProperty**, Storport fails the IRP. If the class driver sends this IRP to the PDO of a device with **PropertyId** set to **StorageAdapterProperty**, Storport forwards the IRP down to the adapter FDO.

For a detailed explanation of storage device descriptors and storage adapter descriptors, see [Storage Class Driver's GetDescriptor Routine](storage-class-driver-s-getdescriptor-routine.md), and the reference pages for [**STORAGE\_PROPERTY\_QUERY**](https://msdn.microsoft.com/library/windows/hardware/ff566997), [**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971), and [**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Querying%20Storport%20for%20Hardware%20Information%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




