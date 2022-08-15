---
title: GPIO controller requirements checklist
description: This topic summarizes the hardware, firmware, and software requirements for General Purpose IO (GPIO) controller devices that are exposed to Windows.
ms.date: 08/18/2021
---

# GPIO controller requirements checklist

This topic summarizes the hardware, firmware, and software requirements for General Purpose IO (GPIO) controller devices that are exposed to Windows.

## GPIO controller hardware requirements

- The GPIO controller is integrated into the SoC (not connected by an SPB bus).

    Increases reliability of Emulated ActiveBoth.

- Level-mode interrupts are supported.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

- Both High and Low interrupt polarities are supported.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

- Interrupt polarity can be re-programmed at run time.

    Required for both Emulated ActiveBoth and Debounce Emulation features.

## GPIO controller firmware requirements

- GPIO controller _CRS includes all resources for all pin banks in the controller.

- GPIO controller _CRS resource ordering provides bank-to-system interrupt mapping.

- \_AEI method, and event method(s) (\_Exx, \_Lxx or \_EVT) exist for any GPIO-signaled ACPI events.

- GPIO controller _DSM included if any ActiveBoth interrupts connected to the controller are asserted logic high instead of logic low.

- Implement \_REG methods for each GPIO controller and prevent use of GeneralPurposeIO OpRegions if \_REG indicates that the region handler is not available.

- Debounce timeout is included in the GPIOInt resource descriptor for any interrupt that requires debouncing.

## GPIO controller driver requirements

- Support version 2 of the interface between GpioClx and the GPIO controller driver:

  - Implement the [*CLIENT_QueryEnabledInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_enabled_interrupts) callback function. This greatly assists in diagnosing interrupt storms.

  - If the **BankIdlePowerMgmtSupported** flag is set in the [**CONTROLLER_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_client_controller_basic_information) structure, the GPIO controller driver must implement the [*CLIENT_SaveBankHardwareContext*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_save_bank_hardware_context) and [*CLIENT_RestoreBankHardwareContext*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_restore_bank_hardware_context) callback functions, and these functions must save/restore bank context appropriately, including the masked/unmasked state of the interrupts. Note that interrupts are not guaranteed to be disconnected at the time this function is called, but, if they are still connected, they are guaranteed to be masked.

  - If the **DeviceIdlePowerMgmtSupported** flag is set in the **CONTROLLER_BASIC_INFORMATION** structure, the [*CLIENT_StartController*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_start_controller) and [*CLIENT_StopController*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_stop_controller) callback functions must save/restore context for all banks appropriately, including the masked/unmasked state of the interrupts. Note that interrupts are not guaranteed to be disconnected at the time this function is called, but, if they are still connected, they are guaranteed to be masked.

- Set the **EmulateDebouncing** flag in the **CONTROLLER_BASIC_INFORMATION** structure. This significantly increases noise immunity for devices whose interrupts are subject to electrostatic discharge (such as buttons, plugs, and so on).

- Set the **EmulateActiveBoth** flag in the **CONTROLLER_BASIC_INFORMATION** structure, and implement the [*CLIENT_ReconfigureInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_reconfigure_interrupt) callback function. This ensures reliable edge detection for ActiveBoth interrupts.
