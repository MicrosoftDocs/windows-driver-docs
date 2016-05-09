---
title: SCSI Miniport Driver's HwScsiAdapterControl Routine
author: windows-driver-content
description: SCSI Miniport Driver's HwScsiAdapterControl Routine
ms.assetid: ccc5aa02-415d-40d1-a1ed-c7d4d881f4ca
keywords: ["SCSI miniport drivers WDK storage , HwScsiAdapterControl", "HwScsiAdapterControl"]
---

# SCSI Miniport Driver's HwScsiAdapterControl Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiadaptercontrol_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIADAPTERCONTROL_ROUTINE_KG"></span>


In NT-based operating systems, miniport drivers should set this entry point to **NULL** in the [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) (see [Required and Optional SCSI Miniport Driver Routines](required-and-optional-scsi-miniport-driver-routines.md)) if the miniport driver does not support Plug and Play. Otherwise, the miniport driver must have a [**HwScsiAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557274)routine to support PnP and power management operations for its HBA.

A miniport driver's *HwScsiAdapterControl* routine is first called by the port driver with **ScsiQuerySupportedControlTypes** after the HBA has been initialized but before the first I/O, to determine the other operations supported by the miniport driver. The miniport driver sets the operations it supports in a SUPPORTED\_CONTROL\_TYPE\_LIST allocated by the port driver. After *HwScsiAdapterControl* returns from this initial call, the port driver calls the routine again only for the operations indicated by the miniport driver.

A miniport driver's *HwScsiAdapterControl* routine can support any or all of the following operations:

-   **ScsiStopAdapter** to shut down the HBA when it has been powered off, removed from the system, or otherwise reconfigured or disabled.

    At the time the SCSI port driver calls *HwScsiAdapterControl* to stop the HBA, it ensures that there are no uncompleted requests. The miniport driver should disable interrupts on the HBA, halt all processing including background processing not subject to interrupts, and put the HBA into an uninitialized state. The miniport driver should not release its resources; if necessary, the port driver will release resources on behalf of the miniport driver. This call to *HwScsiAdapterControl* is preceded by an SRB\_FUNCTION\_FLUSH request, so it is not necessary to flush the cache unless its data has changed since the flush request was completed.

    The miniport driver is not called again for this HBA until either the PnP manager requests that the HBA be restarted, or an HBA that was shut down for power management is powered up.

    Note that *HwScsiAdapterControl*, like any miniport driver routine, might be called to stop the HBA after the HBA has already been removed from the system.

-   **ScsiSetBootConfig** to restore any settings on an HBA that the BIOS might need to boot the system.

    A miniport driver should support **ScsiSetBootConfig** if it needs to call [**ScsiPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff564624) or [**ScsiPortSetBusDataByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff564751) to restore such settings. The port driver calls a miniport driver's *HwScsiAdapterControl* with **ScsiSetBootConfig** after calling the routine to stop the HBA.

-   **ScsiSetRunningConfig** to restore any settings on an HBA that the miniport driver might need to control the HBA while the system is running.

    A miniport driver should support **ScsiSetRunningConfig** if it needs to call **ScsiPortGetBusData** or [**ScsiPortSetBusDataByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff564751) to restore such settings. The port driver calls a miniport driver's *HwScsiAdapterControl* with **ScsiSetRunningConfig** before calling the routine to restart the HBA.

-   **ScsiRestartAdapter** to restart an HBA that has been shut down for power management.

    At the time the port driver calls *HwScsiAdapterControl* to restart the HBA, all resources previously assigned to the miniport driver are still available and its device extension and any logical unit extensions are intact. When restarting its HBA, the miniport driver must not call routines that can only be called from *HwScsiFindAdapter*.

    If the miniport driver does not support **ScsiRestartAdapter**, the port driver calls the miniport driver's *HwScsiFindAdapter* and *HwScsiInitialize* routines to restart the HBA. However, such routines might do detection work that is unnecessary when restarting, so such a miniport driver will not power up its HBA as quickly as a miniport driver that supports **ScsiRestartAdapter**.

See [**HwScsiAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557274) for more information.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiAdapterControl%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


