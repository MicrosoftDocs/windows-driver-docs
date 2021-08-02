---
title: Standard options
description: Standard options are associated with standard features and are identified by predefined names that the GPD language recognizes.
keywords:
- printer options WDK Unidrv , standard
- standard options WDK Unidrv
ms.date: 08/02/2021
ms.localizationpriority: medium
---

# Standard options

Standard options are those that are associated with [standard features](standard-features.md). They are identified by predefined names that the GPD language recognizes. Resource identifiers for strings that represent these names are contained in stdnames.gpd, which is supplied with the Microsoft Windows Driver Kit (WDK).

> [!IMPORTANT]
> This resource may not be available in some languages and countries.

The following table lists the standard option names that are permitted for each standard feature. Use these names as arguments to **\*Option** entries. The features that include Print Schema option keywords are option names that are automatically mapped to Print Schema option keywords. You can also map GPD options to Print Schema keywords manually by using the **PrintSchemaKeywordMap** attribute.

| Feature name | Standard option names | Default Print Schema option keywords | Customized options allowed? |
|--|--|--|--|
| **Collate** | OFF, ON | Uncollated, Collated | No |
| **ColorMode** | No standard options | &nbsp; | Yes. Also see [Handling Color Formats](/windows-hardware/drivers/print/handling-color-formats) and [Controlling Image Quality](/windows-hardware/drivers/print/controlling-image-quality). |
| **Duplex** | HORIZONTAL, VERTICAL, NONE | TwoSidedShortEdge, TwoSidedLongEdge, OneSided | No |
| **Halftone** | HT_PATSIZE_2x2, HT_PATSIZE_2x2_M, HT_PATSIZE_4x4, HT_PATSIZE_4x4_M, HT_PATSIZE_6x6, HT_PATSIZE_6x6_M, HT_PATSIZE_8x8, HT_PATSIZE_8x8_M, HT_PATSIZE_10x10, HT_PATSIZE_10x10_M, HT_PATSIZE_12x12, HT_PATSIZE_12x12_M, HT_PATSIZE_14x14, HT_PATSIZE_14x14_M, HT_PATSIZE_16x16, HT_PATSIZE_16x16_M, HT_PATSIZE_SUPERCELL, HT_PATSIZE_SUPERCELL_M, HT_PATSIZE_AUTO | &nbsp; | Yes, also see [Halftoning with Unidrv](/windows-hardware/drivers/print/halftoning-with-unidrv). |
| **InputBin** | AUTO, CASSETTE, ENVFEED, ENVMANUAL | Cassette | Yes |
| &nbsp; | FORMSOURCE | AutoSelect | &nbsp; |
| &nbsp; | LARGECAPACITY, LARGEFMT, LOWER | High | &nbsp; |
| &nbsp; | MANUAL, MIDDLE, SMALLFMT | Manual | &nbsp; |
| &nbsp; | TRACTOR, UPPER | Tractor | &nbsp; |
| **MediaType** | GLOSSY, STANDARD, TRANSPARENCY | PhotographicGlossy, Plain, Transparency | Yes. Also see [Controlling Image Quality](/windows-hardware/drivers/print/controlling-image-quality). |
| **Memory** | No standard options | &nbsp; | Yes |
| **Orientation** | PORTRAIT, LANDSCAPE_CC90, LANDSCAPE_CC270. For more information about the latter two options, see [Specifying Paper Orientation](/windows-hardware/drivers/print/specifying-paper-orientation). | Portrait, Landscape, ReverseLandscape | No |
| **PageProtect** | ON, OFF | &nbsp; | No |
| **PaperSize** | 10X11, 10X14, 11X17 | NorthAmerica10x11, NorthAmerica10x14, NorthAmerica11x17 | Yes. **Note:** Customized names must not exceed the length specified by **CCHFORMNAME** in **wingdi.h**. |
| &nbsp; | 12X11, 15X11 | &nbsp; | &nbsp; |
| &nbsp; | 9X11, A_PLUS | NorthAmerica9x11, NorthAmericaSuperA | &nbsp; |
| &nbsp; | A2, A3 | ISOA2, ISOA3 | &nbsp; |
| &nbsp; | A3_EXTRA, A3_EXTRA_TRANSVERSE | ISOA3Extra | &nbsp; |
| &nbsp; | A3_ROTATED, A3_TRANSVERSE | ISOA3Extra | &nbsp; |
| &nbsp; | A4, A4_EXTRA, A4_PLUS | ISOA4, ISOA4Extra, OtherMetricA4Plus | &nbsp; |
| &nbsp; | A4_ROTATED, A4_TRANSVERSE | ISOA4Rotated | &nbsp; |
| &nbsp; | A4SMALL | &nbsp; | &nbsp; |
| &nbsp; | A5, A5_EXTRA | ISOA5, ISOA5Extra | &nbsp; |
| &nbsp; | A5_ROTATED, A5_TRANSVERSE | ISOA5Rotated | &nbsp; |
| &nbsp; | A6, A6_ROTATED, B_PLUS, B4, B4_JIS_ROTATED, B5, B5_EXTRA | ISOA6, ISOA6Rotated, NorthAmericaSuperB, JISB4, JISB4Rotated, JISB5, ISOB5Extra | &nbsp; |
| &nbsp; | B5_JIS_ROTATED, B5_TRANSVERSE | JISB5Rotated | &nbsp; |
| &nbsp; | B6_JIS, B6_JIS_ROTATED | JISB6, JISB6Rotated | &nbsp; |
| &nbsp; | CSHEET, CUSTOMSIZE | NorthAmericaCSheet | &nbsp; |
| &nbsp; | DBL_JAPANESE_POSTCARD, DBL_JAPANESE_POSTCARD_ROTATED, DSHEET, ENV_10, ENV_11, ENV_12, ENV_14, ENV_9, ENV_B4, ENV_B5 | JapanDoubleHagakiPostcard, JapanDoubleHagakiPostcardRotated, NorthAmericaDSheet, NorthAmericaNumber10Envelope, NorthAmericaNumber11Envelope, NorthAmericaNumber12Envelope, NorthAmericaNumber14Envelope, NorthAmericaNumber9Envelope, ISOB4Envelope, ISOB5Envelope | &nbsp; |
| &nbsp; | ENV_B6 | &nbsp; | &nbsp; |
| &nbsp; | ENV_C3, ENV_C4, ENV_C5, ENV_C6, ENV_C65, ENV_DL, ENV_INVITE, ENV_ITALY, ENV_MONARCH, ENV_PERSONAL, ESHEET, EXECUTIVE, FANFOLD_LGL_GERMAN | ISOC3Envelope, ISOC4Envelope, ISOC5Envelope, ISOC6Envelope, ISOC6C5Envelope, ISODLEnvelope, OtherMetricInviteEnvelope, OtherMetricItalianEnvelope, NorthAmericaMonarchEnvelope, NorthAmericaPersonalEnvelope, NorthAmericaESheet, NorthAmericaExecutive, NorthAmericaGermanLegalFanfold | &nbsp; |
| &nbsp; | FANFOLD_STD_GERMAN, FANFOLD_US | NorthAmericaGermanStandardFanfold | &nbsp; |
| &nbsp; | FOLIO, ISO_B4, JAPANESE_POSTCARD, JAPANESE_POSTCARD_ROTATED, JENV_CHOU3, JENV_CHOU3_ROTATED, JENV_CHOU4, JENV_CHOU4_ROTATED, JENV_KAKU2, JENV_KAKU2_ROTATED, JENV_KAKU3, JENV_KAKU3_ROTATED, JENV_YOU4, JENV_YOU4_ROTATED | OtherMetricFolio, ISOB4, JapanHagakiPostcard, JapanHagakiPostcardRotated, JapanChou3Envelope, JapanChou3EnvelopeRotated, JapanChou4Envelope, JapanChou4EnvelopeRotated, JapanKaku2Envelope, JapanKaku2EnvelopeRotated, JapanKaku3Envelope, JapanKaku3EnvelopeRotated, JapanYou4Envelope, JapanYou4EnvelopeRotated | &nbsp; |
| &nbsp; | LEDGER | &nbsp; | &nbsp; |
| &nbsp; | LEGAL, LEGAL_EXTRA, LETTER | NorthAmericaLegal, NorthAmericaLegalExtra, NorthAmericaLetter | &nbsp; |
| &nbsp; | LETTER_EXTRA, LETTER_EXTRA_TRANSVERSE | NorthAmericaLetterExtra | &nbsp; |
| &nbsp; | LETTER_PLUS | NorthAmericaLetterPlus | &nbsp; |
| &nbsp; | LETTER_PLUS | NorthAmericaLetterPlus | &nbsp; |
| &nbsp; | LETTER_ROTATED, LETTER_TRANSVERSE | NorthAmericaLetterRotated | &nbsp; |
| &nbsp; | LETTERSMALL | &nbsp; | &nbsp; |
| &nbsp; | NOTE, P16K, P16K_ROTATED, P32K, P32K_ROTATED | NorthAmericaNote, PRC16K, PRC16KRotated, PRC32K, PRC32KRotated | &nbsp; |
| &nbsp; | P32KBIG, P32KBIG_ROTATED | PRC32KBig | &nbsp; |
| &nbsp; | PENV_1, PENV_1_ROTATED, PENV_10, PENV_10_ROTATED, PENV_2, PENV_2_ROTATED, PENV_3, PENV_3_ROTATED, PENV_4, PENV_4_ROTATED, PENV_5, PENV_5_ROTATED, PENV_6, PENV_6_ROTATED, PENV_7, PENV_7_ROTATED, PENV_8, PENV_8_ROTATED, PENV_9, PENV_9_ROTATED, QUARTO, STATEMENT, TABLOID, TABLOID_EXTRA | PRC1Envelope, PRC1EnvelopeRotated, PRC10Envelope, PRC10EnvelopeRotated, PRC2Envelope, PRC2EnvelopeRotated, PRC3Envelope, PRC3EnvelopeRotated, PRC4Envelope, PRC4EnvelopeRotated, PRC5Envelope, PRC5EnvelopeRotated, PRC6Envelope, PRC6EnvelopeRotated, PRC7Envelope, PRC7EnvelopeRotated, PRC8Envelope, PRC8EnvelopeRotated, PRC9Envelope, PRC9EnvelopeRotated, NorthAmericaQuarto, NorthAmericaStatement, NorthAmericaTabloid, NorthAmericaTabloidExtra | &nbsp; |
| **Resolution** | No standard options | &nbsp; | Yes |
| **NUp** | No standard options | &nbsp; | Yes |
| **JobPasscode** | OFF, ON | Off, On | No |

## Related topics

[Controlling Image Quality](controlling-image-quality.md)

[Halftoning with Unidrv](halftoning-with-unidrv.md)

[Specifying Paper Orientation](specifying-paper-orientation.md)

[Standard features](standard-features.md)
