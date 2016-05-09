---
title: SCSI Miniport Driver's HwScsiResetBus Routine
description: SCSI Miniport Driver's HwScsiResetBus Routine
ms.assetid: ca4ab3e6-e23c-443a-bcf6-6fd516569999
keywords: ["SCSI miniport drivers WDK storage , HwScsiResetBus", "HwScsiResetBus", "bus-reset operations WDK SCSI"]
---

# SCSI Miniport Driver's HwScsiResetBus Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiresetbus_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIRESETBUS_ROUTINE_KG"></span>


Every miniport driver must have an [*HwScsiResetBus*](https://msdn.microsoft.com/library/windows/hardware/ff557318) routine, which is called with a pointer to the miniport driver's device extension for HBA state and the **PathId** of the bus to be reset. If an attempted bus-reset operation fails or times out, the miniport driver should call [**ScsiPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff564652) and then program the HBA for a hard reset.

A bus-reset operation might require the miniport driver to clean up the state it maintains in the device extension and/or logical unit extensions for devices on the bus. *HwScsiResetBus* must complete any outstanding requests by calling [**ScsiPortCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff564608) with the **SrbStatus** value SRB\_STATUS\_BUS\_RESET or, for individual SRBs, [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with this status value.

After completing the bus-reset request and any outstanding requests, the miniport driver must call **ScsiPortNotification** (if it has not already done so) with the *NotificationType***NextRequest**, or **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

Note that the operating system - specific port driver manages SCSI bus-reset delays on behalf of miniport drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiResetBus%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




