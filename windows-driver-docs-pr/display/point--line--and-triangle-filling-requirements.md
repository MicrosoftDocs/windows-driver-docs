---
title: Point, Line, and Triangle Filling Requirements
description: Point, Line, and Triangle Filling Requirements
ms.assetid: 1a0a8160-01e2-4fb7-b1a2-6b61f1021fb9
keywords:
- point fill rule WDK Direct3D
- line fill rule WDK Direct3D
- triangle fill rules WDK Direct3D
- filling lines WDK Direct3D
- filling points WDK Direct3D
- filling triangles WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Point, Line, and Triangle Filling Requirements


## <span id="ddk_point_line_and_triangle_filling_requirements_gg"></span><span id="DDK_POINT_LINE_AND_TRIANGLE_FILLING_REQUIREMENTS_GG"></span>


The requirements for filling points, lines, and triangles are as follows:

### <span id="points"></span><span id="POINTS"></span> Points

The point fill and rasterization rules determine how a point is rendered. These rules are identical to the triangle fill rules. All flags and capabilities that apply to triangles also apply to points, and vice-versa. The reference implementation expands a point into a rectangle and applies the triangle fill rules to the result.

Given a point with coordinates P₀(x,y), generate four new points P₁, P₂, P₃, and P₄ as follows:

```cpp
P1(x,y) = (x âˆ’ 0.5, y âˆ’ 0.5)
P2(x,y) = (x âˆ’ 0.5, y + 0.5)
P3(x,y) = (x + 0.5, y + 0.5)
P4(x,y) = (x + 0.5, y âˆ’ 0.5)
```

The rectangle is then generated as two triangles, such as (P₁, P₂, P₃) and (P₁, P₃, P₄). You may also examine the reference rasterizer implementation for rendering points in the source files *setup.cpp* and *scancnv.cpp* of the DirectX Driver Development Kit (DDK).

### <span id="lines"></span><span id="LINES"></span>Lines

Line fill rules (that is, rules that determine how a line is rendered) follow the Grid Intersection Quantization (GIQ) diamond convention. For more information about the GIQ diamond convention, see [Cosmetic Lines](cosmetic-lines.md). An example of line-drawing code that follows these rules can be found in the DirectX DDK in the reference rasterizer source files *setup.cpp* and *scancnv.cpp*.

### <span id="triangles"></span><span id="TRIANGLES"></span>Triangles

The triangle fill rules determine how a triangle is rendered. These rules are identical to the point fill rules. An example of triangle-drawing code that follows the triangle fill rules can be found in the DirectX DDK in the reference rasterizer source files *setup.cpp* and *scancnv.cpp*.

Hardware should supply the culling caps and properly implement the three culling modes. The following code fragment determines whether to cull the current triangle:

```cpp
if (CurrentCullMode != D3DCULL_NONE) {
    int ccw = (((v[0]->sx - v[2]->sx) *
                (v[1]->sy - v[2]->sy)) <
               ((v[1]->sx - v[2]->sx) *
                (v[0]->sy - v[2]->sy)));
if ((CurrentCullMode == D3DCULL_CW && (ccw == 0)) ||
        (CurrentCullMode == D3DCULL_CCW && (ccw != 0))) {
        // Current triangle is culled, move onto
        // next triangle.
    }
}
// Current triangle is not culled, render it
```

The preceding code sample tests to determine which way the triangle is facing. The triangle is defined 0,1,2 and tested for being counterclockwise in screen space. If it is not, and there is clockwise culling, then that triangle is not drawn because the vertices go in clockwise order.

 

 





