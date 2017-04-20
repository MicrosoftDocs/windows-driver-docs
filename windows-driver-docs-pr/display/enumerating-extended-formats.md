---
title: Enumerating Extended Formats
description: Enumerating Extended Formats
ms.assetid: 504464ff-4449-43fa-9fc8-645400ac8236
keywords:
- nonstandard display modes WDK DirectX 9.0 , extended
- extended nonstandard display modes WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumerating Extended Formats


## <span id="ddk_enumerating_extended_formats_gg"></span><span id="DDK_ENUMERATING_EXTENDED_FORMATS_GG"></span>


The DirectX 9.0 runtime must verify which extended nonstandard display modes that a driver supports before performing any operations using those display modes. To verify the number of nonstandard display modes that the driver supports, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETEXTENDEDMODECOUNT value. If the driver does not support any nonstandard display modes, it returns zero in the **dwModeCount** member of the [**DD\_GETEXTENDEDMODECOUNTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551558) structure for this request. To receive information about each supported nonstandard display mode, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETEXTENDEDMODE value for each mode. The driver then returns a D3DDISPLAYMODE structure that specifies the nonstandard display mode in the **mode** member of the [**DD\_GETEXTENDEDMODEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551559) structure. For more information about **GetDriverInfo2**, see [Supporting GetDriverInfo2](supporting-getdriverinfo2.md). For more information about D3DDISPLAYMODE, see the latest DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Enumerating%20Extended%20Formats%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




