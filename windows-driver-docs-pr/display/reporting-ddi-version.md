---
title: Reporting DDI Version
description: Reporting DDI Version
ms.assetid: f539a4b4-4652-4e40-928d-d90a3dd1988d
keywords:
- version numbers WDK DirectX 9.0
- reporting DDI version WDK DirectX 9.0
- DDI version WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting DDI Version


## <span id="ddk_reporting_ddi_version_gg"></span><span id="DDK_REPORTING_DDI_VERSION_GG"></span>


A DirectX 9.0 version driver must report the version of the [DDI](direct3d-driver-ddi.md) that it supports so that the DirectX 9.0 runtime can determine how to handle the driver. To report the DDI version, the driver responds to a **GetDriverInfo2** request that uses the D3DGDI2\_TYPE\_GETDDIVERSION value. The **dwDXVersion** member of the [**DD\_GETDDIVERSIONDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551545) structure is set to 9 to indicate that the DirectX 9.0 runtime makes the request.

The driver sets the **dwDDIVersion** member of DD\_GETDDIVERSIONDATA to the DDI version that it supports for the DirectX 9.0 runtime. If the driver was built with a prereleased version of the DirectX 9.0 Driver Development Kit (DDK) in which the DDI version number was lower than the number in the final version of DirectX 9.0, the runtime treats the driver as DirectX 8.0 instead.

 

 





