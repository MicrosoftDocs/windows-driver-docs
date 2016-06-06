---
title: Partitioning a GPIO Controller into Banks of Pins
author: windows-driver-content
description: A driver developer can, as an option, partition a general-purpose I/O (GPIO) controller device into two or more banks of GPIO pins.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D9425459-E052-48D8-A4F3-91387AE7059A
---

# Partitioning a GPIO Controller into Banks of Pins


A driver developer can, as an option, partition a general-purpose I/O (GPIO) controller device into two or more banks of GPIO pins. For example, a GPIO controller device that has 64 GPIO pins can be described by the GPIO controller driver as two banks, each of which has 32 GPIO pins. The developer can provide a single driver to manage all of the banks in a GPIO controller device, and this driver typically uses one device object to represent the entire device. However, some or all of the banks in the device can be managed independently of the other banks in the device.

Typically, a GPIO controller driver chooses to partition a GPIO controller into two or more banks for one of the following reasons:

-   The power state of the GPIO pins in a bank can be managed independently of the pins in the other banks.
-   The total number of pins in the GPIO controller is greater than 64.

The maximum bank size that the GPIO framework extension (GpioClx) supports is 64 pins. A GPIO controller device that contains more than 64 pins must be partitioned by the driver into two or more banks, each of which contains no more than 64 pins.

To determine how a GPIO controller is partitioned into banks, GpioClx calls the [*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399) event callback function. This function, which is implemented by the GPIO controller driver, supplies a [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358) structure that describes the attributes and capabilities of the GPIO controller. Two members of this structure, **TotalPins** and **NumberOfPinsPerBank**, specify how the pins in the GPIO controller are partitioned into banks. **TotalPins** specifies the total number of pins in the GPIO controller, and **NumberOfPinsPerBank** specifies the number of pins per bank. If N is the number of banks in the controller, the banks are numbered from 0 to N–1. All except the last bank (that is, bank number N–1) must contain the number of pins specified in the **NumberOfPinsPerBank** member. The last bank can have any number of pins from one to **NumberOfPinsPerBank**.

GpioClx determines the total number of banks in the GPIO controller from the values of the **TotalPins** and **NumberOfPinsPerBank** members. GpioClx uses the following integer formula to calculate the total number of banks:

(**TotalPins** + **NumberOfPinsPerBank** – 1) / **NumberOfPinsPerBank**
In some GPIO controller devices, a bank of pins in a device can be turned on or switched to a low-power state independently of the other banks in the same device. Thus, when a particular bank is idle, this bank can be switched to a low-power state to reduce power consumption. To accommodate such devices, GpioClx supports [component-level power management](https://msdn.microsoft.com/library/windows/hardware/hh450935). GpioClx defines two component-level power states, F0 (fully on) and F1 (low-power or off).

To determine whether a bank of GPIO pins supports component-level power management, GpioClx calls the [*CLIENT\_QuerySetControllerInformation*](https://msdn.microsoft.com/library/windows/hardware/hh698241) event callback function. The *InputBuffer* parameter of this function is a pointer to a [**CLIENT\_CONTROLLER\_QUERY\_SET\_INFORMATION\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh698238) structure. To request power-management information, the caller sets the **RequestType** member of this structure to **QueryBankPowerInformation**.

If a GPIO bank supports component-level power management, GpioClx enables a transition to the F1 power state when the bank is idle. Before the bank enters the F1 state, GpioClx calls the [*CLIENT\_SaveBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439419) event callback function to tell the driver to save the hardware context (chiefly, the register contents) of the bank. Later, after the bank enters the F0 state, GpioClx calls the [*CLIENT\_RestoreBankHardwareContext*](https://msdn.microsoft.com/library/windows/hardware/hh439414) event callback function to tell the driver to restore the previously saved hardware context.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20Partitioning%20a%20GPIO%20Controller%20into%20Banks%20of%20Pins%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


