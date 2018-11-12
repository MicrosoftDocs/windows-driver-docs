---
title: Device Node Status Flags
description: Device Node Status Flags
ms.assetid: 64f4548f-ace3-440c-8a36-97bd46cfa986
keywords: ["Plug and Play (PnP), Device Node Status Flags", "Device Node Status Flags", "DNF_XXX"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Device Node Status Flags


## <span id="ddk_device_node_status_flags_dbg"></span><span id="DDK_DEVICE_NODE_STATUS_FLAGS_DBG"></span>


The Device Node Status flags describe the status of a device.

The most important flags are:

<span id="DNF_MADEUP__0x00000001_"></span><span id="dnf_madeup__0x00000001_"></span><span id="DNF_MADEUP__0X00000001_"></span>**DNF\_MADEUP (0x00000001)**  
The device was created and is owned by the PnP Manager. It was not created by a bus driver.

<span id="DNF_DUPLICATE__0x00000002_"></span><span id="dnf_duplicate__0x00000002_"></span><span id="DNF_DUPLICATE__0X00000002_"></span>**DNF\_DUPLICATE (0x00000002)**  
The device node is a duplicate of another enumerated device node.

<span id="DNF_HAL_NODE__0x00000004_"></span><span id="dnf_hal_node__0x00000004_"></span><span id="DNF_HAL_NODE__0X00000004_"></span>**DNF\_HAL\_NODE (0x00000004)**  
The device node is the root node created by the hardware abstraction layer (HAL).

<span id="DNF_REENUMERATE__0x00000008_"></span><span id="dnf_reenumerate__0x00000008_"></span><span id="DNF_REENUMERATE__0X00000008_"></span>**DNF\_REENUMERATE (0x00000008)**  
The device needs to be re-enumerated.

<span id="DNF_ENUMERATED__0x00000010_"></span><span id="dnf_enumerated__0x00000010_"></span><span id="DNF_ENUMERATED__0X00000010_"></span>**DNF\_ENUMERATED (0x00000010)**  
The PDO for the device was exposed by its parent.

<span id="DNF_IDS_QUERIED__0x00000020_"></span><span id="dnf_ids_queried__0x00000020_"></span><span id="DNF_IDS_QUERIED__0X00000020_"></span>**DNF\_IDS\_QUERIED (0x00000020)**  
The operating system should send IRP\_MN\_QUERY\_ID requests to the device driver.

<span id="DNF_HAS_BOOT_CONFIG__0x00000040_"></span><span id="dnf_has_boot_config__0x00000040_"></span><span id="DNF_HAS_BOOT_CONFIG__0X00000040_"></span>**DNF\_HAS\_BOOT\_CONFIG (0x00000040)**  
The device has resources assigned by the BIOS. The device is considered pseudo-started and needs to participate in rebalancing.

<span id="DNF_BOOT_CONFIG_RESERVED__0x00000080_"></span><span id="dnf_boot_config_reserved__0x00000080_"></span><span id="DNF_BOOT_CONFIG_RESERVED__0X00000080_"></span>**DNF\_BOOT\_CONFIG\_RESERVED (0x00000080)**  
The boot resources of the device are reserved.

<span id="DNF_NO_RESOURCE_REQUIRED__0x00000100_"></span><span id="dnf_no_resource_required__0x00000100_"></span><span id="DNF_NO_RESOURCE_REQUIRED__0X00000100_"></span>**DNF\_NO\_RESOURCE\_REQUIRED (0x00000100)**  
The device does not require resources.

<span id="DNF_RESOURCE_REQUIREMENTS_NEED_FILTERED__0x00000200_"></span><span id="dnf_resource_requirements_need_filtered__0x00000200_"></span><span id="DNF_RESOURCE_REQUIREMENTS_NEED_FILTERED__0X00000200_"></span>**DNF\_RESOURCE\_REQUIREMENTS\_NEED\_FILTERED (0x00000200)**  
The device's resource requirements list is a filtered list.

<span id="DNF_RESOURCE_REQUIREMENTS_CHANGED__0x00000400_"></span><span id="dnf_resource_requirements_changed__0x00000400_"></span><span id="DNF_RESOURCE_REQUIREMENTS_CHANGED__0X00000400_"></span>**DNF\_RESOURCE\_REQUIREMENTS\_CHANGED (0x00000400)**  
The device's resource requirements list has changed.

<span id="DNF_NON_STOPPED_REBALANCE__0x00000800_"></span><span id="dnf_non_stopped_rebalance__0x00000800_"></span><span id="DNF_NON_STOPPED_REBALANCE__0X00000800_"></span>**DNF\_NON\_STOPPED\_REBALANCE (0x00000800)**  
The device can be restarted with new resources without being stopped.

<span id="DNF_LEGACY_DRIVER__0x00001000_"></span><span id="dnf_legacy_driver__0x00001000_"></span><span id="DNF_LEGACY_DRIVER__0X00001000_"></span>**DNF\_LEGACY\_DRIVER (0x00001000)**  
The device's controlling driver is a non-PnP driver.

<span id="DNF_HAS_PROBLEM__0x00002000_"></span><span id="dnf_has_problem__0x00002000_"></span><span id="DNF_HAS_PROBLEM__0X00002000_"></span>**DNF\_HAS\_PROBLEM (0x00002000)**  
The device has a problem and will be removed.

<span id="DNF_HAS_PRIVATE_PROBLEM__0x00004000_"></span><span id="dnf_has_private_problem__0x00004000_"></span><span id="DNF_HAS_PRIVATE_PROBLEM__0X00004000_"></span>**DNF\_HAS\_PRIVATE\_PROBLEM (0x00004000)**  
The device reported PNP\_DEVICE\_FAILED without also reporting PNP\_DEVICE\_RESOURCE\_REQUIREMENTS\_CHANGED.

<span id="DNF_HARDWARE_VERIFICATION__0x00008000_"></span><span id="dnf_hardware_verification__0x00008000_"></span><span id="DNF_HARDWARE_VERIFICATION__0X00008000_"></span>**DNF\_HARDWARE\_VERIFICATION (0x00008000)**  
The device node has hardware verification.

<span id="DNF_DEVICE_GONE__0x00010000_"></span><span id="dnf_device_gone__0x00010000_"></span><span id="DNF_DEVICE_GONE__0X00010000_"></span>**DNF\_DEVICE\_GONE (0x00010000)**  
The device's PDO is no longer returned in an IRP\_QUERY\_RELATIONS request.

<span id="DNF_LEGACY_RESOURCE_DEVICENODE__0x00020000_"></span><span id="dnf_legacy_resource_devicenode__0x00020000_"></span><span id="DNF_LEGACY_RESOURCE_DEVICENODE__0X00020000_"></span>**DNF\_LEGACY\_RESOURCE\_DEVICENODE (0x00020000)**  
The device node was created for legacy resource allocation.

<span id="DNF_NEEDS_REBALANCE__0x00040000_"></span><span id="dnf_needs_rebalance__0x00040000_"></span><span id="DNF_NEEDS_REBALANCE__0X00040000_"></span>**DNF\_NEEDS\_REBALANCE (0x00040000)**  
The device node has triggered rebalancing.

<span id="DNF_LOCKED_FOR_EJECT__0x00080000_"></span><span id="dnf_locked_for_eject__0x00080000_"></span><span id="DNF_LOCKED_FOR_EJECT__0X00080000_"></span>**DNF\_LOCKED\_FOR\_EJECT (0x00080000)**  
The device is being ejected or is related to a device that is being ejected.

<span id="DNF_DRIVER_BLOCKED__0x00100000_"></span><span id="dnf_driver_blocked__0x00100000_"></span><span id="DNF_DRIVER_BLOCKED__0X00100000_"></span>**DNF\_DRIVER\_BLOCKED (0x00100000)**  
One or more of the drivers for the device node have been blocked from loading.

<span id="DNF_CHILD_WITH_INVALID_ID__0x00200000_"></span><span id="dnf_child_with_invalid_id__0x00200000_"></span><span id="DNF_CHILD_WITH_INVALID_ID__0X00200000_"></span>**DNF\_CHILD\_WITH\_INVALID\_ID (0x00200000)**  
One or more children of the device node have invalid IDs.

<span id="DNF_ASYNC_START_NOT_SUPPORTED__0x00400000_"></span><span id="dnf_async_start_not_supported__0x00400000_"></span><span id="DNF_ASYNC_START_NOT_SUPPORTED__0X00400000_"></span>**DNF\_ASYNC\_START\_NOT\_SUPPORTED (0x00400000)**  
The device does not support asynchronous starts.

<span id="DNF_ASYNC_ENUMERATION_NOT_SUPPORTED__0x00800000_"></span><span id="dnf_async_enumeration_not_supported__0x00800000_"></span><span id="DNF_ASYNC_ENUMERATION_NOT_SUPPORTED__0X00800000_"></span>**DNF\_ASYNC\_ENUMERATION\_NOT\_SUPPORTED (0x00800000)**  
The device does not support asynchronous enumeration.

<span id="DNF_LOCKED_FOR_REBALANCE__0x01000000_"></span><span id="dnf_locked_for_rebalance__0x01000000_"></span><span id="DNF_LOCKED_FOR_REBALANCE__0X01000000_"></span>**DNF\_LOCKED\_FOR\_REBALANCE (0x01000000)**  
The device is locked for rebalancing.

<span id="DNF_UNINSTALLED__0x02000000_"></span><span id="dnf_uninstalled__0x02000000_"></span><span id="DNF_UNINSTALLED__0X02000000_"></span>**DNF\_UNINSTALLED (0x02000000)**  
An IRP\_MN\_QUERY\_REMOVE\_DEVICE request is in progress for the device.

<span id="DNF_NO_LOWER_DEVICE_FILTERS__0x04000000_"></span><span id="dnf_no_lower_device_filters__0x04000000_"></span><span id="DNF_NO_LOWER_DEVICE_FILTERS__0X04000000_"></span>**DNF\_NO\_LOWER\_DEVICE\_FILTERS (0x04000000)**  
There is no Registry entry of the lower-device-filters type for the device.

<span id="DNF_NO_LOWER_CLASS_FILTERS__0x08000000_"></span><span id="dnf_no_lower_class_filters__0x08000000_"></span><span id="DNF_NO_LOWER_CLASS_FILTERS__0X08000000_"></span>**DNF\_NO\_LOWER\_CLASS\_FILTERS (0x08000000)**  
There is no Registry entry of the lower-class-filters type for the device.

<span id="DNF_NO_SERVICE__0x10000000_"></span><span id="dnf_no_service__0x10000000_"></span><span id="DNF_NO_SERVICE__0X10000000_"></span>**DNF\_NO\_SERVICE (0x10000000)**  
There is no Registry entry of the service the for the device.

<span id="DNF_NO_UPPER_DEVICE_FILTERS__0x20000000_"></span><span id="dnf_no_upper_device_filters__0x20000000_"></span><span id="DNF_NO_UPPER_DEVICE_FILTERS__0X20000000_"></span>**DNF\_NO\_UPPER\_DEVICE\_FILTERS (0x20000000)**  
There is no Registry entry of the upper-device-filters type for the device.

<span id="DNF_NO_UPPER_CLASS_FILTERS__0x40000000_"></span><span id="dnf_no_upper_class_filters__0x40000000_"></span><span id="DNF_NO_UPPER_CLASS_FILTERS__0X40000000_"></span>**DNF\_NO\_UPPER\_CLASS\_FILTERS (0x40000000)**  
There is no Registry entry of the upper-class-filters type for the device.

<span id="DNF_WAITING_FOR_FDO__0x80000000_"></span><span id="dnf_waiting_for_fdo__0x80000000_"></span><span id="DNF_WAITING_FOR_FDO__0X80000000_"></span>**DNF\_WAITING\_FOR\_FDO (0x80000000)**  
Enumeration of the device is waiting until the driver attaches its FDO.

 

 





