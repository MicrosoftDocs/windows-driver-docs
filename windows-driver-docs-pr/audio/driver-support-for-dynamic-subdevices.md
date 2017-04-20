---
title: Driver Support for Dynamic Subdevices
description: Driver Support for Dynamic Subdevices
ms.assetid: ca355dfc-46ad-4df2-ac48-f3a0780dc3d3
keywords:
- dynamic audio subdevices WDK audio
- dynamic topologies WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver Support for Dynamic Subdevices


The code example in [Subdevice Creation](subdevice-creation.md) shows how to use the **PcRegisterSubdevice** routine to register a subdevice. The SB16 sample audio driver in the Windows Driver Kit (WDK) shows how to use the **PcRegisterPhysicalConnection** routine to register the physical connections between subdevices that are contained in the same audio adapter.

The [IUnregisterSubdevice](https://msdn.microsoft.com/library/windows/hardware/ff537030) and [IUnregisterPhysicalConnection](https://msdn.microsoft.com/library/windows/hardware/ff537022) interfaces complement the PcRegister*Xxx* routines. These interfaces contain methods that the sample driver uses to "unregister" devices that were previously registered by calls to the PcRegister*Xxx* routines. As mentioned previously, these two interfaces are available in Windows Server 2003 with SP1 and later and Windows XP with SP2, but not in earlier Windows versions. Thus, the earlier Windows versions lack support for dynamic topologies, although a hot-fix package with dynamic topology support is available for Windows Server 2003, Windows XP, and Windows 2000.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Driver%20Support%20for%20Dynamic%20Subdevices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


