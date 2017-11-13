---
title: WIA\_IPS\_PRINTER\_ENDORSER\_STRING
description: The WIA\_IPS\_PRINTER\_ENDORSER\_STRING property is used to configure the text to be printed/endorsed. The WIA minidriver creates and maintains this property.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: DF4B1361-EC9C-4BEA-97F5-9179DCB77044
keywords: ["WIA_IPS_PRINTER_ENDORSER_STRING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_STRING
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PRINTER\_ENDORSER\_STRING


The **WIA\_IPS\_PRINTER\_ENDORSER\_STRING** property is used to configure the text to be printed/endorsed. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


**Note**  This property replaces [**WIA\_DPS\_ENDORSER\_STRING**](wia-dps-endorser-string.md), which is now obsolete.

 

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The text to be printed/endorsed can be represented by one or multiple character strings. Each character string can contain one or more special character formatting sequences described by the [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md) property. The character strings must contain only characters specified by [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md) and must be NULL terminated. When multiple character strings are configured, the WIA minidriver must print/endorse each string on a new page (cycling through the list of strings).

This property is optional for all Imprinter/Endorser data source items.

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


[**WIA\_DPS\_ENDORSER\_STRING**](wia-dps-endorser-string.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_STRING%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





