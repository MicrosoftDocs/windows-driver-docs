---
title: Thin Provisioning
description: Thin Provisioning
ms.assetid: 0D65DDCC-D207-4EA8-B5D6-56DF57221EE3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Thin Provisioning


## <span id="Overview"></span><span id="overview"></span><span id="OVERVIEW"></span>Overview


Thin provisioning is an end-to-end storage provisioning solution. It requires planning for storage deployment and execution on the host and client application. Windows Server thin provisioning features serve as interfaces between the thin provisioning-capable storage and the host server. Thin provisioning features include thin provisioning logical unit (LUN) identification, threshold notification, handles for resource exhaustion, and space reclamation for delivering highly available and scalable storage provisioning service to end users.

## <span id="Thin_Provisioning_LUN_Identification"></span><span id="thin_provisioning_lun_identification"></span><span id="THIN_PROVISIONING_LUN_IDENTIFICATION"></span>Thin Provisioning LUN Identification


Windows Server has adopted the T10 SCSI Block Command 3 (SBC3) standard specification for identifying thin provisioning LUNs starting with Windows Server 2012. During the initial target device enumeration, Windows Server gathers all property parameters from the target device. Windows Server identifies the provisioning type and the UNMAP and TRIM capability. The storage device reports its provisioning type and UNMAP and TRIM capability according to the SBC3 specification.

If the storage device does not accurately report its current capability, device compatibility issues may occur. For example, if the storage device reports that it supports the UNMAP command, but it does not support the UNMAP command, a disk format hang issue may occur. When provisioning type information is accurate, the storage stack can provide better I/O handling according to the storage provisioning type.

## <span id="Run-time_Provisioning_Type_or_LUN_Capacity_Changes"></span><span id="run-time_provisioning_type_or_lun_capacity_changes"></span><span id="RUN-TIME_PROVISIONING_TYPE_OR_LUN_CAPACITY_CHANGES"></span>Run-time Provisioning Type or LUN Capacity Changes


A storage administrator may change the provisioning type or the capacity of the LUN. When the provisioning type or LUN capacity is changed, the storage array raises a UNIT ATTENTION sense condition that returns the correct information when the sense data is requested. Windows Server logs a system event to alert the system administrator of the provisioning type or LUN capacity change.

## <span id="Threshold_and_Resource_Exhaustion_Handles_"></span><span id="threshold_and_resource_exhaustion_handles_"></span><span id="THRESHOLD_AND_RESOURCE_EXHAUSTION_HANDLES_"></span>Threshold and Resource Exhaustion Handles


A thin provisioning LUN is usually created with less physical disk space than the size of the LUN. Threshold notification is a required function to alert the host and client application of the storage space consumption state. Most thin provisioning storage arrays do not report an event when the threshold is reached. These thin provisioning storage solutions resolve the threshold notification through their proprietary storage management utility. Therefore, for the host and client application, the only event that these storage arrays report is permanent resource exhaustion. The thin provisioning storage device can use the threshold notification handle, temporary resource exhaustion handle, or permanent resource exhaustion handle to alert system administrators or client applications when storage space consumption is nearing capacity.

### <span id="Thin_Provisioning_Threshold_Notification"></span><span id="thin_provisioning_threshold_notification"></span><span id="THIN_PROVISIONING_THRESHOLD_NOTIFICATION"></span>Thin Provisioning Threshold Notification

The storage management utility sets the thin provisioning threshold. Windows Server does not override the threshold set by the storage management utility. For the thin provisioning LUN, the storage administrator must specify the threshold according to the average storage consumption rate. When a write command crosses the threshold that the storage target device has set, the target device terminates the command by using sense data and sends a “THIN PROVISIONING SOFT THRESHOLD REACHED” message. When Windows Server receives the matched sense data, the following occurs:

-   A system event is logged to alert the host administrator that the resource usage or availability threshold was reached on the LUN device.
-   In the system event log, information is reported about the used and available mapped resources from the log page of the target device. For this to occur, the storage array must support the log page specification for logical block provisioning in order for Windows Server to generate the system event.
-   The terminated command is retried.

**Note**  Write commands sent after this error is logged could potentially be lost if FILE\_FLAG\_WRITE\_THROUGH is not set because they may trigger a permanent resource exhaustion condition.

 

### <span id="Temporary_Resource_Exhaustion"></span><span id="temporary_resource_exhaustion"></span><span id="TEMPORARY_RESOURCE_EXHAUSTION"></span>Temporary Resource Exhaustion

When the storage array enables the auto grow function on a LUN, an administrator can use the temporary resource exhaustion notification to ensure that the storage device can allocate additional space to the LUN within four seconds. When a write command causes a temporary resource exhaustion condition, the storage device terminates the command that requests the operation by using sense data and returns a “SPACE ALLOCATION IN PROGRESS” message. Temporary resource exhaustion is handled as follows:

-   Retry the original request four times with the retry interval set to 1 second.
-   If all retries fail, the request is failed back to the application.
-   If the storage device does not handle the temporary resource exhaustion, Windows Server expects the storage device to fail the next write request by returning a permanent resource exhaustion status.

### <span id="Permanent__Resource_Exhaustion"></span><span id="permanent__resource_exhaustion"></span><span id="PERMANENT__RESOURCE_EXHAUSTION"></span>Permanent Resource Exhaustion

The permanent resource exhaustion condition indicates that the thin provisioning LUN has reached the maximum storage space limit. When permanent resource exhaustion occurs during a write command, the storage device terminates the operation by using sense data and sends a “SPACE ALLOCATION FAILED WRITE PROTECT” message. Permanent exhaustion is handled as follows:

-   If the original request has FILE\_FLAG\_WRITE\_THROUGH set, then it is failed back to the application.
-   If the original request does not have FILE\_FLAG\_WRITE\_THROUGH set, then the application may receive a success response without the request being completed nor flushed to physical media.
-   A system event is logged that includes a “permanent resource exhaustion” error message.
-   The error code is passed back to the partition manager and takes the LUN offline.

## <span id="Storage_Space_Reclamation_Using_the_UNMAP_Command"></span><span id="storage_space_reclamation_using_the_unmap_command"></span><span id="STORAGE_SPACE_RECLAMATION_USING_THE_UNMAP_COMMAND"></span>Storage Space Reclamation Using the UNMAP Command


Space reclamation can be triggered by file deletion, a file system level trim, or a storage optimization operation. File system level trim is enabled for a storage device designed to perform “read return zero” after a trim or an unmap operation.

### <span id="Space_Reclamation_Operation_in_the_Storage_Stack"></span><span id="space_reclamation_operation_in_the_storage_stack"></span><span id="SPACE_RECLAMATION_OPERATION_IN_THE_STORAGE_STACK"></span>Space Reclamation Operation in the Storage Stack

When a large file is deleted from the file system or a file system level trim is triggered, Windows Server converts file delete or trim notifications into a corresponding UNMAP request. The storage port driver stack translates the UNMAP request into an SCSI UNMAP command or an ATA TRIM command according to the protocol type of the storage device. During the storage device enumeration, the Windows storage stack gathers information about whether the storage device supports UNMAP or TRIM commands. Only the UNMAP request is sent to the storage device if the device has SCSI UNMAP or ATA TRIM capability. Windows Server also provides an API implementation for unmapping LBAs on a storage target device. Windows Server does not adopt T10 SCSI WRITE SAME command sets.

### <span id="UNMAP_Requests_from_the_Hyper-V_Guest_Operating_System"></span><span id="unmap_requests_from_the_hyper-v_guest_operating_system"></span><span id="UNMAP_REQUESTS_FROM_THE_HYPER-V_GUEST_OPERATING_SYSTEM"></span>UNMAP Requests from the Hyper-V Guest Operating System

During the virtual machine (VM) creation, a Hyper-V host sends an inquiry about whether the storage device where the virtual hard disk (VHD) resides supports UNMAP or TRIM commands. When a large file is deleted from the file system of a VM guest operating system, the guest operating system sends a file delete request to the virtual machine’s virtual hard disk (VHD) or VHD file. The VM’s VHD or VHD file tunnels the SCSI UNMAP request to the class driver stack of the Windows Hyper-V host, as follows:

-   If the VM has a VHD, the VHD converts SCSI UNMAP or ATA TRIM commands into a Data Set Management I/O control code (IOCTL DSM) TRIM request, and then sends the request to the host storage device.
-   If the VM has a VHD file, the VHD file system converts SCSI UNMAP or ATA TRIM commands into file system-level trim requests, and then sends the requests to the host operating system.

Windows Hyper-V also supports IOCTL DSM TRIM calls from the guest operating system.

### <span id="Windows_Optimize_Drives_Utility"></span><span id="windows_optimize_drives_utility"></span><span id="WINDOWS_OPTIMIZE_DRIVES_UTILITY"></span>Windows Optimize Drives Utility

End users or system administrators can use the Optimize Drives utility to reclaim space either by creating a manual request or by optimizing the schedule configuration. If the disk drive is a thin provisioning LUN, the media type of the disk drive appears as “Thin Provisioning Drive”.

The system administrator can schedule a storage space consolidation by using the Optimize Drives utility. The utility can also notify the system administrator if the system misses three consecutive scheduled runs.

## <span id="Retrieving_the_Slab_Mapping_State"></span><span id="retrieving_the_slab_mapping_state"></span><span id="RETRIEVING_THE_SLAB_MAPPING_STATE"></span>Retrieving the Slab Mapping State


In a thin provisioning LUN, all logical blocks are grouped in slabs (clusters). The slab size is set by the OPTIMAL UNMAP GRANULARITY parameter that the storage device reports. All slabs are classified into Mapped, De-allocated or Anchored states. Windows Server treats both De-allocated and Anchored states as unmapped states. Windows Server provides an API implementation, or an IOCTL DSM allocation, to retrieve the LBA provisioning status from thin provisioning LUNs for the storage management operation. The application can call the IOCTL DSM allocation routine to send the SCSI command and retrieve the mapped or unmapped state of each slab in a particular range. If the LBA provisioning status returned does not describe the entire allocation range, the application sends another SCSI command to retrieve the provisioning status of the remaining LBA range.

The storage device does not need to process the entire LBA range in one return. If the partial LBA range of the original request has been returned, another command is sent to retrieve the mapping states of the remaining LBA range.

 

 




