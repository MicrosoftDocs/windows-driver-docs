---
title: Upgrading Firmware for an NVMe Device
description: Updates to the firmware on an NVMe storage device are issued to the miniport driver for that device. 
ms.assetid: A912715A-F82A-41E5-BE14-5B17930C29B7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Upgrading Firmware for an NVMe Device


Updates to the firmware on an NVMe storage device are issued to the miniport driver for that device. Function commands for getting firmware information, downloading, and activating firmware images are issued to the miniport.

## <span id="Firmware_upgrade_process"></span><span id="firmware_upgrade_process"></span><span id="FIRMWARE_UPGRADE_PROCESS"></span>Firmware upgrade process


NVMe devices certified for Windows are capable of updating their firmware while the device is in operation. Firmware is updated using the [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/library/windows/hardware/ff560512) request containing with the associated firmware control data formatted in an SRB. The update process involves:

1.  Gather the firmware slot information to determine where to place the update. There are a few considerations in deciding where the firmware update will reside.

    -   How many slots are available?
    -   How many slots can hold an update? Some slots are read-only or hold images that must be retained if the ability to revert to a prior image is desired.
    -   Which slot contains the current active firmware image (the running firmware)?

    In order to update the device, a slot is chosen that is writeable and not currently active. All existing image data in the selected slot is overwritten when the update is completed.

2.  Download the new firmware image for a selected slot. Depending on the size of the image, this occurs in a single transfer operation or in successive transfers of multiple portions of the image. A portion of an image is limited by **min**(*Controller Maximum Transfer Size*, 512 KB).
3.  In order to make the downloaded image the active firmware image, it is assigned to slot. The active firmware slot is then switched from the currently used slot to the slot assigned to the downloaded image. Depending on the type of download and the changes in the firmware image, a reboot of the system may be required. This is determined by the NVMe controller.

## <span id="Miniport_firmware_control_requests"></span><span id="miniport_firmware_control_requests"></span><span id="MINIPORT_FIRMWARE_CONTROL_REQUESTS"></span>Miniport firmware control requests


Each function command is set in a **FIRMWARE\_REQUEST\_BLOCK** structure which is included with an [**SRB\_IO\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff566339) in the buffer of an [**IOCTL\_SCSI\_MINIPORT**](https://msdn.microsoft.com/library/windows/hardware/ff560512) request. The **ControlCode** member of **SRB\_IO\_CONTROL** is set to **IOCTL\_SCSI\_MINIPORT\_FIRMWARE** to indicate a miniport firmware operation. Each function command has a related information structure located after the **FIRMWARE\_REQUEST\_BLOCK**. The following table lists each function command and the structures included in the system buffer for **IOCTL\_SCSI\_MINIPORT**.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Input data</th>
<th align="left">Output data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>FIRMWARE_FUNCTION_GET_INFO</p></td>
<td align="left"><p>SRB_IO_CONTROL +</p>
<p>FIRMWARE_REQUEST_BLOCK</p></td>
<td align="left"><p>SRB_IO_CONTROL +</p>
<p>FIRMWARE_REQUEST_BLOCK +</p>
<p>STORAGE_FIRMWARE_SLOT_INFO</p></td>
</tr>
<tr class="even">
<td align="left"><p>FIRMWARE_FUNCTION_DOWNLOAD</p></td>
<td align="left"><p>SRB_IO_CONTROL +</p>
<p>FIRMWARE_REQUEST_BLOCK +</p>
<p>STORAGE_FIRMWARE_DOWNLOAD</p></td>
<td align="left"><p>SRB_IO_CONTROL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FIRMWARE_FUNCTION_ACTIVATE</p></td>
<td align="left"><p>SRB_IO_CONTROL +</p>
<p>FIRMWARE_REQUEST_BLOCK +</p>
<p>STORAGE_FIRMWARE_ACTIVATE</p></td>
<td align="left"><p>SRB_IO_CONTROL</p></td>
</tr>
</tbody>
</table>

 

The firmware functions and associated structures are defined in *ntddscsi.h*.

## <span id="Firmware_slot_information"></span><span id="firmware_slot_information"></span><span id="FIRMWARE_SLOT_INFORMATION"></span>Firmware slot information


Firmware images are maintained on the device in locations called slots. It is necessary to find an available slot for the firmware image to reside when it is activated after a download. To find an available slot, an upgrade utility can send an information query to the device to receive the slot information descriptors. The following example function shows how to retrieve the information for all the firmware slots on a selected NVMe device.

```ManagedCPlusPlus
// A device list item structure for an adapter

typedef struct _DEVICE_LIST {
    HANDLE                      Handle;
    STORAGE_ADAPTER_DESCRIPTOR  AdapterDescriptor;
} DEVICE_LIST, *PDEVICE_LIST;

BOOL
DeviceGetFirmwareInfo(
    _In_ PDEVICE_LIST DeviceList,
    _In_ DWORD        Index,
    _Inout_ PUCHAR    Buffer,
    _In_ DWORD        BufferLength,
    _In_ BOOLEAN      DisplayResult
    )
/*++

Routine Description:

    Retrieve the firmware and firmware slot information from NVMe controller.


Arguments:

    DeviceList    – a pointer to device array that contains disks information.
    Index         – the index of NVMe device in DeviceList array.
    Buffer        – a buffer for input and output.
    BufferLength  – the size of the buffer.
    DisplayResult – print information on screen or not.
  
Return Value:

    BOOLEAN

--*/
{
    BOOL    result;
    ULONG   returnedLength;
    ULONG   firmwareInfoOffset;

    PSRB_IO_CONTROL         srbControl;
    PFIRMWARE_REQUEST_BLOCK firmwareRequest;
    PSTORAGE_FIRMWARE_INFO  firmwareInfo;

    srbControl = (PSRB_IO_CONTROL)Buffer;
    firmwareRequest = (PFIRMWARE_REQUEST_BLOCK)(srbControl + 1);

    //
    // The STORAGE_FIRMWARE_INFO is located after SRB_IO_CONTROL and FIRMWARE_RESQUEST_BLOCK
    //
    firmwareInfoOffset = ((sizeof(SRB_IO_CONTROL) + sizeof(FIRMWARE_REQUEST_BLOCK) - 1) / sizeof(PVOID) + 1) * sizeof(PVOID);

    //
    // Setup the SRB control with the firmware ioctl control info
    //
    srbControl->HeaderLength = sizeof(SRB_IO_CONTROL);
    srbControl->ControlCode = IOCTL_SCSI_MINIPORT_FIRMWARE;
    RtlMoveMemory(srbControl->Signature, IOCTL_MINIPORT_SIGNATURE_FIRMWARE, 8);
    srbControl->Timeout = 30;
    srbControl->Length = BufferLength - sizeof(SRB_IO_CONTROL);

    //
    // Set firmware request fields for FIRMWARE_FUNCTION_GET_INFO. This request is to the controller so
    // FIRMWARE_REQUEST_FLAG_CONTROLLER is set in the flags
    //
    firmwareRequest->Version = FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION;
    firmwareRequest->Size = sizeof(FIRMWARE_REQUEST_BLOCK);
    firmwareRequest->Function = FIRMWARE_FUNCTION_GET_INFO;
    firmwareRequest->Flags = FIRMWARE_REQUEST_FLAG_CONTROLLER;
    firmwareRequest->DataBufferOffset = firmwareInfoOffset;
    firmwareRequest->DataBufferLength = BufferLength - firmwareInfoOffset;

    //
    // Send the request to get the device firmware info
    //
    result = DeviceIoControl(DeviceList[Index].Handle,
                              IOCTL_SCSI_MINIPORT,
                              Buffer,
                              BufferLength,
                              Buffer,
                              BufferLength,
                              &returnedLength,
                              NULL
                              );

    //
    // Format and display the firmware info
    //
    if (DisplayResult) {
        if (!result) {
            _tprintf(_T("\t Get Firmware Information Failed: 0x%X\n"), GetLastError());
        } else {
            UCHAR   i;
            TCHAR   revision[16] = {0};

            firmwareInfo = (PSTORAGE_FIRMWARE_INFO)((PUCHAR)srbControl + firmwareRequest->DataBufferOffset);

            _tprintf(_T("\t ----Firmware Information----\n"));
            _tprintf(_T("\t Support upgrade command: %s\n"), firmwareInfo->UpgradeSupport ? _T("Yes") : _T("No"));
            _tprintf(_T("\t Slot Count: %d\n"), firmwareInfo->SlotCount);
            _tprintf(_T("\t Current Active Slot: %d\n"), firmwareInfo->ActiveSlot);

            if (firmwareInfo->PendingActivateSlot == STORAGE_FIRMWARE_INFO_INVALID_SLOT) {
                _tprintf(_T("\t Pending Active Slot: %s\n\n"),  _T("No"));
            } else {
                _tprintf(_T("\t Pending Active Slot: %d\n\n"), firmwareInfo->PendingActivateSlot);
            }

            for (i = 0; i < firmwareInfo->SlotCount; i++) {
                RtlCopyMemory(revision, &firmwareInfo->Slot[i].Revision.AsUlonglong, 8);

                _tprintf(_T("\t\t Slot Number: %d\n"), firmwareInfo->Slot[i].SlotNumber);
                _tprintf(_T("\t\t Slot Read Only: %s\n"), firmwareInfo->Slot[i].ReadOnly ? _T("Yes") : _T("No"));
                _tprintf(_T("\t\t Revision: %s\n"), revision);
                _tprintf(_T("\n"));
            }
        }

        _tprintf(_T("\n"));
    }

    return result;
}
```

Slot information is returned in an array of **STORAGE\_FIRMWARE\_SLOT\_INFO** structures. Each structure indicates the activation status and availability of the firmware slot. Conditions for availability are:

-   The **ReadOnly** member is set to 0.
-   The slot is not the active slot indicated by slot number in the **ActiveSlot** member of **STORAGE\_FIRMWARE\_INFO**.
-   The **PendingActiveSlot** member of **STORAGE\_FIRMWARE\_INFO** is set to STORAGE\_FIRMWARE\_INFO\_INVALID\_SLOT.
-   The **PendingActiveSlot** member of **STORAGE\_FIRMWARE\_INFO** is not set to the desired slot.

Also, if the slot status meets the conditions for availability but the **Info** string contains valid revision data, that is nonzero bytes, then the slot contains a valid firmware image but it may be replaced. All zeros in the **Info** string indicate an empty slot.

## <span id="Example__Firmware_upgrade_-_slot_selection__download__and_activation"></span><span id="example__firmware_upgrade_-_slot_selection__download__and_activation"></span><span id="EXAMPLE__FIRMWARE_UPGRADE_-_SLOT_SELECTION__DOWNLOAD__AND_ACTIVATION"></span>Example: Firmware upgrade - slot selection, download, and activation


An upgrade utility will perform the three steps mentioned earlier to update the firmware in the controller. As an example, the following upgrade routine contains code for each step in the process. The slot discovery step, shown in the *DeviceGetFirmwareInfo* example, is called by the upgrade routine to select an available slot. The image download and activation steps are demonstrated directly following slot selection. Within each step, the use of the corresponding function command is shown.

During the download step, a firmware image file is read into an allocated buffer and the buffer contents are transferred to the controller. If the firmware image file is larger than the size of the buffer, the image file is read multiple times and that portion of the firmware image is transferred until the entire file is read.

Following the completion of the firmware image download, the activation step requires two actions from the controller. First, the selected slot is assigned to the firmware image, and second, the selected slot is set as the active slot.

```ManagedCPlusPlus
VOID
DeviceFirmwareUpgrade(
    _In_ PDEVICE_LIST DeviceList,
    _In_ DWORD        Index,
    _In_ TCHAR*       FileName
    )
/*++

Routine Description:

    Performs a firmware upgrade to the NVMe controller. The an available firmware
    slot is selected, the firmware is downloaded to the controller from an image
    file, and the new firmware is activated.


Arguments:

    DeviceList    – a pointer to device array that contains disks information.
    Index         – the index of NVMe device in DeviceList array.
    FileName      – the name of the firmware upgrade image file.
  
Return Value:

    None

--*/
{
    BOOL                    result;
    PUCHAR                  buffer = NULL;
    ULONG                   bufferSize;
    ULONG                   firmwareStructureOffset;
    ULONG                   imageBufferLength;

    PSRB_IO_CONTROL         srbControl;
    PFIRMWARE_REQUEST_BLOCK firmwareRequest;

    PSTORAGE_FIRMWARE_INFO      firmwareInfo;
    PSTORAGE_FIRMWARE_DOWNLOAD  firmwareDownload;
    PSTORAGE_FIRMWARE_ACTIVATE  firmwareActivate;

    ULONG                   slotNumber;
    ULONG                   returnedLength;
    ULONG                   i;

    HANDLE                  fileHandle = NULL;
    ULONG                   imageOffset;
    ULONG                   readLength;
    BOOLEAN                 moreToDownload;

    //
    // The STORAGE_FIRMWARE_INFO is located after SRB_IO_CONTROL and FIRMWARE_RESQUEST_BLOCK
    //
    firmwareStructureOffset = ((sizeof(SRB_IO_CONTROL) + sizeof(FIRMWARE_REQUEST_BLOCK) - 1) / sizeof(PVOID) + 1) * sizeof(PVOID);

    //
    // The Max Transfer Length limits the part of buffer that may need to transfer to controller, not the whole buffer.
    //
    bufferSize = min(DeviceList[Index].AdapterDescriptor.MaximumTransferLength, 2 * 1024 * 1024);
    bufferSize += firmwareStructureOffset;
    bufferSize += FIELD_OFFSET(STORAGE_FIRMWARE_DOWNLOAD, ImageBuffer);

    buffer = (PUCHAR)malloc(bufferSize);
    if (buffer == NULL) {
        _tprintf(_T("\t FirmwareUpgrade - Allocate buffer failed: 0x%X\n"), GetLastError());
        return;
    }

    //
    // calculate the space available for the firmware image portion of the buffer allocation
    // 
    imageBufferLength = bufferSize - firmwareStructureOffset - sizeof(STORAGE_FIRMWARE_DOWNLOAD);

    RtlZeroMemory(buffer, bufferSize);

    // ---------------------------------------------------------------------------
    // ( 1 ) SELECT A SUITABLE FIRMWARE SLOT
    // ---------------------------------------------------------------------------

    //
    // Get firmware slot information data.
    //
    result = DeviceGetFirmwareInfo(DeviceList, Index, buffer, bufferSize, FALSE);

    if (result == FALSE) {
        _tprintf(_T("\t FirmwareUpgrade: Get Firmware Information Failed: 0x%X\n"), GetLastError());
        goto Exit;
    }

    //
    // Set the request structure pointers
                //
    srbControl = (PSRB_IO_CONTROL)buffer;
    firmwareRequest = (PFIRMWARE_REQUEST_BLOCK)(srbControl + 1);
    firmwareInfo = (PSTORAGE_FIRMWARE_INFO)((PUCHAR)srbControl + firmwareRequest->DataBufferOffset);

    if (srbControl->ReturnCode != FIRMWARE_STATUS_SUCCESS) {
        _tprintf(_T("\t FirmwareUpgrade - get firmware info failed. srbControl->ReturnCode %d.\n"), srbControl->ReturnCode);
        goto Exit;
    }

    //
    // SelectFind the first writable slot.
    //
    slotNumber = (ULONG)-1;

    if (firmwareInfo->UpgradeSupport) {
        for (i = 0; i < firmwareInfo->SlotCount; i++) {
            if (firmwareInfo->Slot[i].ReadOnly == FALSE) {
                slotNumber = firmwareInfo->Slot[i].SlotNumber;
                break;
            }
        }
    }

    //
    // If no writable slot is found, bypass downloading and activation
    //
    if (slotNumber == (ULONG)-1) {
        _tprintf(_T("\t FirmwareUpgrade - No writable Firmware slot.\n"));
        goto Exit;
    }

    // ---------------------------------------------------------------------------
    // ( 2 ) DOWNLOAD THE FIRMWARE IMAGE TO THE CONTROLLER
    // ---------------------------------------------------------------------------

    //
    // initialize image length and offset
    //
    imageBufferLength = (imageBufferLength / sizeof(PVOID)) * sizeof(PVOID);
    imageOffset = 0;
    readLength = 0;
    moreToDownload = TRUE;

    //
    // Open image file and download it to controller.
    //
    if (FileName == NULL) {
        _tprintf(_T("\t FirmwareUpgrade - No firmware file specified.\n"));
        goto Exit;
    }

    fileHandle = CreateFile(FileName,              // file to open
                            GENERIC_READ,          // open for reading
                            FILE_SHARE_READ,       // share for reading
                            NULL,                  // default security
                            OPEN_EXISTING,         // existing file only
                            FILE_ATTRIBUTE_NORMAL, // normal file
                            NULL);                 // no attr. template

    if (fileHandle == INVALID_HANDLE_VALUE) {
        _tprintf(_T("\t FirmwareUpgrade - unable to open file \"%s\" for read.\n"), FileName);
        goto Exit;
    }

    //
    // Read and download the firmware from the image file into image buffer length portions. Send the
    // image portion to the controller.
    //
    while (moreToDownload) {

        RtlZeroMemory(buffer, bufferSize);

        //
        // Setup the SRB control with the firmware ioctl control info
        //
        srbControl->HeaderLength = sizeof(SRB_IO_CONTROL);
        srbControl->ControlCode = IOCTL_SCSI_MINIPORT_FIRMWARE;
        RtlMoveMemory(srbControl->Signature, IOCTL_MINIPORT_SIGNATURE_FIRMWARE, 8);
        srbControl->Timeout = 30;
        srbControl->Length = bufferSize - sizeof(SRB_IO_CONTROL);

        //
        // Set firmware request fields for FIRMWARE_FUNCTION_DOWNLOAD. This request is to the controller so
        // FIRMWARE_REQUEST_FLAG_CONTROLLER is set in the flags
        //
        firmwareRequest->Version = FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION;
        firmwareRequest->Size = sizeof(FIRMWARE_REQUEST_BLOCK);
        firmwareRequest->Function = FIRMWARE_FUNCTION_DOWNLOAD;
        firmwareRequest->Flags = FIRMWARE_REQUEST_FLAG_CONTROLLER;
        firmwareRequest->DataBufferOffset = firmwareStructureOffset;
        firmwareRequest->DataBufferLength = bufferSize - firmwareStructureOffset;

        //
        // Initialize the firmware data buffer pointer to the proper position after the request structure
        //
        firmwareDownload = (PSTORAGE_FIRMWARE_DOWNLOAD)((PUCHAR)srbControl + firmwareRequest->DataBufferOffset);

        if (ReadFile(fileHandle, firmwareDownload->ImageBuffer, imageBufferLength, &readLength, NULL) == FALSE) {
            _tprintf(_T("\t FirmwareUpgrade - Read firmware file failed.\n"));
            goto Exit;
        }

        if (readLength == 0) {
            moreToDownload = FALSE;
            break;
        }

        if ((readLength % sizeof(ULONG)) != 0) {
            _tprintf(_T("\t FirmwareUpgrade - Read firmware file failed.\n"));
        }

        //
        // Set the download parameters and adjust the offset for this portion of the firmware image
        //
        firmwareDownload->Version = 1;
        firmwareDownload->Size = sizeof(STORAGE_FIRMWARE_DOWNLOAD);
        firmwareDownload->Offset = imageOffset;
        firmwareDownload->BufferSize = readLength;

        //
        // download this portion of firmware to the device
        //
        result = DeviceIoControl(DeviceList[Index].Handle,
                                 IOCTL_SCSI_MINIPORT,
                                 buffer,
                                 bufferSize,
                                 buffer,
                                 bufferSize,
                                 &returnedLength,
                                 NULL
                                 );

        if (result == FALSE) {
            _tprintf(_T("\t FirmwareUpgrade - IOCTL - firmware download failed. 0x%X.\n"), GetLastError());
            goto Exit;
        }

        if (srbControl->ReturnCode != FIRMWARE_STATUS_SUCCESS) {
            _tprintf(_T("\t FirmwareUpgrade - firmware download failed. srbControl->ReturnCode %d.\n"), srbControl->ReturnCode);
            goto Exit;
        }

        //
        // Update Image Offset for next iteration.
        //
        imageOffset += readLength;
    }

    // ---------------------------------------------------------------------------
    // ( 3 ) ACTIVATE THE FIRMWARE SLOT ASSIGNED TO THE UPGRADE
    // ---------------------------------------------------------------------------

    //
    // Activate the newly downloaded image with the assigned slot.
    //
    RtlZeroMemory(buffer, bufferSize);

    //
    // Setup the SRB control with the firmware ioctl control info
    //
    srbControl->HeaderLength = sizeof(SRB_IO_CONTROL);
    srbControl->ControlCode = IOCTL_SCSI_MINIPORT_FIRMWARE;
    RtlMoveMemory(srbControl->Signature, IOCTL_MINIPORT_SIGNATURE_FIRMWARE, 8);
    srbControl->Timeout = 30;
    srbControl->Length = bufferSize - sizeof(SRB_IO_CONTROL);

    //
    // Set firmware request fields for FIRMWARE_FUNCTION_ACTIVATE. This request is to the controller so
    // FIRMWARE_REQUEST_FLAG_CONTROLLER is set in the flags
    //
    firmwareRequest->Version = FIRMWARE_REQUEST_BLOCK_STRUCTURE_VERSION;
    firmwareRequest->Size = sizeof(FIRMWARE_REQUEST_BLOCK);
    firmwareRequest->Function = FIRMWARE_FUNCTION_ACTIVATE;
    firmwareRequest->Flags = FIRMWARE_REQUEST_FLAG_CONTROLLER;
    firmwareRequest->DataBufferOffset = firmwareStructureOffset;
    firmwareRequest->DataBufferLength = bufferSize - firmwareStructureOffset;

    //
    // Initialize the firmware activation structure pointer to the proper position after the request structure
    //
    firmwareActivate = (PSTORAGE_FIRMWARE_ACTIVATE)((PUCHAR)srbControl + firmwareRequest->DataBufferOffset);

    //
    // Set the activation parameters with the available slot selected
    //
    firmwareActivate->Version = 1;
    firmwareActivate->Size = sizeof(STORAGE_FIRMWARE_ACTIVATE);
    firmwareActivate->SlotToActivate = (UCHAR)slotNumber;

    //
    // Send the activation request
    //
    result = DeviceIoControl(DeviceList[Index].Handle,
                                IOCTL_SCSI_MINIPORT,
                                buffer,
                                bufferSize,
                                buffer,
                                bufferSize,
                                &returnedLength,
                                NULL
                                );


    if (result == FALSE) {
        _tprintf(_T("\t FirmwareUpgrade - IOCTL - firmware activate failed. 0x%X.\n"), GetLastError());
        goto Exit;
    }

    //
    // Display status result from firmware activation
    //
    switch (srbControl->ReturnCode) {
    case FIRMWARE_STATUS_SUCCESS:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate succeeded.\n"));
        break;

    case FIRMWARE_STATUS_POWER_CYCLE_REQUIRED:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate succeeded. PLEASE REBOOT COMPUTER.\n"));
        break;

    case FIRMWARE_STATUS_ILLEGAL_REQUEST:
    case FIRMWARE_STATUS_INVALID_PARAMETER:
    case FIRMWARE_STATUS_INPUT_BUFFER_TOO_BIG:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate parameter error. srbControl->ReturnCode %d.\n"), srbControl->ReturnCode);
        break;

    case FIRMWARE_STATUS_INVALID_SLOT:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate, slot number invalid.\n"));
        break;

    case FIRMWARE_STATUS_INVALID_IMAGE:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate, invalid firmware image.\n"));
        break;

    case FIRMWARE_STATUS_ERROR:
    case FIRMWARE_STATUS_CONTROLLER_ERROR:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate, error returned.\n"));
        break;

    default:
        _tprintf(_T("\t FirmwareUpgrade - firmware activate, unexpected error. srbControl->ReturnCode %d.\n"), srbControl->ReturnCode);
        break;
   }

Exit:

    if (fileHandle != NULL) {
        CloseHandle(fileHandle);
    }

    if (buffer != NULL) {
        free(buffer);
    }

    return;
}
```

**Note**  Downloading multiple firmware images simultaneously is not supported. A single firmware download is always followed by a single firmware activation.

 

A firmware image already resident in a slot can be reactivated by using just the activate function command with the corresponding slot number.

The **IOCTL\_SCSI\_MINIPORT\_FIRMWARE** control code for SRB I/O control is available starting with Windows 8.1.

 

 




