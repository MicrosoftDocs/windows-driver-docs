---
title: WIA Driver Services Library
description: Describes the WIA driver services library that contains functions a WIA minidriver can call for assistance in performing specific tasks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Driver Services Library


The WIA driver services library contains functions that a WIA minidriver can call for assistance in performing the following tasks:

-   [Building and Maintaining an Item Tree](#ddk-building-and-maintaining-an-item-tree-si)
-   [Logging Error and Trace Messages](#ddk-logging-error-and-trace-messages-si)
-   [Reading and Storing an Item's Properties](#ddk-reading-and-storing-an-item-s-properties-si)
-   [Updating and Transferring Data](#ddk-updating-and-transferring-data-si)

A WIA minidriver calls most of these functions from its [IWiaMiniDrv Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) methods as needed. Each WIA minidriver, however, must call the [**wiasCreateDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem) function in the [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) method to create driver items. Each successful call to a **wiasCreateDrvItem** function creates an **IWiaDrvItem** item object, which is used in the minidriver's item tree. Several [IWiaDrvItem Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiadrvitem) methods have a parameter of type **IWiaDrvItem**, including the [**IWiaDrvItem::AddItemToFolder**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-additemtofolder), [**IWiaDrvItem::GetFirstChildItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getfirstchilditem), [**IWiaDrvItem::GetNextSiblingItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getnextsiblingitem), and [**IWiaDrvItem::GetParentItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiadrvitem-getparentitem). Also, the [**wiasGetDrvItem**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetdrvitem) function has a parameter of this type.

The driver services library provides the following functions.

## <a href="" id="ddk-building-and-maintaining-an-item-tree-si"></a>Building and Maintaining an Item Tree


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatechildappitem" data-raw-source="[&lt;strong&gt;wiasCreateChildAppItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatechildappitem)"><strong>wiasCreateChildAppItem</strong></a></p></td>
<td><p>Creates a new application item and inserts it as a child of the specified (parent) item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem" data-raw-source="[&lt;strong&gt;wiasCreateDrvItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatedrvitem)"><strong>wiasCreateDrvItem</strong></a></p></td>
<td><p>Creates an <strong>IWiaDrvItem</strong> object.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchildrencontexts" data-raw-source="[&lt;strong&gt;wiasGetChildrenContexts&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchildrencontexts)"><strong>wiasGetChildrenContexts</strong></a></p></td>
<td><p>Retrieves an array of item contexts belonging to the current item's children.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetcontextfromname" data-raw-source="[&lt;strong&gt;wiasGetContextFromName&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetcontextfromname)"><strong>wiasGetContextFromName</strong></a></p></td>
<td><p>Retrieves the item context for an item name.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetdrvitem" data-raw-source="[&lt;strong&gt;wiasGetDrvItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetdrvitem)"><strong>wiasGetDrvItem</strong></a></p></td>
<td><p>Retrieves a driver item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetrootitem" data-raw-source="[&lt;strong&gt;wiasGetRootItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetrootitem)"><strong>wiasGetRootItem</strong></a></p></td>
<td><p>Retrieves the root item context of a specified WIA item.</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="ddk-logging-error-and-trace-messages-si"></a>Logging Error and Trace Messages


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreateloginstance" data-raw-source="[&lt;strong&gt;wiasCreateLogInstance&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreateloginstance)"><strong>wiasCreateLogInstance</strong></a></p></td>
<td><p>Creates an instance of a logging object.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdebugerror" data-raw-source="[&lt;strong&gt;wiasDebugError&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdebugerror)"><strong>wiasDebugError</strong></a></p></td>
<td><p>Prints a debug error string in the Device Manager debug console. The output color is always red. This function is provided for compatibility only. In Microsoft Windows XP, it is recommended to use <a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lerror" data-raw-source="[&lt;strong&gt;WIAS_LERROR&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lerror)"><strong>WIAS_LERROR</strong></a> instead.</p>
<p>In Windows Vista, it is recommended to use <a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_error" data-raw-source="[&lt;strong&gt;WIAS_ERROR&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_error)"><strong>WIAS_ERROR</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdebugtrace" data-raw-source="[&lt;strong&gt;wiasDebugTrace&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdebugtrace)"><strong>wiasDebugTrace</strong></a></p></td>
<td><p>Prints a debug trace string in the Device Manager debug console. This function is provided for compatibility only. In Microsoft Windows XP, it is recommended to use <a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_ltrace" data-raw-source="[&lt;strong&gt;WIAS_LTRACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_ltrace)"><strong>WIAS_LTRACE</strong></a> instead.</p>
<p>In Windows Vista, it is recommended to use <a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_trace" data-raw-source="[&lt;strong&gt;WIA_TRACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_trace)"><strong>WIA_TRACE</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasformatargs" data-raw-source="[&lt;strong&gt;wiasFormatArgs&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasformatargs)"><strong>wiasFormatArgs</strong></a></p></td>
<td><p>Formats an argument list into a packaged string for logging.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasprintdebughresult" data-raw-source="[&lt;strong&gt;wiasPrintDebugHResult&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasprintdebughresult)"><strong>wiasPrintDebugHResult</strong></a></p></td>
<td><p>Prints an HRESULT string on the Device Manager debug console. This function is provided for compatibility only. It is obsolete for Windows XP and later, and is no longer supported. Use <a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lhresult" data-raw-source="[&lt;strong&gt;WIAS_LHRESULT&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lhresult)"><strong>WIAS_LHRESULT</strong></a> instead.</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="ddk-reading-and-storing-an-item-s-properties-si"></a>Reading and Storing an Item's Properties


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext" data-raw-source="[&lt;strong&gt;wiasCreatePropContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext)"><strong>wiasCreatePropContext</strong></a></p></td>
<td><p>Allocates a property context to indicate which of an item's properties are changing.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasfreepropcontext" data-raw-source="[&lt;strong&gt;wiasFreePropContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasfreepropcontext)"><strong>wiasFreePropContext</strong></a></p></td>
<td><p>Releases the memory occupied by a <a href="/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_context" data-raw-source="[&lt;strong&gt;WIA_PROPERTY_CONTEXT&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_context)"><strong>WIA_PROPERTY_CONTEXT</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat" data-raw-source="[&lt;strong&gt;wiasGetChangedValueFloat&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat)"><strong>wiasGetChangedValueFloat</strong></a></p></td>
<td><p>Determines whether a property with a floating-point value has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvalueguid" data-raw-source="[&lt;strong&gt;wiasGetChangedValueGuid&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvalueguid)"><strong>wiasGetChangedValueGuid</strong></a></p></td>
<td><p>Determines whether a property with a GUID value has been changed by an application.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluelong" data-raw-source="[&lt;strong&gt;wiasGetChangedValueLong&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluelong)"><strong>wiasGetChangedValueLong</strong></a></p></td>
<td><p>Determines whether a property with a long integer value has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluestr" data-raw-source="[&lt;strong&gt;wiasGetChangedValueStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluestr)"><strong>wiasGetChangedValueStr</strong></a></p></td>
<td><p>Determines whether a property with a string value has been changed by an application.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetitemtype" data-raw-source="[&lt;strong&gt;wiasGetItemType&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetitemtype)"><strong>wiasGetItemType</strong></a></p></td>
<td><p>Indicates a root or child item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetpropertyattributes" data-raw-source="[&lt;strong&gt;wiasGetPropertyAttributes&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetpropertyattributes)"><strong>wiasGetPropertyAttributes</strong></a></p></td>
<td><p>Retrieves the access flags and valid values for a set of properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasispropchanged" data-raw-source="[&lt;strong&gt;wiasIsPropChanged&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasispropchanged)"><strong>wiasIsPropChanged</strong></a></p></td>
<td><p>Tests whether the specified property has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadmultiple" data-raw-source="[&lt;strong&gt;wiasReadMultiple&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadmultiple)"><strong>wiasReadMultiple</strong></a></p></td>
<td><p>Reads multiple properties from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropbin" data-raw-source="[&lt;strong&gt;wiasReadPropBin&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropbin)"><strong>wiasReadPropBin</strong></a></p></td>
<td><p>Reads a single binary property from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropfloat" data-raw-source="[&lt;strong&gt;wiasReadPropFloat&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropfloat)"><strong>wiasReadPropFloat</strong></a></p></td>
<td><p>Retrieves a floating-point property value from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropguid" data-raw-source="[&lt;strong&gt;wiasReadPropGuid&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropguid)"><strong>wiasReadPropGuid</strong></a></p></td>
<td><p>Retrieves a GUID property value from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadproplong" data-raw-source="[&lt;strong&gt;wiasReadPropLong&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadproplong)"><strong>wiasReadPropLong</strong></a></p></td>
<td><p>Retrieves a long integer property value from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropstr" data-raw-source="[&lt;strong&gt;wiasReadPropStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasreadpropstr)"><strong>wiasReadPropStr</strong></a></p></td>
<td><p>Retrieves a string property value from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetitempropattribs" data-raw-source="[&lt;strong&gt;wiasSetItemPropAttribs&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetitempropattribs)"><strong>wiasSetItemPropAttribs</strong></a></p></td>
<td><p>Sets the access flags and valid values for an item's set of properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetitempropnames" data-raw-source="[&lt;strong&gt;wiasSetItemPropNames&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetitempropnames)"><strong>wiasSetItemPropNames</strong></a></p></td>
<td><p>Writes property names to item properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetpropchanged" data-raw-source="[&lt;strong&gt;wiasSetPropChanged&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetpropchanged)"><strong>wiasSetPropChanged</strong></a></p></td>
<td><p>Modifies a property context to indicate that a property is being changed.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetpropertyattributes" data-raw-source="[&lt;strong&gt;wiasSetPropertyAttributes&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetpropertyattributes)"><strong>wiasSetPropertyAttributes</strong></a></p></td>
<td><p>Sets the access flags and property values of an item's properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidflag" data-raw-source="[&lt;strong&gt;wiasSetValidFlag&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidflag)"><strong>wiasSetValidFlag</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_FLAG property.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistfloat" data-raw-source="[&lt;strong&gt;wiasSetValidListFloat&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistfloat)"><strong>wiasSetValidListFloat</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_R4.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistguid" data-raw-source="[&lt;strong&gt;wiasSetValidListGuid&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistguid)"><strong>wiasSetValidListGuid</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of subtype VT_CLSID.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistlong" data-raw-source="[&lt;strong&gt;wiasSetValidListLong&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidlistlong)"><strong>wiasSetValidListLong</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_I4.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidliststr" data-raw-source="[&lt;strong&gt;wiasSetValidListStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidliststr)"><strong>wiasSetValidListStr</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_BSTR.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidrangefloat" data-raw-source="[&lt;strong&gt;wiasSetValidRangeFloat&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidrangefloat)"><strong>wiasSetValidRangeFloat</strong></a></p></td>
<td><p>Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_R4.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidrangelong" data-raw-source="[&lt;strong&gt;wiasSetValidRangeLong&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassetvalidrangelong)"><strong>wiasSetValidRangeLong</strong></a></p></td>
<td><p>Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_I4.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasupdatevalidformat" data-raw-source="[&lt;strong&gt;wiasUpdateValidFormat&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasupdatevalidformat)"><strong>wiasUpdateValidFormat</strong></a></p></td>
<td><p>Updates the valid format of the property context for the current minidriver.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasvalidateitemproperties" data-raw-source="[&lt;strong&gt;wiasValidateItemProperties&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasvalidateitemproperties)"><strong>wiasValidateItemProperties</strong></a></p></td>
<td><p>Validates a list of simple item properties against their current valid values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritemultiple" data-raw-source="[&lt;strong&gt;wiasWriteMultiple&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritemultiple)"><strong>wiasWriteMultiple</strong></a></p></td>
<td><p>Writes multiple property values to a WIA item (the properties may be of different types).</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropbin" data-raw-source="[&lt;strong&gt;wiasWritePropBin&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropbin)"><strong>wiasWritePropBin</strong></a></p></td>
<td><p>Writes a single binary property value to a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropfloat" data-raw-source="[&lt;strong&gt;wiasWritePropFloat&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropfloat)"><strong>wiasWritePropFloat</strong></a></p></td>
<td><p>Writes a floating-point property value to a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropguid" data-raw-source="[&lt;strong&gt;wiasWritePropGuid&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropguid)"><strong>wiasWritePropGuid</strong></a></p></td>
<td><p>Writes a GUID property value to a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswriteproplong" data-raw-source="[&lt;strong&gt;wiasWritePropLong&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswriteproplong)"><strong>wiasWritePropLong</strong></a></p></td>
<td><p>Writes a long integer property value to a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropstr" data-raw-source="[&lt;strong&gt;wiasWritePropStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropstr)"><strong>wiasWritePropStr</strong></a></p></td>
<td><p>Writes a string property value to a WIA item.</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="ddk-updating-and-transferring-data-si"></a>Updating and Transferring Data


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdownsamplebuffer" data-raw-source="[&lt;strong&gt;wiasDownSampleBuffer&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasdownsamplebuffer)"><strong>wiasDownSampleBuffer</strong></a></p></td>
<td><p>Takes in a buffer of pixel data and downsamples it to the specified size.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetimageinformation" data-raw-source="[&lt;strong&gt;wiasGetImageInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetimageinformation)"><strong>wiasGetImageInformation</strong></a></p></td>
<td><p>Retrieves transfer context information from an item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasparseendorserstring" data-raw-source="[&lt;strong&gt;wiasParseEndorserString&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasparseendorserstring)"><strong>wiasParseEndorserString</strong></a></p></td>
<td><p>Parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with the tokens.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassendendofpage" data-raw-source="[&lt;strong&gt;wiasSendEndOfPage&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiassendendofpage)"><strong>wiasSendEndOfPage</strong></a></p></td>
<td><p>Calls the client callback routine during a data transfer, sending the current total page count.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasupdatescanrect" data-raw-source="[&lt;strong&gt;wiasUpdateScanRect&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasupdatescanrect)"><strong>wiasUpdateScanRect</strong></a></p></td>
<td><p>Updates the scanning area sizes of the scanning device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritebuftofile" data-raw-source="[&lt;strong&gt;wiasWriteBufToFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritebuftofile)"><strong>wiasWriteBufToFile</strong></a></p></td>
<td><p>Writes the contents of a temporary page buffer to an image file.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepagebuftofile" data-raw-source="[&lt;strong&gt;wiasWritePageBufToFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepagebuftofile)"><strong>wiasWritePageBufToFile</strong></a></p></td>
<td><p>Writes the contents of a temporary page buffer to an image file. Use this function to write a page to a multi-page TIFF file.</p></td>
</tr>
</tbody>
</table>

 

