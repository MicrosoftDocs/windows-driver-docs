---
title: PCL XL Issues
description: PCL XL Issues
ms.assetid: 65db50fb-b58f-44f0-aa2a-67c23a448d32
keywords: ["PCL XL vector graphics WDK Unidrv , additional considerations"]
---

# PCL XL Issues


## <a href="" id="ddk-pcl-xl-issues-gg"></a>


-   Windows XP and later supports print optimization functionality on the **Advanced** tab of the printer property pages. If **Print Optimizations** are disabled, Unidrv prints PCL XL data in raster mode.

-   \*MirrorRasterPage? is not supported in PCL XL mode.

-   PCL XL does not support switching between PCL XL and raster modes.

-   The GPD \*TextHalftoneThreshold attribute name is not supported on a PCL XL minidriver. Text in any resolution is grayscaled in PCL XL mode.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PCL%20XL%20Issues%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




