---
title: CD-ROM Exclusive Access Mode
description: CD-ROM Exclusive Access Mode
ms.assetid: 4432f6d6-e98c-4354-a7ba-b043a624f064
keywords:
- CD-ROM drivers WDK storage
- storage CD-ROM drivers WDK
- exclusive access mode WDK CD-ROM
- IOCTL_CDROM_EXCLUSIVE_ACCESS
- CDROM_EXCLUSIVE_LOCK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CD-ROM Exclusive Access Mode


The CD-ROM *exclusive access* mechanism (also known as *exclusive access mode*) enables applications and system components to obtain exclusive access to a CD-ROM device. Applications that require exclusive access to CD-ROM devices include the following examples:

<span id="Optical_media-authoring_applications"></span><span id="optical_media-authoring_applications"></span><span id="OPTICAL_MEDIA-AUTHORING_APPLICATIONS"></span>Optical media-authoring applications  
Some optical authoring software requires exclusive access to a CD-ROM device to write data without any interruption from other applications. Otherwise, data might be written incorrectly, causing data corruption.

<span id="Firmware_update_utilities"></span><span id="firmware_update_utilities"></span><span id="FIRMWARE_UPDATE_UTILITIES"></span>Firmware update utilities  
Many manufacturers of CD-ROM devices provide a firmware update utility. If an application sends a command to the device during a firmware update, it might make the device unusable.

Without the exclusive access mechanism, the only way for vendors to give these two types of applications exclusive access would be to install a custom filter driver that fails I/O requests from other applications and components, and this approach causes system instability. You should not use filter drivers to obtain exclusive access to CD-ROM devices.

To use the exclusive access mechanism, applications must send an [**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](https://msdn.microsoft.com/library/windows/hardware/ff559327) request to the CD-ROM class driver at PASSIVE\_LEVEL IRQL. When the caller makes this request, the caller must provide an identification string in the **CallerName** member of [**CDROM\_EXCLUSIVE\_LOCK**](https://msdn.microsoft.com/library/windows/hardware/ff551363). The class driver uses this string to identify the application that has exclusive access.

Applications should query for the current state of the device before attempting to lock it. If the device is already locked, the class driver returns the identification string of the current owner of the device. Before locking the device, the caller must open it in read/write access mode. Therefore, the caller must have administrator privileges or permission to open the CD-ROM device in write access mode.

Callers that request exclusive access should not open the CD-ROM device by simply sending a create request to the file system driver, because there is no guarantee that the CD-ROM class driver will receive the request. Instead, applications should use the **SetupDi***Xxx* routines to enumerate the interfaces for all CD-ROM devices in the system and then open the appropriate device interface.

When a caller opens a device by using the drive letter or names like *CdRom0* with the access mode set to 0, the file system driver is guaranteed to pass the create request to the CD-ROM class driver. But this guarantee is still not sufficient because the handle that the application obtains by this procedure does not give the caller read/write access to the device.

Exclusive access mode has the following characteristics:

-   Only the owner of the exclusive access lock can access the device.

-   The system fails requests for access from other applications.

-   The system processes Plug and Play (PnP) and power I/O request packets (IRPs) in the typical way.

-   Media change notification is disabled for the device.

-   The system fails requests to open the device while it is locked.

-   Other applications that send an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) request to the CD-ROM class driver will receive cached information from the device while it is locked. Specifically, if the [**STORAGE\_QUERY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff566998) is **PropertyExistsQuery**, the IOCTL will behave the same as it does when the device is not locked. Also, if the **STORAGE\_QUERY\_TYPE** is **PropertyStandardQuery** and the [**STORAGE\_PROPERTY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff566996) is **StorageDeviceProperty** or **StorageAdapterProperty**, the IOCTL returns information cached in the CD-ROM class driver. With other combinations of **STORAGE\_QUERY\_TYPE** and **STORAGE\_PROPERTY\_ID**, the IOCTL fails with the status value STATUS\_ACCESS\_DENIED.

-   Other applications that send an [**IOCTL\_CDROM\_GET\_INQUIRY\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559345) request to the CD-ROM class driver receive cached information from the device while it is locked, and also when it is unlocked.

The system removes exclusive access to a CD-ROM device when any of the following occurs:

-   The owner of the exclusive access lock sends an [**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](https://msdn.microsoft.com/library/windows/hardware/ff559327) request to the CD-ROM class driver with the **RequestType** member of [**CDROM\_EXCLUSIVE\_ACCESS**](https://msdn.microsoft.com/library/windows/hardware/ff551362) set to **ExclusiveAccessUnlockDevice**.

-   The owner of the exclusive access lock closes the device handle.

-   The application that owns the exclusive access lock terminates.

After removing the exclusive access lock on a device, the CD-ROM class driver takes the following actions :

-   Enables media change notification on the device.

-   Sets the DO\_VERIFY\_VOLUME flag in the device extension, so that the system will remount the device's file system.

-   Forces an update of the device's multimedia capabilities.

 

 




