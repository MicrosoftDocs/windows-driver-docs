---
title: Font cartridges
description: Font cartridges
keywords:
- printer font descriptions WDK Unidrv , cartridges
- font cartridges WDK Unidrv
- cartridge fonts WDK Unidrv
ms.date: 06/23/2023
---

# Font cartridges

[!include[Print Support Apps](../includes/print-support-apps.md)]

If your printer accepts font cartridges, the cartridges are described using \***FontCartridge** GPD file entries. This entry's format is:

\*FontCartridge: *CartridgeName* {*FontCartridgeAttributes*}

where *CartridgeName* is a text string representing the name of the cartridge and *FontCartridgeAttributes* is a set of one or more [font cartridge attributes](font-cartridge-attributes.md).

Alternatively, the fonts supplied by font cartridges can be specified using [Unidrv font format files](customized-font-management.md#unidrv-font-format-files) (.uff files). Typically, the most commonly supplied font cartridges are described in a GPD file, while less commonly used cartridges are specified with .uff files.
