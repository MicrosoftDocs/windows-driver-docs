---
title: Performing a Hardware Functionality Scan
description: Performing a Hardware Functionality Scan
ms.assetid: 966b30b7-2f08-4611-9f4d-f85b301de414
keywords:
- OPM WDK display , HFS
- OPM WDK display , hardware functionality scan
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Performing a Hardware Functionality Scan


A display miniport driver's Hardware Functionality Scan (HFS) ensures that the miniport driver communicates with the required hardware. For more information about HFS, download the Output Content Protection document at the [Output Content Protection and Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=204788) website.

A display miniport driver must start performing an HFS whenever the Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the following driver functions:

-   [**DxgkDdiStartDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560775)

-   [**DxgkDdiSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff560764) with the graphics adapter's power state set to D0.

The HFS can be asynchronous and is not required to complete before [**DxgkDdiStartDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560775) or [**DxgkDdiSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff560764) returns. However, no [OPM DDI](https://msdn.microsoft.com/library/windows/hardware/ff568627) function can return until the HFS completes.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Performing%20a%20Hardware%20Functionality%20Scan%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




