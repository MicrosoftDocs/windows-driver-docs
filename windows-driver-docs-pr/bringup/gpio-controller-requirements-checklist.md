---
title: GPIO controller requirements checklist
description: This topic summarizes the hardware, firmware, and software requirements for General Purpose IO (GPIO) controller devices that are exposed to Windows.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8097F391-ABF0-44A6-94D2-243AFBA3F984
---

# GPIO controller requirements checklist


This topic summarizes the hardware, firmware, and software requirements for General Purpose IO (GPIO) controller devices that are exposed to Windows.

## <a href="" id="hw"></a>GPIO controller hardware requirements


-   The GPIO controller is integrated into the SoC (not connected by an SPB bus).

    Increases reliability of Emulated ActiveBoth.

-   Level-mode interrupts are supported.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

-   Both High and Low interrupt polarities are supported.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

-   Interrupt polarity can be re-programmed at run time.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

## <a href="" id="fw"></a>GPIO controller firmware requirements


-   GPIO controller \_CRS includes all resources for all pin banks in the controller.
-   GPIO controller \_CRS resource ordering provides bank-to-system interrupt mapping.
-   \_AEI method, and event method(s) (\_Exx, \_Lxx or \_EVT) exist for any GPIO-signaled ACPI events.
-   GPIO controller \_DSM included if any ActiveBoth interrupts connected to the controller are asserted logic high instead of logic low.
-   Implement \_REG methods for each GPIO controller and prevent use of GeneralPurposeIO OpRegions if \_REG indicates that the region handler is not available.
-   Debounce timeout is included in the GPIOInt resource descriptor for any interrupt that requires debouncing.

## <a href="" id="driver"></a>GPIO controller driver requirements


-   Support version 2 of the interface between GpioClx and the GPIO controller driver:

    -   Implement the [*CLIENT\_QueryEnabledInterrupts*](https://msdn.microsoft.com/library/windows/hardware/dn265184) callback function. This greatly assists in diagnosing interrupt storms.
    -   If the **BankIdlePowerMgmtSupported** flag is set in the [**CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358) structure, the GPIO controller driver must implement the [*CLIENT\_SaveBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439419) and [*CLIENT\_RestoreBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439414) callback functions, and these functions must save/restore bank context appropriately, including the masked/unmasked state of the interrupts. Note that interrupts are not guaranteed to be disconnected at the time this function is called, but, if they are still connected, they are guaranteed to be masked.
    -   If the **DeviceIdlePowerMgmtSupported** flag is set in the **CONTROLLER\_BASIC\_INFORMATION** structure, the [*CLIENT\_StartController*](https://msdn.microsoft.com/library/windows/hardware/hh439424) and [*CLIENT\_StopController*](https://msdn.microsoft.com/library/windows/hardware/hh439430) callback functions must save/restore context for all banks appropriately, including the masked/unmasked state of the interrupts. Note that interrupts are not guaranteed to be disconnected at the time this function is called, but, if they are still connected, they are guaranteed to be masked.
-   Set the **EmulateDebouncing** flag in the **CONTROLLER\_BASIC\_INFORMATION** structure. This significantly increases noise immunity for devices whose interrupts are subject to electrostatic discharge (such as buttons, plugs, and so on).
-   Set the **EmulateActiveBoth** flag in the **CONTROLLER\_BASIC\_INFORMATION** structure, and implement the [*CLIENT\_ReconfigureInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh698243) callback function. This ensures reliable edge detection for ActiveBoth interrupts.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20GPIO%20controller%20requirements%20checklist%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




