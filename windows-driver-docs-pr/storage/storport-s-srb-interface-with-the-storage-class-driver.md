---
title: Storport's SRB Interface with the Storage Class Driver
description: Storport's SRB Interface with the Storage Class Driver
ms.assetid: c7e55516-0ba9-48bc-9b68-e6344552f070
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport's SRB Interface with the Storage Class Driver


Storage class drivers and other higher-level components communicate with the Storport driver by building SCSI Request Blocks (SRBs). An SRB contains a SCSI command descriptor block (CDB) and a pointer to the data buffer that is to be used to transfer data to or from the device (if any). It may contain a pointer to a sense buffer that is used to hold SCSI sense data in the event the SCSI command fails with Check Condition status. For more information about SRBs, see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393). Storage class drivers pass the SRBs that they create to Storport in an IRP with the **MajorFunction** member set to IRP\_MJ\_SCSI. For a description of the steps that a storage class driver must take to build an SRB before passing it to a port driver, see [Storage Class Driver's BuildRequest Routine](storage-class-driver-s-buildrequest-routine.md).

Before forwarding an SRB down the stack, Storport sets certain values in the SRB, such as the path, the target number, and the logical unit number of the target device.

Unlike other port drivers, such as the system-supplied port drivers for the IDE/ATAPI and IEEE 1394 buses, Storport does not have to translate the command descriptor block (CDB) in the SRBs that it receives into a different format before forwarding it to the underlying adapter. Storport simply adds some target-specific information to the SRB and passes it to the miniport driver with the CDB unaltered. Therefore, Storport simply passes SRBs that contain CDBs down the stack.

For this reason, most aspects of the SRB interface between the storage class driver and Storport are covered in the general documentation for storage class and storage miniport drivers and their accompanying reference materials. For a list of sections related to the SRB interface between the storage class driver and the Storport-miniport driver pair, see [Storport's Interface with Storport Miniport Drivers](storport-s-interface-with-storport-miniport-drivers.md).

 

 




