---
title: Making an ISR Active or Inactive
author: windows-driver-content
description: Starting with Windows 8, a driver can call the IoReportInterruptActive or IoReportInterruptInactive routine to make a registered interrupt service routine (ISR) active or inactive.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 788D9341-D1F8-4126-8C30-AA49DE27F4BB
---

# Making an ISR Active or Inactive


Starting with Windows 8, a driver can call the [**IoReportInterruptActive**](https://msdn.microsoft.com/library/windows/hardware/jj158875) or [**IoReportInterruptInactive**](https://msdn.microsoft.com/library/windows/hardware/jj158876) routine to make a registered interrupt service routine (ISR) active or inactive.

To register an ISR, and to connect the ISR to an interrupt or a set of interrupts, the driver calls the [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine. After the ISR is registered, the driver can use **IoReportInterruptActive** and **IoReportInterruptInactive** to perform lightweight (or "soft") connect and disconnect operations that leave the ISR's registration unchanged. **IoReportInterruptInactive** disables calls to the ISR by soft-disconnecting the associated interrupt or interrupts. **IoReportInterruptActive** soft-connects these interrupts to enable calls to the ISR.

For example, a driver might call **IoReportInterruptInactive** to soft-disconnect a set of interrupts before a device exits the D0 power state, and call **IoReportInterruptActive** to soft-connect these interrupts after the device reenters D0. In principle, a driver might instead call [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093) before the device exits D0, and call **IoConnectInterruptEx** after the device reenters D0. However, **IoReportInterrupt*Xxx*** calls are faster than than **IoConnectInterruptEx** and **IoDisconnectInterruptEx** calls. In contrast to **IoConnectInterruptEx** and **IoDisconnectInterruptEx** calls, which might fail for a variety of reasons (for example, insufficient system resources), **IoReportInterrupt*Xxx*** calls rarely, if ever, fail. Additionally, the **IoReportInterrupt*Xxx*** routines can be called at IRQL &lt;= DISPATCH\_LEVEL, whereas **IoConnectInterruptEx** and **IoDisconnectInterruptEx** can be called only at PASSIVE\_LEVEL.

By default, the ISR is active (and calls to the ISR are enabled) after **IoConnectInterruptEx** successfully registers the ISR.

Calls to **IoReportInterruptInactive** and **IoReportInterruptActive** are optional. If a driver never calls these routines, the registered ISR stays active until the driver calls the [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093) routine to unregister the ISR.

The driver should configure the device to issue interrupts only when the ISR for these interrupts is active. Failure to prevent a device from issuing interrupts when the ISR is inactive might cause system instability. For example, if a device shares a level-triggered interrupt line with other devices, and the device issues interrupt requests when the ISR is inactive, the ISRs for the other devices on the line will not acknowledge the interrupt and the interrupt will continue to fire. Before calling **IoReportInterruptInactive**, the driver should configure the device to stop issuing interrupts. After calling **IoReportInterruptActive**, the driver should configure the device to start issuing interrupts.

To unregister an ISR, a driver can call **IoDisconnectInterruptEx** regardless of whether the ISR is currently active or inactive.

An **IoReportInterruptActive** call that occurs when the ISR is already active has no effect, but is not treated as an error. Similarly, an **IoReportInterruptInactive** call that occurs when the ISR is already inactive has no effect, but is not treated as an error.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Making%20an%20ISR%20Active%20or%20Inactive%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


