---
title: Compressing Raster Data
description: Compressing Raster Data
ms.assetid: 8c74e7f3-5601-4510-9fcd-261f5cd48e9c
keywords: ["Unidrv, raster data compression", "GPD files WDK Unidrv , raster data compression", "raster data compression WDK Unidrv", "compressing raster data WDK Unidrv", "Unidrv WDK print"]
---

# Compressing Raster Data


## <a href="" id="ddk-compressing-raster-data-gg"></a>


Unidrv supports raster data compression using the following three formats:

-   Tagged Image File Format (TIFF), version 4.0

-   Delta-Row Compression (DRC)

-   East Asian Run-Length Encoding (FE-RLE)

These methods are defined in the *HP PCL 5 Printer Language Technical Reference*. (This resource may not be available in some languages and countries.)

You can include entries in a GPD file to indicate which of these compression formats your printer supports. You can also provide your own compression algorithm.

For more information about raster data compression, see the following topics:

[Using Unidrv-Supported Compression](using-unidrv-supported-compression.md)

[Using Customized Compression](using-customized-compression.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Compressing%20Raster%20Data%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




