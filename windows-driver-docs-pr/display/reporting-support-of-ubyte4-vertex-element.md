---
title: Reporting Support of UBYTE4 Vertex Element
description: Reporting Support of UBYTE4 Vertex Element
ms.assetid: d5091ceb-71de-4310-95d9-c52361772ebc
keywords:
- UBYTE4 vertex element WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support of UBYTE4 Vertex Element


## <span id="ddk_reporting_support_of_ubyte4_vertex_element_gg"></span><span id="DDK_REPORTING_SUPPORT_OF_UBYTE4_VERTEX_ELEMENT_GG"></span>


A DirectX 9.0 version driver must report support of the UBYTE4 vertex element type by setting the D3DDTCAPS\_UBYTE4 bit in the **DeclTypes** member of the D3DCAPS9 structure. To indicate nonsupport of the UBYTE4 vertex element type, the driver does not set the D3DDTCAPS\_UBYTE4 bit. In contrast, A DirectX 8.1 and earlier driver sets the D3DVTXPCAPS\_NO\_VSDT\_UBYTE4 bit to indicate nonsupport of the UBYTE4 vertex element type.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20of%20UBYTE4%20Vertex%20Element%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




