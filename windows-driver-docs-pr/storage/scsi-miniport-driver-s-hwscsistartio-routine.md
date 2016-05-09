---
title: SCSI Miniport Driver's HwScsiStartIo Routine
description: SCSI Miniport Driver's HwScsiStartIo Routine
ms.assetid: cb818e5f-b91f-44cb-972b-22f75459edeb
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "incoming I/O requests WDK SCSI"]
---

# SCSI Miniport Driver's HwScsiStartIo Routine


## <span id="ddk_scsi_miniport_drivers_hwscsistartio_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSISTARTIO_ROUTINE_KG"></span>


As its name suggests, a [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine is the entry point for incoming requests to peripheral devices on the HBA-driven bus(es). *HwScsiStartIo* is called with pointers to a SCSI request block (SRB) and to the miniport driver's device extension for per-HBA state. For information about the syntax of this routine see **HwScsiStartIo**.

If the miniport driver's **DriverEntry** routine also requested that memory be allocated for logical unit extensions (see [Calling ScsiPortInitialize](calling-scsiportinitialize.md)), the *HwScsiStartIo* routine calls **ScsiPortGetLogicalUnit** with the input device extension pointer and the **PathId**, **TargetId**, and **Lun** values from the input SRB.

If the **DriverEntry** routine requested that memory be allocated for SRB extensions, the **SrbExtension** member in each SRB contains a pointer to the miniport driver's per-request storage area. Note that a miniport driver must request that memory be allocated for **SrbExtension**s if it maintains per-request state information. It cannot use an SRB for this purpose.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiStartIo%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




