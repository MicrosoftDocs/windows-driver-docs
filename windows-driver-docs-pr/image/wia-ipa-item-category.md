---
title: WIA_IPA_ITEM_CATEGORY
description: The WIA_IPA_ITEM_CATEGORY property contains grouped categories for WIA items.
keywords: ["WIA_IPA_ITEM_CATEGORY Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ITEM_CATEGORY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_ITEM_CATEGORY

The WIA_IPA_ITEM_CATEGORY property contains grouped categories for WIA items.

Property Type: VT_CLSID

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA minidriver creates and maintains this property.

WIA defines the following categories:

| Category | Description |
|--|--|
| WIA_CATEGORY_BARCODE_READER | A barcode reader item that is a programmable data source, transfer enabled to download barcode metadata. |
| WIA_CATEGORY_ENDORSER | The endorsing category of a programmable data source item that represents both imprinting and endorsing, and can be transfer enabled to upload and download the data content to be printed/endorsed. |
| WIA_CATEGORY_FEEDER | A feeder item that is a programmable data source, that follows the standard rules, and that has the WIA properties that are required to support document feeders. |
| WIA_CATEGORY_FEEDER_BACK | A programmable data source item that describes the back side data source of a duplex base feeder item (WIA_CATEGORY_FEEDER). |
| WIA_CATEGORY_FEEDER_FRONT | A programmable data source item that describes the front side data source of a duplex base feeder item (WIA_CATEGORY_FEEDER). |
| WIA_CATEGORY_FILM | A film item that is a programmable data source, that follows the standard rules, and that has the WIA properties that are required to support film-scanning units. |
| WIA_CATEGORY_FINISHED_FILE | *Not* a programmable data source. The device provides data in a finished file format or in a folder item that contains the finished-file-format item. |
| WIA_CATEGORY_FLATBED | A flatbed item that is a programmable data source, that follows the standard rules, and that has the WIA properties that are required to support flatbed-platen scanning. |
| WIA_CATEGORY_FOLDER | A folder storage item (not a programmable data source) containing other folder items and/or finished files. |
| WIA_CATEGORY_IMPRINTER | The imprinting category of a programmable data source item that represents both imprinting and endorsing, and can be transfer enabled to upload and download the data content to be printed/endorsed. |
| WIA_CATEGORY_MICR_READER | A (Magnetic Ink Character Recognition) MICR reader item that is a programmable data source, transfer enabled to download MICR text. |
| WIA_CATEGORY_PATCH_CODE_READER | A patch code reader item that is a programmable data source, transfer enabled to download patch code metadata. |
| WIA_CATEGORY_ROOT | The root item for the device. |
| WIA_CATEGORY_AUTO | In Windows 7 and later, an [auto item](./auto-item.md) has the WIA properties that are required to support [auto-configured scanning](./auto-configured-scanning.md). |

The preceding categories define how a WIA item should be treated or used. For example, if the item represents a finished file, you can assume that the data is static and located on the device. If the item represents a feeder, you can expect it to contain the required document-feeder properties and to operate like a document feeder. For more information about these categories, see [WIA Item Categories](./wia-item-categories.md).

The following table shows the WIA grouped categories and their item flags. This table does not include a full list of all of the WIA item flags that WIA defines. For a complete list of these flags, see [**WIA_IPA_ITEM_FLAGS**](wia-ipa-item-flags.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>WIA category</th>
<th>WIA item flags</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_CATEGORY_BARCODE_READER</p></td>
<td><p>WiaItemTypeProgrammableDataSource</p>
<p><strong>Required</strong></p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeFile</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_ENDORSER</p></td>
<td><p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeImage</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeFile</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FEEDER</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeFile</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeFolder</p>
<p>(ADF root item only, if WIA_CATEGORY_FEEDER_FRONT and WIA_CATEGORY_FEEDER_BACK items are present)</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_FEEDER_BACK</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeFile</p>
<p><strong>Optional</strong></p>
<p>None</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FEEDER_FRONT</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeFile</p>
<p><strong>Optional</strong></p>
<p>None</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_FILM</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeFile</p>
<p>WiaItemTypeFolder</p>
<p><strong>Optional</strong></p>
<p>None</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FINISHED_FILE</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeFile</p>
<p>WiaItemTypeTransfer</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeAudio</p>
<p>WiaItemTypeDeleted</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_FLATBED</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeFile</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeFolder</p>
<p>(On the FB root item only if multiple scan regions items are supported)</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FOLDER</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeStorage</p>
<p>WiaItemTypeFolder</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeDeleted</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_IMPRINTER</p></td>
<td><p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeImage</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeFile</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_MICR_READER</p></td>
<td><p>WiaItemTypeProgrammableDataSource</p>
<p><strong>Required</strong></p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeFile</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_PATCH_CODE_READER</p></td>
<td><p>WiaItemTypeProgrammableDataSource</p>
<p><strong>Required</strong></p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeFile</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_ROOT</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeRoot</p>
<p>WiaItemTypeFolder</p>
<p><strong>Optional</strong></p>
<p>WiaItemTypeDevice</p>
<p>WiaItemTypeDisconnected</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_AUTO</p></td>
<td><p><strong>Required</strong></p>
<p>WiaItemTypeProgrammableDataSource</p>
<p>WiaItemTypeTransfer</p>
<p>WiaItemTypeImage</p>
<p>WiaItemTypeFile</p>
<p><strong>Optional</strong></p>
<p><em>None</em></p></td>
</tr>
</tbody>
</table>

The following table shows the WIA grouped categories and their WIA properties and WIA items.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>WIA category</th>
<th>WIA properties</th>
<th>WIA items</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_CATEGORY_FEEDER</p></td>
<td><p>Properties include those for feeder-scanner control.</p>
<p>Image-specific and document-specific properties are typically included.</p></td>
<td><p>WIA Feeder items, including child items that represent the front and back pages of a document.</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_FEEDER_BACK</p></td>
<td><p>Properties include those for feeder-scanner control.</p>
<p>Image-specific and document-specific properties are typically included.</p></td>
<td><p>WIA Feeder item that represents the back page of a document.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FEEDER_FRONT</p></td>
<td><p>Properties include those for feeder-scanner control.</p>
<p>Image-specific and document-specific properties are typically included.</p></td>
<td><p>WIA Feeder item that represents the front page of a document.</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_FILM</p></td>
<td><p>Properties include those for film-scanner control.</p>
<p>Image-specific and document-specific properties are typically included.</p></td>
<td><p>WIA Film items, including child items that represent the individual scanning frames.</p>
<p>However, child items cannot have the <strong>WiaItemTypeFolder</strong> flag.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FINISHED_FILE</p></td>
<td><p>Properties depend on the item type that is reported. For example, <strong>WiaItemTypeImage</strong> should have some image-item properties, such as bits per pixel.</p></td>
<td><p>WIA Storage items, including child items that represent finished file content (in other words, data files such as <em>.jpg</em>, <em>.htm</em>, and <em>.txt</em> files).</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_FLATBED</p></td>
<td><p>Properties include those for flatbed-scanner control.</p>
<p>Image-specific and document-specific properties are typically included.</p></td>
<td><p>WIA Flatbed items, including child items that represent the regions that are being scanned on the scanner's flatbed platen.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_FOLDER</p></td>
<td><p>Properties include those for folder and device naming, access rights, document handling, and document status.</p></td>
<td><p>Items that represent storage units. For scanners with storage, they must have at least one folder scanner item. This item can have subfolder items that represent individual storage items.</p></td>
</tr>
<tr class="even">
<td><p>WIA_CATEGORY_ROOT</p></td>
<td><p>Properties include those for device control, name, access rights, document handling, and device type.</p></td>
<td><p>The root item only.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_CATEGORY_AUTO</p></td>
<td><p>Properties include those for auto-configured scanning. For more information, see <a href="/windows-hardware/drivers/image/wia-properties-supported-by-an-auto-item" data-raw-source="[WIA Properties Supported by an Auto Item](./wia-properties-supported-by-an-auto-item.md)">WIA Properties Supported by an Auto Item</a>.</p></td>
<td><p>WIA auto item that represents the scanner's auto-configured scanning settings.</p></td>
</tr>
</tbody>
</table>

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_ITEM_FLAGS**](wia-ipa-item-flags.md)
