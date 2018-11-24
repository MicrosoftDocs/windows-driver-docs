---
title: WIA\_DPS\_ENDORSER\_CHARACTERS
description: The WIA\_DPS\_ENDORSER\_CHARACTERS property contains all of the valid characters that an application can use to create valid endorser strings.
ms.assetid: 7bf0676b-df85-486b-a448-ab7275ac846d
keywords: ["WIA_DPS_ENDORSER_CHARACTERS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_ENDORSER_CHARACTERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_ENDORSER\_CHARACTERS


The WIA\_DPS\_ENDORSER\_CHARACTERS property contains all of the valid characters that an application can use to create valid endorser strings.

## <span id="ddk_wia_dps_endorser_characters_si"></span><span id="DDK_WIA_DPS_ENDORSER_CHARACTERS_SI"></span>


**Note**  This property is now obsolete. Use [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md) instead.

 

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An "endorser" is a printer that is installed on a scanner that imprints a text message on every page that is scanned. The WIA minidriver should validate the setting of the [**WIA\_DPS\_ENDORSER\_STRING**](wia-dps-endorser-string.md) property against the valid character set in the WIA\_DPS\_ENDORSER\_CHARACTERS property. The minidriver creates and maintains this property.

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


[**WIA\_DPS\_ENDORSER\_STRING**](wia-dps-endorser-string.md)

[**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md)

 

 






