---
title: Supporting Cross-Adapter Resource Scan-Out
description: A WDDM 2.9 driver can support cross-adapter resource scan-out, reducing the number of copies between GPUs and cross-adapter resources from two to one.
ms.date: 12/06/2023
---

# Supporting cross-adapter resource scan-out (CASO)

## Pre-CASO performance (two-copy path)

Starting in Windows 8.1 (WDDM 1.3), D3D9 and DXGI applications were able to use cross-adapter presentation support on multi-adapter configurations such as [hybrid systems](using-cross-adapter-resources-in-a-hybrid-system.md). With this support, the rendering is done on a render adapter (typically the discrete GPU), and then two copies are done to get the contents to the display adapter (typically the integrated GPU) for scanning-out to the display.

* Copy 1 is from the render adapter resource to a cross-adapter resource.
* Copy 2 is from the cross-adapter resource to the display adapter resource.

These copies can limit the performance of apps, especially for apps optimized for low-latency.

## Using CASO to optimize flip presentation model (one-copy path)

Windows Server 2022 (WDDM 2.9) and later drivers can declare support for an appropriate cross-adapter resource tier, allowing the system's presentation stack to optimize cross-adapter presents. Drivers must declare support for this feature based on their own adapter capability, regardless of device configuration, such that the feature value scales across all applicable hardware configurations. This scaling includes, but isn't limited to, a single GPU device with dynamic attaching of other external GPUs.

If the display adapter supports CASO, the system only does the first copy from the render adapter surface to the cross-adapter surface, and then scans out from the cross-adapter surface directly. This feature results in reduced processing, bandwidth, power, and latency.

The CASO feature is implemented for the DXGI runtime for the flip presentation model.

## DDI changes and additions for CASO

### Indicating tier support for cross-adapter resources

DXGI implements three tiers of support for cross-adapter resources:

1. Copying to and from cross-adapter resources (lowest tier)
2. Texturing from cross-adapter resources
3. Scan-out of cross-adapter resources (highest tier)

Each higher tier of support must guarantee the support of the tier(s) below it. For example, to claim support for scan-out of cross-adapter resources, the driver must also support texturing and copy.

Drivers declare support for each tier by setting the following [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) bit field values in [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps).**MemoryManagementCaps**:

| Tier   | Tier Meaning | DXGK_VIDMMCAPS Value |
| ----   | ------------ | -------------------- |
| Tier 1 | Copy support: Copy to and from cross-adapter resources | **CrossAdapterResource** (Exposed to user mode by graphics kernel via the **SupportCrossAdapterResource** bit in [**D3DKMT_WDDM_1_3_CAPS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmt_wddm_1_3_caps) |
| Tier 2 | Texture support: Texture from cross-adapter resources) |  **CrossAdapterResourceTexture** (includes support for shader resource view, unordered access view, and render target) |
| Tier 3 | CASO support: Scan-out from cross-adapter resources  | **CrossAdapterResourceScanout** |

The graphics kernel fails the adapter start if it doesn't indicate support in a superset manner for the three tiers. For example, **CrossAdapterResource** must be set if **CrossAdapterResourceTexture** is set.

#### Tier 1 support requirements

Cross-adapter resources are still defined the same, as used for [WDDM 1.3 tier 1 copy support](using-cross-adapter-resources-in-a-hybrid-system.md).

#### Tier 2 support requirements

The requirements are similar to the D3D12 user-mode driver [**CrossAdapterRowMajorTextureSupported**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options) capability (cap); that is, the device supports shader resource views, unordered access views, and render target views of cross-adapter row-major textures. However, while D3D12's **CrossAdapterRowMajorTextureSupported** requires support of all relevant texture formats, this tier 2 cap only requires support on the **DisplayScanOut** formats listed in *Tier 3 support requirements*, at minimum.

Since D3D12's cap is a superset of this tier 2 cap, [**D3D12CreateDevice**](/windows/win32/api/d3d12/nf-d3d12-d3d12createdevice) also verifies that the kernel driver's **CrossAdapterResourceTexture** cap is set if its **CrossAdapterRowMajorTextureSupported** cap is set, and fails the device creation if it isn't.

#### Tier 3 support requirements

The system must be able to perform the supported flipping capabilities, as declared by the driver in [**DXGK_FLIPCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_flipcaps), for cross-adapter resources of the following minimum specifications:

* A cross-adapter primary buffer size of 1920 x 1080 or smaller
* A buffer pixel format of any of the supported **DisplayScanOut** formats. As of Windows 10 version 20H1, these formats are:
  * DXGI_FORMAT_R16G16B16A16_FLOAT
  * DXGI_FORMAT_R10G10B10A2_UNORM
  * DXGI_FORMAT_R8G8B8A8_UNORM
  * DXGI_FORMAT_R8G8B8A8_UNORM_SRGB
  * DXGI_FORMAT_B8G8R8A8_UNORM
  * DXGI_FORMAT_B8G8R8A8_UNORM_SRGB

If the driver supports scanning out cross-adapter resources of more texture formats, then it must also support texturing from those formats, per the tier support requirements.

>[!NOTE]
> The DXGI runtime queries the driver for its **CrossAdapterResourceScanout** support. If supported, the presentation stack goes down the one-copy path. Therefore, drivers that declare support for **CrossAdapterResourceScanout** are required to support the [**DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) DDI. In addition, it must also support all the relevant presentation-related DDIs for cross-adapter primaries of the above minimum specifications. A few examples are: [**pfnCreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource2), [**pfnCheckMultiplaneOverlaySupport**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3), and [**pfnPresentMultiplaneOverlay**](/windows-hardware/drivers/ddi/d3dkmthk/nc-d3dkmthk-pfnd3dkmt_presentmultiplaneoverlay)/[**pfnPresent1**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_present1). For more information, see [Multiplane overlay support](./multiplane-overlay-support.md). For more information about falling out of CASO, see [*Driver DDIs for presentation optimization*](#driver-ddis-for-presentation-optimization).

Both of these tiers have accompanying [HLK tests](#hlk-testing) for verification.

### Supporting StaticCheck flag for DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3

The **StaticCheck** flag was added to [**DXGK_MULTIPLANE_OVERLAY_FLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_multiplane_overlay_flags) in WDDM 3.0. This flag expands the use of the [**DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) DDI for CASO support. This flag allows **DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3** to query a driver to determine whether the plane marked with the **StaticCheck** flag is capable of scan-out. This call is a one-off call and shouldn't affect real presentation behavior. Hence, drivers that perform any caching of present information from **DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3** shouldn't include the information from DDI calls with a **StaticCheck** plane. They should just perform the support determination in a standalone or static manner.

[**DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) with the **StaticCheck** flag set is guaranteed to:

* Have exactly one plane marked with the flag
* Not contain any *PostComposition* plane information

A call to [**DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) with the **StaticCheck** flag set is used from the app process from DXGI during buffer creation, such as during swapchain creation or ResizeBuffers, as a best effort attempt to determine whether CASO is supported for the current hardware configuration.
  
### HybridIntegrated special case

It's important to note that [**HybridIntegrated**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_adaptertype) drivers are designed to have tier 3 scan-out support. Starting in WDDM 3.0, **HybridIntegrated** drivers are required to declare support for **CrossAdapterResourceScanout**. An HLK test verifies this requirement.

Existing hybrid caps might be considered for deprecation in the future. Therefore, it's key that the **CrossAdapterResourceScanout** cap is decoupled to allow for greater flexibility to evolve in this space going forward. Hence, even drivers that aren't **HybridIntegrated** can set the cross-adapter support tier as appropriate.

## Graphics Kernel changes

Starting in WDDM 2.9, the following additions/changes were made for cross-adapter resource support:

* The **KMTQAITYPE_CROSSADAPTERRESOURCE_SUPPORT** value was added to the existing [**KMTQUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype) enum

* The [**D3DKMT_CROSSADAPTERRESOURCE_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-d3dkmt_crossadapterresource_support) structure and [**D3DKMT_CROSSADAPTERRESOURCE_SUPPORT_TIER**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-d3dkmt_crossadapterresource_support_tier) enumeration were added

Sample usage:

``` cpp
D3DKMT_CROSSADAPTERRESOURCE_SUPPORT KernelSupport = {};
D3DKMT_QUERYADAPTERINFO QueryAdapterInfo;
QueryAdapterInfo.hAdapter = m_hAdapter;
QueryAdapterInfo.Type = KMTQAITYPE_CROSSADAPTERRESOURCE_SUPPORT;
QueryAdapterInfo.pPrivateDriverData = &KernelSupport;
QueryAdapterInfo.PrivateDriverDataSize = sizeof( KernelSupport );
VERIFY_SUCCEEDED(D3DKMTQueryAdapterInfo(&QueryAdapterInfo));

// Use KernelSupport.SupportTier as appropriate
```

### Driver DDIs for presentation optimization

Drivers use the following DDIs to indicate whether cross-adapter scan-out is supported:

* [**DXGK_VIDMMCAPS::CrossAdapterResourceScanout**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) cap

   The system queries this cap early to determine if the driver supports the CASO capability.

   If the driver supports CASO, DXGI continues with the one-copy CASO path; otherwise, DXGI falls back to the two-copy path.

* [**pfnCreateResource**](/en-us/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) DDI

   On the one-copy CASO path, DXGI creates the cross-adapter resource as primary on the display adapter, via **pfnCreateResource**. The driver should evaluate based on the resource properties whether it can scan out from that resource.

   If the driver supports scan-out based on the resource properties, DXGI continues with the one-copy CASO path. Otherwise, the driver should opt out of scan-outs by returning **DXGI_DDI_PRIMARY_DRIVER_FLAG_NO_SCANOUT**. In this case, DXGI falls back to the two-copy path. This fallback should happen only if the resource properties are beyond the minimum requirements as listed in [Tier 3 support requirements](#tier-3-support-requirements).

* [**pfnCheckMultiplaneOverlaySupport**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) DDI

   Per current behavior, the Desktop Windows Manager (DWM) calls the display driver's **pfnCheckMultiplaneOverlaySupport** DDI to accurately determine whether the primary surface can be scanned out. If supported by the driver, the scan-out occurs. Otherwise, DWM falls back to DWM composition mode.

   Note that DWM-composed presents are likely to be less desirable than [Independent Flip](/windows/win32/direct3ddxgi/for-best-performance--use-dxgi-flip-model#directflip) (iFlip) via the two-copy path or iFlip via the one-copy CASO path. Hence, there might be common display scenarios where presentation bandwidth is limited, such as rotated or multiple displays, where drivers might consistently fail **pfnCheckMultiplaneOverlaySupport** support in DWM, likely resulting in a poorer experience than the two-copy path.

   To mitigate the negative fallback experience, DXGI calls **pfnCheckMultiplaneOverlaySupport** during buffer creation with the cross-adapter resource as a plane marked with the **StaticCheck** flag, to verify with high accuracy whether the driver can perform scan-out given the existing known bandwidth characteristics. If supported, DXGI continues with the one-copy CASO path; otherwise, it falls back to the two-copy path.

## HLK Testing

A WDDM 3.0 HLK requirement and feature, with its corresponding HLK tests, were added. This requirement is tied to the [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) support that drivers can declare; specifically, **CrossAdapterResourceTexture** and **CrossAdapterResourceScanout**.

### CrossAdapterResourceTexture

An HLK test was added to verify shader resource view (SRV) operations on cross-adapter resources.

* For D3D12, the existing HLK "D3D12 - Cross Adapter Resource DX12" for Device.Graphics.AdapterRender.D3D12Core.CoreRequirement test was added to; specifically, the CrossAdapterResource::CrossAdapterTextureSRV test case.

  Added to this HLK test case is verification of the superset relationship between the **CrossAdapterResourceTexture** KMD cap and D3D12 UMD **CrossAdapterRowMajorTextureSupported** cap. Similarly, logic was added in [**D3D12CreateDevice**](/windows/win32/api/d3d12/nf-d3d12-d3d12createdevice) to ensure that if its UMD cap is set, then the kernel tier 2 driver cap must be set too, and fail the device creation if it doesn't.

* For D3D11, the above test case was added to the HLK test for Device.Graphics.WDDM30.Render.CrossAdapterScanOut; specifically, D3DConf_11_CrossAdapterResource::CrossAdapterResourceSRV.

### Cross-Adapter Resource Scan-out

The following HLK tests were added:

* Device.Graphics.WDDM30.Render.CrossAdapterScanOut
  * An HLK test to verify that drivers can create cross-adapter primary resources successfully without opting out of scan-out behavior via the **DXGI_DDI_PRIMARY_DRIVER_FLAG_NO_SCANOUT** flag.
  * An HLK test to verify that these drivers support the **DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3** DDI.
  * A manual HLK test for a tester to manually verify that:
    * The scanned out cross-adapter surface is free of visual corruption/artifacts or unexpected tearing
    * The cross-adapter surface is directly scanned out without any prior internal transformations or copies.

  These end-to-end tests also naturally verify that the **CheckMultiplaneOverlaySupport** and Present DDIs are supported for cross-adapter resources. The manual test app has some specific hardware requirements such as a high resolution and high refresh rate monitor. For more information, see the [reference document](/windows-hardware/test/hlk/testref/cf519014-522c-49ff-8d70-4b304a00d61b) accompanying the test.

* Device.Graphics.WDDM30.Render.CoreRequirement
  * An HLK test to verify that drivers that declare **HybridIntegrated** cap also declare the **CrossAdapterResourceScanout** cap.
* System.Fundamentals.Graphics.HybridGraphics.MultiGPU
  * A system-based HLK test to enable OEMs to run these tests on their hybrid devices capable of exercising DXGI's one-copy path as part of end-to-end system validation.
