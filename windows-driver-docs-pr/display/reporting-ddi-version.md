---
title: Reporting DDI Version
description: Reporting DDI Version
ms.assetid: f539a4b4-4652-4e40-928d-d90a3dd1988d
keywords: ["version numbers WDK DirectX 9.0", "reporting DDI version WDK DirectX 9.0", "DDI version WDK DirectX 9.0"]
---

# Reporting DDI Version


## <span id="ddk_reporting_ddi_version_gg"></span><span id="DDK_REPORTING_DDI_VERSION_GG"></span>


A DirectX 9.0 version driver must report the version of the [DDI](direct3d-driver-ddi.md) that it supports so that the DirectX 9.0 runtime can determine how to handle the driver. To report the DDI version, the driver responds to a **GetDriverInfo2** request that uses the D3DGDI2\_TYPE\_GETDDIVERSION value. The **dwDXVersion** member of the [**DD\_GETDDIVERSIONDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551545) structure is set to 9 to indicate that the DirectX 9.0 runtime makes the request.

The driver sets the **dwDDIVersion** member of DD\_GETDDIVERSIONDATA to the DDI version that it supports for the DirectX 9.0 runtime. If the driver was built with a prereleased version of the DirectX 9.0 Driver Development Kit (DDK) in which the DDI version number was lower than the number in the final version of DirectX 9.0, the runtime treats the driver as DirectX 8.0 instead.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20DDI%20Version%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




