---
title: Setting Again and Returning from HwScsiFindAdapter
description: Setting Again and Returning from HwScsiFindAdapter
ms.assetid: 8a9cde40-06fa-4b56-818d-63a9c71da208
keywords: ["HwScsiFindAdapter", "SCSI miniport drivers WDK storage , HwScsiFindAdapter", "Again WDK SCSI", "return values WDK SCSI"]
---

# Setting Again and Returning from HwScsiFindAdapter


## <span id="ddk_setting_again_and_returning_from_hwscsifindadapter_kg"></span><span id="DDK_SETTING_AGAIN_AND_RETURNING_FROM_HWSCSIFINDADAPTER_KG"></span>


For a supported and successfully configured HBA, [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) returns SP\_RETURN\_FOUND.

Before it returns, the *HwScsiFindAdapter* of both legacy and Plug and Play miniport drivers should set *Again* as described in this section. Although *Again* is irrelevant when a miniport driver is loaded as a Plug and Play driver, *Again* must be set appropriately so the system can run a Plug and Play miniport driver as a legacy driver if necessary.

*HwScsiFindAdapter* should set *Again* to **TRUE** to indicate it should be called again *with exactly the same PORT\_CONFIGURATION\_INFORMATION but a new device extension* if another of its HBAs might be connected on the same I/O bus.

If *HwScsiFindAdapter* cannot find an HBA it supports, it should set *Again* to **FALSE** and return SP\_RETURN\_NOT\_FOUND. If *HwScsiFindAdapter* finds a supported HBA but the input [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) has inconsistent configuration data (such as an invalid **DmaChannel** or **BusInterruptLevel** on an EISA bus), it should set *Again* to **FALSE** and return SP\_RETURN\_BAD\_CONFIG. For an HBA on a PCI bus, *HwScsiFindAdapter* must accept the interrupt configuration information supplied by the system.

Note that setting *Again* to **FALSE** and returning control with SP\_RETURN\_NOT\_FOUND or SP\_RETURN\_BAD\_CONFIG indicates that a given I/O bus, identified by the **SystemIoBusNumber** in the input PORT\_CONFIGURATION\_INFORMATION, has no HBA that the miniport driver can support. It does not prevent the system port driver from calling *HwScsiFindAdapter* again with updated PORT\_CONFIGURATION\_INFORMATION to scan another I/O bus for HBA(s) if the machine has additional I/O buses of the same **AdapterInterfaceType**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Setting%20Again%20and%20Returning%20from%20HwScsiFindAdapter%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




