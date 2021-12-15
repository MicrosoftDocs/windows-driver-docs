---
title: Optional and Required GPIO Callback Functions
description: A general-purpose I/O (GPIO) controller driver calls the GPIO_CLX_RegisterClient method to register as a client of the GPIO framework extension (GpioClx).
ms.date: 04/20/2017
---

# Optional and Required GPIO Callback Functions


A general-purpose I/O (GPIO) controller driver calls the [**GPIO\_CLX\_RegisterClient**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_registerclient) method to register as a client of the GPIO framework extension (GpioClx). During this call, the driver passes a registration packet to GpioClx that specifies a list of event callback functions that are implemented by the driver. GpioClx calls these callback functions to configure the GPIO controller hardware, perform I/O operations, and manage interrupts. GpioClx requires a GPIO controller driver to implement certain callback functions, but support for other callback functions is optional.

The registration packet is a [**GPIO\_CLIENT\_REGISTRATION\_PACKET**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_gpio_client_registration_packet) structure. If the GPIO controller driver implements a particular callback function, it writes the function pointer to that callback function into the corresponding member of this structure. Or, to indicate that a particular callback function is not supported, the driver writes NULL to the corresponding member.

The following callback functions must be included in the registration packet:

[*CLIENT\_PrepareController*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_prepare_controller)
[*CLIENT\_QueryControllerBasicInformation*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information)
[*CLIENT\_StartController*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_start_controller)
[*CLIENT\_StopController*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_stop_controller)
[*CLIENT\_ReleaseController*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_release_controller)
If any callback function in the preceding list is missing (that is, if the corresponding function pointer in the registration packet is NULL), the **GPIO\_CLX\_RegisterClient** method fails.

A GPIO controller driver is not required to support reading from or writing to GPIO I/O pins, which are pins that are configured as data inputs or data outputs. (A GPIO controller with no I/O pins could still relay interrupt requests from peripheral devices.) However, if the registration packet includes either of the following I/O-related callback functions, the packet must include both of the following callback functions:

[*CLIENT\_ConnectIoPins*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_connect_io_pins)
[*CLIENT\_DisconnectIoPins*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disconnect_io_pins)
In addition, if the registration packet includes the two callback functions in the preceding list, the driver must additionally support reading from GPIO I/O pins, writing to GPIO I/O pins, or both. Specifically, the registration packet must include at least one callback function in the following list:

[*CLIENT\_ReadGpioPins*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins) or [*CLIENT\_ReadGpioPinsUsingMask*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins_mask)
[*CLIENT\_WriteGpioPins*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins) or [*CLIENT\_WriteGpioPinsUsingMask*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins_mask)
A driver that supports reads must implement one of the two *CLIENT\_ReadGpioPins*Xxx callback functions in the preceding list. A driver that supports writes must implement one of the two *CLIENT\_WriteGpioPins*Xxx callback functions in the preceding list.

A driver that implements *CLIENT\_ReadGpioPinsUsingMask*, *CLIENT\_WriteGpioPinsUsingMask*, or both, must set the **FormatIoRequestsAsMasks** flag bit in the device information that is supplied by the [*CLIENT\_QueryControllerBasicInformation*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information) callback function. A driver that implements *CLIENT\_ReadGpioPins*, *CLIENT\_WriteGpioPins*, or both, must not set this flag bit. For more information, see the description of the **Flags** member in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_client_controller_basic_information).

A GPIO controller driver is not required to support GPIO interrupts. However, if the registration packet includes any of the following interrupt-related callback functions, the packet must include all of the following callback functions:

[*CLIENT\_EnableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_enable_interrupt)
[*CLIENT\_DisableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disable_interrupt)
[*CLIENT\_MaskInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_mask_interrupts)
[*CLIENT\_QueryActiveInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_active_interrupts)
[*CLIENT\_UnmaskInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_unmask_interrupt)
A driver that supports the masking of interrupts must implement the *CLIENT\_MaskInterrupts* callback function. A driver that supports the querying of active interrupts must implement the *CLIENT\_QueryActiveInterrupts* callback function.

The [*CLIENT\_ClearActiveInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_clear_active_interrupts) callback function is a special case. If the GPIO controller hardware automatically clears active interrupts when they are read, the *CLIENT\_ClearActiveInterrupts* function is not needed and the corresponding function pointer in the registration packet should be set to NULL. However, if active interrupts are not automatically cleared when they are read, and if the interrupt-related callback functions in the preceding list are supplied in the registration packet, the *CLIENT\_ClearActiveInterrupts* function must be included in the packet. To indicate that the hardware automatically clears the active interrupts when they are read, the driver sets the **ActiveInterruptsAutoClearOnRead** flag bit in the device information that is supplied by the [*CLIENT\_QueryControllerBasicInformation*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information) callback function. For more information, see the description of the **Flags** member in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_client_controller_basic_information).

If the GPIO controller driver supports GPIO interrupts, the registration packet can, as an option, include the following callback function:

[*CLIENT\_QueryEnabledInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_enabled_interrupts)
GpioClx supports the *CLIENT\_QueryEnabledInterrupts* function starting with Windows 8.1.

A driver that supports [component-level power management](../kernel/component-level-power-management.md) must implement both of the following callback functions:

[*CLIENT\_RestoreBankHardwareContext*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_restore_bank_hardware_context)
[*CLIENT\_SaveBankHardwareContext*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_save_bank_hardware_context)
To indicate that the hardware supports component-level power management, the driver sets the **BankIdlePowerMgmtSupported** flag bit in the device information that is supplied by the [*CLIENT\_QueryControllerBasicInformation*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information) callback function. For more information, see the description of the **Flags** member in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_client_controller_basic_information).

The [*CLIENT\_PreProcessControllerInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_pre_process_controller_interrupt), [*CLIENT\_ReconfigureInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_reconfigure_interrupt), and [*CLIENT\_ControllerSpecificFunction*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_controller_specific_function) callback functions are optional and are supported by GpioClx to address hardware-specific issues in some GPIO controller implementations. Only GPIO controller drivers with special requirements implement these functions.

 

