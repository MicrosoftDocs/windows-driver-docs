---
title: Setting Again and Returning from HwScsiFindAdapter
description: Setting Again and Returning from HwScsiFindAdapter
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
- Again WDK SCSI
- return values WDK SCSI
ms.date: 04/20/2017
---

# Setting Again and Returning from HwScsiFindAdapter


## <span id="ddk_setting_again_and_returning_from_hwscsifindadapter_kg"></span><span id="DDK_SETTING_AGAIN_AND_RETURNING_FROM_HWSCSIFINDADAPTER_KG"></span>


For a supported and successfully configured HBA, [*HwScsiFindAdapter*](/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) returns SP\_RETURN\_FOUND.

Before it returns, the *HwScsiFindAdapter* of both legacy and Plug and Play miniport drivers should set *Again* as described in this section. Although *Again* is irrelevant when a miniport driver is loaded as a Plug and Play driver, *Again* must be set appropriately so the system can run a Plug and Play miniport driver as a legacy driver if necessary.

*HwScsiFindAdapter* should set *Again* to **TRUE** to indicate it should be called again *with exactly the same PORT\_CONFIGURATION\_INFORMATION but a new device extension* if another of its HBAs might be connected on the same I/O bus.

If *HwScsiFindAdapter* cannot find an HBA it supports, it should set *Again* to **FALSE** and return SP\_RETURN\_NOT\_FOUND. If *HwScsiFindAdapter* finds a supported HBA but the input [**PORT\_CONFIGURATION\_INFORMATION**](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information) has inconsistent configuration data (such as an invalid **DmaChannel** or **BusInterruptLevel** on an EISA bus), it should set *Again* to **FALSE** and return SP\_RETURN\_BAD\_CONFIG. For an HBA on a PCI bus, *HwScsiFindAdapter* must accept the interrupt configuration information supplied by the system.

Note that setting *Again* to **FALSE** and returning control with SP\_RETURN\_NOT\_FOUND or SP\_RETURN\_BAD\_CONFIG indicates that a given I/O bus, identified by the **SystemIoBusNumber** in the input PORT\_CONFIGURATION\_INFORMATION, has no HBA that the miniport driver can support. It does not prevent the system port driver from calling *HwScsiFindAdapter* again with updated PORT\_CONFIGURATION\_INFORMATION to scan another I/O bus for HBA(s) if the machine has additional I/O buses of the same **AdapterInterfaceType**.

 

