---
title: Using Customized Compression
author: windows-driver-content
description: Using Customized Compression
MS-HAID:
- 'nt5gpd\_49e5194a-829f-4b56-9531-086390366f44.xml'
- 'print.using\_customized\_compression'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 959c0015-4b31-4790-8d2b-26d6acc19ac7
keywords: ["raster data compression WDK Unidrv", "compressing raster data WDK Unidrv", "customized raster data compression WDK Unidrv"]
---

# Using Customized Compression


## <a href="" id="ddk-using-customized-compression-gg"></a>


If you want to supply a customized compression algorithm, you include a CmdEnableOEMComp command entry to specify the command that enables your algorithm. If your printer can disable compression, you can optionally include a CmdDisableCompression entry to specify the command that disables compression. You must also provide a [rendering plug-in](rendering-plug-ins.md) that implements the [**IPrintOemUni::Compression**](https://msdn.microsoft.com/library/windows/hardware/ff554224) method.

If you provide a customized compression algorithm, you can also enable the use of Unidrv-supported algorithms. For each scan line, Unidrv tries each compression algorithm and chooses the algorithm that produces the most compressed result. (For information about Unidrv-supported algorithms, see [Using Unidrv-Supported Compression](using-unidrv-supported-compression.md).) When Unidrv finds the best algorithm, it compresses the scan line data. Then it sends to the printer the command specified by the appropriate command entry, followed by the compressed data.

For more information about CmdEnableOEMComp and CmdDisableCompression entries, see [Raster Data Compression Commands](raster-data-compression-commands.md).

For more information about customized compression, see [Customized Data Stream Compression](customized-data-stream-compression.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20Customized%20Compression%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


