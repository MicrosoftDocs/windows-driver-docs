---
title: Minimal Interoperability Configuration Sets
description: Minimal Interoperability Configuration Sets
ms.assetid: 2390c710-8693-4af4-903f-89068436141d
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , restricted profiles
- Video Acceleration WDK DirectX , restricted profiles
- VA WDK DirectX , restricted profiles
- restricted profiles WDK DirectX VA
- minimal interoperability configuration set WDK DirectX VA
- interoperability configuration sets WDK DirectX VA
- configuration sets WDK DirectX VA
- DXVA_ConfigPictureDecode
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Minimal Interoperability Configuration Sets


## <span id="ddk_minimal_interoperability_configuration_sets_gg"></span><span id="DDK_MINIMAL_INTEROPERABILITY_CONFIGURATION_SETS_GG"></span>


All DirectX VA decoders must operate with all DirectX VA accelerators to use a [restricted profile](restricted-profiles.md). Every decoder must be capable of operation with any member of a set of connection configurations, and every accelerator must be capable of operation with at least one member of that set. There are three configuration sets that define the minimal level of functionality that a device driver must provide:

[Compressed Picture Decoding Set](compressed-picture-decoding-set.md)

[Alpha-Blend Data Loading Set](alpha-blend-data-loading-set.md)

[Alpha-Blend Combination Set](alpha-blend-combination-set.md)

For each set the decoder and accelerator must support the same DirectX VA restricted-mode GUID.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Minimal%20Interoperability%20Configuration%20Sets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




