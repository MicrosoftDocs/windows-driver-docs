---
title: WIA_IPA_ITEM_CATEGORY
description: The WIA_IPA_ITEM_CATEGORY property contains grouped categories for WIA items.
keywords: ["WIA_IPA_ITEM_CATEGORY Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_ITEM_CATEGORY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/11/2023
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
| WIA_CATEGORY_FEEDER | A feeder item that is a programmable data source that follows the standard rules and that has the WIA properties that are required to support document feeders. |
| WIA_CATEGORY_FEEDER_BACK | A programmable data source item that describes the back side data source of a duplex base feeder item (WIA_CATEGORY_FEEDER). |
| WIA_CATEGORY_FEEDER_FRONT | A programmable data source item that describes the front side data source of a duplex base feeder item (WIA_CATEGORY_FEEDER). |
| WIA_CATEGORY_FILM | A film item that is a programmable data source that follows the standard rules and that has the WIA properties that are required to support film-scanning units. |
| WIA_CATEGORY_FINISHED_FILE | *Not* a programmable data source. The device provides data in a finished file format or in a folder item that contains the finished-file-format item. |
| WIA_CATEGORY_FLATBED | A flatbed item that is a programmable data source that follows the standard rules and that has the WIA properties that are required to support flatbed-platen scanning. |
| WIA_CATEGORY_FOLDER | A folder storage item (not a programmable data source) containing other folder items and/or finished files. |
| WIA_CATEGORY_IMPRINTER | The imprinting category of a programmable data source item that represents both imprinting and endorsing, and can be transfer enabled to upload and download the data content to be printed/endorsed. |
| WIA_CATEGORY_MICR_READER | A (Magnetic Ink Character Recognition) MICR reader item that is a programmable data source, transfer enabled to download MICR text. |
| WIA_CATEGORY_PATCH_CODE_READER | A patch code reader item that is a programmable data source, transfer enabled to download patch code metadata. |
| WIA_CATEGORY_ROOT | The root item for the device. |
| WIA_CATEGORY_AUTO | In Windows 7 and later, an [auto item](./auto-item.md) has the WIA properties that are required to support [auto-configured scanning](./auto-configured-scanning.md). |

The preceding categories define how a WIA item should be treated or used. For example, if the item represents a finished file, you can assume that the data is static and located on the device. If the item represents a feeder, you can expect it to contain the required document-feeder properties and to operate like a document feeder. For more information about these categories, see [WIA Item Categories](./wia-item-categories.md).

The following table shows the WIA grouped categories and their item flags. This table doesn't include a full list of all of the WIA item flags that WIA defines. For a complete list of these flags, see [**WIA_IPA_ITEM_FLAGS**](wia-ipa-item-flags.md).

| WIA category | WIA item flags |
|--|--|
| WIA_CATEGORY_BARCODE_READER | WiaItemTypeProgrammableDataSource<br><br>**Required**<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeFile |
| WIA_CATEGORY_ENDORSER | WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeImage<br><br>**Optional**<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeFile |
| WIA_CATEGORY_FEEDER | **Required**<br><br>WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeImage<br><br>WiaItemTypeFile<br><br>**Optional**<br><br>WiaItemTypeFolder<br><br>(ADF root item only, if WIA_CATEGORY_FEEDER_FRONT and WIA_CATEGORY_FEEDER_BACK items are present) |
| WIA_CATEGORY_FEEDER_BACK | **Required**<br><br>WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeImage<br><br>WiaItemTypeFile<br><br>**Optional**<br><br>*None* |
| WIA_CATEGORY_FEEDER_FRONT | **Required**<br><br>WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeImage<br><br>WiaItemTypeFile<br><br>**Optional**<br><br>*None* |
| WIA_CATEGORY_FILM | **Required**<br><br>WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeImage<br><br>WiaItemTypeFile<br><br>WiaItemTypeFolder<br><br>**Optional**<br><br>*None* |
| WIA_CATEGORY_FINISHED_FILE | **Required**<br><br>WiaItemTypeFile<br><br>WiaItemTypeTransfer<br><br>**Optional**<br><br>WiaItemTypeImage<br><br>WiaItemTypeAudio<br><br>WiaItemTypeDeleted |
| WIA_CATEGORY_FLATBED | **Required**<br><br>WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeImage<br><br>WiaItemTypeFile<br><br>**Optional**<br><br>WiaItemTypeFolder<br><br>(On the FB root item only if multiple scan regions items are supported) |
| WIA_CATEGORY_FOLDER | **Required**<br><br>WiaItemTypeStorage<br><br>WiaItemTypeFolder<br><br>**Optional**<br><br>WiaItemTypeDeleted |
| WIA_CATEGORY_IMPRINTER | WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeImage<br><br>**Optional**<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeFile |
| WIA_CATEGORY_MICR_READER | WiaItemTypeProgrammableDataSource<br><br>**Required**<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeFile |
| WIA_CATEGORY_PATCH_CODE_READER | WiaItemTypeProgrammableDataSource<br><br>**Required**<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeFile |
| WIA_CATEGORY_ROOT | **Required**<br><br>WiaItemTypeRoot<br><br>WiaItemTypeFolder<br><br>**Optional**<br><br>WiaItemTypeDevice<br><br>WiaItemTypeDisconnected |
| WIA_CATEGORY_AUTO | **Required**<br><br>WiaItemTypeProgrammableDataSource<br><br>WiaItemTypeTransfer<br><br>WiaItemTypeImage<br><br>WiaItemTypeFile<br><br>**Optional**<br><br>*None* |

The following table shows the WIA grouped categories and their WIA properties and WIA items.

| WIA category | WIA properties | WIA items |
|--|--|--|
| WIA_CATEGORY_FEEDER | Properties include those for feeder-scanner control.<br><br>Image-specific and document-specific properties are typically included. | WIA Feeder items, including child items that represent the front and back pages of a document. |
| WIA_CATEGORY_FEEDER_BACK | Properties include those for feeder-scanner control.<br><br>Image-specific and document-specific properties are typically included. | WIA Feeder item that represents the back page of a document. |
| WIA_CATEGORY_FEEDER_FRONT | Properties include those for feeder-scanner control.<br><br>Image-specific and document-specific properties are typically included. | WIA Feeder item that represents the front page of a document. |
| WIA_CATEGORY_FILM | Properties include those for film-scanner control.<br><br>Image-specific and document-specific properties are typically included. | WIA Film items, including child items that represent the individual scanning frames.<br><br>However, child items can't have the **WiaItemTypeFolder** flag. |
| WIA_CATEGORY_FINISHED_FILE | Properties depend on the item type that is reported. For example, **WiaItemTypeImage** should have some image-item properties, such as bits per pixel. | WIA Storage items, including child items that represent finished file content (in other words, data files such as *.jpg*, *.htm*, and *.txt* files). |
| WIA_CATEGORY_FLATBED | Properties include those for flatbed-scanner control.<br><br>Image-specific and document-specific properties are typically included. | WIA Flatbed items, including child items that represent the regions that are being scanned on the scanner's flatbed platen. |
| WIA_CATEGORY_FOLDER | Properties include those for folder and device naming, access rights, document handling, and document status. | Items that represent storage units. For scanners with storage, they must have at least one folder scanner item. This item can have subfolder items that represent individual storage items. |
| WIA_CATEGORY_ROOT | Properties include those for device control, name, access rights, document handling, and device type. | The root item only. |
| WIA_CATEGORY_AUTO | Properties include those for auto-configured scanning. For more information, see [WIA Properties Supported by an Auto Item](./wia-properties-supported-by-an-auto-item.md) | WIA auto item that represents the scanner's auto-configured scanning settings. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_ITEM_FLAGS**](wia-ipa-item-flags.md)
