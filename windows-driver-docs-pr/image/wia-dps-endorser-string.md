---
title: WIA\_DPS\_ENDORSER\_STRING
description: The WIA\_DPS\_ENDORSER\_STRING property contains a string that is to be endorsed (that is, printed) on each page that the minidriver scans.
ms.assetid: c51a2941-9101-4749-8fa7-b9f3bbcb0803
keywords: ["WIA_DPS_ENDORSER_STRING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_ENDORSER_STRING
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

# WIA\_DPS\_ENDORSER\_STRING


The WIA\_DPS\_ENDORSER\_STRING property contains a string that is to be endorsed (that is, printed) on each page that the minidriver scans.

## <span id="ddk_wia_dps_endorser_string_si"></span><span id="DDK_WIA_DPS_ENDORSER_STRING_SI"></span>


**Note**  This property is now obsolete. Use [**WIA\_IPS\_PRINTER\_ENDORSER\_STRING**](wia-ips-printer-endorser-string.md) instead.

 

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_DPS\_ENDORSER\_STRING property by using the valid character set that is reported in the [**WIA\_DPS\_ENDORSER\_CHARACTERS**](wia-dps-endorser-characters.md) property. The WIA minidriver should endorse documents only if a string is set in WIA\_DPS\_ENDORSER\_STRING. An empty string means that the endorser functionality is disabled.

Because the driver must interpret the endorser string, your driver can use special characters in WIA\_DPS\_ENDORSER\_STRING. However, only your applications will understand these characters.

A driver that supports the WIA\_DPS\_ENDORSER\_STRING property must support the following list of tokens:

<span id="_DATE__"></span><span id="_date__"></span>$DATE$   
The date in the form YYYY/MM/DD.

<span id="_DAY__"></span><span id="_day__"></span>$DAY$   
The day, in the form DD.

<span id="_MONTH__"></span><span id="_month__"></span>$MONTH$   
The month of the year, in the form MM.

<span id="_PAGE_COUNT__"></span><span id="_page_count__"></span>$PAGE\_COUNT$   
The number of pages that are transferred.

<span id="_TIME__"></span><span id="_time__"></span>$TIME$   
The time of day, in the form HH:MM:SS.

<span id="_YEAR__"></span><span id="_year__"></span>$YEAR$   
The year, in the form YYYY.

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


[**WIA\_DPS\_ENDORSER\_CHARACTERS**](wia-dps-endorser-characters.md)

[**WIA\_IPS\_PRINTER\_ENDORSER\_STRING**](wia-ips-printer-endorser-string.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_ENDORSER_STRING%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





