---
title: Printer Capability Attributes
description: Printer Capability Attributes
keywords:
- printer capability attributes WDK Unidrv
- general printer attributes WDK Unidrv , printer capability
- capability attributes WDK Unidrv
ms.date: 01/26/2024
---

# Printer capability attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

Printer capability attributes are [general printing attributes](general-printing-attributes.md) that specify such printer characteristics as page margin, rotation, and text printing capabilities that affect all paper sizes and orientations.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **MemoryUsage** | LIST of constants indicating the types of data that are stored in printer memory. Can be one or more of: FONT RASTER VECTOR. If a data type is listed but not supported by the printer, it's ignored. | Optional. If not specified, the default value is LIST(FONT, RASTER, VECTOR). For more information, see [Describing printer memory configurations](describing-printer-memory-configurations.md). |
| **OEMCustomData** | Quoted text string to be supplied to a [rendering plug-in](rendering-plug-ins.md) when it calls [**IPrintOemDriverUni::DrvGetGPDData**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetgpddata). | Required if a rendering plug-in calls **IPrintOemDriverUni::DrvGetGPDData**. Interpretation of text string contents is determined by the rendering plug-in. This attribute is a relocatable global attribute; it may be placed at the root level (see [Root-level-only attributes](root-level-only-attributes.md)) to signify that it has no dependency on printer configuration, or it may appear with Option or Case constructs if there's some dependency. |
| **OutputOrderReversed?** | **TRUE** or **FALSE**, indicating whether multipage documents are sorted from last page to first. | Optional. If not specified, the default value is **FALSE**. The EXTERN_GLOBAL symbol shouldn't be used with **OutputOrderReversed?**. |
| **ReselectFont** | LIST of constants indicating operations after which Unidrv must reselect the current font. Can be on of the following: AFTER_GRXDATA - After any CmdSendXxxxData [raster data emission commands](raster-data-emission-commands.md). AFTER_XMOVE - After any x-movement [cursor commands](cursor-commands.md). AFTER_FF - After the CmdFF command. | Optional. If not specified, Unidrv doesn't reselect fonts. |
| **ReverseBandOrderForEvenPages?** | **TRUE** or **FALSE**, indicating whether reverse banding is enabled. This attribute is used to support printers with autoduplex capability; that is, printers that are able to print on both sides of a sheet of paper. The section following this table contains more information. | The default value of this attribute is **FALSE**. Setting this attribute to **TRUE** enables reverse banding order. This attribute is a relocatable global attribute. It may be placed at the root level (see [Root-level-only attributes](root-level-only-attributes.md)) to signify that it has no dependency on printer configuration, or it may appear with Option or Case constructs if there's some dependency. |
| **RotateCoordinate?** | **TRUE** or **FALSE**, indicating whether the printer supports commands to rotate the coordinate system to match the page orientation. | Optional. If not specified, the default value is **FALSE**. If **TRUE**, Option entries for the Orientation feature must specify printer commands. Can't be placed in a Case entry. |
| **RotateFont?** | **TRUE** or **FALSE**, indicating whether the printer automatically rotates fonts to match the page orientation. | Optional. If not specified, the default value is **FALSE**. If **TRUE**, then RotateCoordinate? must also be **TRUE**. Can't be placed in a Case entry. |
| **RotateRaster?** | **TRUE** or **FALSE**, indicating whether the printer automatically rotates raster data to match the page orientation. | Optional. If not specified, the default value is **FALSE**. If **TRUE**, then **RotateCoordinate?** must also be **TRUE**. Can't be placed in a Case entry. |
| **TextCaps** | LIST of constants indicating the printer's text capabilities. Can consist of one or more of the TC_xxx flags described in [**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps). | Optional. If not specified, Unidrv assumes no text capabilities are supported. |

For examples, see the [sample GPD files](sample-gpd-files.md).

## Additional information about ReverseBandOrderForEvenPages?

A side effect of the autoduplex capability is that the bottom edge of a page that has been printed is fed back into the printer, to become the top edge of the next page. To maintain the orientation of the second page relative to the first, the raster image of the second page must be sent to the printer in reverse order. In other words, if the printer printed the front side by sending the top scan line first, it must print the back side bottom scan line first.

When **ReverseBandOrderForEvenPages?** is **TRUE** and duplexing is on, Unidrv enumerates each band in reverse order for even-numbered pages (the back sides of odd-numbered pages). The OEM rendering plug-in needs to cache only one band of data before sending it to the printer. The order of the scan lines within each band isn't reversed, so the plug-in must still handle that task, and it must also reverse the order of the bits within each scan line. Although this is extra work for the plug-in, the advantage is that the plug-in doesn't need to cache any raster data and can begin sending data to the printer immediately.

The **ReverseBandOrderForEvenPages?** attribute is evaluated only when duplexing is set to "Flip on Long Edge". This attribute is ignored when duplexing is set to "Flip on Short Edge".

Both the value of the **ReverseBandOrderForEvenPages?** attribute and the driver-simulated rotation affect the way bands are enumerated, which is shown in the following table. The band enumeration order specified in the column headed with **TRUE** applies when **ReverseBandOrderForEvenPages?** is **TRUE**, and duplexing is selected, and the page to be printed is the second (or back) side. Otherwise the column headed with **FALSE** applies.

| Driver-simulated rotation | TRUE and Even page | FALSE or Odd page |
|--|--|--|
| CCW_ROTATE90 | SW_LTOR | SW_RTOL |
| CCW_ROTATE270 | SW_RTOL | SW_LTOR |
| No Rotation | SW_UP | SW_DOWN |

Legend: SW_LTOR = Left To Right, SW_RTOL = Right To Left, SW_UP = Bottom To Top, SW_DOWN = Top To Bottom.

An OEM rendering plug-in can support autoduplexing without using the **ReverseBandOrderForEvenPages?** attribute. The plug-in can do so by caching all of the data for the entire page and sending it to the printer, beginning with the bottom scan line. That scan line, and all the others on that page, must be sent in reverse order.

The OEM rendering plug-in is responsible for reversing the order of the bits with each scan line and the order of the scan lines with each band as it sends the data to the printer. To determine when this must be done, the value of the PageNumber standard variable can be obtained by making a call to [**IPrintOemDriverUni::DrvGetStandardVariable**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetstandardvariable), using the index SVI_PAGENUMBER. If the page number is odd, no reversing is needed. If the number is even and duplexing is selected, reversing is needed.
