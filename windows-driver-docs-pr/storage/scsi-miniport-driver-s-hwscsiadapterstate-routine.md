---
title: SCSI Miniport Driver's HwScsiAdapterState Routine
description: SCSI Miniport Driver's HwScsiAdapterState Routine
ms.assetid: 359c41ba-b8d9-4e2d-87d7-025db377606b
keywords: ["SCSI miniport drivers WDK storage , HwScsiAdapterState", "HwScsiAdapterState"]
---

# SCSI Miniport Driver's HwScsiAdapterState Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiadapterstate_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIADAPTERSTATE_ROUTINE_KG"></span>


In NT-based operating systems, miniport drivers should set this entry point to **NULL** in the [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) (see [Required and Optional SCSI Miniport Driver Routines](required-and-optional-scsi-miniport-driver-routines.md)) only if either of the following conditions hold:

-   The miniport driver drives an HBA to be connected on an I/O bus commonly found only in high-end, RISC-based platforms. That is, an x86-based platform running an x86-only Microsoft Windows system would not have an I/O bus of a type to support the HBA.

-   The miniport driver drives an HBA that could be found in an x86-based platform running an x86-only Windows system, but the HBA has neither a BIOS nor an x86-only real-mode driver.

Otherwise, a miniport driver must have a *HwScsiAdapterState* routine to be portable across NT-based operating systems and x86-only Microsoft Windows systems.

A [**HwScsiAdapterState**](https://msdn.microsoft.com/library/windows/hardware/ff557278) routine is responsible for saving and restoring the state of its HBA, as requested by the x86-only system during transitions between x86 real and protected processor mode.

See [**HwScsiAdapterState**](https://msdn.microsoft.com/library/windows/hardware/ff557278) for more information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiAdapterState%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




