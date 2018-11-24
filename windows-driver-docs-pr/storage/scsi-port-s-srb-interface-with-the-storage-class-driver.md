---
title: SCSI Port's SRB Interface with the Storage Class Driver
description: SCSI Port's SRB Interface with the Storage Class Driver
ms.assetid: ca30bf9b-6d76-4160-8a4e-54c681dfc843
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Port's SRB Interface with the Storage Class Driver


## <span id="ddk_scsi_ports_srb_interface_with_the_storage_class_driver_kg"></span><span id="DDK_SCSI_PORTS_SRB_INTERFACE_WITH_THE_STORAGE_CLASS_DRIVER_KG"></span>


Storage class drivers and other higher-level components communicate with the SCSI Port driver by building SCSI Request Blocks (SRBs). For more information about SRBs, see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393). Storage class drivers pass the SRBs that they create to SCSI Port in an IRP with the **MajorFunction** member set to IRP\_MJ\_SCSI. For a description of the steps that a storage class driver must take to build an SRB before passing it to a port driver, see [Storage Class Driver's BuildRequest Routine](storage-class-driver-s-buildrequest-routine.md).

Before forwarding an SRB down the stack, SCSI Port sets certain values in the SRB, such as the port number, the path, the target number, and the logical unit number of the target device.

Unlike other port drivers, such as the system-supplied port drivers for the IDE/ATAPI and IEEE 1394 buses, SCSI Port does not have to translate the command descriptor block (CDB) in the SRBs that it receives into a different format before forwarding it to the underlying adapter. SCSI Port simply adds some target-specific information to the SRB and passes it to the miniport driver with the CDB unaltered. Therefore, SCSI Port is simply a messenger that passes SRBs that contain CDBs down the stack.

For this reason, most aspects of the SRB interface between the storage class driver and SCSI Port are covered in the general documentation for storage class and storage miniport drivers and their accompanying reference materials. For a list of sections related to the SRB interface between the storage class driver and the SCSI Port-miniport driver pair, see [SCSI Port's Interface with SCSI Port Miniport Drivers](scsi-port-s-interface-with-scsi-port-miniport-drivers.md).

 

 




