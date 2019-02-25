---
title: WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION
description: The WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION property contains the registration, or alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.
ms.assetid: 76868baf-ee31-4395-9122-c056784a9047
keywords: ["WIA_DPS_SHEET_FEEDER_REGISTRATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SHEET_FEEDER_REGISTRATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION


The WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION property contains the registration, or alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_sheet_feeder_registration_si"></span><span id="DDK_WIA_DPS_SHEET_FEEDER_REGISTRATION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION property indicates how a document is horizontally positioned on the scanning head of a handheld or sheet-fed scanner. The scanner uses the property to predict where a user places a document on the scanning head.

The following table describes the constants that are valid with WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LEFT_JUSTIFIED</p></td>
<td><p>The document is positioned to the left with respect to the scanning head.</p></td>
</tr>
<tr class="even">
<td><p>CENTERED</p></td>
<td><p>The document is centered on the scanning head.</p></td>
</tr>
<tr class="odd">
<td><p>RIGHT_JUSTIFIED</p></td>
<td><p>The document is positioned to the right with respect to the scanning head.</p></td>
</tr>
</tbody>
</table>

 

For scanners that support more than one scanning head, the WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION property is relative to the topmost scanning head. This property is required for sheet-fed, scroll-fed, and handheld scanners.

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
<td><p>For Windows Vista and later operating systems, use the WIA_IPS_SHEET_FEEDER_REGISTRATION property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPS\_SHEET\_FEEDER\_REGISTRATION**](wia-ips-sheet-feeder-registration.md)

 

 






