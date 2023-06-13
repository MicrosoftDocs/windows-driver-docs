---
title: CD-ROM I/O control codes
description: Class drivers for CD-ROM devices handle additional public I/O control codes, described in this topic.
keywords:
- CD-ROM drivers WDK storage
- IOCTLs WDK CD-ROM
ms.date: 12/20/2018
---

# CD-ROM I/O control codes

All public I/O control codes for drivers of CD-ROM devices use buffered I/O. Consequently, the input or output data for these requests is at Irp->AssociatedIrp.SystemBuffer.

Class drivers for CD-ROM devices handle additional public I/O control codes, along with those described in this section. For more information about requirements for storage class drivers, see [General Storage I/O Control Codes](general-storage-io-control-codes.md).

|I/O control code|Description|
|----|----|
|[IOCTL_CDROM_CHECK_VERIFY](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_check_verify)|This IOCTL is replaced by [IOCTL_STORAGE_CHECK_VERIFY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_check_verify). The only difference between the two IOCTLs is the base value.|
|**IOCTL_CDROM_CLOSE_DOOR**|This I/O control code has been replaced by [IOCTL_STORAGE_LOAD_MEDIA](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_load_media).|
|[IOCTL_CDROM_ENABLE_STREAMING](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_enable_streaming)|Enables or disables CDROM streaming mode on a per-handle basis for raw read and write requests. To perform this operation, call the **DeviceIoControl** function and specify the **IOCTL_CDROM_ENABLE_STREAMING** I/O control request as the *dwIoControlCode* parameter.|
|[IOCTL_CDROM_EXCLUSIVE_ACCESS](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_exclusive_access)|Instructs the CD-ROM class driver to export the access state of a CD-ROM device, lock a CD-ROM device for exclusive access, and unlock a CD-ROM device for exclusive access.|
|[IOCTL_CDROM_FIND_NEW_DEVICES](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_find_new_devices)|This IOCTL is replaced by [IOCTL_STORAGE_FIND_NEW_DEVICES](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_find_new_devices). The only difference between the two IOCTLs is the base value.|
|[IOCTL_CDROM_GET_CONFIGURATION](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_configuration)|Requests feature and profile information from a CD-ROM device.|
|[IOCTL_CDROM_GET_DRIVE_GEOMETRY](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_drive_geometry)|Returns information about the CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).|
|[IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_drive_geometry_ex)|Returns information about a CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).|
|[IOCTL_CDROM_GET_INQUIRY_DATA](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_inquiry_data)|Returns the SCSI inquiry data for the CD-ROM device. This IOCTL can be used when a device has been exclusively locked with [IOCTL_CDROM_EXCLUSIVE_ACCESS](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_exclusive_access).|
|[IOCTL_CDROM_GET_LAST_SESSION](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_last_session)|Queries the device for the first complete session number, the last complete session number, and the last complete session starting address.|
|[IOCTL_CDROM_GET_PERFORMANCE](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_performance)|Retrieves the supported speeds from the device. The **IOCTL_CDROM_GET_PERFORMANCE** I/O control request is a wrapper over the MMC command, GET PERFORMANCE.|
|[IOCTL_CDROM_LOAD_MEDIA](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_load_media)|Draws a protruding CDROM tray back into the drive.|
|[IOCTL_CDROM_RAW_READ](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_raw_read)|Reads data from the CD-ROM in raw mode.|
|[IOCTL_CDROM_READ_Q_CHANNEL](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_read_q_channel)|Returns the current position (obsolete), media catalog, or ISRC track data.|
|[IOCTL_CDROM_READ_TOC](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_read_toc)|Obsolete. Returns the table of contents of the media.|
|[IOCTL_CDROM_READ_TOC_EX](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_read_toc_ex)|Queries the target device for the table of contents (TOC), the program memory area (PMA), and the absolute time in pregroove (ATIP).|
|[IOCTL_CDROM_SEND_OPC_INFORMATION](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_send_opc_information)|Used in file systems and other implementations that want to perform the Optimum Power Calibration (OPC) procedure in advance, so that the first streaming write does not have to wait for the procedure to finish.|
|[IOCTL_CDROM_SET_SPEED](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_set_speed)|Sets the spindle speed of the CD-ROM drive.|


## Media playback control
Beginning with Windows Vista, CDROM class drivers do not use these IOCTLs. Prior to Windows Vista, these IOCTLs were used for audio playback on older CD-ROM drives that supported direct audio output in hardware.

Client applications should use the [Media Control Interface (MCI)](/windows/win32/multimedia/media-control-interface--mci) API rather than issuing these IOCTLs.

|I/O control code|Description|
|----|----|
|[IOCTL_CDROM_GET_CONTROL](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_control)|Determines the current audio playback mode.|
|[IOCTL_CDROM_GET_VOLUME](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_get_volume)|Determines the current volume for each of its device's audio ports.|
|[IOCTL_CDROM_PAUSE_AUDIO](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_pause_audio)|Suspends audio play.|
|[IOCTL_CDROM_PLAY_AUDIO_MSF](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_play_audio_msf)|Plays the specified range of the media.|
|[IOCTL_CDROM_READ_Q_CHANNEL](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_read_q_channel)|Returns the current position (obsolete), media catalog, or ISRC track data.|
|[IOCTL_CDROM_RESUME_AUDIO](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_resume_audio)|Resumes a suspended audio operation.|
|[IOCTL_CDROM_SEEK_AUDIO_MSF](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_seek_audio_msf)|Moves the heads to the specified MSF on the media.|
|[IOCTL_CDROM_SET_VOLUME](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_set_volume)|Resets the volume for its device's audio ports.|
|[IOCTL_CDROM_STOP_AUDIO](/windows-hardware/drivers/ddi/ntddcdrm/ni-ntddcdrm-ioctl_cdrom_stop_audio)|Ends audio play.|
