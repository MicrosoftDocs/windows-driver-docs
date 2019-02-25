---
title: Port-Driver-Supplied ConfigInfo for HwScsiFindAdapter
description: Port-Driver-Supplied ConfigInfo for HwScsiFindAdapter
ms.assetid: 9691f47d-1ea8-4ef6-8e0d-57570ff70a16
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
- ConfigInfo
- port-driver-supplied ConfigInfo WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Port-Driver-Supplied ConfigInfo for HwScsiFindAdapter


## <span id="ddk_port_driver_supplied_configinfo_for_hwscsifindadapter_kg"></span><span id="DDK_PORT_DRIVER_SUPPLIED_CONFIGINFO_FOR_HWSCSIFINDADAPTER_KG"></span>


The system port driver always sets up the following [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) before it calls a miniport driver's *HwScsiFindAdapter* routine with a pointer to the PORT\_CONFIGURATION\_INFORMATION (the *ConfigInfo* buffer):

-   **Length** to **sizeof**(PORT\_CONFIGURATION\_INFORMATION)

-   **AdapterInterfaceType** to the miniport driver's [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) specification

-   **InterruptMode** to **LevelSensitive** for a PCI bus or **Latched** for all other bus types

    If the miniport driver has no *HwScsiInterrupt* routine and, therefore, sets the **HwInterrupt** entry point to **NULL** in the HW\_INITIALIZATION\_DATA, this member is irrelevant.

-   **AtdiskPrimaryClaimed** to **TRUE** if a previously loaded driver is using the I/O port range 0x1F0 to 0x1FF

-   **AtdiskSecondaryClaimed** to **TRUE** if a previously loaded driver is using the I/O port range 0x170 to 0x17F

-   **NumberOfAccessRanges** to the miniport driver's HW\_INITIALIZATION\_DATA specification

-   **Dma64BitAddresses** to the miniport driver's HW\_INITIALIZATION\_DATA specification if the system has memory with physical addresses above 4 GB

The port driver also attempts to fill in the following members with values from other sources in the system, such as the registry for a legacy miniport driver or from the Plug and Play manager for a Plug and Play miniport driver:

-   **SystemIoBusNumber** set to the system-assigned value for the I/O bus

    The miniport driver's [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine can be called for each bus of the given **AdapterInterfaceType** with an updated value for **SystemIoBusNumber**, or this can be set to a system-determined value if the system detects an HBA on a particular bus of the given **AdapterInterfaceType**.

-   **AccessRanges** elements of type ACCESS\_RANGE, set with the bus-relative **RangeStart** address and **RangeLength**, as well as whether each range is a **RangeInMemory**

    **RangeInMemory** set to **FALSE** indicates a range of ports in I/O space, rather than a memory-space range.

    The port driver either supplies all the information in an ACCESS\_RANGE element or it sets all members of the element to (default) zero. Usually, the port driver supplies additional configuration information if it provides nonzero values for an access range.

    A miniport driver must map any bus-relative access range values supplied by the port driver with [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) and use the mapped logical address values to determine whether the corresponding HBA is one that the driver supports. *Never* map and use a miniport driver-supplied range to access an HBA on the bus if the port driver supplies filled-in access range elements in the PORT\_CONFIGURATION\_INFORMATION it passes to the *HwScsiFindAdapter* routine. Using miniport driver-supplied addresses when the port driver has supplied range configuration information can reset an already configured HBA, making it dysfunctional, or even cause the system to fail the boot process.

    For more information about using mapped logical access ranges, see [Setting up ConfigInfo in HwScsiFindAdapter](setting-up-configinfo-in-hwscsifindadapter.md).

-   **BusInterruptLevel** or **BusInterruptVector**

    This member is irrelevant if the miniport driver has no [**HwScsiInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557312) routine.

-   **DmaChannel** or **DmaPort** if the HBA uses a system DMA controller

    If the HBA is a bus master or uses PIO, these members are irrelevant.

-   **InitiatorBusId**

    If the input **InitiatorBusId\[0\]** has the value zero, the miniport driver can assign a default value if its HBA does not require the use of particular value(s) determined by querying the HBA. Otherwise, the miniport driver should use any nonzero value assigned by the port driver if possible. Every miniport driver must update **InitiatorBusId** specifications to match what its HBA uses, if necessary querying the HBA to determine the appropriate values(s).

    A miniport driver must set an entry for each SCSI bus supported by the HBA, as indicated by the value of **NumberOfBuses**.

 

 




