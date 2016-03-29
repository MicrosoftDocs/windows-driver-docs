---
title: Supporting Vendor-Defined Paper Sizes
description: Supporting Vendor-Defined Paper Sizes
ms.assetid: 5c356857-ef43-41e4-a4ed-fae6655bd9ce
keywords: ["vendor-supplied paper sizes WDK Unidrv", "nonstandard paper sizes WDK Unidrv"]
---

# Supporting Vendor-Defined Paper Sizes


## <a href="" id="ddk-supporting-vendor-defined-paper-sizes-gg"></a>


Vendor-defined paper sizes are vendor-specific and must be fully described by each printer's GPD file. These sizes are also called nonstandard paper sizes, because they are not included in the [standard options](standard-options.md) for the PaperSize feature.

For each vendor-defined paper size that a printer supports, the GPD file's PaperSize feature must include an \*Option entry whose argument is not one of the standard option names. Within this entry, the following option attributes are required:

\*PageDimensions
\*PrintableArea
\*PrintableOrigin
\*rcNameID or \*Name
\*Command
The following option attributes can be used, but are not required:

\*CursorOrigin
\*RotateSize?
\*PageProtectMem
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Supporting%20Vendor-Defined%20Paper%20Sizes%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




