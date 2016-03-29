---
title: Customized Data Stream Compression
description: Customized Data Stream Compression
ms.assetid: 7e42f3c7-c833-49ee-976b-ed32b921af95
keywords: ["Unidrv, data stream compression", "data stream compression WDK Unidrv", "customized data stream compression WDK Unidrv", "compressed data streams WDK Unidrv", "Unidrv WDK print"]
---

# Customized Data Stream Compression


## <a href="" id="ddk-customized-data-stream-compression-gg"></a>


Unidrv allows you to perform data compression operations using customized code. To perform customized compression operations, perform the following steps:

1.  Provide a rendering plug-in that implements the [**IPrintOemUni::Compression**](https://msdn.microsoft.com/library/windows/hardware/ff554224) method.

2.  Include a CmdEnableOEMComp command entry in the printer's [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file.

The IPrintOemUni::Compression method receives scan line data as input. The method must compress the data and then return the result to Unidrv. The **CmdEnableOEMComp** command entry specifies the command that must be sent to the printer so that the printer can accept the compressed data. For each scan line that is to be sent to the printer, Unidrv calls IPrintOemUni::Compression to compress the scan line data. Then, if this is the only compression method available, Unidrv sends to the printer the command specified by the **CmdEnableOEMComp** command entry, followed by the compressed data.

If the printer minidriver contains GPD entries that also enable Unidrv-supported compression methods, Unidrv tries each compression algorithm for each scan line and chooses the algorithm that produces the best result. For more information about Unidrv's compression capabilities, see [Compressing Raster Data](compressing-raster-data.md).

Only one customized compression method can be enabled at one time.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Data%20Stream%20Compression%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




