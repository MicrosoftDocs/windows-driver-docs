---
title: Universal camera driver design guide for Windows 10
author: windows-driver-content
description: The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.
ms.assetid: CB5EEDF2-650D-4CD3-A5DE-DF0D6F10B394
---

# Universal camera driver design guide for Windows 10


The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The universal camera driver model also contains new DDIs, including:

[Digital video stabilization](https://msdn.microsoft.com/library/windows/hardware/dn936754)
[Variable frame rate](https://msdn.microsoft.com/library/windows/hardware/dn917971)
[Face detection](https://msdn.microsoft.com/library/windows/hardware/dn917937)
[Video high dynamic range (HDR)](https://msdn.microsoft.com/library/windows/hardware/dn936752)
[Optical stabilization](https://msdn.microsoft.com/library/windows/hardware/dn917954)
[Scene analysis: photo HDR, flash no flash, ultra low light](https://msdn.microsoft.com/library/windows/hardware/dn917934)
[Capture stats: metadata framework/attributes, histograms](https://msdn.microsoft.com/library/windows/hardware/dn917945)
[Smooth zoom](https://msdn.microsoft.com/library/windows/hardware/dn936756)
[Hardware optimization hints](https://msdn.microsoft.com/library/windows/hardware/dn917956)
[Camera profiles](camera-driver-functions.md)
## Build a universal camera driver


The universal camera driver is an AVStream minidriver built on the [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM).

For more information, see the following sections in the [Universal camera driver model reference for Windows 10](windows-10-technical-preview-camera-drivers-reference.md):

[New camera driver controls](camera-driver-controls.md)
[New camera driver enumerations](camera-driver-enumerations.md)
[New camera driver functions](camera-driver-functions.md)
[New camera driver structures](camera-driver-structures.md)
For more information about building AVStream minidrivers, see the following topics:

[Roadmap for Developing Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568130)
[AVStream Overview](avstream-overview.md)
[Writing an AVStream Minidriver](writing-an-avstream-minidriver.md)
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Universal%20camera%20driver%20design%20guide%20for%20Windows%2010%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


