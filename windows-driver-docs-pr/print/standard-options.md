---
title: Standard Options
author: windows-driver-content
description: Standard Options
ms.assetid: db4578c1-0954-4c51-a11a-923ab7df2b5b
keywords:
- printer options WDK Unidrv , standard
- standard options WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Standard Options


Standard options are those that are associated with [standard features](standard-features.md). They are identified by predefined names that the GPD language recognizes. Resource identifiers for strings that represent these names are contained in stdnames.gpd, which is supplied with the Microsoft Windows Driver Kit \[WDK\]. (This resource may not be available in some languages and countries.)

The following table lists the standard option names that are permitted for each standard feature. Use these names as arguments to \*Option entries. The features that include Print Schema option keywords are option names that are automatically mapped to Print Schema option keywords. You can also map GPD options to Print Schema keywords manually by using the PrintSchemaKeywordMap attribute. The Print Schema is documented in the Microsoft Windows SDK.

| Feature name | Standard option names | Default Print Schema option keywords | Customized options allowed? |
|---|---|---|---|
| **Collate** | OFF <br> ON | Uncollated<br>Collated | No |
| **ColorMode** <td colspan=2>No standard options. | Yes. Also see [Handling Color Formats](handling-color-formats.md) and [Controlling Image Quality](controlling-image-quality.md). |
| **Duplex** | HORIZONTAL<br>VERTICAL<br>NONE | TwoSidedShortEdge<br>TwoSidedLongEdge<br>OneSided | No |
| **Halftone** <td colspan=2> HT\_PATSIZE\_2x2<br>HT\_PATSIZE\_2x2\_M<br>HT\_PATSIZE\_4x4<br>HT\_PATSIZE\_4x4\_M<br>HT\_PATSIZE\_6x6<br>HT\_PATSIZE\_6x6\_M<br>HT\_PATSIZE\_8x8<br>HT\_PATSIZE\_8x8\_M<br>HT\_PATSIZE\_10x10<br>HT\_PATSIZE\_10x10\_M<br>HT\_PATSIZE\_12x12<br>HT\_PATSIZE\_12x12\_M<br>HT\_PATSIZE\_14x14<br>HT\_PATSIZE\_14x14\_M<br>HT\_PATSIZE\_16x16<br>HT\_PATSIZE\_16x16\_M<br>HT\_PATSIZE\_SUPERCELL<br>HT\_PATSIZE\_SUPERCELL\_M<br>HT\_PATSIZE\_AUTO<br> | Yes. Also see [Halftoning with Unidrv](halftoning-with-unidrv.md). |
<td rowspan=5>**InputBin** | AUTO<br>CASSETTE<br>ENVFEED<br>ENVMANUAL | Cassette <td rowspan=5>Yes | FORMSOURCE | AutoSelect | LARGECAPACITY<br>LARGEFMT<br>LOWER | High | MANUAL<br>MIDDLE<br>SMALLFMT | Manual | TRACTOR<br>UPPER | Tractor | **MediaType** | GLOSSY<br>STANDARD<br>TRANSPARENCY | PhotographicGlossy<br>Plain<br>Transparency | Yes. Also see [Controlling Image Quality](controlling-image-quality.md). |


### TEST END


**Memory**
No standard options.
Yes
**Orientation**
PORTRAIT
LANDSCAPE\_CC90
LANDSCAPE\_CC270
(For more information about the latter two options, see [Specifying Paper Orientation](specifying-paper-orientation.md).)
Portrait
Landscape
ReverseLandscape
No
**PageProtect**
ON, OFF
No
10X11
10X14
11X17
NorthAmerica10x11
NorthAmerica10x14
NorthAmerica11x17
**PaperSize**
12X11
15X11
Yes. Customized names must not exceed the length specified by CCHFORMNAME in *wingdi.h*.
9X11
A\_PLUS
NorthAmerica9x11
NorthAmericaSuperA
A2
A3
ISOA2
ISOA3
A3\_EXTRA
A3\_EXTRA\_TRANSVERSE
ISOA3Extra
A3\_ROTATED
A3\_TRANSVERSE
ISOA3Rotated
A4
A4\_EXTRA
A4\_PLUS
ISOA4
ISOA4Extra
OtherMetricA4Plus
A4\_ROTATED
A4\_TRANSVERSE
ISOA4Rotated
A4SMALL
A5
A5\_EXTRA
ISOA5
ISOA5Extra
A5\_ROTATED
A5\_TRANSVERSE
ISOA5Rotated
A6
A6\_ROTATED
B\_PLUS
B4
B4\_JIS\_ROTATED
B5
B5\_EXTRA
ISOA6
ISOA6Rotated
NorthAmericaSuperB
JISB4
JISB4Rotated
JISB5
ISOB5Extra
B5\_JIS\_ROTATED
B5\_TRANSVERSE
JISB5Rotated
B6\_JIS
B6\_JIS\_ROTATED
JISB6
JISB6Rotated
CSHEET
CUSTOMSIZE
NorthAmericaCSheet
DBL\_JAPANESE\_POSTCARD
DBL\_JAPANESE\_POSTCARD\_ROTATED
DSHEET
ENV\_10
ENV\_11
ENV\_12
ENV\_14
ENV\_9
ENV\_B4
ENV\_B5
JapanDoubleHagakiPostcard
JapanDoubleHagakiPostcardRotated
NorthAmericaDSheet
NorthAmericaNumber10Envelope
NorthAmericaNumber11Envelope
NorthAmericaNumber12Envelope
NorthAmericaNumber14Envelope
NorthAmericaNumber9Envelope
ISOB4Envelope
ISOB5Envelope
ENV\_B6
ENV\_C3
ENV\_C4
ENV\_C5
ENV\_C6
ENV\_C65
ENV\_DL
ENV\_INVITE
ENV\_ITALY
ENV\_MONARCH
ENV\_PERSONAL
ESHEET
EXECUTIVE
FANFOLD\_LGL\_GERMAN
ISOC3Envelope
ISOC4Envelope
ISOC5Envelope
ISOC6Envelope
ISOC6C5Envelope
ISODLEnvelope
OtherMetricInviteEnvelope
OtherMetricItalianEnvelope
NorthAmericaMonarchEnvelope
NorthAmericaPersonalEnvelope
NorthAmericaESheet
NorthAmericaExecutive
NorthAmericaGermanLegalFanfold
FANFOLD\_STD\_GERMAN
FANFOLD\_US
NorthAmericaGermanStandardFanfold
FOLIO
ISO\_B4
JAPANESE\_POSTCARD
JAPANESE\_POSTCARD\_ROTATED
JENV\_CHOU3
JENV\_CHOU3\_ROTATED
JENV\_CHOU4
JENV\_CHOU4\_ROTATED
JENV\_KAKU2
JENV\_KAKU2\_ROTATED
JENV\_KAKU3
JENV\_KAKU3\_ROTATED
JENV\_YOU4
JENV\_YOU4\_ROTATED
OtherMetricFolio
ISOB4
JapanHagakiPostcard
JapanHagakiPostcardRotated
JapanChou3Envelope
JapanChou3EnvelopeRotated
JapanChou4Envelope
JapanChou4EnvelopeRotated
JapanKaku2Envelope
JapanKaku2EnvelopeRotated
JapanKaku3Envelope
JapanKaku3EnvelopeRotated
JapanYou4Envelope
JapanYou4EnvelopeRotated
LEDGER
LEGAL
LEGAL\_EXTRA
LETTER
NorthAmericaLegal
NorthAmericaLegalExtra
NorthAmericaLetter
LETTER\_EXTRA
LETTER\_EXTRA\_TRANSVERSE
NorthAmericaLetterExtra
LETTER\_PLUS
NorthAmericaLetterPlus
LETTER\_ROTATED
LETTER\_TRANSVERSE
NorthAmericaLetterRotated
LETTERSMALL
NOTE
P16K
P16K\_ROTATED
P32K
P32K\_ROTATED
NorthAmericaNote
PRC16K
PRC16KRotated
PRC32K
PRC32KRotated
P32KBIG
P32KBIG\_ROTATED
PRC32KBig
PENV\_1
PENV\_1\_ROTATED
PENV\_10
PENV\_10\_ROTATED
PENV\_2
PENV\_2\_ROTATED
PENV\_3
PENV\_3\_ROTATED
PENV\_4
PENV\_4\_ROTATED
PENV\_5
PENV\_5\_ROTATED
PENV\_6
PENV\_6\_ROTATED
PENV\_7
PENV\_7\_ROTATED
PENV\_8
PENV\_8\_ROTATED
PENV\_9
PENV\_9\_ROTATED
QUARTO
STATEMENT
TABLOID
TABLOID\_EXTRA
PRC1Envelope
PRC1EnvelopeRotated
PRC10Envelope
PRC10EnvelopeRotated
PRC2Envelope
PRC2EnvelopeRotated
PRC3Envelope
PRC3EnvelopeRotated
PRC4Envelope
PRC4EnvelopeRotated
PRC5Envelope
PRC5EnvelopeRotated
PRC6Envelope
PRC6EnvelopeRotated
PRC7Envelope
PRC7EnvelopeRotated
PRC8Envelope
PRC8EnvelopeRotated
PRC9Envelope
PRC9EnvelopeRotated
NorthAmericaQuarto
NorthAmericaStatement
NorthAmericaTabloid
NorthAmericaTabloidExtra
**Resolution**
No standard options.
Yes.
 

## Related topics
[Controlling Image Quality](controlling-image-quality.md)  
[Halftoning with Unidrv](halftoning-with-unidrv.md)  
[Specifying Paper Orientation](specifying-paper-orientation.md)  
[standard features](standard-features.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Standard%20Options%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


