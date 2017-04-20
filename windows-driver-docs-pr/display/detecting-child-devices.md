---
title: Detecting Child Devices
description: Detecting Child Devices
ms.assetid: 36c0c4ef-7810-4e8a-b349-0b7c1f8c2f0c
keywords:
- video miniport drivers WDK Windows 2000 , child devices
- child devices WDK video miniport , detecting
- detecting child devices WDK video miniport
- HwVidGetVideoChildDescriptor
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Detecting Child Devices


## <span id="ddk_detecting_child_devices_gg"></span><span id="DDK_DETECTING_CHILD_DEVICES_GG"></span>


You must implement [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) in your miniport driver for the Plug and Play manager to be able to detect child devices of a graphics adapter.

By default, [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) cannot be called until after the parent device is started; that is, *HwVidGetVideoChildDescriptor* cannot be called until after [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) has completed. To override this default, thus allowing child enumeration to occur at any time, you can set the **AllowEarlyEnumeration** member of [**VIDEO\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff570505) to **TRUE**.

Some devices generate an interrupt when new hardware is connected to the system or when existing hardware is disconnected from the system. To handle such an interrupt, the miniport driver should do the following:

-   Implement a DPC ([**HwVidDpcRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff567327)) that calls [**VideoPortEnumerateChildren**](https://msdn.microsoft.com/library/windows/hardware/ff570297).

-   Implement an interrupt handler ([*HwVidInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff567349)) that calls [**VideoPortQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff570339) to queue the DPC when an interrupt on the device occurs.

[**VideoPortEnumerateChildren**](https://msdn.microsoft.com/library/windows/hardware/ff570297) forces the reenumeration of the adapter's child devices by causing the miniport driver's [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341) function to be called for each of the parent device's children. The Plug and Play manager will update the relationship between the parent device and its children accordingly.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Detecting%20Child%20Devices%20%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




