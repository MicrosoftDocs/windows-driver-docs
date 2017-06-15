---
title: DeviceWake
author: windows-driver-content
description: DeviceWake
MS-HAID:
- 'PwrMgmt\_a1346131-8e8f-4cf7-8c06-662ad8986630.xml'
- 'kernel.devicewake'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3b82c095-1ee7-41e9-991e-ac0bcf959024
keywords: ["DeviceWake"]
---

# DeviceWake


## <a href="" id="ddk-devicewake-kg"></a>


The **DeviceWake** member of [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) contains the lowest (least-powered) device power state from which the device can signal a wake event, or **PowerDeviceUnspecified** if the device cannot wake in response to an external signal.

The bus driver sets this value. A higher-level driver can change the value to a higher-powered state. For example, if the bus driver sets **DeviceWake** to D3 but a driver further up the device stack supports wake-up only from D2, the higher-level driver can change the value to D2.

Note that if a driver changes **DeviceWake**, it might also have to change [**SystemWake**](systemwake.md) to avoid conflicts with the system-to-device mappings in the **DeviceState** array. For example, assume that the bus driver sets the following:

-   **DeviceState**\[**PowerSystemSleeping1**\] = **PowerDeviceD1**

-   **DeviceState**\[**PowerSystemSleeping2**\] = **PowerDeviceD3**

-   **DeviceWake** = **PowerDeviceD3**

-   **SystemWake** = **PowerSystemSleeping2**

If a higher-level driver determines that its device cannot wake the system from D3, but only from D2 or higher, it can change **DeviceWake** to D2. However, this change causes the mapping from S2 to D3 to be impossible. Remember that the **DeviceState** array lists the highest device power state a device can support for a given system power state. If the system power state in the example is **PowerSystemSleeping2**, the device power state cannot be **PowerDeviceD2**. To eliminate this problem, the driver must also change **SystemWake** to **PowerSystemSleeping1**. The same is true for the **WakeFromD***x* and **DeviceD***x* settings. A driver must ensure that any changes it makes to **SystemWake** or **DeviceWake** do not conflict with the **WakeFromD***x* and **DeviceD***x* values. The values of *WakeFromDx* and **DeviceD***x* reflect hardware characteristics that a driver cannot change.

If both the **SystemWake** and **DeviceWake** members are nonzero (that is, not **PowerSystemUnspecified**), then the device and its drivers support wake-up on this system.

On non-ACPI hardware, the **DeviceWake** member contains zero (**PowerSystemUnspecified**).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DeviceWake%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


