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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

## See also


[**WIA\_DPS\_ENDORSER\_CHARACTERS**](wia-dps-endorser-characters.md)

[**WIA\_IPS\_PRINTER\_ENDORSER\_STRING**](wia-ips-printer-endorser-string.md)

 

 






