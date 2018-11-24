---
title: WIA\_DPS\_PAGES
description: The WIA\_DPS\_PAGES property contains the current number of pages to acquire from an automatic document feeder.
ms.assetid: 51ab2eab-c7b4-4d54-bfc7-d53a8f66c7a9
keywords: ["WIA_DPS_PAGES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_PAGES


The WIA\_DPS\_PAGES property contains the current number of pages to acquire from an automatic document feeder.

## <span id="ddk_wia_dps_pages_si"></span><span id="DDK_WIA_DPS_PAGES_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE (from zero through the maximum number of pages that the scanner can scan; set to zero \[0\] to scan continuously.)

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_DPS\_PAGES property to determine a document feeder's page capacity. The application also sets this property to the number of pages it is going to scan. The WIA minidriver creates and maintains WIA\_DPS\_PAGES.

The following table describes the constant that is valid with the WIA\_DPS\_PAGES property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>ALL_PAGES</p></td>
<td><p>The same as setting WIA_PROP_RANGE to zero (0). All pages. Scan continuously until no more documents are fed into the ADF.</p></td>
</tr>
</tbody>
</table>

 

**Note**   If duplex mode is enabled (that is, the [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](wia-dps-document-handling-select.md) property is set to FEEDER | DUPLEX), WIA\_DPS\_PAGES is still equal to the number of pages to scan.
One sheet of paper will automatically contain two pages if DUPLEX is enabled, even if the back side of the page is blank.

If you set WIA\_DPS\_PAGES to 1, the scanner will process one of the sides of the page. If a scanner is unable to scan only one side of a page while in duplex mode, you should change the WIA\_DPS\_PAGES value for the **Inc** member of the [**WIA\_PROPERTY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552751) structure to 2. This value signals to the application that it must request pages in multiples of two. If WIA\_DPS\_PAGES is zero, the scanner will scan *all* pages that are currently loaded into the document feeder.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available for Microsoft Windows XP. For Windows Vista and later, use the identical WIA_IPS_PAGES property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](wia-dps-document-handling-select.md)

[**WIA\_IPS\_PAGES**](wia-ips-pages.md)

[**WIA\_PROPERTY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552751)

 

 






