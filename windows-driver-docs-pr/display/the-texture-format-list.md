---
title: The Texture Format List
description: The Texture Format List
ms.assetid: 5e60d6e3-d0a2-4b52-86cb-06de839f970a
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , texture format lists
- texture format lists WDK DirectX 8.0
- DPIXELFORMAT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Texture Format List


## <span id="ddk_the_texture_format_list_gg"></span><span id="DDK_THE_TEXTURE_FORMAT_LIST_GG"></span>


Direct 8.0 introduces a new mechanism for describing pixel formats. In previous versions of DirectDraw and Direct3D pixel formats were described by a data structure ([**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274)) that contained information about the number of bits per color channel and bitmasks for each color channel (along with flags and size field). Pixel formats in DirectX 8.0 are simple DWORDs that identify a particular pixel format and are compatible with [*FOURCCs*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) (Direct3D pixel formats are simply FOURCCs with all but the least significant bytes being zero).

The DDPIXELFORMAT data structure is no longer exposed through API level interfaces. However, it is still used at the DDI level. The driver reports its supported texture formats through a texture format array that consists of surface descriptions with their embedded DDPIXELFORMAT data structures. However, the embedded pixel format structures can now be used to report new style pixel formats. To specify a new style pixel format using the DDPIXELFORMAT data structure, set the **dwFlags** field of the structure to the value DDPF\_D3DFORMAT and store the new pixel format identifier in the **dwFourCC** field.

In addition, certain other new fields have been added to DDPIXELFORMAT (the new fields have been added as members of unions with existing fields so the size of the data structure is the same). These fields include: **dwOperations**, **dwPrivateFormatBitCount**, and **wFlipMSTypes** and **wBltMSTypes**.

A DirectX 8.0 DDI compliant driver should continue to report DX7 style surface formats through the standard mechanisms, that is, the texture format list reported in the global driver data structure ([**D3DHAL\_GLOBALDRIVERDATA**](https://msdn.microsoft.com/library/windows/hardware/ff545963)) and the Z/Stencil list reported in response to a GUID\_ZPixelFormats from [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404). However, the driver should also report all of its supported surface formats through the new DirectX 8.0 DDI mechanism described below.

DirectX 8.0 DDI style surface formats are reported using **GetDriverInfo2**. Two **GetDriverInfo2** query types are used by the runtime to query for surface formats from the driver. D3DGDI2\_TYPE\_GETFORMATCOUNT is used to request the number of DirectX 8.0 style surface formats supported by the driver. D3DGDI2\_TYPE\_GETFORMAT is used to query for a particular surface format from the driver.

To handle the D3DGDI2\_TYPE\_GETFORMATCOUNT, the driver must store the number of DirectX 8.0 DDI style surface formats that it supports in the **dwFormatCount** field of the [**DD\_GETFORMATCOUNTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551566).

When the runtime has received the number of supported formats from the driver, it then queries for each surface format in turn with **GetDriverInfo2** queries of type D3DGDI2\_TYPE\_GETFORMAT. The data structure pointed to by the **lpvData** field of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) data structure is, in this case, [**DD\_GETFORMATDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551569).

The DirectX 8.0 runtime scans the texture format list reported by the driver examining the **dwFlags** fields of each pixel format. If any of the texture formats have **dwFlags** set to DDPF\_D3DFORMAT, then the runtime identifies this texture format list as DX8 style and filters all texture formats whose pixel format is not flagged as DDPF\_D3DFORMAT. Furthermore, a DX7 runtime filters any texture format that has DDPF\_D3DFORMAT set. Therefore, a driver supporting the DX8 DDI can return a texture format list that contains two entries for each supported format, one specified in the old style and one in the new. DX8 runtimes use the formats specified in the new style and DX7 runtimes use the formats specified in the old style.

All supported surface formats, such as textures, depth or stencil buffers, or render targets, should be reported through the **GetDriverInfo2** mechanism. The runtime ignores the texture and Z/Stencil formats returned through legacy mechanisms (D3DHAL\_GLOBALDRIVERDATA and GUID\_ZPixelFormats). No attempt is made to map these formats to DX8 style formats for DirectX 8.0 drivers. However, legacy formats are mapped to the new style for DirectX 7.0 or earlier drivers. Therefore, a driver must report all supported surface formats through the DirectX 8.0 DDI. Furthermore, because legacy runtimes do not map new style surface formats to old style formats it is essential that the driver continues to report DirectX 7.0 style surface and Z/Stencil formats through the legacy mechanism.

 

 





