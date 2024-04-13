---
title: Reporting DirectX 8.0 Style Direct3D Capabilities
description: Reporting DirectX 8.0 Style Direct3D Capabilities
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities
- D3DCAPS8
ms.date: 04/20/2017
---

# Reporting DirectX 8.0 Style Direct3D Capabilities


## <span id="ddk_reporting_directx_8_0_style_direct3d_capabilities_gg"></span><span id="DDK_REPORTING_DIRECTX_8_0_STYLE_DIRECT3D_CAPABILITIES_GG"></span>


In response to a **GetDriverInfo2** query with type D3DGDI2\_TYPE\_GETD3DCAPS8, the driver should copy an initialized D3DCAPS8 structure into the **lpvData** field of the [**DD\_GETDRIVERINFODATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverinfodata) structure. This structure is new for DirectX 8.0 and is used for both reporting capabilities from the driver to runtime and from the runtime to the application.

D3DCAPS8 has fields that describe both capabilities new to DirectX 8.0 and capabilities carried forward from DirectX 7.0. D3DCAPS8 is not a complete replacement for existing capabilities. Although this structure (along with information of supported surface formats) is a complete description of the device's capabilities from an API perspective, it is not sufficient for the DDI. The runtime makes use of the DirectDraw capabilities reported by the driver for such information as supported surface capabilities (DDSCAPS) even though these are not exposed directly through the DirectX 8.0 API.

Furthermore, the driver is required to continue to report legacy capability structures (such as [**D3DHAL\_D3DEXTENDEDCAPS**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_d3dextendedcaps)) as applications using legacy interfaces (DirectX 7.0 and earlier) continue to request these capabilities. Therefore, reporting DirectX 8.0 style caps through D3DCAPS8 is an additional requirement, rather than a replacement for the existing capability reporting mechanisms. When DirectX 8.0 interfaces are used by the application the runtime does not query for extended D3D capabilities such as D3DHAL\_D3DEXTENDEDCAPS if the driver reports DirectX 8.0 capabilities with D3DCAPS8.

D3DCAPS8 is described in the DirectX 8.0 SDK documentation. The driver should not initialize the **DeviceType** or **AdapterOrdinal** fields. These are initialized to appropriate values by the runtime. The driver should set these fields to zero.

 

