---
title: Device Working State D0
author: windows-driver-content
description: Device Working State D0
MS-HAID:
- 'PwrMgmt\_d8e8114c-5805-4518-9987-017b62089f10.xml'
- 'kernel.device\_working\_state\_d0'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6b0ec03a-eaf1-4c96-aaae-dfe821583787
keywords: ["device power states WDK kernel", "Dx names WDK power management", "device working state WDK power management", "continuous power WDK kernel", "delays WDK power management", "working states WDK power management"]
---

# Device Working State D0


## <a href="" id="ddk-device-working-state-d0-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Device%20Working%20State%20D0%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


