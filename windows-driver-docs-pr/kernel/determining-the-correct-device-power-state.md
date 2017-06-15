---
title: Determining the Correct Device Power State
author: windows-driver-content
description: Determining the Correct Device Power State
MS-HAID:
- 'PwrMgmt\_88ccf2fe-a6dc-47bf-9ac8-953c05b49bda.xml'
- 'kernel.determining\_the\_correct\_device\_power\_state'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4acefe93-1d7a-4c12-8701-03c2a8929591
keywords: ["DEVICE_CAPABILITIES structure", "correct device power states WDK power management", "device power states WDK power management"]
---

# Determining the Correct Device Power State


## <a href="" id="ddk-determining-the-correct-device-power-state-kg"></a>


The power policy owner checks the [**DeviceState**](devicestate.md) array in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure to determine the valid range of device power states for each system power state. The array lists the highest device power state the underlying device can support for each system power state.

When choosing a specific state from this range, consider the following:

-   Most devices enter the D0 state when the system enters the S0 state.

-   Most devices enter the D3 state when the system enters any sleeping state. However, a device that is enabled for wake-up might be required to enter D1 or D2 instead, if it supports such states. For further information, see [Reporting Device Power Capabilities](reporting-device-power-capabilities.md).

-   Special rules apply for the device that will hold the hibernation file. If the system IRP requests **PowerSystemHibernate**, the device that will hold the hibernation file must not power off. The power policy owner for such a device should request device power state D3 and save context, but the device's drivers must not power off the device.

If the system IRP requests **PowerSystemShutdown**, the driver should check the POWER\_ACTION value at **Irp-&gt;Parameters.Power.ShutdownType** to determine the reason for the state change. For further information, see [System Power Actions](system-power-actions.md).

The device power policy owner must send a device set-power IRP for each system set-power IRP, even if the device is already in the correct device power state. If the driver previously suspended device operations in response to a query-power IRP, the set-power IRP notifies it to stop queuing IRPs and return to normal operation for its current power state. The only exception occurs when the device is in the D3 state; in this case, the driver need not send an additional [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request for D3.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Determining%20the%20Correct%20Device%20Power%20State%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


