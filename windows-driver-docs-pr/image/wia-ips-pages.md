---
title: WIA\_IPS\_PAGES
description: The WIA\_IPS\_PAGES property contains the current number of pages to acquire from an automatic document feeder.
MS-HAID:
- 'WIA\_PropTable\_4e933090-cb42-473d-8fc8-110fc97e2611.xml'
- 'image.wia\_ips\_pages'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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

## <span id="see_also"></span>See also


[**WIA\_DPS\_PAGES**](wia-dps-pages.md)

[**WIA\_PROPERTY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552751)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PAGES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





