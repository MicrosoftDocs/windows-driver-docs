---
title: Font Cartridges
description: Font Cartridges
ms.assetid: bc92e2eb-ea75-4f0f-85b7-1433d57401f3
keywords:
- printer font descriptions WDK Unidrv , cartridges
- font cartridges WDK Unidrv
- cartridge fonts WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Font Cartridges





If your printer accepts font cartridges, cartridges can be described by \***FontCartridge** GPD file entries. This entry's format is:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*FontCartridge: <em>CartridgeName</em> {<em>FontCartidgeAttributes</em>}</p></td>
</tr>
</tbody>
</table>

 

where *CartridgeName* is a text string representing the name of the cartridge and *FontCartridgeAttributes* is a set of one or more [font cartridge attributes](font-cartridge-attributes.md).

Alternatively, the fonts supplied by font cartridges can be specified using [Unidrv font format files](customized-font-management.md#ddk-unidrv-font-format-files-gg) (.uff files). Typically, the most commonly supplied font cartridges are described in a GPD file, while less commonly-used cartridges are specified with .uff files.

 

 




