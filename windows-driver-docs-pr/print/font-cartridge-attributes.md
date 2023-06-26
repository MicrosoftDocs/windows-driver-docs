---
title: Font cartridge attributes
description: Font cartridge attributes
keywords:
- printer font descriptions WDK Unidrv , cartridges
- font cartridges WDK Unidrv
- cartridge fonts WDK Unidrv
ms.date: 06/22/2023
---

# Font cartridge attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table contains attributes that can be included in a \*FontCartridge GPD entry.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **\*CartridgeName** | Text string representing the cartridge name. | Required, unless **\*rcCartridgeNameID** is specified. |
| **\*Fonts** | LIST of RC_UFM or RC_FONT resource identifiers representing fonts contained in the cartridge that are available for both portrait and landscape orientations. | At least one of **\*Fonts**, **\*PortraitFonts** or **\*LandscapeFonts** must be specified. Font resource identifiers should be numbered contiguously from 1. |
| **\*LandscapeFonts** | LIST of RC_UFM or RC_FONT resource identifiers representing fonts contained in the cartridge that are available only for landscape orientation. | At least one of **\*Fonts**, **\*PortraitFonts** or **\*LandscapeFonts** must be specified. Font resource identifiers should be numbered contiguously from 1. |
| **\*PortraitFonts** | LIST of RC_UFM or RC_FONT resource identifiers representing fonts contained in the cartridge that are available only for portrait orientation. | At least one of **\*Fonts**, **\*PortraitFonts** or **\*LandscapeFonts** must be specified. Font resource identifiers should be numbered contiguously from 1. |
| **\*rcCartridgeNameID** | Resource identifier of a String resource representing the cartridge name. | Required, unless **\*CartridgeName** is specified. |
