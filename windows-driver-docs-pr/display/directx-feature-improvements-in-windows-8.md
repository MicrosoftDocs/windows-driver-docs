---
title: DirectX feature improvements in Windows 8
description: Windows 8 includes Microsoft DirectX feature improvements that benefit developers, end users and system manufacturers.
ms.assetid: 0622DA0D-41ED-4B47-B090-8D5B85E10EB3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX feature improvements in Windows 8


Windows 8 includes Microsoft DirectX feature improvements that benefit developers, end users and system manufacturers.

The feature improvements are in the following areas:

-   [Pixel formats (5551, 565, 4444)](#pixelformats): Higher performance for DirectX applications on lower-power hardware configurations.
-   [Double-precision shader functionality](#dblshader): High Level Shader model performance improvements that let you do more on the GPU without involving the CPU.
-   [Target-independent rasterization](#tir): Higher performance anti-aliasing path for Direct2D applications.
-   [No overwrite and discard](#noow): Higher performance for Microsoft Direct3D 11.1 applications on mobile platforms and power constraint devices that use tile-based renderers.
-   [UAVs at every stage](#uav): Added capabilities to enable shader debugging at all shader stages on DirectX 11.1 hardware.
-   [Cross-process sharing of texture arrays (for supporting Stereoscopic 3D)](#stereo): Provides a basis to enable Stereoscopic 3-D.
-   [Unordered access views with multi-sample anti-alias sample access](#unordered): Enables Direct3D 11 applications to implement high-quality rendering algorithms without needing to allocate memory for large numbers of samples.
-   [Logic ops](#logicops): Improvements to deferred shading techniques.
-   [Improved control of constant buffers](#buffers): Efficient buffer management for game developers.

## <span id="pixelformats"></span><span id="PIXELFORMATS"></span>Pixel formats (5551, 565, 4444)


To better support graphics in low-power configurations using DirectX, the following DirectX 9 pixel formats from the [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) enumeration must be supported in Direct3D for Windows 8:

-   **DXGI\_FORMAT\_B5G6R5\_UNORM**
-   **DXGI\_FORMAT\_B5G5R5A1\_UNORM**
-   **DXGI\_FORMAT\_B4G4R4A4\_UNORM**

These additional formats provide increased performance on lower-power hardware in DirectX applications. These formats are supported on all GPUs to date. This table describes the required support for these formats, depending on the hardware feature level.

**Required format support depending on hardware feature levels**

| Capability                       | Feature level 9\_x                                      | Feature level 10.0                                             | Feature level 10.1                        | Feature level 11+                         |
|----------------------------------|---------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| Typed Buffer                     | No                                                      | Required                                                       | Required                                  | Required                                  |
| Input Assembler Vertex Buffer    | No                                                      | Optional                                                       | Optional                                  | Optional                                  |
| Texture1D                        | No                                                      | Required                                                       | Required                                  | Required                                  |
| Texture2D                        | Required                                                | Required                                                       | Required                                  | Required                                  |
| Texture3D                        | No                                                      | Required                                                       | Required                                  | Required                                  |
| TextureCube                      | Required                                                | Required                                                       | Required                                  | Required                                  |
| Shader ld\*                      | No                                                      | Required                                                       | Required                                  | Required                                  |
| Shader sample\* (with filtering) | Required                                                | Required                                                       | Required                                  | Required                                  |
| Shader gather4                   | No                                                      | No                                                             | No                                        | Required                                  |
| Mipmap                           | Required                                                | Required                                                       | Required                                  | Required                                  |
| Mipmap Auto-Generation           | Required for 565, optional for 4444, 5551               | Required for 565, optional for 4444, 5551                      | Required for 565, optional for 4444, 5551 | Required for 565, optional for 4444, 5551 |
| RenderTarget                     | Required for 565, no for 4444, 5551                     | Required for 565, optional for 4444, 5551                      | Required for 565, optional for 4444, 5551 | Required for 565, optional for 4444, 5551 |
| Blendable RenderTarget           | Required for 565, no for 4444, 5551                     | Required for 565, optional for 4444, 5551                      | Required for 565, optional for 4444, 5551 | Required for 565, optional for 4444, 5551 |
| UAV Typed Store                  | No                                                      | No                                                             | No                                        | Optional                                  |
| CPU Lockable                     | Required                                                | Required                                                       | Required                                  | Required                                  |
| 4x MSAA                          | Optional                                                | Optional                                                       | Required for 565, optional for 4444, 5551 | Required for 565, optional for 4444, 5551 |
| 8x MSAA                          | Optional                                                | Optional                                                       | Optional                                  | Required for 565, optional for 4444, 5551 |
| Other MSAA Sample Count          | Optional                                                | Optional                                                       | Optional                                  | Optional                                  |
| Multisample Resolve              | Required (if MSAA supported) for 565, no for 4444, 5551 | Required (if MSAA supported) for 565, optional for 4444, 5551  | Required for 565, optional for 4444, 5551 | Required for 565, optional for 4444, 5551 |
| Multisample Load                 | No                                                      | Required (if MSAA supported) for 565, optional for 4444, 5551) | Required for 565, optional for 4444, 5551 | Required for 565, optional for 4444, 5551 |

 

## <span id="dblshader"></span><span id="DBLSHADER"></span>Double-precision shader functionality


In Windows 8, Windows Display Driver Model (WDDM) 1.2 drivers that support double precision must also support additional double-precision floating-point instructions in High Level Shader model 5 in all shader stages. The instructions are:

-   Double-precision reciprocal
-   Double-precision divide
-   Double-precision fused multiply-add

Because the runtime can pass these instructions directly to the driver, the implementation can optimize their performance, or implement them as specialized single instructions in hardware.

**Note**  
To use these features, developers must ensure that they are running with FEATURE\_LEVEL\_11 or higher with double-precision support (D3D11\_FEATURE\_DOUBLES) on a WDDM 1.2 or later driver.

 

### <span id="Sum_of_absolute_differences"></span><span id="sum_of_absolute_differences"></span><span id="SUM_OF_ABSOLUTE_DIFFERENCES"></span>Sum of absolute differences

Image processing is a critical application in modern devices. A common operation is pattern matching or search. Video-encoding operations typically search for matching square tiles (typically 8x8 or 16x16), and image recognition algorithms search for more general shapes that are identified by a bit mask. To improve the performance of these scenarios, a new intrinsic has been added to the Microsoft High Level Shader Language (HLSL) for Shader Model 5.0 in all shader stages. This intrinsic msad4() corresponds to and generates a group of masked sum of absolute differences (MSAD) instructions in the shader IL. All WDDM 1.2 and later drivers must support this instruction either directly in hardware or as a set of other instructions (emulated).

**Note**  
Ideally, the MSAD instruction should be implemented so that overflow results in saturation, not in a wrap behavior. Be aware that overflow behavior is undefined.

Developers must check to make sure that they are running with FEATURE\_LEVEL\_11 or higher on a WDDM 1.2 or later driver to use this feature. Developers must not rely on result accuracy for accumulation values that overflow (that is, go above 65535).

 

## <span id="tir"></span><span id="TIR"></span>Target-independent rasterization (TIR)


Target-independent rasterization (TIR) provides a high performance anti-aliasing path for Direct2D usage scenarios that involve high-quality anti-aliasing of structured graphics. TIR enables Direct2D to move the rasterization step from the CPU to the GPU while it preserves the Direct2D anti-aliasing semantics and quality. Using this capability, the software layer can evaluate a large number of sub-pixel sample positions for coverage, yet only allocate the memory that is required for a smaller number of samples. This provides the performance advantage of using the GPU to render but retaining the image quality of a CPU-rendered implementation. This allows a single sample to be broadcast to multiple samples of a multi-sample anti-aliased render target.

### <span id="SampleCount__1__Limited_TIR_on_10__10.1___11_"></span><span id="samplecount__1__limited_tir_on_10__10.1___11_"></span><span id="SAMPLECOUNT__1__LIMITED_TIR_ON_10__10.1___11_"></span>SampleCount =1 (Limited TIR on 10, 10.1 & 11)

Direct3D 10.0 - Direct3D 11.0 hardware (and Feature Level 10\_0 - 11\_0) supports ForcedSampleCount set to 1 (and any sample count for Render Target View) along with the described limitations (for example, no depth/stencil).

For 10\_0, 10\_1 and 11\_0 hardware, when [**D3D11\_1\_DDI\_RASTERIZER\_DESC**](https://msdn.microsoft.com/library/windows/hardware/hh451052).**ForcedSampleCount** is set to 1, line rendering cannot be configured to 2-triangle (quadrilateral)-based mode (that is, the **MultisampleEnable** state cannot be set to true). This limitation isn't present for 11\_1 hardware. Note that the naming of the **MultisampleEnable** state is misleading because it no longer has anything to do with enabling multisampling; instead, it is now one of the controls together with **AntialiasedLineEnable** for selecting line-rendering mode.

This limited form of target-independent rasterization, with **ForcedSampleCount** = 1, closely matches a mode that was present in Direct3D 10.0, but became unavailable for Direct3D 10.1 and Direct3D (and Feature Levels 10\_1 and 11\_0) due to API changes. In Direct3D 10.0, this mode was the center-sampled rendering even on a Multiple Sample Anti Aliasing (MSAA) surface that was available when **MultisampleEnable** was set to false (and this could be toggled by toggling **MultisampleEnable**). In Direct3D 10.1+, **MultisampleEnable** no longer affects multisampling (despite the name), and only controls line-rendering behavior.

## <span id="noow"></span><span id="NOOW"></span>No overwrite and discard


### <span id="Rendering_content_on_a_tile-based_deferred-rendering__TBDR__architecture"></span><span id="rendering_content_on_a_tile-based_deferred-rendering__tbdr__architecture"></span><span id="RENDERING_CONTENT_ON_A_TILE-BASED_DEFERRED-RENDERING__TBDR__ARCHITECTURE"></span>Rendering content on a tile-based deferred-rendering (TBDR) architecture

Render targets in Direct3D 11.1 can now support a discard behavior by using a new set of resource APIs. Developers must be aware of this capability and call an additional Discard() method to run more efficiently on TBDR architectures (with no penalty to traditional graphics hardware). This will improve performance on mobile platforms and other power-constrained devices that use tiled renderers.

### <span id="Updating_resources_on_a_TBDR_architecture"></span><span id="updating_resources_on_a_tbdr_architecture"></span><span id="UPDATING_RESOURCES_ON_A_TBDR_ARCHITECTURE"></span>Updating resources on a TBDR architecture

Because TBDR architectures complete multiple passes over the same command buffer, you must use special care to notify the driver when a portion of a sub-resource was not modified during a previous draw call. Having a NO\_OVERWRITE usage on a Direct3D**UpdateSubResource** function can help the driver to manage resources where no previous draw calls were made to a region of a texture. This simply requires that you inform the driver of the application's intent of either discarding the existing data, or protecting it from overwrite. This enables more efficient rendering on TBDR architectures and introduces no penalties when it is run on traditional desktop hardware.

New variants of the Direct3D 11 UpdateSubresource() and CopySubresourceRegions APIs, which both update a portion of a GPU surface, provide an addition Flags field where NO\_OVERWRITE or DISCARD can be specified.

These APIs drive the Direct3D 11.1 device driver interface (DDI) and Direct3D 9 DDIs. New drivers for any DirectX 9+ hardware are required to support revised BLT, BUFBLT, VOLBLT, and TEXBLT DDIs by adding the flags discussed here.

These are also required to be supported for all Direct3D 10+ hardware with Direct3D 11.1 drivers.

## <span id="uav"></span><span id="UAV"></span>UAVs at every stage


In Microsoft Direct3D 11, the number of unordered-access views (UAVs) was limited to eight at the Compute Shader and to eight combined (render target views (RTVs) + UAVs) at the Pixel Shader. In DirectX 11.1, the number that can be bound has been increased. For DirectCompute, the limit is now 64, and for graphics the combined total bound at the output merger is 64 (that is, graphics can have 64 minus the up-to-eight that are potentially used by RTVs).

Unordered access views can be accessed from any shader stage, but still come out of the total for the graphics pipeline

Adding UAVs at every shader stage allows you to add debugging information to the pipeline. This ease of development makes Windows a more desirable platform for writing GPU-accelerated applications.

This requires at least a DirectX 11.1 feature level.

## <span id="stereo"></span><span id="STEREO"></span>Cross-process sharing of texture arrays (for supporting Stereoscopic 3-D)


Although Stereoscopic 3-D is an optional WDDM 1.2 system feature, there is underlying infrastructure that must be implemented by all WDDM 1.2 device drivers regardless of whether they support the Stereoscopic 3-D system feature.

DirectX 10 (or greater)-capable graphics hardware must support cross-process sharing of texture arrays. This capability provides a basis to enable Stereoscopic 3-D. The WDDM 1.2 Direct3D DDIs require support of arrayed buffers as render targets independent of hardware feature level.

This requirement ensures that stereo applications won't have failures in mono modes. For example: even for cases when stereo is not enabled on the system, applications should be able to create stereo swap chains or arrayed buffers as render targets and then call **Present**. In this case, only the left view is displayed (or if the *prefer right* Microsoft DirectX Graphics Infrastructure (DXGI) present flag is set, only the right view).

Therefore, WDDM 1.2 drivers (Full Graphics & Render devices) must support Direct3D 11 APIs by adding support for cross process sharing of texture arrays. In earlier versions, cross-process shared resources could be only single-layer surfaces. In Windows 8, the maximum size of a shared array is two elements (which is sufficient for stereo). For more information on this requirement, see **Device.Graphics ¦ Stereoscopic3DArraySupport** in [Windows Hardware Certification Requirements](http://go.microsoft.com/fwlink/p/?linkid=324537). Other relevant Microsoft WindowsWindowsWindows HCK requirements are **Device.Graphics ¦ ProcessingStereoscopicVideoContent** and **Device.Display.Monitor.Stereoscopic3DModes**.

## <span id="unordered"></span><span id="UNORDERED"></span>UAVs with multi-sample anti-alias sample access


Direct3D 11 allows rasterization to unordered access views (UAVs) with no render target views (RTVs)/DSVs bound. Even though UAVs can have arbitrary sizes, the implementation can operate the rasterizer by using the pixel dimensions of the viewport/scissor rectangle. The sample pattern for DirectX 11 hardware is single sample only. The DirectX 11.1 hardware specification expands to allow multiple samples. This is a variation of target-independent rasterization where only UAVs are bound for output.

UAV-only rendering together with multisampling at the rasterizer is now possible by keying off the ForcedSampleCount state, with the sample patterns limited to 0, 1, 4, and 8 (not 16, which TIR supports). (The UAVs themselves are not multi-sampled in terms of allocation.) A setting of 0 is equivalent to the setting 1 - single sample rasterization.

Shaders can request pixel-frequency invocation with UAV-only rendering. However, requesting sample-frequency invocation is invalid (produces undefined shading results). The SampleMask rasterizer state does not affect rasterization behavior here at all.

Support for this feature is available on DirectX 11.0+ hardware, including hardware that does not support full 11\_1 level of target-independent rasterization with RTVs. The driver can report that it supports UAV-only multi-sample anti-alias sample access (MSAA) rendering (implying 4 and 8 samples are both supported). All DirectX 11+ hardware supports 1. If the hardware can perform full 11\_1 target-independent rasterization with RTVs (which requires 16-sample support), then UAV-only MSAA rasterization support is required (meaning 4 and 8 samples in the UAV-only case).

This feature enables applications to implement high quality rendering algorithms such as analytic anti-aliasing without needing to allocate memory for large numbers of samples.

## <span id="logicops"></span><span id="LOGICOPS"></span>Logic operations


Allowing for logic operations at the output merger allows you to perform some operations on images that are currently not possible. For example, you can compute masks much more effectively and easily and also implement modern deferred-shading techniques for 3-D rendering.

Although this functionality exists in most 3-D hardware, it is not currently as general as the color blending is. As a result, the configuration of logic ops is constrained in the following ways:

-   When logic ops are used in the first RT blend desc, IndependentBlendEnable must be set to false, so that the same logic op applies to all RTs.
-   When logic ops are used, all RenderTargets bound must have a UINT or SINT format, otherwise the rendering is undefined.

## <span id="buffers"></span><span id="BUFFERS"></span>Improved control of constant buffers


### <span id="partialbuffer"></span><span id="PARTIALBUFFER"></span>Partial constant buffer updates

Constant buffers today require monolithic copies from source to destination during updates that clobber the entire buffer. Where it's desired to update only a portion of the constant buffer, an offset for the writes is ideal. This ability to random-access write into a constant buffer is requested by game developers and makes constant buffer management more natural and efficient. These capabilities were already supported for other buffer types, and are added to constant buffers in WDDM 1.2 drivers.

This feature must be supported for all Direct3D 10+ hardware with Direct3D 11.1 drivers. For the developer, this is emulated on DirectX 9 hardware so it works on all feature levels.

**Note**  
You must specify either the NO\_OVERWRITE or DISCARD flag.

 

### <span id="Offsetting_constant_buffer_updates"></span><span id="offsetting_constant_buffer_updates"></span><span id="OFFSETTING_CONSTANT_BUFFER_UPDATES"></span>Offsetting constant buffer updates

A common desire for high-performance game engines is to collect a large batch of constant buffer updates for constants to be referenced by separate **Draw\\*** calls, each needing its own constants, all at once. This is facilitated by allowing the application to create a large buffer and then pointing individual shaders to regions within it (similar to a view, but without having to make a whole object to describe the view).

Constant buffers now can be created that have a size larger than the maximum constant buffer size addressable by an individual shader (at most 4096 16-byte elements - 65kB, where each element is one four-component shader constant). The constant buffer resource size is now limited only by the size of memory allocation that the system is capable of handling.

When a constant buffer larger than 4096 elements is bound to the pipeline by using **\*SetShaderConstants**APIs such as **VSSetShaderConstants**, it appears to the shader as if it is only 4096 elements in size.

A variant of the **\*SetShaderConstants**APIs, **\*SetShaderConstants1**, allows a "FirstConstant" and "ConstantCount" to be specified together with the binding. When the shader accesses a constant buffer bound this way, it appears as if it starts at the specified "FirstConstant" offset (where 1 means 16 bytes) and has a size defined by ConstantCount (number of 16-byte constants). This is basically a lightweight "View" of a region of a larger constant buffer. (Both FirstConstant and ConstantCount must be a multiple of 16).

This feature must be supported by all WDDM 1.2 drivers for Direct3D 10+ hardware. The Direct3D 11 runtime emulates the appropriate behavior for Feature Level 9\_x.

## <span id="clearview"></span><span id="CLEARVIEW"></span>Clearview


This feature enables the implementation to perform an efficient clear operation on a video memory resource, clearing multiple rects in a single API/DDI call. The API includes support for rectangles that define a subset of the resource to be cleared. This capability was supported in the DirectX 9 DDI, and is required for Windows 8 drivers (WDDM 1.2). This approach results in improved performance for 2-D operations such as those used in imaging and UI.

## <span id="cpyflag"></span><span id="CPYFLAG"></span>Tileable copy flag


A tileable copy operation allows an application to notify the implementation that the image source and destination are pixel-aligned and will not participate in cross-pixel exchange of information in a subsequent rendering pass. This enables significant performance improvements on some implementations that benefit from caching subsets of the image data during the copy operation. This capability was supported in the DirectX 9 DDI, and is required for Windows 8 and later drivers (WDDM 1.2).

## <span id="blits"></span><span id="BLITS"></span>Same-surface blits


Many UI operations, such as scrolling, require transferring image data from one portion of an image to another. This feature adds support for a copy operation where both source rectangle and destination rectangle are in the same image or resource. In the case of overlapping source and destination rectangles, the situation must be handled correctly by the implementation and driver. This was already required by the DirectX 9 DDI and is required in WDDM 1.2 for all hardware. This approach results in significant performance improvements of key UI scenarios.

## <span id="direct3d_11.1_ddi"></span><span id="DIRECT3D_11.1_DDI"></span>Direct3D 11.1 DDI


These functions and structures are new or updated for Windows 8:

-   [*AssignDebugBinary*](https://msdn.microsoft.com/library/windows/hardware/hh406234)
-   [*CalcPrivateBlendStateSize(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh406237)
-   [*ClearView*](https://msdn.microsoft.com/library/windows/hardware/hh406255)
-   [*DefaultConstantBufferUpdateSubresourceUP(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh802464)
-   [*ResourceUpdateSubresourceUP(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh439847)
-   [*VsSetConstantBuffers(D3D11\_1)*](https://msdn.microsoft.com/library/windows/hardware/hh439921)
-   [**D3D11\_1DDI\_D3D11\_OPTIONS\_DATA**](https://msdn.microsoft.com/library/windows/hardware/hh406442)
-   [**D3DDDI\_BLTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544379)
-   [**D3DDDI\_COPY\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh451175)
-   [**D3DDDIARG\_BUFFERBLT1**](https://msdn.microsoft.com/library/windows/hardware/hh451069)
-   [**D3DDDIARG\_DISCARD**](https://msdn.microsoft.com/library/windows/hardware/hh451076)
-   [**D3DDDIARG\_TEXBLT1**](https://msdn.microsoft.com/library/windows/hardware/hh451142)
-   [**D3DDDIARG\_VOLUMEBLT1**](https://msdn.microsoft.com/library/windows/hardware/hh451145)
-   [**D3DDDICAPS\_ARCHITECTURE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451150)
-   [**D3DDDICAPS\_SHADER\_MIN\_PRECISION**](https://msdn.microsoft.com/library/windows/hardware/hh451152)
-   [**D3DDDICAPS\_SHADER\_MIN\_PRECISION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/hh451154)
-   [**D3DDDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff544132)

 

 





