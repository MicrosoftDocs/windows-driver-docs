---
title: Reporting Support for 32-bit Indices
description: Reporting Support for 32-bit Indices
ms.assetid: e9ea5f0e-9b95-4671-a947-55692eca8902
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , index buffers
- index buffers WDK Directx 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Support for 32-bit Indices


## <span id="ddk_reporting_support_for_32_bit_indices_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_32_BIT_INDICES_GG"></span>


Before DirectX 8.0, vertex indices were restricted to 16-bit quantities. DirectX 8.0 adds support for 32-bit indices. A driver reports support for 32-bit indices by setting the value of the **MaxVertexIndex** field of D3DCAPS8 (currently also in [**D3DHAL\_D3DEXTENDEDCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544753)) to a value greater than 0xFFFF. This field also allows the driver to report that although it supports indices requiring 32-bits of storage it does not support the full range of 32-bit values.

**DirectX 9.0 and later versions only.**

 

In order for a driver to expose its Direct3D hardware abstraction layer (HAL) device to applications through DirectX 9.0 interfaces, the driver must set the value of **MaxVertexIndex** to a value greater than or equal to 0xFFFF.
 

 





