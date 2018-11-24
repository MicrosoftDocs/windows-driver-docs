---
title: DeviceWake
description: DeviceWake
ms.assetid: 3b82c095-1ee7-41e9-991e-ac0bcf959024
keywords: ["DeviceWake"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DeviceWake





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

 

 




