---
title: WIA Driver Services Library
description: Describes the WIA driver services library that contains functions a WIA minidriver can call for assistance in performing specific tasks.
ms.date: 05/11/2023
---

# WIA driver services library

The WIA driver services library contains functions that a WIA minidriver can call for assistance in performing the following tasks:

- [Build and maintain an item tree](#build-and-maintain-an-item-tree)

- [Log error and trace messages](#log-error-and-trace-messages)

- [Read and store item properties](#read-and-store-item-properties)

- [Update and transfer data](#update-and-transfer-data)

A WIA minidriver calls most of these functions from its [IWiaMiniDrv Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) methods as needed. Each WIA minidriver, however, must call the [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem) function in the [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) method to create driver items. Each successful call to a **wiasCreateDrvItem** function creates an **IWiaDrvItem** item object, which is used in the minidriver's item tree. Several [IWiaDrvItem Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem) methods have a parameter of type **IWiaDrvItem**, including the [**IWiaDrvItem::AddItemToFolder**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-additemtofolder), [**IWiaDrvItem::GetFirstChildItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getfirstchilditem), [**IWiaDrvItem::GetNextSiblingItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getnextsiblingitem), and [**IWiaDrvItem::GetParentItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getparentitem). Also, the [**wiasGetDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetdrvitem) function has a parameter of this type.

The driver services library provides the following functions.

## Build and maintain an item tree

| Function | Description |
|--|--|
| [**wiasCreateChildAppItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatechildappitem) | Creates a new application item and inserts it as a child of the specified (parent) item. |
| [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem) | Creates an **IWiaDrvItem** object. |
| [**wiasGetChildrenContexts**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchildrencontexts) | Retrieves an array of item contexts belonging to the current item's children. |
| [**wiasGetContextFromName**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetcontextfromname) | Retrieves the item context for an item name. |
| [**wiasGetDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetdrvitem) | Retrieves a driver item. |
| [**wiasGetRootItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetrootitem) | Retrieves the root item context of a specified WIA item. |

## Log error and trace messages

| Function | Description |
|--|--|
| [**wiasCreateLogInstance**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreateloginstance) | Creates an instance of a logging object. |
| [**wiasDebugError**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdebugerror) | Prints a debug error string in the Device Manager debug console. The output color is always red. This function is provided for compatibility only. It is recommended to use [**WIAS_ERROR**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_error) instead. |
| [**wiasDebugTrace**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdebugtrace) | Prints a debug trace string in the Device Manager debug console. This function is provided for compatibility only. It is recommended to use [**WIA_TRACE**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_trace) instead. |
| [**wiasFormatArgs**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasformatargs) | Formats an argument list into a packaged string for logging. |
| [**wiasPrintDebugHResult**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasprintdebughresult) | Prints an HRESULT string on the Device Manager debug console. This function is provided for compatibility only. It is obsolete and is no longer supported. Use [**WIAS_LHRESULT**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lhresult) instead. |

## Read and store item properties

| Function | Description |
|--|--|
| [**wiasCreatePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext) | Allocates a property context to indicate which of an item's properties are changing. |
| [**wiasFreePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasfreepropcontext) | Releases the memory occupied by a [**WIA_PROPERTY_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_context) structure. |
| [**wiasGetChangedValueFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat) | Determines whether a property with a floating-point value has been changed by an application. |
| [**wiasGetChangedValueGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvalueguid) | Determines whether a property with a GUID value has been changed by an application. |
| [**wiasGetChangedValueLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluelong) | Determines whether a property with a long integer value has been changed by an application. |
| [**wiasGetChangedValueStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluestr) | Determines whether a property with a string value has been changed by an application. |
| [**wiasGetItemType**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetitemtype) | Indicates a root or child item. |
| [**wiasGetPropertyAttributes**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetpropertyattributes) | Retrieves the access flags and valid values for a set of properties. |
| [**wiasIsPropChanged**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasispropchanged) | Tests whether the specified property has been changed by an application. |
| [**wiasReadMultiple**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadmultiple) | Reads multiple properties from a WIA item. |
| [**wiasReadPropBin**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropbin) | Reads a single binary property from a WIA item. |
| [**wiasReadPropFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropfloat) | Retrieves a floating-point property value from a WIA item. |
| [**wiasReadPropGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropguid) | Retrieves a GUID property value from a WIA item. |
| [**wiasReadPropLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadproplong) | Retrieves a long integer property value from a WIA item. |
| [**wiasReadPropStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropstr) | Retrieves a string property value from a WIA item. |
| [**wiasSetItemPropAttribs**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetitempropattribs) | Sets the access flags and valid values for an item's set of properties. |
| [**wiasSetItemPropNames**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetitempropnames) | Writes property names to item properties. |
| [**wiasSetPropChanged**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetpropchanged) | Modifies a property context to indicate that a property is being changed. |
| [**wiasSetPropertyAttributes**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetpropertyattributes) | Sets the access flags and property values of an item's properties. |
| [**wiasSetValidFlag**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidflag) | Sets the valid values for a WIA_PROP_FLAG property. |
| [**wiasSetValidListFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistfloat) | Sets the valid values for a WIA_PROP_LIST property of type sub-VT_R4. |
| [**wiasSetValidListGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistguid) | Sets the valid values for a WIA_PROP_LIST property of subtype VT_CLSID. |
| [**wiasSetValidListLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistlong) | Sets the valid values for a WIA_PROP_LIST property of type sub-VT_I4. |
| [**wiasSetValidListStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidliststr) | Sets the valid values for a WIA_PROP_LIST property of type sub-VT_BSTR. |
| [**wiasSetValidRangeFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidrangefloat) | Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_R4. |
| [**wiasSetValidRangeLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidrangelong) | Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_I4. |
| [**wiasUpdateValidFormat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasupdatevalidformat) | Updates the valid format of the property context for the current minidriver. |
| [**wiasValidateItemProperties**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasvalidateitemproperties) | Validates a list of simple item properties against their current valid values. |
| [**wiasWriteMultiple**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritemultiple) | Writes multiple property values to a WIA item (the properties may be of different types). |
| [**wiasWritePropBin**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropbin) | Writes a single binary property value to a WIA item. |
| [**wiasWritePropFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropfloat) | Writes a floating-point property value to a WIA item. |
| [**wiasWritePropGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropguid) | Writes a GUID property value to a WIA item. |
| [**wiasWritePropLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswriteproplong) | Writes a long integer property value to a WIA item. |
| [**wiasWritePropStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropstr) | Writes a string property value to a WIA item. |

## Update and transfer data

| Function | Description |
|--|--|
| [**wiasDownSampleBuffer**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdownsamplebuffer) | Takes in a buffer of pixel data and downsamples it to the specified size. |
| [**wiasGetImageInformation**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetimageinformation) | Retrieves transfer context information from an item. |
| [**wiasParseEndorserString**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasparseendorserstring) | Parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with the tokens. |
| [**wiasSendEndOfPage**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassendendofpage) | Calls the client callback routine during a data transfer, sending the current total page count. |
| [**wiasUpdateScanRect**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasupdatescanrect) | Updates the scanning area sizes of the scanning device. |
| [**wiasWriteBufToFile**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritebuftofile) | Writes the contents of a temporary page buffer to an image file. |
| [**wiasWritePageBufToFile**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepagebuftofile) | Writes the contents of a temporary page buffer to an image file. Use this function to write a page to a multi-page TIFF file. |
