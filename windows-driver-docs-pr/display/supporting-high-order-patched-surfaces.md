---
title: Supporting High-Order Patched Surfaces
description: Supporting High-Order Patched Surfaces
ms.assetid: 020fb91c-c8cd-43e8-a180-bbb2ef606be8
keywords:
- high-order patched surfaces WDK DirectX 9.0
- displacement mapping WDK DirectX 9.0
- adaptive-tessellation render states WDK DirectX 9.0
- tessellation mapping WDK DirectX 9.0
- patched surfaces WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting High-Order Patched Surfaces


## <span id="ddk_supporting_high_order_patched_surfaces_gg"></span><span id="DDK_SUPPORTING_HIGH_ORDER_PATCHED_SURFACES_GG"></span>


A DirectX 9.0 version driver for a device that supports adaptive tessellation and displacement mapping for high-order patched surfaces must indicate such support with capability bits and be able to process new adaptive-tessellation render states and a displacement-map texture stage state. For more information about adaptive tessellation and displacement mapping, see the latest DirectX SDK.

To indicate support of adaptive tessellation and displacement mapping, the driver sets the following capability bits in the **DevCaps2** member of the D3DCAPS9 structure:

<span id="D3DDEVCAPS2_ADAPTIVETESSRTPATCH"></span><span id="d3ddevcaps2_adaptivetessrtpatch"></span>D3DDEVCAPS2\_ADAPTIVETESSRTPATCH  
Device can adaptively tessellate render-target patches.

<span id="D3DDEVCAPS2_ADAPTIVETESSNPATCH"></span><span id="d3ddevcaps2_adaptivetessnpatch"></span>D3DDEVCAPS2\_ADAPTIVETESSNPATCH  
Device can adaptively tessellate N-patches.

<span id="D3DDEVCAPS2_DMAPNPATCH"></span><span id="d3ddevcaps2_dmapnpatch"></span>D3DDEVCAPS2\_DMAPNPATCH  
Device supports displacement maps for N-patches.

<span id="D3DDEVCAPS2_PRESAMPLEDDMAPNPATCH"></span><span id="d3ddevcaps2_presampleddmapnpatch"></span>D3DDEVCAPS2\_PRESAMPLEDDMAPNPATCH  
Device supports presampled displacement maps for N-patches.

To indicate the maximum number of N-patch subdivisions that the display device can support, the driver sets the **MaxNpatchTessellationLevel** member of the D3DCAPS9 structure to the maximum number. Applications that use presampled displacement mapping are affected by the device clamping to this maximum number.

The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

The driver specifies the D3DFORMAT\_OP\_DMAP flag in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for a particular surface format to mark the format for displacement-map sampling. When a texture surface is created, the Direct3D runtime sets the DDSCAPS3\_DMAP bit of the **dwCaps3** member of the DDSCAPSEX ([**DDSCAPS2**](https://msdn.microsoft.com/library/windows/hardware/ff550292)) structure to indicate that the texture can be sampled in the tessellation unit.

Note that DirectX 9.0 and later drivers must turn off the N-patch feature only when the value of the D3DRS\_PATCHSEGMENTS render state is less than 1.0f. DirectX 8.1 and earlier drivers are not required to behave in this manner.

The following adaptive-tessellation render states along with their default values are new for DirectX 9.0:

D3DRS\_MAXTESSELLATIONLEVEL = 1.0f

D3DRS\_MINTESSELLATIONLEVEL = 1.0f

D3DRS\_ADAPTIVETESS\_X = 0.0f

D3DRS\_ADAPTIVETESS\_Y = 0.0f

D3DRS\_ADAPTIVETESS\_Z = 1.0f

D3DRS\_ADAPTIVETESS\_W = 0.0f

D3DRS\_ENABLEADAPTIVETESSELLATION = **FALSE**

The D3DDMAPSAMPLER sampler, which is also new for DirectX 9.0, is used in the tessellation unit to set a displacement map texture.

**Note**   DirectX 9.0 and later applications can use the D3DSAMP\_DMAPOFFSET value in the D3DSAMPLERSTATETYPE enumeration to control the offset, in vertices, into the presampled displacement map. The runtime maps user-mode sampler states (D3DSAMP\_*Xxx*) to kernel-mode D3DTSS\_*Xxx* values so that DirectX 9.0 and later drivers are not required to process user-mode sampler states. Therefore, drivers must instead process the D3DTSS\_DMAPOFFSET value in the **TSState** member of the [**D3DHAL\_DP2TEXTURESTAGESTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545878) structure for D3DDP2OP\_TEXTURESTAGESTATE operations. For more information about D3DSAMPLERSTATETYPE and presampled displacement mapping, see the latest DirectX SDK documentation.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20High-Order%20Patched%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




