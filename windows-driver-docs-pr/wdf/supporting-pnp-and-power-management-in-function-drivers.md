---
title: Supporting PnP and Power Management in Function Drivers
description: Supporting PnP and Power Management in Function Drivers
ms.assetid: 487d4a69-a8a8-406c-8572-688388deabe3
keywords:
- PnP WDK KMDF , function drivers
- Plug and Play WDK KMDF , function drivers
- power management WDK KMDF , function drivers
- function drivers WDK KMDF
- power policy WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting PnP and Power Management in Function Drivers


*Function drivers* control the operation of a device and therefore they access device hardware. These drivers must support PnP and power management operations and typically register several event callback functions when they [create device objects](creating-a-framework-device-object.md).

Typically, a function driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function calls [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135) to register the following callback functions:

-   [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880), which delivers the device's system-assigned resources to the driver. The driver can perform operations, such as mapping the device's bus-relative memory into the processor's virtual address space, that make the hardware accessible to the driver.

-   [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848), which performs operations, such as loading firmware, that are needed each time that the driver's device enters its working (D0) state.

-   [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855), which performs operations that are needed each time that the driver's device leaves its working (D0) state and enters a low-power state.

-   [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890), which releases any system resources that [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) allocated.

Like all framework-defined callback functions, the ones in the preceding list are optional. You have to supply them only if your driver needs them.

Function drivers can call [**WdfDeviceSetPnpCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff546898) and [**WdfDeviceSetPowerCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff546901) to report a device's PnP and power management capabilities to the operating system.

Typically, you will use the framework's *power-managed I/O queues* for most I/O requests. If an I/O queue is power-managed, the framework delivers requests to the driver only if its device is in its working (D0) state. For more information about power-managed I/O queues, see [Power Management for I/O Queues](power-management-for-i-o-queues.md).

Typically, the device's function driver is the *power policy owner* for the driver stack. The power policy owner determines the appropriate [device power state](https://msdn.microsoft.com/library/windows/hardware/ff543162) for a device and sends requests to the device's driver stack whenever the device's power state should change. For framework-based drivers, the framework handles this responsibility, so you do not have to provide code in your driver to request changes in a device's power state.

The power policy owner has two additional responsibilities: it controls a device's ability to enter a low-power state when it is idle and the system remains in its [working (S0) state](https://msdn.microsoft.com/library/windows/hardware/ff564591), and it controls the device's ability to generate a wake signal when it detects an external event from a low-power state. If your device has idle or wake capabilities, your function driver can provide additional callback functions. For more information about the responsibilities of the power policy owner, see [Power Policy Ownership](power-policy-ownership.md).

 

 





