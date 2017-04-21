---
title: Reporting Support for 32-bit Indices
description: Reporting Support for 32-bit Indices
ms.assetid: e9ea5f0e-9b95-4671-a947-55692eca8902
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , index buffers
- index buffers WDK Directx 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for 32-bit Indices


## <span id="ddk_reporting_support_for_32_bit_indices_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_32_BIT_INDICES_GG"></span>


Before DirectX 8.0, vertex indices were restricted to 16-bit quantities. DirectX 8.0 adds support for 32-bit indices. A driver reports support for 32-bit indices by setting the value of the **MaxVertexIndex** field of D3DCAPS8 (currently also in [**D3DHAL\_D3DEXTENDEDCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544753)) to a value greater than 0xFFFF. This field also allows the driver to report that although it supports indices requiring 32-bits of storage it does not support the full range of 32-bit values.

**DirectX 9.0 and later versions only.**

 

In order for a driver to expose its Direct3D hardware abstraction layer (HAL) device to applications through DirectX 9.0 interfaces, the driver must set the value of **MaxVertexIndex** to a value greater than or equal to 0xFFFF.
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%2032-bit%20Indices%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




