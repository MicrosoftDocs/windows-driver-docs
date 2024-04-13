---
title: WIA_IPS_PAGES
description: The WIA_IPS_PAGES property contains the current number of pages to acquire from an automatic document feeder.
keywords: ["WIA_IPS_PAGES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_PAGES

The WIA_IPS_PAGES property contains the current number of pages to acquire from an automatic document feeder.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE (zero through the maximum number of pages that the scanner can scan; set to zero (0) to scan continuously)

Access Rights: Read/write

## Remarks

An application reads WIA_IPS_PAGES to determine a document feeder's page capacity. The application sets this property to the maximum number of pages it is willing to scan in the current WIA session. The WIA minidriver creates and maintains this property.

The following table describes the constant that is valid with WIA_IPS_PAGES.

| Value | Definition |
|--|--|
| ALL_PAGES | Scan continuously until no more documents are fed into the ADF. This value is the same as setting WIA_PROP_RANGE to zero (0). |

**Note**   If duplex mode is enabled (that is, if WIA_IPS_DOCUMENT_HANDLING_SELECT is set to FEEDER | DUPLEX), WIA_IPS_PAGES is still equal to the number of pages to scan.
One sheet of paper will automatically contain two pages if DUPLEX is enabled, even if the back side of the page is blank.

If you set WIA_IPS_PAGES to 1, the scanner will process one of the sides of the page. We recommend that, if a scanner is unable to scan only one side of a page while in duplex mode, you should change the WIA_IPS_PAGES value for the **Inc** member of the [**WIA_PROPERTY_INFO**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_info) structure to 2. With this value, the application must request pages in multiples of two. A value of zero means that *all* pages that are currently loaded into the document feeder are to be scanned.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_PAGES**](wia-dps-pages.md)

[**WIA_PROPERTY_INFO**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_info)
