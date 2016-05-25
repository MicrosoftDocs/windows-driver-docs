---
title: Handling SRB\_FUNCTION\_EXECUTE\_SCSI
author: windows-driver-content
description: Handling SRB\_FUNCTION\_EXECUTE\_SCSI
ms.assetid: 221e1070-12d8-4870-a23c-426ed4a25b84
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_EXECUTE_SCSI"]
---

# Handling SRB\_FUNCTION\_EXECUTE\_SCSI


## <span id="ddk_handling_srb_function_execute_scsi_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_EXECUTE_SCSI_KG"></span>


After the higher-level storage class drivers have loaded, most of the SRBs sent to the [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine have the **Function** member set to SRB\_FUNCTION\_EXECUTE\_SCSI.

On receipt of an SRB\_FUNCTION\_EXECUTE\_SCSI request, a miniport driver's *HwScsiStartIo* routine does the following:

-   Gets and/or sets up whatever context the miniport driver maintains in its device, logical unit, and/or SRB extensions

    For example, a miniport driver might set up a logical unit extension with pointers to the SRB itself and the SRB **DataBuffer** pointer, the SRB **DataTransferLength** value, and a driver-defined value (or CDB SCSIOP\_*XXX* value) indicating the operation to be carried out on the HBA.

-   Calls an internal routine to program the HBA, as partially directed by the **SrbFlags**, for the requested operation

    For a device I/O operation, such an internal routine generally selects the target device and sends the CDB over the bus to the target logical unit.

If the miniport driver uses system DMA, it must call [**ScsiPortIoMapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff564649)*before* programming the HBA to transfer data. **ScsiPortIoMapTransfer** sets up the system DMA controller and calls the miniport driver's *HwScsiDmaStarted* routine, described later in [SCSI Miniport Driver's HwScsiDmaStarted Routine](scsi-miniport-driver-s-hwscsidmastarted-routine.md).

All system-defined, required device I/O control requests sent to NT-based operating system storage class drivers are mapped to SRBs with the **Function** member set to SRB\_FUNCTION\_EXECUTE\_SCSI.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_EXECUTE_SCSI%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


