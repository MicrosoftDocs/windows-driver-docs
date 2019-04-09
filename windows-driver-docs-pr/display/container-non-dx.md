---
title: Container Support for non-DX APIs
description: Non-DX APIs must interact with drivers and kernel more directly, so they are exposed to more complications
ms.assetid: 6c4a6974-c67b-4710-80c6-48a5b378e088
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container Support for non-DX APIs

Windows 10 added several features that significantly impact non-DX APIs,
and the lower-level WDDM architectural details they rely on.
1. Paravirtualized WDDM adapters 
2. Users now have control over the adapter used by applications that don't discriminate themselves
3. [Universal drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-universal-drivers) introduces a new set of design principals

Maintaining compatibility with the latest Windows 10 features requires the following modifications:

The registry and driver store must be accessed indirectly through
[D3DKMTQueryAdapterInfo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtqueryadapterinfo)
with 
[KMTQAITYPE_QUERYREGISTRY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype),
and [D3DDDI_QUERYREGISTRY_INFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dukmdt/ns-d3dukmdt-_d3dddi_queryregistry_info).

The default adapter must honor the user's choice, which requires:
1. Enumerating adapters through DXGI's [IDXGIFactory::EnumAdapters](https://docs.microsoft.com/windows/desktop/api/dxgi/nf-dxgi-idxgifactory-enumadapters),
as DXGI honors the user's choice. 
Adapter 0 changes based on the [user's settings](https://blogs.windows.com/windowsexperience/2018/02/07/announcing-windows-10-insider-preview-build-17093-pc/).
2. Match the adapter order gotten through [D3DKMTEnumAdapters2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtenumadapters2) to DXGI's.
Adapter identities can be matched up by correlating the LUID between both enumeration techniques.
DXGI returns its LUID through [IDXGIAdapter::GetDesc](https://docs.microsoft.com/windows/desktop/api/dxgi/nf-dxgi-idxgiadapter-getdesc).

Honor as many universal driver design principals as possible, which may vary based on the exact device being supported.
