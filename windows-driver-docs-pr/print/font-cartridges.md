---
title: Font Cartridges
author: windows-driver-content
description: Font Cartridges
ms.assetid: bc92e2eb-ea75-4f0f-85b7-1433d57401f3
keywords:
- printer font descriptions WDK Unidrv , cartridges
- font cartridges WDK Unidrv
- cartridge fonts WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Font Cartridges


## <a href="" id="ddk-font-cartridges-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Font%20Cartridges%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


