---
title: ACLs and the Device Stack
description: ACLs and the Device Stack
ms.assetid: DAFC851D-E808-4588-86D2-E608584FD05B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ACLs and the Device Stack


The access to the volume and the device are controlled by ACLs that are set on each of the respective interfaces. ACLs on the device interface determine:

-   Whether the user receives the requested access permission when an application requests to open a handle to the device.

-   Which commands can be sent to the device.

The driver stacks for removable media such as a CD drive can have more than one interface:

-   The one associated with the PDO, which is managed by the port driver.

-   The one associated with the FDO, which is managed by the class driver (Cdrom.sys).

The driver stack for hot-pluggable devices such as UFD also offers an interface to the volume manager. For example, a formatting utility would open a handle to the volume interface to format the volume.

For direct access, applications can use the port driver and class driver interfaces to open a handle to the drive. For example, if an application wants to send a SCSI command to the device through the physical drive interface, the process is as follows:

-   The application first opens a handle to the drive interface for Read and Write access.

-   After the handle is opened successfully, the application can use the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function to send the SCSI request to the device.

When the driver stack creates the device interface, an ACL is applied on that device. The ACL’s access control elements (ACE) describe the user groups and related access permissions. For example, an ACE for the Administrators group might describe the Read and Write access permissions that administrators have for that device interface.

When an application attempts to open a handle to the device, the I/O manager uses the device’s ACL to determine whether the caller is allowed the requested access. For example, if the caller requests a handle to the device for Read and Write access, the handle is provided only if the caller is allowed to read and write through that interface. If the caller does not have the requested access permissions, the I/O manager returns an Access Denied error and the open handle request fails.

Device ACLs are created by these Windows components: I/O manager, PnP manager, and the new Group Policy Service for removable storage devices.

## <span id="I_O_Manager_and_Removable_Media_Device_ACLs"></span><span id="i_o_manager_and_removable_media_device_acls"></span><span id="I_O_MANAGER_AND_REMOVABLE_MEDIA_DEVICE_ACLS"></span>I/O Manager and Removable Media Device ACLs


When the driver stack creates the device object, the I/O manager sets a default ACL that is based on the device type. The default ACL gives Full access to SYSTEM and Administrators, and it gives only Execute access to everyone else.

-   By default the I/O manager grants the IU group Full access for device objects for removable media devices such as CD drives and for those disk device objects that have defined FILE\_REMOVABLE\_MEDIA characteristics.

    **Note**  Prior to Windows Vista, the entry for IU was not present in the ACL that was set by the I/O manager. Starting with Windows Vista, the I/O manager provides Full access to the IU group, so that applications can receive direct access to a volume without requiring elevation of privilege, as discussed earlier. However, UFD devices that do not set the **Removable** property do not benefit from this because the I/O manager does not treat them as removable.

     

-   The disk class driver sets the FILE\_REMOVABLE\_MEDIA characteristic if the identity data (received from the device in response to the SCSI INQUIRY command) has the **Removable** property set. Because some UFD devices set this property even though they are not truly removable media, the I/O manager treats such devices as removable disks and provides the IU group Read and Write access to the volume.

-   By default the I/O manager gives only Execute access for remotely connected users for removable media device objects (CD devices) and for those disk device objects that have FILE\_REMOVABLE\_MEDIA characteristics set. Because of this, remote users cannot burn data by using a CD or DVD drive or perform backup to an optical media or format a removable disk. Administrators can set the Removable Storage Access group policy to override the default behavior. When this policy is set, the I/O manager grants Full access to remote user for these devices, allowing read and write capabilities.

## <span id="PnP_Manager_and_Removable_Media_Device_ACLs"></span><span id="pnp_manager_and_removable_media_device_acls"></span><span id="PNP_MANAGER_AND_REMOVABLE_MEDIA_DEVICE_ACLS"></span>PnP Manager and Removable Media Device ACLs


When the device driver stack is started, the PnP manager changes the ACL on the device only if the device’s key in the registry specifies a security descriptor for that device. The device vendor can set this descriptor by using **SetupDiSetDeviceRegistryProperty** with the property set as in the following.

|          |                                  |
|----------|----------------------------------|
| Property | SPDRP\_SECURITY                  |
| Value    | **SECURITY\_DESCRIPTOR**         |
| Size     | **sizeof**(SECURITY\_DESCRIPTOR) |

 

These properties can also be set through a driver package installer, by specifying the related parameters in an INF file.

## <span id="Group_Policy_Service_for_Removable_Storage_Devices_ACLs"></span><span id="group_policy_service_for_removable_storage_devices_acls"></span><span id="GROUP_POLICY_SERVICE_FOR_REMOVABLE_STORAGE_DEVICES_ACLS"></span>Group Policy Service for Removable Storage Devices ACLs


This is a Windows service that lets administrators set ACLs for the volume interface for disks and the volume interface for CD or DVD, tape and floppy disk drives, and WPD devices through the Group Policy framework. This group policy can be changed dynamically. When the policy is applied to the machine, the service updates the ACL for the devices. The ACL that is applied by this service overrides the default ACL that was set by the I/O manager and the PnP manager.

The Group Policy Service sets the ACL on the volume interface for the disk, but not on the interface that the disk class driver provided. This is because, when an application accesses files and directories on the volume, I/O manager uses the ACL on the corresponding volume object to determine whether the caller has the required access permissions. Therefore, by setting the ACL on the volume device object, the Group Policy service enforces the access rights that the administrator set for that volume.

## <span id="Security_Check_Process"></span><span id="security_check_process"></span><span id="SECURITY_CHECK_PROCESS"></span>Security Check Process


When an application attempts to open a handle to the device interface, the I/O manager checks whether the user has been granted the access permissions that are requested in the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) call. If yes, the handle is opened; otherwise, the call fails with error ACCESS\_DENIED.

After the handle is opened, the application can send commands directly to the device, typically by using an IOCTL. For example, to send a SCSI pass-through command, an application would use **IOCTL\_SCSI\_PASS\_THROUGH** or **IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**.

-   **IOCTL\_DISK\_GET\_PARTITION\_INFO** requires just Read access.

-   **IOCTL\_SCSI\_PASS\_THROUGH** and **IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT** require the caller to have opened the handle to the interface (which is provided by storage device driver) for both Read and Write access.

The opcode in the command descriptor block (CDB) that is given in the SCSI pass-through request is not checked to determine whether Read, Write, or both Read and Write access is required. That is why Windows always requires the handle to the device to be opened for Reads and Writes for pass-through requests, even if the application is only doing a read, a write, or no data transfer at all.

**IOCTL\_DISK\_VERIFY** can be sent without regard to the access permissions that were requested in a [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) call. When the I/O manager receives an IOCTL, it checks the access permissions required for that IOCTL and compares them with the access permissions granted to the caller in the **CreateFile** call. If there is a match, the IOCTL is sent to the target device; otherwise, the IOCTL call is failed with the error ACCESS\_DENIED.

For example, if the caller has opened a handle for Read-only access, like the following.

-   **IOCTL\_SCSI\_PASS\_THROUGH** fails with error ACCESS\_DENIED because it requires both Read and Write access.

-   **IOCTL\_DISK\_GET\_PARTITION\_INFO** is sent to the driver stack because it requires only Read access.

 

 




