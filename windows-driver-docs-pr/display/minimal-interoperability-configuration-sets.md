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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minimal Interoperability Configuration Sets


## <span id="ddk_minimal_interoperability_configuration_sets_gg"></span><span id="DDK_MINIMAL_INTEROPERABILITY_CONFIGURATION_SETS_GG"></span>


All DirectX VA decoders must operate with all DirectX VA accelerators to use a [restricted profile](restricted-profiles.md). Every decoder must be capable of operation with any member of a set of connection configurations, and every accelerator must be capable of operation with at least one member of that set. There are three configuration sets that define the minimal level of functionality that a device driver must provide:

[Compressed Picture Decoding Set](compressed-picture-decoding-set.md)

[Alpha-Blend Data Loading Set](alpha-blend-data-loading-set.md)

[Alpha-Blend Combination Set](alpha-blend-combination-set.md)

For each set the decoder and accelerator must support the same DirectX VA restricted-mode GUID.

 

 





