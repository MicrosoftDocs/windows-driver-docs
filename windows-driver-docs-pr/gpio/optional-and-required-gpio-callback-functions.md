---
title: Optional and Required GPIO Callback Functions
description: A general-purpose I/O (GPIO) controller driver calls the GPIO_CLX_RegisterClient method to register as a client of the GPIO framework extension (GpioClx).
ms.assetid: 2F126431-13AB-4E3F-9E5E-56DC7D9AF024
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optional and Required GPIO Callback Functions


A general-purpose I/O (GPIO) controller driver calls the [**GPIO\_CLX\_RegisterClient**](https://msdn.microsoft.com/library/windows/hardware/hh439490) method to register as a client of the GPIO framework extension (GpioClx). During this call, the driver passes a registration packet to GpioClx that specifies a list of event callback functions that are implemented by the driver. GpioClx calls these callback functions to configure the GPIO controller hardware, perform I/O operations, and manage interrupts. GpioClx requires a GPIO controller driver to implement certain callback functions, but support for other callback functions is optional.

The registration packet is a [**GPIO\_CLIENT\_REGISTRATION\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh439479) structure. If the GPIO controller driver implements a particular callback function, it writes the function pointer to that callback function into the corresponding member of this structure. Or, to indicate that a particular callback function is not supported, the driver writes NULL to the corresponding member.

The following callback functions must be included in the registration packet:

[*CLIENT\_PrepareController*](https://msdn.microsoft.com/library/windows/hardware/hh439389)
[*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399)
[*CLIENT\_StartController*](https://msdn.microsoft.com/library/windows/hardware/hh439424)
[*CLIENT\_StopController*](https://msdn.microsoft.com/library/windows/hardware/hh439430)
[*CLIENT\_ReleaseController*](https://msdn.microsoft.com/library/windows/hardware/hh439411)
If any callback function in the preceding list is missing (that is, if the corresponding function pointer in the registration packet is NULL), the **GPIO\_CLX\_RegisterClient** method fails.

A GPIO controller driver is not required to support reading from or writing to GPIO I/O pins, which are pins that are configured as data inputs or data outputs. (A GPIO controller with no I/O pins could still relay interrupt requests from peripheral devices.) However, if the registration packet includes either of the following I/O-related callback functions, the packet must include both of the following callback functions:

[*CLIENT\_ConnectIoPins*](https://msdn.microsoft.com/library/windows/hardware/hh439347)
[*CLIENT\_DisconnectIoPins*](https://msdn.microsoft.com/library/windows/hardware/hh439374)
In addition, if the registration packet includes the two callback functions in the preceding list, the driver must additionally support reading from GPIO I/O pins, writing to GPIO I/O pins, or both. Specifically, the registration packet must include at least one callback function in the following list:

[*CLIENT\_ReadGpioPins*](https://msdn.microsoft.com/library/windows/hardware/hh439404) or [*CLIENT\_ReadGpioPinsUsingMask*](https://msdn.microsoft.com/library/windows/hardware/hh439406)
[*CLIENT\_WriteGpioPins*](https://msdn.microsoft.com/library/windows/hardware/hh439439) or [*CLIENT\_WriteGpioPinsUsingMask*](https://msdn.microsoft.com/library/windows/hardware/hh439445)
A driver that supports reads must implement one of the two *CLIENT\_ReadGpioPins*Xxx callback functions in the preceding list. A driver that supports writes must implement one of the two *CLIENT\_WriteGpioPins*Xxx callback functions in the preceding list.

A driver that implements *CLIENT\_ReadGpioPinsUsingMask*, *CLIENT\_WriteGpioPinsUsingMask*, or both, must set the **FormatIoRequestsAsMasks** flag bit in the device information that is supplied by the [*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399) callback function. A driver that implements *CLIENT\_ReadGpioPins*, *CLIENT\_WriteGpioPins*, or both, must not set this flag bit. For more information, see the description of the **Flags** member in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358).

A GPIO controller driver is not required to support GPIO interrupts. However, if the registration packet includes any of the following interrupt-related callback functions, the packet must include all of the following callback functions:

[*CLIENT\_EnableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439377)
[*CLIENT\_DisableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439371)
[*CLIENT\_MaskInterrupts*](https://msdn.microsoft.com/library/windows/hardware/hh439380)
[*CLIENT\_QueryActiveInterrupts*](https://msdn.microsoft.com/library/windows/hardware/hh439395)
[*CLIENT\_UnmaskInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439435)
A driver that supports the masking of interrupts must implement the *CLIENT\_MaskInterrupts* callback function. A driver that supports the querying of active interrupts must implement the *CLIENT\_QueryActiveInterrupts* callback function.

The [*CLIENT\_ClearActiveInterrupts*](https://msdn.microsoft.com/library/windows/hardware/hh439341) callback function is a special case. If the GPIO controller hardware automatically clears active interrupts when they are read, the *CLIENT\_ClearActiveInterrupts* function is not needed and the corresponding function pointer in the registration packet should be set to NULL. However, if active interrupts are not automatically cleared when they are read, and if the interrupt-related callback functions in the preceding list are supplied in the registration packet, the *CLIENT\_ClearActiveInterrupts* function must be included in the packet. To indicate that the hardware automatically clears the active interrupts when they are read, the driver sets the **ActiveInterruptsAutoClearOnRead** flag bit in the device information that is supplied by the [*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399) callback function. For more information, see the description of the **Flags** member in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358).

If the GPIO controller driver supports GPIO interrupts, the registration packet can, as an option, include the following callback function:

[*CLIENT\_QueryEnabledInterrupts*](https://msdn.microsoft.com/library/windows/hardware/dn265184)
GpioClx supports the *CLIENT\_QueryEnabledInterrupts* function starting with Windows 8.1.

A driver that supports [component-level power management](https://msdn.microsoft.com/library/windows/hardware/hh450935) must implement both of the following callback functions:

[*CLIENT\_RestoreBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439414)
[*CLIENT\_SaveBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439419)
To indicate that the hardware supports component-level power management, the driver sets the **BankIdlePowerMgmtSupported** flag bit in the device information that is supplied by the [*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399) callback function. For more information, see the description of the **Flags** member in [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358).

The [*CLIENT\_PreProcessControllerInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439392), [*CLIENT\_ReconfigureInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh698243), and [*CLIENT\_ControllerSpecificFunction*](https://msdn.microsoft.com/library/windows/hardware/hh698237) callback functions are optional and are supported by GpioClx to address hardware-specific issues in some GPIO controller implementations. Only GPIO controller drivers with special requirements implement these functions.

 

 




