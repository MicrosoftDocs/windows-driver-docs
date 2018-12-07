---
title: Setting up ConfigInfo in HwScsiFindAdapter
description: Setting up ConfigInfo in HwScsiFindAdapter
ms.assetid: f9c5d23d-feab-4cc4-9cd9-29c21d4fdf0b
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
- ConfigInfo
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting up ConfigInfo in HwScsiFindAdapter


## <span id="ddk_setting_up_configinfo_in_hwscsifindadapter_kg"></span><span id="DDK_SETTING_UP_CONFIGINFO_IN_HWSCSIFINDADAPTER_KG"></span>


An [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine can call [**ScsiPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff564624) and examine the returned bus-type-specific configuration information, such as POS data or EISA configuration data, for a supported HBA.

If the **AccessRanges** elements in the input PORT\_CONFIGURATION\_INFORMATION (the *ConfigInfo* buffer) have been filled in by the port driver, the *HwScsiFindAdapter* routine should map the bus-relative access ranges with [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) and use the returned logical access range addresses to communicate with the HBA. If access range addresses are supplied by the port driver, *HwScsiFindAdapter* must not scan for HBAs at other locations on that I/O bus.

In addition, if the port driver supplies access range values, *HwScsiFindAdapter* must not use the *HwContext* parameter. Such access range values are usually accompanied by additional configuration information, which indicates a Plug and Play environment. In such an environment, *HwScsiFindAdapter* is being called after the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine has returned and thus the *HwContext* pointer is no longer valid. Only drivers that receive zero access range values from the port driver and that do their own scanning for supported HBAs can safely use the *HwContext* pointer.

If the input [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) contains no configuration information other than that previously supplied by the miniport driver in the [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456), *HwScsiFindAdapter* can use values returned by [**ScsiPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff564624) or, if necessary, set miniport driver-defined default values for **AccessRanges** elements, **BusInterruptLevel** or **BusInterruptVector**, **DmaChannel** or **DmaPort** if the HBA uses system DMA, and **InitiatorBusId**.

*HwScsiFindAdapter* must call [**ScsiPortValidateRange**](https://msdn.microsoft.com/library/windows/hardware/ff564761) to check whether such miniport driver-supplied access ranges can be used safely *before* it accesses an HBA on the bus. If **ScsiPortValidateRange** returns **TRUE**, the miniport driver can call [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) to map the range and use the returned logical addresses in calls to **ScsiPortRead***Xxx* and/or **ScsiPortWrite***Xxx* to determine whether it supports an HBA on the I/O bus. If **ScsiPortValidateRange** returns **FALSE**, the miniport driver must not attempt to map and use those bus-relative access range values.

Similarly, if the port driver calls a Plug and Play miniport driver to detect devices on a nonenumerable bus, the miniport driver must validate access ranges before calling **ScsiPortGetDeviceBase**.

If the port driver provides interrupt configuration information, the miniport driver must accept it and, if its HBA supports programmable interrupt configuration, should program its HBA to use the supplied interrupt value. If no interrupt configuration is supplied, as indicated either by the value zero or the value SP\_UNINITIALIZED\_VALUE, the miniport driver should either query its HBA if the HBA supports interrupt selection using jumpers or it should supply a nonzero default interrupt configuration, unless the HBA does not use interrupts. The interrupt configuration value zero indicates that the miniport driver controls its HBA in a polled mode.

When *HwScsiFindAdapter* finds an HBA it can support, this routine must fill in pertinent members, as appropriate for its HBA and the given **AdapterInterfaceType**, in the PORT\_CONFIGURATION\_INFORMATION. A miniport driver that supplies access ranges must fill in the **AccessRanges** information, converting each **AccessRanges** element's bus-relative **RangeStart** value with [**ScsiPortConvertUlongToPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564613) before setting the bus-relative base address for a range in the PORT\_CONFIGURATION\_INFORMATION.

For a supported HBA, *HwScsiFindAdapter* also should save the mapped logical range addresses returned by **ScsiPortGetDeviceBase** in the miniport driver's device extension. Every miniport driver must call the **ScsiPortRead***Xxx* and **ScsiPortWrite***Xxx* with these mapped system addresses to communicate with its HBA(s).

For each successfully validated and mapped range in I/O space, the miniport driver calls the **ScsiPortRead/WritePort***Xxx* routines to communicate with its HBA. For each such range in memory space, the miniport driver calls the **ScsiPortRead/WriteRegister***Xxx*.

For an "AT-compatible" HBA, *HwScsiFindAdapter* should check the input **Atdisk..Claimed** members and attempt to claim an "AT" range by resetting the value to **TRUE**.

 

 




