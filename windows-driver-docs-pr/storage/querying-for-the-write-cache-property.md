---
title: Querying for the Write Cache Property
description: Querying for the Write Cache Property
ms.assetid: 80b7c366-3b54-4dae-8ac7-63caaa1767f9
keywords: ["storage drivers WDK , write cache", "write cache WDK storage", "write back WDK storage", "write through WDK storage", "sync cache support WDK storage", "battery backup WDK storage", "cache WDK storage", "querying write cache", "write-through requests WDK storage"]
---

# Querying for the Write Cache Property


Storage devices often buffer data in a write cache before writing the data to nonvolatile media, such as a disk platter. This type of buffer improves device performance but it also also decreases data integrity. If the write cache does not have a battery backup, a power failure can cause the loss of cached data.

One remedy for the problem of data loss is to flush the write cache (with a SCSI SYNCHRONIZE CACHE command on SCSI devices). However, flushing the write cache is an expensive operation, and, if done frequently, it can significantly degrade performance. Instead of flushing the write cache, many storage devices allow *write-through* requests. A write-through request bypasses the write cache and sends data directly to the media.

For example, database applications can use write-through requests to ensure that transaction logs reach the media, and file system drivers can use write-through requests to ensure that file system metadata reaches the media.

However, not all storage devices that have write caches support write-through requests or SYNCHRONIZE CACHE; and some devices do not need to bypass or flush cached data as a precaution because they have battery backup systems that prevent data corruption during power failures. Applications and drivers must have information about the properties of a device's write cache before they can make effective use of it.

In Windows Vista, you can use the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) request with a **StorageDeviceWriteCacheProperty** property identifier to query the storage class driver for a write cache property that specifies the characteristics of the device's write cache. The write cache property includes the following information about the caching capabilities of the device:

-   *Presence of a write cache*. The write cache property specifies whether the device has a write cache.

-   *Type of write cache*. There are two main types of write cache: *write back* and *write through*. With a write-back cache, the device does not copy cache data to nonvolatile media until absolutely necessary. This operation improves the performance of write operations. With a write-through cache, the device writes data to the cache and the media in parallel. This does not improve write performance, but it makes subsequent read operations faster.

    Do not confuse a write-through *cache* with a write-through *request*. A write-through request can be used with any kind of cache, including a write-back cache, if the device supports write-through requests. For example, suppose that the target is a SCSI device with a write-back cache. If the device supports write-through requests, the initiator can bypass the write cache by setting the force unit access (FUA) bit in the command descriptor block (CDB) of the write command.

-   *Sync cache support*. The write cache property indicates whether the device supports the SCSI SYNC CACHE command, or an equivalent command on other buses.

-   *Battery backup*. The write cache property indicates whether the device has a battery backup that will protect the integrity of cache data during power failures.

For a complete description of the information that the write cache property reports, see [**STORAGE\_WRITE\_CACHE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff567017).

Without the write cache property mechanism (that is, using the IOCTL\_STORAGE\_QUERY\_PROPERTY request and the **StorageDeviceWriteCacheProperty** property identifier), applications and drivers must query for a device's write cache characteristics with a different sequence of commands for every bus. For example, if the target device is attached to an IEEE 1394 bus and uses the Reduced Block Command (RBC) protocol, the initiator must retrieve page 6 of the device's mode data to determine if the write cache is enabled. But if the target device is SCSI-compliant, the initiator must retrieve page 8 of the mode data. The write-cache property mechanism hides the details of these operations from the initiator and provides a technique to query for the characteristics of a storage device's write cache that is the same across different buses.

The write cache property mechanism is not supported for RAID devices (because there is no standard technique for querying these devices) or for flash memory devices.

The write cache property is supported on the 64-bit versions of Windows.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Querying%20for%20the%20Write%20Cache%20Property%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




