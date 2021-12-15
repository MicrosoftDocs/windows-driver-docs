---
title: WIA_DPS_PAGES
description: The WIA_DPS_PAGES property contains the current number of pages to acquire from an automatic document feeder.
keywords: ["WIA_DPS_PAGES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PAGES

The WIA_DPS_PAGES property contains the current number of pages to acquire from an automatic document feeder.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE (from zero through the maximum number of pages that the scanner can scan; set to zero \[0\] to scan continuously.)

Access Rights: Read/write

## Remarks

An application reads the WIA_DPS_PAGES property to determine a document feeder's page capacity. The application also sets this property to the number of pages it is going to scan. The WIA minidriver creates and maintains WIA_DPS_PAGES.

The following table describes the constant that is valid with the WIA_DPS_PAGES property.

| Value | Definition |
|--|--|
| ALL_PAGES | The same as setting WIA_PROP_RANGE to zero (0). All pages. Scan continuously until no more documents are fed into the ADF. |

If duplex mode is enabled (that is, the [**WIA_DPS_DOCUMENT_HANDLING_SELECT**](wia-dps-document-handling-select.md) property is set to FEEDER | DUPLEX), WIA_DPS_PAGES is still equal to the number of pages to scan.

One sheet of paper will automatically contain two pages if DUPLEX is enabled, even if the back side of the page is blank.

If you set WIA_DPS_PAGES to 1, the scanner will process one of the sides of the page. If a scanner is unable to scan only one side of a page while in duplex mode, you should change the WIA_DPS_PAGES value for the **Inc** member of the [**WIA_PROPERTY_INFO**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_info) structure to 2. This value signals to the application that it must request pages in multiples of two. If WIA_DPS_PAGES is zero, the scanner will scan *all* pages that are currently loaded into the document feeder.

## Requirements

**Version:** Obsolete, use the WIA_IPS_PAGES property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_DOCUMENT_HANDLING_SELECT**](wia-dps-document-handling-select.md)

[**WIA_IPS_PAGES**](wia-ips-pages.md)

[**WIA_PROPERTY_INFO**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_info)
