---
title: SCSI Miniport Driver's HwScsiDmaStarted Routine
description: SCSI Miniport Driver's HwScsiDmaStarted Routine
ms.assetid: 697839f0-e912-42a5-abe0-f6bb946c86d8
keywords: ["SCSI miniport drivers WDK storage , HwScsiDmaStarted", "HwScsiDmaStarted", "DMA controllers WDK SCSI"]
---

# SCSI Miniport Driver's HwScsiDmaStarted Routine


## <span id="ddk_scsi_miniport_drivers_hwscsidmastarted_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIDMASTARTED_ROUTINE_KG"></span>


A miniport driver of an HBA that uses the system DMA controller must have an [**HwScsiDmaStarted**](https://msdn.microsoft.com/library/windows/hardware/ff557291) routine.

For a data transfer operation, such a miniport driver must call [**ScsiPortIoMapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff564649), passing in the pointers to its device extension for per-HBA data and to the SRB requesting the transfer, along with a range of logical addresses for the buffer from which or into which the data will be transferred.

Note that the logical address range passed to **ScsiPortIoMapTransfer** either must be the mapped values for the input SRB's **DataBuffer** and **DataTransferLength** or a proper subset of this range. For most transfer requests, a miniport driver writer can assume that all data specified in the input SRB can be transferred in a single DMA operation.

In particular, a miniport driver might have to carry out more than one subordinate DMA transfer operation to satisfy a given SRB only if the HBA provides application-dedicated support and the application sends large transfer requests directly to the miniport driver. Otherwise, it is the responsibility of the storage class drivers to split up large transfer requests into a set of partial transfer requests, each sized to suit the capabilities of the HBA (see [Storage Class Drivers](storage-class-drivers.md)).

**ScsiPortIoMapTransfer** calls the miniport driver's *HwScsiDmaStarted* routine when the system DMA controller is ready to transfer data between system memory and the HBA. *HwScsiDmaStarted* must set up the HBA for the transfer operation.

When a transfer operation is complete, the miniport driver must call [**ScsiPortFlushDma**](https://msdn.microsoft.com/library/windows/hardware/ff564618) before it calls **ScsiPortNotification** with the SRB and/or calls **ScsiPortIoMapTransfer** to set up the DMA controller again for a subrange in an application-supplied buffer if the HBA is dedicated to the support of a user-mode application.

**ScsiPortFlushDma** flushes any remaining data cached in the DMA controller. Note that **ScsiPortFlushDma** also can be called to cancel a system DMA transfer, even if the miniport driver's *HwScsiDmaStarted* routine has not yet been called.

See [**ScsiPortIoMapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff564649) and [**ScsiPortFlushDma**](https://msdn.microsoft.com/library/windows/hardware/ff564618) for more information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiDmaStarted%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




