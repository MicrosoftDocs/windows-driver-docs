---
title: WIA\_IPS\_PRINTER\_ENDORSER
description: The WIA\_IPS\_PRINTER\_ENDORSER property is used by the WIA minidriver to list the locations where a printer/endorser device is available, and is used by an application to select one of these locations to enable imprinting/endorsing.
ms.assetid: A9BAC8D3-AB06-4600-9EF7-E9F4846B5215
keywords: ["WIA_IPS_PRINTER_ENDORSER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER
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

# WIA\_IPS\_PRINTER\_ENDORSER


The **WIA\_IPS\_PRINTER\_ENDORSER** property is used by the WIA minidriver to list the locations where a printer/endorser device is available, and is used by an application to select one of these locations to enable imprinting/endorsing. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the required values for the **WIA\_IPS\_PRINTER\_ENDORSER** property.

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
<td><p>WIA_PRINTER_ENDORSER_DISABLED</p></td>
<td><p>Printing/endorsing is disabled. This is the required default value for the property.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_AUTO</p></td>
<td><p>Printing/endorsing is enabled. The location (if there are multiple locations available for this imprinter/endorser) is automatically selected by the device at run time depending on the active scan input source.</p></td>
</tr>
</tbody>
</table>

 

The WIA minidriver is allowed to accept property configuration, but at scan time it ignores requests to enable printing/endorsing to an inactive scan input source.

The following table describes the optional values for the **WIA\_IPS\_PRINTER\_ENDORSER** property.

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
<td><p>WIA_PRINTER_ENDORSER_FLATBED</p></td>
<td><p>Printing/endorsing is enabled for the documents scanned on a flatbed scanner.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_FEEDER_FRONT</p></td>
<td><p>Printing/endorsing is enabled for the front side of the documents scanned through a feeder (either in simplex or duplex image scan mode).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_FEEDER_BACK</p></td>
<td><p>Printing/endorsing is enabled for the back side of the documents scanned through a feeder (either in simplex or duplex image scan mode).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_FEEDER_DUPLEX</p></td>
<td><p>Printing/endorsing is enabled for both sides of the documents scanned through a feeder (either in simplex or duplex image scan mode).</p></td>
</tr>
</tbody>
</table>

 

This property must be supported by all Imprinter/Endorser data source items. The required default value is **WIA\_PRINTER\_ENDORSER\_DISABLED**.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




