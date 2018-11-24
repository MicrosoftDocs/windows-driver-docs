---
title: Multimatrix Vertex Blending
description: Multimatrix Vertex Blending
ms.assetid: d7348609-324d-4852-b217-4c298b8aaab7
keywords:
- lending WDK Direct3D
- vertex blending WDK Direct3D
- Direct3D WDK Windows 2000 display , vertex blending
- multimatrix vertex blending WDK Direct3D
- multimatrix vertex blending WDK Direct3D , about multimatrix vertex blending
- transforms WDK Direct3D
- skin blending WDK Direct3D
- geometry blending WDK Direct3D
- joint blending WDK Direct3D
- matrix vertex blending WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multimatrix Vertex Blending


## <span id="ddk_multimatrix_vertex_blending_gg"></span><span id="DDK_MULTIMATRIX_VERTEX_BLENDING_GG"></span>


Multimatrix vertex blending is a technique for rendering objects with smoothly blended skin joints. While this particular technique is not common in current software, some kind of smooth-skinning is currently used by most games involving animated characters.

There are a variety of geometry blending techniques. The technique described here is a form of geometry blending. This technique blends vertices across the joints of segmented articulated models, providing increased realism with reduced polygon count. As the joint changes in each frame, the geometry pipeline updates the positions of nearby vertices to smoothly blend between the segments at that joint. This capability can operate between segments that are related by joint types other than rotations, such as translations, scales, shears, or any combination that is able to be represented by a 4X4 transformation matrix.

The general principle is to extend the typical segmented character by blending mesh vertices at joints.

Segmented models are considered to be built up from segments, or coordinate systems, each defined by a transformation matrix. Traditionally, each vertex of a mesh is considered to belong to only a single segment. This paradigm has been extended to allow vertices to have partial membership in other segments. Each vertex near the joint between two or more segments can have a skin weight *Beta value*, representing the proportion by which it actually belongs to the other segments.

When used in classic hierarchical modeling, the root segment gets no blending. It is always a rigid body because there is no other transform with which to blend. The skin weight Beta is defined as the proportion of the parent coordinate system that is to be used. This will be 0.0 over the entire object if it is entirely rigid-body.

The Beta will be 1.0 for those portions that are rigidly attached to the parent segment. This will drop as the proportion of the parent segment's contribution to the blend drops. There must be some set of points with 1.0 in them (and 0.0) in order to maintain geometric continuity between several segments.

Multimatrix vertex blending allows smooth skin blending to be performed by updating the position of each vertex, without requiring a separate 4X4 transform to be specified for each vertex. It addresses the common case of a continuous smooth surface and yet requires only one additional value --the skin weight *Beta* -- per vertex, minimizing additional bandwidth requirements.

The specified vertex position data is transformed by all active world matrices, and the results are blended together using corresponding vertex weights.

The same steps are performed for any normal present in the vertex. This produces a single vertex (with position and normal) that is then fed into the rest of the pipeline for conventional lighting and clipping. For more details, see [Multimatrix Vertex Blending Algorithm](multimatrix-vertex-blending-algorithm.md).

Characters often can contain the majority of the polygons in a scene, and are a key performance issue. Geometry pipelines that do not handle smooth-skinning well will have difficulty with a majority of the content.

Furthermore, the number of characters visible is one of the most highly variable components of the scene. This has serious impact on frame-rate leveling behavior. For interactive applications, level frame rate is more important than high average frame rate, making efficient character rendering a very critical feature.

Vertex blending must be performed after transformations. If blending is not integrated into the rendering pipeline, the transformations must be performed twice: once for skinning and once for rendering.

Integrating vertex blending into the geometry pipeline allows this case to be handled with a single traversal of the vertex data, which makes it just as fast as unblended vertices in bandwidth limited cases.

The following sections provide implementation details for multimatrix vertex blending:

[Multimatrix Vertex Blending Algorithm](multimatrix-vertex-blending-algorithm.md)

[FVF Code Changes](fvf-code-changes.md)

[D3DTRANSFORMSTATE Changes](d3dtransformstate-changes.md)

[D3DRENDERSTATETYPE Changes](d3drenderstatetype-changes.md)

 

 





