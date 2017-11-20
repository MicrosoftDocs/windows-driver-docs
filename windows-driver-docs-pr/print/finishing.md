---
title: Finishing
description: Finishing
MS-HAID:
- 'autocfg\_422fd6d0-36d4-4500-9e0e-6732dbf4a956.xml'
- 'print.finishing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5c8e556b-102a-4caf-92d3-8b61bec1a29f
---

# Finishing


Schema Path:\\Printer.Finishing

Node Type:Property

The Finishing property contains data about operations performed after printing is complete. This includes whether the document can be collated, stapled, hole punched, along with information about available output bins.

The Finishing property contains two child values, CollationSupported and JogOffsetSupported; it also is the parent of the [Staple](staple3.md), [HolePunch](holepunch3.md), and [OutputBins](outputbins2.md) properties.

### <span id="collationsupported"></span><span id="COLLATIONSUPPORTED"></span> CollationSupported

Schema Path:\\Printer.Finishing:CollationSupported

Node Type:Value

Data Type:BIDI\_BOOL

Description:Indicates whether the printer supports hardware collation of printed documents. If **TRUE**, collation is supported; if **FALSE**, collation is not supported.

### <span id="jogoffsetsupported"></span><span id="JOGOFFSETSUPPORTED"></span> JogOffsetSupported

Schema Path:\\Printer.Finishing:JogOffsetSupported

Node Type:Value

Data Type:BIDI\_BOOL

Description:Determines whether the printer supports placing separate copies of a print job or separate print jobs in the output trays in staggered groups. If **TRUE**, the printer supports jog offset; if **FALSE**, the printer does not support this capability.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Finishing%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




