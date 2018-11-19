---
title: Detecting Child Devices
description: Detecting Child Devices
ms.assetid: 36c0c4ef-7810-4e8a-b349-0b7c1f8c2f0c
keywords:
- video miniport drivers WDK Windows 2000 , child devices
- child devices WDK video miniport , detecting
- detecting child devices WDK video miniport
- HwVidGetVideoChildDescriptor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Detecting Child Devices


## <span id="ddk_detecting_child_devices_gg"></span><span id="DDK_DETECTING_CHILD_DEVICES_GG"></span>


You must implement [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) in your miniport driver for the Plug and Play manager to be able to detect child devices of a graphics adapter.

By default, [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) cannot be called until after the parent device is started; that is, *HwVidGetVideoChildDescriptor* cannot be called until after [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) has completed. To override this default, thus allowing child enumeration to occur at any time, you can set the **AllowEarlyEnumeration** member of [**VIDEO\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff570505) to **TRUE**.

Some devices generate an interrupt when new hardware is connected to the system or when existing hardware is disconnected from the system. To handle such an interrupt, the miniport driver should do the following:

-   Implement a DPC ([**HwVidDpcRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff567327)) that calls [**VideoPortEnumerateChildren**](https://msdn.microsoft.com/library/windows/hardware/ff570297).

-   Implement an interrupt handler ([*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349)) that calls [**VideoPortQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff570339) to queue the DPC when an interrupt on the device occurs.

[**VideoPortEnumerateChildren**](https://msdn.microsoft.com/library/windows/hardware/ff570297) forces the reenumeration of the adapter's child devices by causing the miniport driver's [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) function to be called for each of the parent device's children. The Plug and Play manager will update the relationship between the parent device and its children accordingly.

 

 





