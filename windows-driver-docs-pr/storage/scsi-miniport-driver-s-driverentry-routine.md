---
title: SCSI Miniport Driver's DriverEntry Routine
description: SCSI Miniport Driver's DriverEntry Routine
ms.assetid: b143bb19-2c9e-4e43-841f-a3c47c7f1a1b
keywords: ["DriverEntry WDK storage"]
---

# SCSI Miniport Driver's DriverEntry Routine


## <span id="ddk_scsi_miniport_drivers_driverentry_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_DRIVERENTRY_ROUTINE_KG"></span>


A [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine is the initial entry point for most Microsoft Windows NT kernel-mode drivers and for every SCSI miniport driver. A miniport driver's **DriverEntry** routine is called with two input arguments of type PVOID and must do the following:

1.  Initialize a [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) structure on the stack with zeros.

2.  Set the **HwInitializationDataSize** member to **sizeof**(HW\_INITIALIZATION\_DATA).

3.  Set driver-specific and HBA-specific values in the HW\_INITIALIZATION\_DATA members, including the miniport driver's entry points. The following entry points must be set:

    -   [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300)
    -   [*HwScsiInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff557302)
    -   [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323)
    -   [*HwScsiResetBus*](https://msdn.microsoft.com/library/windows/hardware/ff557318)

    The following entry points can be set to a driver-supplied routine or must be set to **NULL**:

    -   [**HwScsiInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557312) (**NULL** if the miniport driver uses polling exclusively)
    -   [**HwScsiDmaStarted**](https://msdn.microsoft.com/library/windows/hardware/ff557291) (**NULL** if the HBA uses PIO or is a bus master)
    -   [**HwScsiAdapterState**](https://msdn.microsoft.com/library/windows/hardware/ff557278) (**NULL** if the miniport driver runs only on NT-based operating system platforms or if it is designed to also run on x86-only Windows platforms but the HBA has neither a BIOS nor x86-real-mode driver)
    -   [**HwScsiAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557274) (**NULL** if the miniport driver does not support Plug and Play)

4.  In an a legacy miniport driver, set up any driver-determined context data that the miniport driver's *HwScsiFindAdapter* routine will use.

5.  Call [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) with the pointers that were input to the **DriverEntry** routine, the address of the filled-in HW\_INITIALIZATION\_DATA, and the address of the context data, if any.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20DriverEntry%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




