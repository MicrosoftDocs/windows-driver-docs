---
title: W-Buffering DDI
description: W-Buffering DDI
ms.assetid: eb1270c3-0eaa-47a4-8fc6-53aea981b597
keywords:
- Direct3D WDK Windows 2000 display , w-buffering
- w-buffering WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# W-Buffering DDI


## <span id="ddk_w_buffering_ddi_gg"></span><span id="DDK_W_BUFFERING_DDI_GG"></span>


The driver supports w-buffering by enabling the D3DPRASTERCAPS\_WBUFFER cap in the **dwRasterCaps** member of the [**D3DPRIMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549034) structure. The D3DRENDERSTATE\_ZENABLE render state is passed to the driver to enable or disable w-buffering or z-buffering.

The [**D3DHAL\_DP2VIEWPORTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff545936) structure supports fields that correspond to world-space front and back clip planes (hither and yon respectively). This information can be used to adjust fog tables as well.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20W-Buffering%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




