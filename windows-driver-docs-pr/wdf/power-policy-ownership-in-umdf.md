---
title: Power Policy Ownership in UMDF
description: Power Policy Ownership in UMDF
keywords:
- power policy ownership WDK UMDF
- power policy ownership WDK UMDF , overview
- power management WDK UMDF , power policy ownership
ms.date: 04/20/2017
---

# Power Policy Ownership in UMDF


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

For each device, one (and only one) of the device's drivers must be the device's *power policy owner*. The power policy owner determines the appropriate [device power state](../kernel/device-power-states.md) for a device and sends requests to the device's driver stack whenever the device's power state should change.

Framework-based drivers do not contain code that requests changes in a device's power state, because the framework provides that code. By default, whenever the system enters a [system sleeping state](../kernel/system-sleeping-states.md), the framework asks the driver for your device's bus to lower the device power state to D3. (Your driver can change the default behavior so that the framework sets your device's sleep state to D1 or D2, if the device provides wake-up capabilities.) When the system power returns to its [working (S0) state](../kernel/system-working-state-s0.md), the framework requests the bus driver to restore your device to its working (D0) state.

The power policy owner is also responsible for enabling and disabling the following device features:

-   Your device's ability to enter a [low-power (sleeping) state](../kernel/device-sleeping-states.md) when it is idle and the system remains in its working (S0) state

-   Your device's ability to wake itself from a sleeping state when it detects an external event

-   Your device's ability to wake up the entire system from a system sleeping state when it detects an external event

If your device supports these idle power-down and system wake-up capabilities, the power policy owner can also support the framework's [IPowerPolicyCallbackWakeFromS0](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefroms0) and [IPowerPolicyCallbackWakeFromSx](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefromsx) interfaces, which define a set of power policy event callback functions.

By default, UMDF-based drivers are not power policy owners. The device's kernel-mode function driver is the default power policy owner. (If there is no kernel-mode function driver and the bus driver has called [**WdfPdoInitAssignRawDevice**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassignrawdevice), the bus driver is the power policy owner). If you want your UMDF-based driver to be the power policy owner for a driver stack, the driver must call [**IWDFDeviceInitialize::SetPowerPolicyOwnership**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-setpowerpolicyownership), and the kernel-mode default power policy owner must call [**WdfDeviceInitSetPowerPolicyOwnership**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyownership) to disable ownership.

In addition, if you are providing a UMDF-based driver for a USB device, and if you want your driver to be the power policy owner, the driver's INF file must contain an [**INF AddReg directive**](../install/inf-addreg-directive.md) that sets the WinUsbPowerPolicyOwnershipDisabled value in the registry. If this REG\_DWORD-sized value is set to any nonzero number, it disables the [WinUSB](../usbcon/winusb.md) driver's ability to be the device's power policy owner. The AddReg directive must be in an [**INF DDInstall.HW section**](../install/inf-ddinstall-hw-section.md), as the following example shows.

```cpp
[MyDriver_Install.NT.hw]
AddReg=MyDriver_AddReg

[MyDriver_AddReg]
HKR,,"WinUsbPowerPolicyOwnershipDisabled",0x00010001,1
```

The framework does the following work for the power policy owner:

-   It handles all power policy communication between your driver and the rest of the driver stack. For example, your driver does not have to request the bus driver to change the device's power state, because the framework makes the request.

-   If your driver registers power policy event callback functions, the framework calls them when it is time to enable or disable the device's ability to wake itself from a low-power state.

-   If your driver allows users to modify idle and wake settings, the framework provides a user interface in the form of a property sheet page that Device Manager displays.

For more information about the power policy owner's responsibilities, see the following topics:

-   [Supporting Idle Power-Down in UMDF-based Drivers](supporting-idle-power-down-in-umdf-drivers.md)

-   [Supporting System Wake-Up in UMDF-based Drivers](supporting-system-wake-up-in-umdf-drivers.md)

-   [User Control of Device Idle and Wake Behavior in UMDF](user-control-of-device-idle-and-wake-behavior-in-umdf.md)

