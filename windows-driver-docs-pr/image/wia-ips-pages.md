---
title: WIA\_IPS\_PAGES
description: The WIA\_IPS\_PAGES property contains the current number of pages to acquire from an automatic document feeder.
ms.assetid: 638f816b-0efd-4885-b285-4fa6a42272bc
keywords: ["WIA_IPS_PAGES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PAGES


The WIA\_IPS\_PAGES property contains the current number of pages to acquire from an automatic document feeder.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE (zero through the maximum number of pages that the scanner can scan; set to zero (0) to scan continuously)

Access Rights: Read/write

Remarks
-------

An application reads WIA\_IPS\_PAGES to determine a document feeder's page capacity. The application sets this property to the maximum number of pages it is willing to scan in the current WIA session. The WIA minidriver creates and maintains this property.

The following table describes the constant that is valid with WIA\_IPS\_PAGES.

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
<td><p>Scan continuously until no more documents are fed into the ADF. This value is the same as setting WIA_PROP_RANGE to zero (0).</p></td>
</tr>
</tbody>
</table>

 

**Note**   If duplex mode is enabled (that is, if WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT is set to FEEDER | DUPLEX), WIA\_IPS\_PAGES is still equal to the number of pages to scan.
One sheet of paper will automatically contain two pages if DUPLEX is enabled, even if the back side of the page is blank.

If you set WIA\_IPS\_PAGES to 1, the scanner will process one of the sides of the page. We recommend that, if a scanner is unable to scan only one side of a page while in duplex mode, you should change the WIA\_IPS\_PAGES value for the **Inc** member of the [**WIA\_PROPERTY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552751) structure to 2. With this value, the application must request pages in multiples of two. A value of zero means that *all* pages that are currently loaded into the document feeder are to be scanned.

 

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
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_PAGES property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_PAGES**](wia-dps-pages.md)

[**WIA\_PROPERTY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552751)

 

 






