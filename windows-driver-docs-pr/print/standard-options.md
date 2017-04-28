---
title: Standard Options
description: Standard options are associated with standard features and are identified by predefined names that the GPD language recognizes. 
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


Standard options are those that are associated with [standard features](standard-features.md). They are identified by predefined names that the GPD language recognizes. Resource identifiers for strings that represent these names are contained in stdnames.gpd, which is supplied with the Microsoft Windows Driver Kit (WDK). 

**Note** This resource may not be available in some languages and countries.

The following table lists the standard option names that are permitted for each standard feature. Use these names as arguments to **\*Option** entries. The features that include Print Schema option keywords are option names that are automatically mapped to Print Schema option keywords. You can also map GPD options to Print Schema keywords manually by using the **PrintSchemaKeywordMap** attribute. The Print Schema is documented in the Microsoft Windows SDK.

<table>
	<tbody>
		<tr>
			<td><b>Feature name</b></td>
			<td><b>Standard option names</b></td>
			<td><b>Default Print Schema option keywords</b></td>
			<td><b>Customized options allowed?</b></td>
		</tr>
        <tr>
			<td><b>Collate</b></td>
			<td>OFF<br>ON</td>
			<td>Uncollated<br>Collated</td>
			<td>No</td>
		</tr>
		<tr>
			<td><b>ColorMode</b></td>
			<td colspan="2">No standard options</td>
			<td>Yes<br>Also see [Handling Color Formats](handling-color-formats.md)<br>and [Controlling Image Quality](controlling-image-quality.md).</td>
		</tr>
		<tr>
			<td><b>Duplex</b></td>
			<td>HORIZONTAL<br>VERTICAL<br>NONE</td>
			<td>TwoSidedShortEdge<br>TwoSidedLongEdge<br>OneSided</td>
			<td>No</td>
		</tr>
		<tr>
			<td><b>Halftone</b></td>
			<td colspan="2">HT_PATSIZE_2x2<br>HT_PATSIZE_2x2_M<br>HT_PATSIZE_4x4<br>HT_PATSIZE_4x4_M<br>HT_PATSIZE_6x6<br>HT_PATSIZE_6x6_M<br>HT_PATSIZE_8x8<br>HT_PATSIZE_8x8_M<br>HT_PATSIZE_10x10<br>HT_PATSIZE_10x10_M<br>HT_PATSIZE_12x12<br>HT_PATSIZE_12x12_M<br>HT_PATSIZE_14x14<br>HT_PATSIZE_14x14_M<br>HT_PATSIZE_16x16<br>HT_PATSIZE_16x16_M<br>HT_PATSIZE_SUPERCELL<br>HT_PATSIZE_SUPERCELL_M<br>HT_PATSIZE_AUTO</td>
			<td>Yes<br>Also see [Halftoning with Unidrv].</td>
		</tr>
		<tr>
			<td rowspan="5"><b>InputBin</b></td>
			<td>AUTO<br>CASSETTE<br>ENVFEED<br>ENVMANUAL</td>
			<td>Cassette</td>
			<td rowspan="5">Yes</td>
		</tr>
		<tr>
			<td>FORMSOURCE</td>
			<td>AutoSelect</td>
		</tr>
		<tr>
			<td>LARGECAPACITY<br>LARGEFMT<br>LOWER</td>
			<td>High</td>
		</tr>
		<tr>
			<td>MANUAL<br>MIDDLE<br>SMALLFMT</td>
			<td>Manual</td>
		</tr>
		<tr>
			<td>TRACTOR<br>UPPER</td>
			<td>Tractor</td>
		</tr>
		<tr>
			<td><b>MediaType</b></td>
			<td>GLOSSY<br>STANDARD<br>TRANSPARENCY</td>
			<td>PhotographicGlossy<br>Plain<br>Transparency</td>
			<td>Yes<br>Also see [Controlling Image Quality](controlling-image-quality.md).</td>
		</tr>
		<tr>
			<td><b>Memory</b></td>
			<td colspan="2">No standard options</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td><b>Orientation</b></td>
			<td>PORTRAIT<br>LANDSCAPE_CC90<br>LANDSCAPE_CC270<br>For more information about the latter two options, see [Specifying Paper Orientation](specifying-paper-orientation.md).</td>
			<td>Portrait<br>Landscape<br>ReverseLandscape</td>
			<td>No</td>
		</tr>
		<tr>
			<td><b>PageProtect</b></td>
			<td colspan="2">ON<br>OFF</td>
			<td>No</td>
		</tr>
		<tr>
			<td rowspan="29"><b>PaperSize</b></td>
			<td>10X11<br>10X14<br>11X17</td>
			<td>NorthAmerica10x11<br>NorthAmerica10x14<br>NorthAmerica11x17</td>
			<td rowspan="29">Yes<br>Customized names must not exceed the length specified by <b>CCHFORMNAME</b> in <b>wingdi.h</b>.</td>
		</tr>
		<tr>
			<td colspan="2">12X11<br>15X11</td>
		</tr>
		<tr>
			<td>9X11<br>A_PLUS</td>
			<td>NorthAmerica9x11<br>NorthAmericaSuperA</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td><b>Resolution</b></td>
			<td colspan="2">No standard options</td>
			<td>Yes</td>
		</tr>
	</tbody>
</table>


### TEST END



**Orientation**
PORTRAIT
LANDSCAPE_CC90
LANDSCAPE_CC270
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
A_PLUS
NorthAmerica9x11
NorthAmericaSuperA
A2
A3
ISOA2
ISOA3
A3_EXTRA
A3_EXTRA_TRANSVERSE
ISOA3Extra
A3_ROTATED
A3_TRANSVERSE
ISOA3Rotated
A4
A4_EXTRA
A4_PLUS
ISOA4
ISOA4Extra
OtherMetricA4Plus
A4_ROTATED
A4_TRANSVERSE
ISOA4Rotated
A4SMALL
A5
A5_EXTRA
ISOA5
ISOA5Extra
A5_ROTATED
A5_TRANSVERSE
ISOA5Rotated
A6
A6_ROTATED
B_PLUS
B4
B4_JIS_ROTATED
B5
B5_EXTRA
ISOA6
ISOA6Rotated
NorthAmericaSuperB
JISB4
JISB4Rotated
JISB5
ISOB5Extra
B5_JIS_ROTATED
B5_TRANSVERSE
JISB5Rotated
B6_JIS
B6_JIS_ROTATED
JISB6
JISB6Rotated
CSHEET
CUSTOMSIZE
NorthAmericaCSheet
DBL_JAPANESE_POSTCARD
DBL_JAPANESE_POSTCARD_ROTATED
DSHEET
ENV_10
ENV_11
ENV_12
ENV_14
ENV_9
ENV_B4
ENV_B5
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
ENV_B6
ENV_C3
ENV_C4
ENV_C5
ENV_C6
ENV_C65
ENV_DL
ENV_INVITE
ENV_ITALY
ENV_MONARCH
ENV_PERSONAL
ESHEET
EXECUTIVE
FANFOLD_LGL_GERMAN
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
FANFOLD_STD_GERMAN
FANFOLD_US
NorthAmericaGermanStandardFanfold
FOLIO
ISO_B4
JAPANESE_POSTCARD
JAPANESE_POSTCARD_ROTATED
JENV_CHOU3
JENV_CHOU3_ROTATED
JENV_CHOU4
JENV_CHOU4_ROTATED
JENV_KAKU2
JENV_KAKU2_ROTATED
JENV_KAKU3
JENV_KAKU3_ROTATED
JENV_YOU4
JENV_YOU4_ROTATED
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
LEGAL_EXTRA
LETTER
NorthAmericaLegal
NorthAmericaLegalExtra
NorthAmericaLetter
LETTER_EXTRA
LETTER_EXTRA_TRANSVERSE
NorthAmericaLetterExtra
LETTER_PLUS
NorthAmericaLetterPlus
LETTER_ROTATED
LETTER_TRANSVERSE
NorthAmericaLetterRotated
LETTERSMALL
NOTE
P16K
P16K_ROTATED
P32K
P32K_ROTATED
NorthAmericaNote
PRC16K
PRC16KRotated
PRC32K
PRC32KRotated
P32KBIG
P32KBIG_ROTATED
PRC32KBig
PENV_1
PENV_1_ROTATED
PENV_10
PENV_10_ROTATED
PENV_2
PENV_2_ROTATED
PENV_3
PENV_3_ROTATED
PENV_4
PENV_4_ROTATED
PENV_5
PENV_5_ROTATED
PENV_6
PENV_6_ROTATED
PENV_7
PENV_7_ROTATED
PENV_8
PENV_8_ROTATED
PENV_9
PENV_9_ROTATED
QUARTO
STATEMENT
TABLOID
TABLOID_EXTRA
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

 

## Related topics
[Controlling Image Quality](controlling-image-quality.md)  
[Halftoning with Unidrv](halftoning-with-unidrv.md)  
[Specifying Paper Orientation](specifying-paper-orientation.md)  
[Standard features](standard-features.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Standard%20Options%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


