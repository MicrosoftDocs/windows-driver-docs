---
title: Calling ScsiPortInitialize
description: Calling ScsiPortInitialize
ms.assetid: a736f279-9ade-4043-90f7-209fca260a39
keywords:
- ScsiPortInitialize
- initializing SCSI miniport drivers
- SCSI miniport drivers WDK storage , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling ScsiPortInitialize


## <span id="ddk_calling_scsiportinitialize_kg"></span><span id="DDK_CALLING_SCSIPORTINITIALIZE_KG"></span>


If a miniport driver's HBA can be connected on more than one type of I/O bus, the miniport driver must call [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) for each bus type and can have a different *HwScsiFindAdapter* routine for each bus type.

After each call to **ScsiPortInitialize**, such a miniport driver must:

-   Modify the AdapterInterfaceType member.

-   Modify the HwScsiFindAdapter member in [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) if the miniport driver has a different HwScsiFindAdapter routine for that bus type.

-   Modify the miniport driver-supplied context data for the new bus type.

-   Call ScsiPortInitialize for each type of bus on which a supported HBA might be connected.

If the miniport driver is a legacy driver that does not support Plug and Play, **ScsiPortInitialize** calls the miniport driver's *HwScsiFindAdapter* routine one or more times before it returns control to the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine. All of the [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) calls are made in the context of the miniport driver's **DriverEntry** routine, in the order **DriverEntry** called **ScsiPortInitialize**.

If the miniport driver supports Plug and Play, **ScsiPortInitialize** stores the initialization data for future use and returns STATUS\_SUCCESS to the miniport driver's **DriverEntry** routine. The port driver does not call the miniport driver's *HwScsiFindAdapter* routine until the Plug and Play manager detects an HBA for which the miniport driver is registered as a service.

For both Plug and Play and legacy miniport drivers, the port driver does all of the following before it calls the miniport driver's *HwScsiFindAdapter* routine:

-   Checks the validity of the HW\_INITIALIZATION\_DATA.

-   Collects and stores pertinent information in the device extension of a device object that it creates to represent the HBA.

-   Allocates memory for and initializes with zeros a device extension of the requested size in which the miniport driver can store driver-determined information about the HBA.

-   Allocates memory for a configuration information buffer that is **sizeof**([**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900)).

-   In the configuration information buffer, fills in a PORT\_CONFIGURATION\_INFORMATION structure with as much configuration information about an HBA on a particular I/O bus as possible, from the miniport driver-supplied HW\_INITIALIZATION\_DATA and from other sources, such as the registry for a legacy miniport driver or from the Plug and Play manager for a Plug and Play miniport driver.

For more information about the miniport driver's *HwScsiFindAdapter* routine, see [SCSI Miniport Driver's HwScsiFindAdapter Routine](scsi-miniport-driver-s-hwscsifindadapter-routine.md).

If the miniport driver's **DriverEntry** routine sets a particular **AdapterInterfaceType** value in the HW\_INITIALIZATION\_DATA but there is no bus of that type in the machine, the port driver returns an operating system-specific status value indicating that such an HBA does not exist in the current machine. It does not call the driver-supplied *HwScsiFindAdapter* routine for that bus type.

A miniport driver does not remain loaded if the machine has no I/O buses of the type(s) specified by the miniport driver's **DriverEntry** routine.

For a legacy miniport driver, note that **ScsiPortInitialize** also is responsible for the following before it returns control to the legacy miniport driver's **DriverEntry** routine:

-   Setting up all necessary system objects.

-   Getting configuration information from and setting configuration information in the registry.

-   Allocating system resources on behalf of the miniport driver, including memory in the amounts indicated by the miniport driver-specified **DeviceExtensionSize**, **SpecificLuExtensionSize**, and/or **SrbExtensionSize** in which the miniport driver can maintain HBA-specific state, per-logical-unit state, and/or per-request state, respectively.

For a Plug and Play miniport driver, the port driver performs these operations after the miniport driver's *HwScsiFindAdapter* routine returns and before the port driver calls the miniport driver's [*HwScsiInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff557302) routine.

Each SCSI miniport driver defines the internal structure and contents of its device extension, logical unit extensions (if any), and SRB extensions (if any). A pointer to the HBA-specific device extension is an input argument to every system-defined miniport driver routine except **DriverEntry**. Many **ScsiPort***Xxx* routines require this pointer as an argument.

**ScsiPortInitialize** can be called only from a miniport driver's **DriverEntry** routine. For more information, see [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) and [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645).

 

 




