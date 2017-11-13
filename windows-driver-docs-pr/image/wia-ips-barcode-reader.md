---
title: WIA\_IPS\_BARCODE\_READER
description: The WIA\_IPS\_BARCODE\_READER property is used by the WIA minidriver to list the available barcode reader location (one/fixed or multiple) and by the application client to select one of these locations and enable barcode detection.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: EED6CE6D-38CC-4368-8722-5765849C5A7D
keywords: ["WIA_IPS_BARCODE_READER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_BARCODE_READER
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_BARCODE\_READER


The **WIA\_IPS\_BARCODE\_READER** property is used by the WIA minidriver to list the available barcode reader location (one/fixed or multiple) and by the application client to select one of these locations and enable barcode detection.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the required values for the **WIA\_IPS\_BARCODE\_READER** property.

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
<td><p>WIA_BARCODE_READER_DISABLED</p></td>
<td><p>Barcode detection is disabled. This is the required default value.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_READER_AUTO</p></td>
<td><p>Barcode detection is enabled. The barcode reader location is automatically selected by the device at run time depending on the active scan input source.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the optional values for the **WIA\_IPS\_BARCODE\_READER** property.

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
<td><p>WIA_BARCODE_READER_FLATBED</p></td>
<td><p>Barcode detection is enabled for the documents scanned on the scanner flatbed.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_READER_FEEDER_FRONT</p></td>
<td><p>Barcode detection is enabled for the front side of the documents scanned on the scanner feeder.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_READER_FEEDER_BACK</p></td>
<td><p>Barcode detection is enabled for the front side of the documents scanned on the scanner feeder.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_READER_FEEDER_DUPLEX</p></td>
<td><p>Barcode detection is enabled. The barcode reader location is automatically selected by the device at run time depending on the active scan input source.</p></td>
</tr>
</tbody>
</table>

 

**Note**  The WIA minidriver is allowed to accept property configuration for the optional values but at scan time ignore requests to enable barcode detection to an inactive scan input source.

 

This property is required for all Barcode Reader items. The WIA\_BARCODE\_READER\_DISABLED and WIA\_BARCODE\_READER\_AUTO values are required. WIA\_BARCODE\_READER\_DISABLED is the required default value.

The [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) property is also required for all Barcode Reader items.

The following table describes the required values for the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) property when it is implemented on a Barcode Reader item.

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
<td><p>WiaImgFmt_XmlBar</p></td>
<td><p>Barcode metadata is transferred as an XML file whose content is compliant with the WIA Barcode Metadata Schema.</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_RawBar</p></td>
<td><p>Barcode metadata is transferred as a WIA Barcode Metadata Raw Format file.</p></td>
</tr>
</tbody>
</table>

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_BARCODE_READER%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




