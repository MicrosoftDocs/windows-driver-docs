---
title: GPIO controller requirements checklist
description: This topic summarizes the hardware, firmware, and software requirements for General Purpose IO (GPIO) controller devices that are exposed to Windows.
ms.assetid: 8097F391-ABF0-44A6-94D2-243AFBA3F984
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPIO controller requirements checklist


This topic summarizes the hardware, firmware, and software requirements for General Purpose IO (GPIO) controller devices that are exposed to Windows.

## GPIO controller hardware requirements


-   The GPIO controller is integrated into the SoC (not connected by an SPB bus).

    Increases reliability of Emulated ActiveBoth.

-   Level-mode interrupts are supported.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

-   Both High and Low interrupt polarities are supported.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

-   Interrupt polarity can be re-programmed at run time.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

## GPIO controller firmware requirements


-   GPIO controller \_CRS includes all resources for all pin banks in the controller.
-   GPIO controller \_CRS resource ordering provides bank-to-system interrupt mapping.
-   \_AEI method, and event method(s) (\_Exx, \_Lxx or \_EVT) exist for any GPIO-signaled ACPI events.
-   GPIO controller \_DSM included if any ActiveBoth interrupts connected to the controller are asserted logic high instead of logic low.
-   Implement \_REG methods for each GPIO controller and prevent use of GeneralPurposeIO OpRegions if \_REG indicates that the region handler is not available.
-   Debounce timeout is included in the GPIOInt resource descriptor for any interrupt that requires debouncing.

## GPIO controller driver requirements


-   Support version 2 of the interface between GpioClx and the GPIO controller driver:

    -   Implement the [*CLIENT\_QueryEnabledInterrupts*](https://msdn.microsoft.com/library/windows/hardware/dn265184) callback function. This greatly assists in diagnosing interrupt storms.
    -   If the **BankIdlePowerMgmtSupported** flag is set in the [**CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358) structure, the GPIO controller driver must implement the [*CLIENT\_SaveBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439419) and [*CLIENT\_RestoreBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439414) callback functions, and these functions must save/restore bank context appropriately, including the masked/unmasked state of the interrupts. Note that interrupts are not guaranteed to be disconnected at the time this function is called, but, if they are still connected, they are guaranteed to be masked.
    -   If the **DeviceIdlePowerMgmtSupported** flag is set in the **CONTROLLER\_BASIC\_INFORMATION** structure, the [*CLIENT\_StartController*](https://msdn.microsoft.com/library/windows/hardware/hh439424) and [*CLIENT\_StopController*](https://msdn.microsoft.com/library/windows/hardware/hh439430) callback functions must save/restore context for all banks appropriately, including the masked/unmasked state of the interrupts. Note that interrupts are not guaranteed to be disconnected at the time this function is called, but, if they are still connected, they are guaranteed to be masked.
-   Set the **EmulateDebouncing** flag in the **CONTROLLER\_BASIC\_INFORMATION** structure. This significantly increases noise immunity for devices whose interrupts are subject to electrostatic discharge (such as buttons, plugs, and so on).
-   Set the **EmulateActiveBoth** flag in the **CONTROLLER\_BASIC\_INFORMATION** structure, and implement the [*CLIENT\_ReconfigureInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh698243) callback function. This ensures reliable edge detection for ActiveBoth interrupts.

 

 




