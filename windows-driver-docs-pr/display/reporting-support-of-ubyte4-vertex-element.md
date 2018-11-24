---
title: Reporting Support of UBYTE4 Vertex Element
description: Reporting Support of UBYTE4 Vertex Element
ms.assetid: d5091ceb-71de-4310-95d9-c52361772ebc
keywords:
- UBYTE4 vertex element WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Support of UBYTE4 Vertex Element


## <span id="ddk_reporting_support_of_ubyte4_vertex_element_gg"></span><span id="DDK_REPORTING_SUPPORT_OF_UBYTE4_VERTEX_ELEMENT_GG"></span>


A DirectX 9.0 version driver must report support of the UBYTE4 vertex element type by setting the D3DDTCAPS\_UBYTE4 bit in the **DeclTypes** member of the D3DCAPS9 structure. To indicate nonsupport of the UBYTE4 vertex element type, the driver does not set the D3DDTCAPS\_UBYTE4 bit. In contrast, A DirectX 8.1 and earlier driver sets the D3DVTXPCAPS\_NO\_VSDT\_UBYTE4 bit to indicate nonsupport of the UBYTE4 vertex element type.

 

 





