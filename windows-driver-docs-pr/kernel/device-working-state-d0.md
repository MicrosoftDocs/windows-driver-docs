---
title: Device Working State D0
description: Device Working State D0
ms.assetid: 6b0ec03a-eaf1-4c96-aaae-dfe821583787
keywords: ["device power states WDK kernel", "Dx names WDK power management", "device working state WDK power management", "continuous power WDK kernel", "delays WDK power management", "working states WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Device Working State D0





In the D0 device power state, the device is fully on and operational. In this state, a device driver can interact with the device to perform I/O operations, and the device can generate interrupts. If the device has hardware registers that are mapped into memory or I/O address space, the driver can access these registers.

Starting with Windows 8, a device driver can connect a [passive-level interrupt service routine](using-passive-level-interrupt-handling-routines.md) (ISR) to the interrupt from a device. The device can generate interrupts regardless of whether it is in D0. When in a low-power Dx state, the device can generate an interrupt that acts as a trigger to bring the device back to D0. The ISR is scheduled to run at IRQL = PASSIVE\_LEVEL after the device enters D0. In earlier versions of Windows, including Windows 7, a device must not generate interrupts when it is in a device power state other than D0.

A transition from D0 to a low-power Dx state can occur only when the device driver, while acting as the power policy owner for the device, initiates the transition by calling the [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) routine. When the power manager responds to this call by sending a power IRP ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)), the device driver, the bus driver, and the platform firmware (through the [Windows ACPI driver](acpi-driver.md), Acpi.sys) cooperatively handle this IRP to change the power state of the device.

Device hardware typically monitors a set of internal events that can generate either run-time interrupts or wake signals, depending on how the device is configured. The driver implements one code path to respond to interrupts, and another to respond to wake events. The driver code can be simplified if the interrupt code path does not need to deal with wake events, and the wake code path does not need to deal with interrupts. As a best practice, the driver should configure the device to generate interrupts only when the device is in D0, and to generate wake signals only when the device is in a low-power Dx state. Typically, the driver configures the device to generate a wake signal just before the device exits D0, and configures the device to generate interrupts just after the device enters D0.

Typically, a device enters the D0 state when its hardware reset signal is asserted. In fact, the specifications for buses such as PCI and PCI Express require this behavior.

These are the characteristics of the D0 state:

<a href="" id="power-consumption"></a>**Power consumption**  
Highest level of continuous power consumption for the device.

<a href="" id="device-context"></a>**Device context**  
All context retained.

<a href="" id="device-driver-behavior"></a>**Device driver behavior**  
Normal operation.

<a href="" id="restore-time"></a>**Restore time**  
Not applicable.

<a href="" id="wake-up-capability"></a>**Wake-up capability**  
Not applicable.

 

 




