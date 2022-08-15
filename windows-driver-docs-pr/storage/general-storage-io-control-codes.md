---
title: General Storage I/O Control Codes
description: Describes a set of standard services and accompanying device control codes that are frequently required by storage devices.
keywords:
- storage drivers WDK storage
- wdk CD-ROM drivers
- IOCTLs WDK CD-ROM
ms.date: 12/19/2018
---

# General Storage I/O Control Codes

Storage devices of different kinds often require the same services. Rather than duplicate the IOCTL requests that provide these services for each device type, this section defines a set of standard services and accompanying device control codes that are frequently required by storage devices. The I/O control codes defined here have the form IOCTL_STORAGE_*XXX* and they replace the IOCTL_*DeviceType_XXX* control codes, where *DeviceType* was DISK, TAPE, or CDROM. For example, **IOCTL_STORAGE_RESERVE** replaces **IOCTL_DISK_RESERVE**, **IOCTL_TAPE_RESERVE**, and **IOCTL_CDROM_RESERVE**. The IOCTL_STORAGE_*XXX* control codes have identical values for function code, transfer method, and required access as the previous disk, tape, and CD-ROM codes. The only difference is the device type.

The storage class driver initiates some of these requests, but usually it is an application that does so. Storage class drivers must handle some or all of these requests, depending on the type of storage device. Where no storage class driver exists, the application might make the request directly to the port driver.

|IOCTL|Description|
|----|----|
|[IOCTL_STORAGE_BREAK_RESERVATION](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_break_reservation)|Breaks a disk reservation.|
|[IOCTL_STORAGE_CHECK_VERIFY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_check_verify)|Determines whether the media has changed on a removable-media device that the caller has opened for read or write access.|
|[IOCTL_STORAGE_CHECK_VERIFY2](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_check_verify2)|Determines whether the media has changed on a removable-media device - the caller has opened with **FILE_READ_ATTRIBUTES**.|
|[IOCTL_STORAGE_DEVICE_POWER_CAP](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_device_power_cap)|Specifies a maximum operational power consumption level for a storage device.|
|[IOCTL_STORAGE_EJECT_MEDIA](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_eject_media)|Causes the device to eject the media if the device supports ejection capabilities.|
|[IOCTL_STORAGE_EJECTION_CONTROL](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_ejection_control)|Locks the device to prevent removal of the media.|
|[IOCTL_STORAGE_FIND_NEW_DEVICES](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_find_new_devices)|Determines whether another device that the driver supports has been connected to the I/O bus, either since the system was booted or since the driver last processed this request.|
|[IOCTL_STORAGE_FIRMWARE_ACTIVATE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_activate)|Activates a firmware image on a storage device.|
|[IOCTL_STORAGE_FIRMWARE_DOWNLOAD](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_download)|Downloads a firmware image to a storage device, but does not activate it.|
|[IOCTL_STORAGE_FIRMWARE_GET_INFO](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_get_info)|Queries a storage device for detailed firmware information.|
|[IOCTL_STORAGE_GET_DEVICE_NUMBER](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_device_number)|Returns a **STORAGE_DEVICE_NUMBER** structure that contains the FILE_DEVICE_XXX type, device number, and, for a partitionable device, the partition number assigned to a device by the driver when the device is started.|
|[IOCTL_STORAGE_GET_HOTPLUG_INFO](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_hotplug_info)|Retrieves the hotplug configuration of the specified device.|
|[IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_lb_provisioning_map_resources)|The **IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES** request is sent to the storage class driver to determine available and used mapping resources on a storage device.|
|[IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_media_serial_number)|Queries the USB generic parent driver for the serial number of a USB device.|
|[IOCTL_STORAGE_GET_MEDIA_TYPES](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_media_types)|Returns information about the geometry of floppy drives.|
|[IOCTL_STORAGE_GET_MEDIA_TYPES_EX](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_media_types_ex)|Returns information about the types of media supported by a device.|
|[IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_physical_element_status)|The **IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS** control code queries for and returns the physical element status from a device.|
|[IOCTL_STORAGE_LOAD_MEDIA](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_load_media)|Causes media to be loaded in a device that the caller has opened for read or write access.|
|[IOCTL_STORAGE_LOAD_MEDIA2](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_load_media2)|Causes media to be loaded in a device that the caller has opened with **FILE_READ_ATTRIBUTES**.|
|[IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_manage_data_set_attributes)|This **IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES** request is used to send a manage data set attributes request to a storage device.|
|[IOCTL_STORAGE_MCN_CONTROL](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_mcn_control)|Temporarily enables or disables delivery of the custom PnP events **GUID_IO_MEDIA_ARRIVAL** and **GUID_IO_MEDIA_REMOVAL** on a removable-media device.|
|[IOCTL_STORAGE_MEDIA_REMOVAL](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_media_removal)|Locks the device to prevent removal of the media.|
|[IOCTL_STORAGE_PERSISTENT_RESERVE_IN](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_persistent_reserve_in)|The generic storage class driver (classpnp.sys) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve In commands.|
|[IOCTL_STORAGE_PERSISTENT_RESERVE_OUT](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_persistent_reserve_out)|The generic storage class driver (classpnp.sys) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve Out commands.|
|[IOCTL_STORAGE_PREDICT_FAILURE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_predict_failure)|Polls for a prediction of device failure.|
|[IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command)|A driver can use **IOCTL_STORAGE_PROTOCOL_COMMAND** to pass vendor-specific commands to a storage device|
|[IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property)|A driver can use **IOCTL_STORAGE_QUERY_PROPERTY** to return properties of a storage device or adapter.|
|[IOCTL_STORAGE_READ_CAPACITY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_read_capacity)|The **IOCTL_STORAGE_READ_CAPACITY** request returns the read capacity information for the target storage device.|
|[IOCTL_STORAGE_REINITIALIZE_MEDIA](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_reinitialize_media)|A driver can use the **IOCTL_STORAGE_REINITIALIZE_MEDIA** control code to reinitialize/erase a device.|
|[IOCTL_STORAGE_RELEASE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_release)|Releases a device previously reserved for the exclusive use of the caller on a bus that supports multiple initiators and the concept of reserving a device, such as a SCSI bus.|
|[IOCTL_STORAGE_RESERVE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_reserve)|Claims a device for the exclusive use of the caller on a bus that supports multiple initiators and the concept of reserving a device, such as a SCSI bus.|
|[IOCTL_STORAGE_RESET_BUS](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_reset_bus)|Resets an I/O bus and, indirectly, each device on the bus.|
|[IOCTL_STORAGE_RESET_DEVICE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_reset_device)|If possible, resets a non-SCSI storage device without affecting other devices on the bus.|
|[IOCTL_STORAGE_SET_HOTPLUG_INFO](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_hotplug_info)|Sets the hotplug configuration of the specified device.|
|[IOCTL_STORAGE_SET_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_property)|Indicates whether a request to change a property is successful or causes an error.
|[IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_temperature_threshold)|A driver can use **IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD** to set the temperature threshold of a storage device (when supported by the hardware).|
