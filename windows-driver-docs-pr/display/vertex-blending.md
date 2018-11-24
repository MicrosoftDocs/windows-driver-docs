---
title: Vertex Blending
description: Vertex Blending
ms.assetid: 58e740fb-01e4-4c8c-8e44-f0c358fd621a
keywords:
- lending WDK Direct3D
- vertex blending WDK Direct3D
- Direct3D WDK Windows 2000 display , vertex blending
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vertex Blending


## <span id="ddk_vertex_blending_gg"></span><span id="DDK_VERTEX_BLENDING_GG"></span>


Vertex blending operations are supported for the latest Direct X release. Vertex blending works in this way: an object from modeling space is multiplied by a 4X4 world matrix, placing the model's origin in a particular world space relative to the origin of that world space. One part of the matrix does orientation and another part does the position. There can be up to three world matrices applied, allowing objects to be "bent" by blending the vertices with different weighting over the span of the object.

Next, the view matrix is applied, which effectively compresses the space relative to a particular viewpoint; much like a camera renders the real world onto a two-dimensional picture.

 

 





