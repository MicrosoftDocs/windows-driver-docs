---
title: SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine
description: SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine
ms.assetid: d6c668cc-cb8d-42f4-a6e0-74bbd8b1b27a
keywords: ["SCSI miniport drivers WDK storage , HwScsiDisableInterruptsCallback", "HwScsiDisableInterruptsCallback", "interrupts WDK SCSI"]
---

# SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine


## <span id="ddk_scsi_miniport_drivers_hwscsidisableinterruptscallback_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIDISABLEINTERRUPTSCALLBACK_ROUTINE_KG"></span>


An [**HwScsiDisableInterruptsCallback**](https://msdn.microsoft.com/library/windows/hardware/ff557288) routine should do the following:

-   Reenable interrupts from the HBA

-   Return control

Note that this routine must execute as quickly as possible to avoid using I/O operations for other devices in the machine. Consequently, an *HwScsiDisableInterruptsCallback* must do no more than reenable interrupts on the HBA before it returns control.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiDisableInterruptsCallback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




