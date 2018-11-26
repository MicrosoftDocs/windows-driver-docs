---
title: Standard Options
description: Standard options are associated with standard features and are identified by predefined names that the GPD language recognizes. 
ms.assetid: db4578c1-0954-4c51-a11a-923ab7df2b5b
keywords:
- printer options WDK Unidrv , standard
- standard options WDK Unidrv
ms.date: 01/30/2018
ms.localizationpriority: medium
---

# Standard Options


Standard options are those that are associated with [standard features](standard-features.md). They are identified by predefined names that the GPD language recognizes. Resource identifiers for strings that represent these names are contained in stdnames.gpd, which is supplied with the Microsoft Windows Driver Kit (WDK). 

> [!IMPORTANT]
> This resource may not be available in some languages and countries.

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
			<td>Yes<br>Also see <a href="https://docs.microsoft.com/windows-hardware/drivers/print/handling-color-formats">Handling Color Formats</a> and <a href="https://docs.microsoft.com/windows-hardware/drivers/print/controlling-image-quality">Controlling Image Quality</a>.</td>
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
			<td>Yes<br>Also see <a href="https://docs.microsoft.com/windows-hardware/drivers/print/halftoning-with-unidrv">Halftoning with Unidrv</a>.</td>
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
			<td>Yes<br>Also see <a href="https://docs.microsoft.com/windows-hardware/drivers/print/controlling-image-quality">Controlling Image Quality</a>.</td>
		</tr>
		<tr>
			<td><b>Memory</b></td>
			<td colspan="2">No standard options</td>
			<td>Yes</td>
		</tr>
		<tr>
			<td><b>Orientation</b></td>
			<td>PORTRAIT<br>LANDSCAPE_CC90<br>LANDSCAPE_CC270<br><br>For more information about the latter two options, see <a href="https://docs.microsoft.com/windows-hardware/drivers/print/specifying-paper-orientation">Specifying Paper Orientation</a>.</td>
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
			<td rowspan="29">Yes<br><b>Note</b> Customized names must not exceed the length specified by <b>CCHFORMNAME</b> in <b>wingdi.h</b>.</td>
		</tr>
		<tr>
			<td colspan="2">12X11<br>15X11</td>
		</tr>
		<tr>
			<td>9X11<br>A_PLUS</td>
			<td>NorthAmerica9x11<br>NorthAmericaSuperA</td>
		</tr>
		<tr>
			<td>A2<br>A3</td>
			<td>ISOA2<br>ISOA3</td>
		</tr>
		<tr>
			<td>A3_EXTRA<br>A3_EXTRA_TRANSVERSE</td>
			<td>ISOA3Extra</td>
		</tr>
		<tr>
			<td>A3_ROTATED<br>A3_TRANSVERSE</td>
			<td>ISOA3Rotated</td>
		</tr>
		<tr>
			<td>A4<br>A4_EXTRA<br>A4_PLUS</td>
			<td>ISOA4<br>ISOA4Extra<br>OtherMetricA4Plus</td>
		</tr>
		<tr>
			<td>A4_ROTATED<br>A4_TRANSVERSE</td>
			<td>ISOA4Rotated</td>
		</tr>
		<tr>
			<td colspan="2">A4SMALL</td>
		</tr>
		<tr>
			<td>A5<br>A5_EXTRA</td>
			<td>ISOA5<br>ISOA5Extra</td>
		</tr>
		<tr>
			<td>A5_ROTATED<br>A5_TRANSVERSE</td>
			<td>ISOA5Rotated</td>
		</tr>
		<tr>
			<td>A6<br>A6_ROTATED<br>B_PLUS<br>B4<br>B4_JIS_ROTATED<br>B5<br>B5_EXTRA</td>
			<td>ISOA6<br>ISOA6Rotated<br>NorthAmericaSuperB<br>JISB4<br>JISB4Rotated<br>JISB5<br>ISOB5Extra</td>
		</tr>
		<tr>
			<td>B5_JIS_ROTATED<br>B5_TRANSVERSE</td>
			<td>JISB5Rotated</td>
		</tr>
		<tr>
			<td>B6_JIS<br>B6_JIS_ROTATED</td>
			<td>JISB6<br>JISB6Rotated</td>
		</tr>
		<tr>
			<td>CSHEET<br>CUSTOMSIZE</td>
			<td>NorthAmericaCSheet</td>
		</tr>
		<tr>
			<td>DBL_JAPANESE_POSTCARD<br>DBL_JAPANESE_POSTCARD_ROTATED<br>DSHEET<br>ENV_10<br>ENV_11<br>ENV_12<br>ENV_14<br>ENV_9<br>ENV_B4<br>ENV_B5</td>
			<td>JapanDoubleHagakiPostcard<br>JapanDoubleHagakiPostcardRotated<br>NorthAmericaDSheet<br>NorthAmericaNumber10Envelope<br>NorthAmericaNumber11Envelope<br>NorthAmericaNumber12Envelope<br>NorthAmericaNumber14Envelope<br>NorthAmericaNumber9Envelope<br>ISOB4Envelope<br>ISOB5Envelope</td>
		</tr>
		<tr>
			<td colspan="2">ENV_B6</td>
		</tr>
		<tr>
			<td>ENV_C3<br>ENV_C4<br>ENV_C5<br>ENV_C6<br>ENV_C65<br>ENV_DL<br>ENV_INVITE<br>ENV_ITALY<br>ENV_MONARCH<br>ENV_PERSONAL<br>ESHEET<br>EXECUTIVE<br>FANFOLD_LGL_GERMAN</td>
			<td>ISOC3Envelope<br>ISOC4Envelope<br>ISOC5Envelope<br>ISOC6Envelope<br>ISOC6C5Envelope<br>ISODLEnvelope<br>OtherMetricInviteEnvelope<br>OtherMetricItalianEnvelope<br>NorthAmericaMonarchEnvelope<br>NorthAmericaPersonalEnvelope<br>NorthAmericaESheet<br>NorthAmericaExecutive<br>NorthAmericaGermanLegalFanfold</td>
		</tr>
		<tr>
			<td>FANFOLD_STD_GERMAN<br>FANFOLD_US</td>
			<td>NorthAmericaGermanStandardFanfold</td>
		</tr>
		<tr>
			<td>FOLIO<br>ISO_B4<br>JAPANESE_POSTCARD<br>JAPANESE_POSTCARD_ROTATED<br>JENV_CHOU3<br>JENV_CHOU3_ROTATED<br>JENV_CHOU4<br>JENV_CHOU4_ROTATED<br>JENV_KAKU2<br>JENV_KAKU2_ROTATED<br>JENV_KAKU3<br>JENV_KAKU3_ROTATED<br>JENV_YOU4<br>JENV_YOU4_ROTATED</td>
			<td>OtherMetricFolio<br>ISOB4<br>JapanHagakiPostcard<br>JapanHagakiPostcardRotated<br>JapanChou3Envelope<br>JapanChou3EnvelopeRotated<br>JapanChou4Envelope<br>JapanChou4EnvelopeRotated<br>JapanKaku2Envelope<br>JapanKaku2EnvelopeRotated<br>JapanKaku3Envelope<br>JapanKaku3EnvelopeRotated<br>JapanYou4Envelope<br>JapanYou4EnvelopeRotated</td>
		</tr>
		<tr>
			<td colspan="2">LEDGER</td>
		</tr>
		<tr>
			<td>LEGAL<br>LEGAL_EXTRA<br>LETTER</td>
			<td>NorthAmericaLegal<br>NorthAmericaLegalExtra<br>NorthAmericaLetter</td>
		</tr>
		<tr>
			<td>LETTER_EXTRA<br>LETTER_EXTRA_TRANSVERSE</td>
			<td>NorthAmericaLetterExtra</td>
		</tr>
		<tr>
			<td>LETTER_PLUS</td>
			<td>NorthAmericaLetterPlus</td>
		</tr>
		<tr>
			<td>LETTER_ROTATED<br>LETTER_TRANSVERSE</td>
			<td>NorthAmericaLetterRotated</td>
		</tr>
		<tr>
			<td colspan="2">LETTERSMALL</td>
		</tr>
		<tr>
			<td>NOTE<br>P16K<br>P16K_ROTATED<br>P32K<br>P32K_ROTATED</td>
			<td>NorthAmericaNote<br>PRC16K<br>PRC16KRotated<br>PRC32K<br>PRC32KRotated</td>
		</tr>
		<tr>
			<td>P32KBIG<br>P32KBIG_ROTATED</td>
			<td>PRC32KBig</td>
		</tr>
		<tr>
			<td>PENV_1<br>PENV_1_ROTATED<br>PENV_10<br>PENV_10_ROTATED<br>PENV_2<br>PENV_2_ROTATED<br>PENV_3<br>PENV_3_ROTATED<br>PENV_4<br>PENV_4_ROTATED<br>PENV_5<br>PENV_5_ROTATED<br>PENV_6<br>PENV_6_ROTATED<br>PENV_7<br>PENV_7_ROTATED<br>PENV_8<br>PENV_8_ROTATED<br>PENV_9<br>PENV_9_ROTATED<br>QUARTO<br>STATEMENT<br>TABLOID<br>TABLOID_EXTRA</td>
			<td>PRC1Envelope<br>PRC1EnvelopeRotated<br>PRC10Envelope<br>PRC10EnvelopeRotated<br>PRC2Envelope<br>PRC2EnvelopeRotated<br>PRC3Envelope<br>PRC3EnvelopeRotated<br>PRC4Envelope<br>PRC4EnvelopeRotated<br>PRC5Envelope<br>PRC5EnvelopeRotated<br>PRC6Envelope<br>PRC6EnvelopeRotated<br>PRC7Envelope<br>PRC7EnvelopeRotated<br>PRC8Envelope<br>PRC8EnvelopeRotated<br>PRC9Envelope<br>PRC9EnvelopeRotated<br>NorthAmericaQuarto<br>NorthAmericaStatement<br>NorthAmericaTabloid<br>NorthAmericaTabloidExtra</td>
		</tr>
		<tr>
			<td><b>Resolution</b></td>
			<td colspan="2">No standard options</td>
			<td>Yes</td>
		</tr>
	</tbody>
</table>


## Related topics


[Controlling Image Quality](controlling-image-quality.md)  
[Halftoning with Unidrv](halftoning-with-unidrv.md)  
[Specifying Paper Orientation](specifying-paper-orientation.md)  
[Standard features](standard-features.md)  





