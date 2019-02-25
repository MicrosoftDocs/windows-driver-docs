---
title: Making an ISR Active or Inactive
description: Starting with Windows 8, a driver can call the IoReportInterruptActive or IoReportInterruptInactive routine to make a registered interrupt service routine (ISR) active or inactive.
ms.assetid: 788D9341-D1F8-4126-8C30-AA49DE27F4BB
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Making an ISR Active or Inactive


Starting with Windows 8, a driver can call the [**IoReportInterruptActive**](https://msdn.microsoft.com/library/windows/hardware/jj158875) or [**IoReportInterruptInactive**](https://msdn.microsoft.com/library/windows/hardware/jj158876) routine to make a registered interrupt service routine (ISR) active or inactive.

To register an ISR, and to connect the ISR to an interrupt or a set of interrupts, the driver calls the [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine. After the ISR is registered, the driver can use **IoReportInterruptActive** and **IoReportInterruptInactive** to perform lightweight (or "soft") connect and disconnect operations that leave the ISR's registration unchanged. **IoReportInterruptInactive** disables calls to the ISR by soft-disconnecting the associated interrupt or interrupts. **IoReportInterruptActive** soft-connects these interrupts to enable calls to the ISR.

For example, a driver might call **IoReportInterruptInactive** to soft-disconnect a set of interrupts before a device exits the D0 power state, and call **IoReportInterruptActive** to soft-connect these interrupts after the device reenters D0. In principle, a driver might instead call [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093) before the device exits D0, and call **IoConnectInterruptEx** after the device reenters D0. However, **IoReportInterrupt*Xxx*** calls are faster than **IoConnectInterruptEx** and **IoDisconnectInterruptEx** calls. In contrast to **IoConnectInterruptEx** and **IoDisconnectInterruptEx** calls, which might fail for a variety of reasons (for example, insufficient system resources), **IoReportInterrupt*Xxx*** calls rarely, if ever, fail. Additionally, the **IoReportInterrupt*Xxx*** routines can be called at IRQL &lt;= DISPATCH\_LEVEL, whereas **IoConnectInterruptEx** and **IoDisconnectInterruptEx** can be called only at PASSIVE\_LEVEL.

By default, the ISR is active (and calls to the ISR are enabled) after **IoConnectInterruptEx** successfully registers the ISR.

Calls to **IoReportInterruptInactive** and **IoReportInterruptActive** are optional. If a driver never calls these routines, the registered ISR stays active until the driver calls the [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093) routine to unregister the ISR.

The driver should configure the device to issue interrupts only when the ISR for these interrupts is active. Failure to prevent a device from issuing interrupts when the ISR is inactive might cause system instability. For example, if a device shares a level-triggered interrupt line with other devices, and the device issues interrupt requests when the ISR is inactive, the ISRs for the other devices on the line will not acknowledge the interrupt and the interrupt will continue to fire. Before calling **IoReportInterruptInactive**, the driver should configure the device to stop issuing interrupts. After calling **IoReportInterruptActive**, the driver should configure the device to start issuing interrupts.

To unregister an ISR, a driver can call **IoDisconnectInterruptEx** regardless of whether the ISR is currently active or inactive.

An **IoReportInterruptActive** call that occurs when the ISR is already active has no effect, but is not treated as an error. Similarly, an **IoReportInterruptInactive** call that occurs when the ISR is already inactive has no effect, but is not treated as an error.

 

 




