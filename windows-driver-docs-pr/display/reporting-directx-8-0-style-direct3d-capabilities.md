---
title: Reporting DirectX 8.0 Style Direct3D Capabilities
description: Reporting DirectX 8.0 Style Direct3D Capabilities
ms.assetid: a03a7cbc-95be-4251-8e3a-bef4a093f03d
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities", "D3DCAPS8"]
---

# Reporting DirectX 8.0 Style Direct3D Capabilities


## <span id="ddk_reporting_directx_8_0_style_direct3d_capabilities_gg"></span><span id="DDK_REPORTING_DIRECTX_8_0_STYLE_DIRECT3D_CAPABILITIES_GG"></span>


In response to a **GetDriverInfo2** query with type D3DGDI2\_TYPE\_GETD3DCAPS8, the driver should copy an initialized D3DCAPS8 structure into the **lpvData** field of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure. This structure is new for DirectX 8.0 and is used for both reporting capabilities from the driver to runtime and from the runtime to the application.

D3DCAPS8 has fields that describe both capabilities new to DirectX 8.0 and capabilities carried forward from DirectX 7.0. D3DCAPS8 is not a complete replacement for existing capabilities. Although this structure (along with information of supported surface formats) is a complete description of the device's capabilities from an API perspective, it is not sufficient for the DDI. The runtime makes use of the DirectDraw capabilities reported by the driver for such information as supported surface capabilities (DDSCAPS) even though these are not exposed directly through the DirectX 8.0 API.

Furthermore, the driver is required to continue to report legacy capability structures (such as [**D3DHAL\_D3DEXTENDEDCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544753)) as applications using legacy interfaces (DirectX 7.0 and earlier) continue to request these capabilities. Therefore, reporting DirectX 8.0 style caps through D3DCAPS8 is an additional requirement, rather than a replacement for the existing capability reporting mechanisms. When DirectX 8.0 interfaces are used by the application the runtime does not query for extended D3D capabilities such as D3DHAL\_D3DEXTENDEDCAPS if the driver reports DirectX 8.0 capabilities with D3DCAPS8.

D3DCAPS8 is described in the DirectX 8.0 SDK documentation. The driver should not initialize the **DeviceType** or **AdapterOrdinal** fields. These are initialized to appropriate values by the runtime. The driver should set these fields to zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20DirectX%208.0%20Style%20Direct3D%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




