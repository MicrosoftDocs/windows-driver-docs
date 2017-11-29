---
title: WIA\_DPS\_SCAN\_AHEAD\_PAGES
description: The WIA\_DPS\_SCAN\_AHEAD\_PAGES property contains a value that indicates whether a scanner will cache pages in a scanner buffer before sending them to an application.
ms.assetid: 8c00b029-dc9f-43e1-af4a-088e143351ca
keywords: ["WIA_DPS_SCAN_AHEAD_PAGES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SCAN_AHEAD_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_DPS\_SCAN\_AHEAD\_PAGES


The WIA\_DPS\_SCAN\_AHEAD\_PAGES property contains a value that indicates whether a scanner will cache pages in a scanner buffer before sending them to an application.

## <span id="ddk_wia_dps_scan_ahead_pages_si"></span><span id="DDK_WIA_DPS_SCAN_AHEAD_PAGES_SI"></span>


**Note**  This property is now obsolete. Use [**WIA\_IPS\_SCAN\_AHEAD**](wia-ips-scan-ahead.md) instead.

 

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE (from zero through the maximum number of pages that the document feeder can hold)

Access Rights: Read/write

Remarks
-------

If the WIA\_DPS\_SCAN\_AHEAD\_PAGES property is zero, scan ahead is disabled, and the scanner will not scan ahead any pages.

If the scanner performs data transfers on the buffered scan-ahead item, the scanner will retrieve the buffered pages. WIA properties cannot be changed during a scan-ahead operation. WIA\_DPS\_SCAN\_AHEAD\_PAGES is optional.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_IPS\_SCAN\_AHEAD**](wia-ips-scan-ahead.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_SCAN_AHEAD_PAGES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





