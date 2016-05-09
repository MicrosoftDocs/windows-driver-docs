---
title: SCSI Miniport Driver's HwScsiFindAdapter Routine
author: windows-driver-content
description: SCSI Miniport Driver's HwScsiFindAdapter Routine
ms.assetid: c89ad751-ff29-4aa7-b907-cb490d060906
keywords: ["HwScsiFindAdapter", "SCSI miniport drivers WDK storage , HwScsiFindAdapter"]
---

# SCSI Miniport Driver's HwScsiFindAdapter Routine


## <span id="ddk_scsi_miniport_drivers_hwscsifindadapter_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIFINDADAPTER_ROUTINE_KG"></span>


The operating system-specific port driver fills in as much of the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) in the configuration information buffer as it can from the miniport driver's [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) specification and other sources in the system before calling the given *HwScsiFindAdapter* routine with a pointer to the configuration information buffer.

In general, an *HwScsiFindAdapter* routine is responsible for using the supplied configuration information and/or for calling **ScsiPort***Xxx* to collect sufficient configuration information to determine whether it supports an HBA on the I/O bus identified by the **SystemIoBusNumber** in the PORT\_CONFIGURATION\_INFORMATION supplied by the port driver. If so, *HwScsiFindAdapter* is responsible for filling in any remaining configuration information for the supported HBA in the PORT\_CONFIGURATION\_INFORMATION, for setting up the miniport driver's device extension with driver-determined state about that HBA, and for setting the *Again* parameter to an appropriate value before it returns control.

See [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) and [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) for more information.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiFindAdapter%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


