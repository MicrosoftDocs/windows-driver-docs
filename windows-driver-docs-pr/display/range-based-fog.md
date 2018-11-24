---
title: Range Based Fog
description: Range Based Fog
ms.assetid: 6410dd21-bb9d-4985-a765-03898d9b5d0b
keywords:
- range-based fog WDK Direct3D
- fogging WDK Direct3D
- D3DPRASTERCAPS_FOGRANGE
- D3DRENDERSTATE_RANGEFOGENABLE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Range Based Fog


## <span id="ddk_range_based_fog_gg"></span><span id="DDK_RANGE_BASED_FOG_GG"></span>


Fog can also be range-based. With normal z, or depth-based, fog an object can appear at the side of the view, but then as the viewer rotates toward it, the object disappears back into the fog because its z-value changes.

However, if fog is based on range instead of depth, it does not vary as the viewer rotates in place, as illustrated in the following figure.

![diagram illustrating range-based fog](images/d3dfig26.png)

Objects that are visible remain visible, regardless of the rotation. This is compelling for flight simulators, tank games, and other applications where it is undesirable to have objects disappearing and reappearing in the distance as the viewer rotates.

To set up fog to be range-based, D3DPRASTERCAPS\_FOGRANGE and the D3DRENDERSTATE\_RANGEFOGENABLE render state should be set. This render state works only with D3DVERTEX vertices. When the application specifies D3DLVERTEX or D3DTLVERTEX vertices, the F (fog) component of the RGBF fog value should already be corrected for range. The D3DVERTEX, D3DLVERTEX, and D3DTLVERTEX structures are defined in the Direct3D SDK documentation.

 

 





