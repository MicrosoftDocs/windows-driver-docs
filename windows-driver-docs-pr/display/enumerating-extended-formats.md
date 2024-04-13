---
title: Enumerating Extended Formats
description: Enumerating Extended Formats
keywords:
- nonstandard display modes WDK DirectX 9.0 , extended
- extended nonstandard display modes WDK DirectX 9.0
ms.date: 04/20/2017
---

# Enumerating Extended Formats


## <span id="ddk_enumerating_extended_formats_gg"></span><span id="DDK_ENUMERATING_EXTENDED_FORMATS_GG"></span>


The DirectX 9.0 runtime must verify which extended nonstandard display modes that a driver supports before performing any operations using those display modes. To verify the number of nonstandard display modes that the driver supports, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETEXTENDEDMODECOUNT value. If the driver does not support any nonstandard display modes, it returns zero in the **dwModeCount** member of the [**DD\_GETEXTENDEDMODECOUNTDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_dd_getextendedmodecountdata) structure for this request. To receive information about each supported nonstandard display mode, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETEXTENDEDMODE value for each mode. The driver then returns a D3DDISPLAYMODE structure that specifies the nonstandard display mode in the **mode** member of the [**DD\_GETEXTENDEDMODEDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_dd_getextendedmodedata) structure. For more information about **GetDriverInfo2**, see [Supporting GetDriverInfo2](supporting-getdriverinfo2.md). For more information about D3DDISPLAYMODE, see the latest DirectX SDK documentation.

 

