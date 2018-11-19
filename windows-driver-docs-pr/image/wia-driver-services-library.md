---
title: WIA Driver Services Library
ms.assetid: c179483b-74c3-4788-aa04-20cec0e0eb3a
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

A WIA minidriver calls most of these functions from its [IWiaMiniDrv Interface](https://msdn.microsoft.com/library/windows/hardware/ff545027) methods as needed. Each WIA minidriver, however, must call the [**wiasCreateDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549160) function in the [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986) method to create driver items. Each successful call to a **wiasCreateDrvItem** function creates an **IWiaDrvItem** item object, which is used in the minidriver's item tree. Several [IWiaDrvItem Interface](https://msdn.microsoft.com/library/windows/hardware/ff543896) methods have a parameter of type **IWiaDrvItem**, including the [**IWiaDrvItem::AddItemToFolder**](https://msdn.microsoft.com/library/windows/hardware/ff543856), [**IWiaDrvItem::GetFirstChildItem**](https://msdn.microsoft.com/library/windows/hardware/ff543878), [**IWiaDrvItem::GetNextSiblingItem**](https://msdn.microsoft.com/library/windows/hardware/ff543889), and [**IWiaDrvItem::GetParentItem**](https://msdn.microsoft.com/library/windows/hardware/ff543892). Also, the [**wiasGetDrvItem**](https://msdn.microsoft.com/library/windows/hardware/ff549243) function has a parameter of this type.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549156" data-raw-source="[&lt;strong&gt;wiasCreateChildAppItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549156)"><strong>wiasCreateChildAppItem</strong></a></p></td>
<td><p>Creates a new application item and inserts it as a child of the specified (parent) item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549160" data-raw-source="[&lt;strong&gt;wiasCreateDrvItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549160)"><strong>wiasCreateDrvItem</strong></a></p></td>
<td><p>Creates an <strong>IWiaDrvItem</strong> object.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549224" data-raw-source="[&lt;strong&gt;wiasGetChildrenContexts&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549224)"><strong>wiasGetChildrenContexts</strong></a></p></td>
<td><p>Retrieves an array of item contexts belonging to the current item&#39;s children.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549233" data-raw-source="[&lt;strong&gt;wiasGetContextFromName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549233)"><strong>wiasGetContextFromName</strong></a></p></td>
<td><p>Retrieves the item context for an item name.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549243" data-raw-source="[&lt;strong&gt;wiasGetDrvItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549243)"><strong>wiasGetDrvItem</strong></a></p></td>
<td><p>Retrieves a driver item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549264" data-raw-source="[&lt;strong&gt;wiasGetRootItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549264)"><strong>wiasGetRootItem</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549163" data-raw-source="[&lt;strong&gt;wiasCreateLogInstance&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549163)"><strong>wiasCreateLogInstance</strong></a></p></td>
<td><p>Creates an instance of a logging object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549170" data-raw-source="[&lt;strong&gt;wiasDebugError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549170)"><strong>wiasDebugError</strong></a></p></td>
<td><p>Prints a debug error string in the Device Manager debug console. The output color is always red. This function is provided for compatibility only. In Microsoft Windows XP, it is recommended to use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549580" data-raw-source="[&lt;strong&gt;WIAS_LERROR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549580)"><strong>WIAS_LERROR</strong></a> instead.</p>
<p>In Windows Vista, it is recommended to use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549565" data-raw-source="[&lt;strong&gt;WIAS_ERROR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549565)"><strong>WIAS_ERROR</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549178" data-raw-source="[&lt;strong&gt;wiasDebugTrace&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549178)"><strong>wiasDebugTrace</strong></a></p></td>
<td><p>Prints a debug trace string in the Device Manager debug console. This function is provided for compatibility only. In Microsoft Windows XP, it is recommended to use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549600" data-raw-source="[&lt;strong&gt;WIAS_LTRACE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549600)"><strong>WIAS_LTRACE</strong></a> instead.</p>
<p>In Windows Vista, it is recommended to use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549619" data-raw-source="[&lt;strong&gt;WIA_TRACE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549619)"><strong>WIA_TRACE</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549190" data-raw-source="[&lt;strong&gt;wiasFormatArgs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549190)"><strong>wiasFormatArgs</strong></a></p></td>
<td><p>Formats an argument list into a packaged string for logging.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549287" data-raw-source="[&lt;strong&gt;wiasPrintDebugHResult&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549287)"><strong>wiasPrintDebugHResult</strong></a></p></td>
<td><p>Prints an HRESULT string on the Device Manager debug console. This function is provided for compatibility only. It is obsolete for Windows XP and later, and is no longer supported. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549589" data-raw-source="[&lt;strong&gt;WIAS_LHRESULT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549589)"><strong>WIAS_LHRESULT</strong></a> instead.</p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549167" data-raw-source="[&lt;strong&gt;wiasCreatePropContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549167)"><strong>wiasCreatePropContext</strong></a></p></td>
<td><p>Allocates a property context to indicate which of an item&#39;s properties are changing.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549195" data-raw-source="[&lt;strong&gt;wiasFreePropContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549195)"><strong>wiasFreePropContext</strong></a></p></td>
<td><p>Releases the memory occupied by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552749" data-raw-source="[&lt;strong&gt;WIA_PROPERTY_CONTEXT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552749)"><strong>WIA_PROPERTY_CONTEXT</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549200" data-raw-source="[&lt;strong&gt;wiasGetChangedValueFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549200)"><strong>wiasGetChangedValueFloat</strong></a></p></td>
<td><p>Determines whether a property with a floating-point value has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549211" data-raw-source="[&lt;strong&gt;wiasGetChangedValueGuid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549211)"><strong>wiasGetChangedValueGuid</strong></a></p></td>
<td><p>Determines whether a property with a GUID value has been changed by an application.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549214" data-raw-source="[&lt;strong&gt;wiasGetChangedValueLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549214)"><strong>wiasGetChangedValueLong</strong></a></p></td>
<td><p>Determines whether a property with a long integer value has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549219" data-raw-source="[&lt;strong&gt;wiasGetChangedValueStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549219)"><strong>wiasGetChangedValueStr</strong></a></p></td>
<td><p>Determines whether a property with a string value has been changed by an application.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549255" data-raw-source="[&lt;strong&gt;wiasGetItemType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549255)"><strong>wiasGetItemType</strong></a></p></td>
<td><p>Indicates a root or child item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549257" data-raw-source="[&lt;strong&gt;wiasGetPropertyAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549257)"><strong>wiasGetPropertyAttributes</strong></a></p></td>
<td><p>Retrieves the access flags and valid values for a set of properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549271" data-raw-source="[&lt;strong&gt;wiasIsPropChanged&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549271)"><strong>wiasIsPropChanged</strong></a></p></td>
<td><p>Tests whether the specified property has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549300" data-raw-source="[&lt;strong&gt;wiasReadMultiple&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549300)"><strong>wiasReadMultiple</strong></a></p></td>
<td><p>Reads multiple properties from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549308" data-raw-source="[&lt;strong&gt;wiasReadPropBin&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549308)"><strong>wiasReadPropBin</strong></a></p></td>
<td><p>Reads a single binary property from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549320" data-raw-source="[&lt;strong&gt;wiasReadPropFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549320)"><strong>wiasReadPropFloat</strong></a></p></td>
<td><p>Retrieves a floating-point property value from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549325" data-raw-source="[&lt;strong&gt;wiasReadPropGuid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549325)"><strong>wiasReadPropGuid</strong></a></p></td>
<td><p>Retrieves a GUID property value from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549330" data-raw-source="[&lt;strong&gt;wiasReadPropLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549330)"><strong>wiasReadPropLong</strong></a></p></td>
<td><p>Retrieves a long integer property value from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549341" data-raw-source="[&lt;strong&gt;wiasReadPropStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549341)"><strong>wiasReadPropStr</strong></a></p></td>
<td><p>Retrieves a string property value from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549358" data-raw-source="[&lt;strong&gt;wiasSetItemPropAttribs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549358)"><strong>wiasSetItemPropAttribs</strong></a></p></td>
<td><p>Sets the access flags and valid values for an item&#39;s set of properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549369" data-raw-source="[&lt;strong&gt;wiasSetItemPropNames&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549369)"><strong>wiasSetItemPropNames</strong></a></p></td>
<td><p>Writes property names to item properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549374" data-raw-source="[&lt;strong&gt;wiasSetPropChanged&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549374)"><strong>wiasSetPropChanged</strong></a></p></td>
<td><p>Modifies a property context to indicate that a property is being changed.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549381" data-raw-source="[&lt;strong&gt;wiasSetPropertyAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549381)"><strong>wiasSetPropertyAttributes</strong></a></p></td>
<td><p>Sets the access flags and property values of an item&#39;s properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549390" data-raw-source="[&lt;strong&gt;wiasSetValidFlag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549390)"><strong>wiasSetValidFlag</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_FLAG property.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549399" data-raw-source="[&lt;strong&gt;wiasSetValidListFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549399)"><strong>wiasSetValidListFloat</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_R4.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549409" data-raw-source="[&lt;strong&gt;wiasSetValidListGuid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549409)"><strong>wiasSetValidListGuid</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of subtype VT_CLSID.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549414" data-raw-source="[&lt;strong&gt;wiasSetValidListLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549414)"><strong>wiasSetValidListLong</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_I4.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549421" data-raw-source="[&lt;strong&gt;wiasSetValidListStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549421)"><strong>wiasSetValidListStr</strong></a></p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_BSTR.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549425" data-raw-source="[&lt;strong&gt;wiasSetValidRangeFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549425)"><strong>wiasSetValidRangeFloat</strong></a></p></td>
<td><p>Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_R4.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549434" data-raw-source="[&lt;strong&gt;wiasSetValidRangeLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549434)"><strong>wiasSetValidRangeLong</strong></a></p></td>
<td><p>Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_I4.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549448" data-raw-source="[&lt;strong&gt;wiasUpdateValidFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549448)"><strong>wiasUpdateValidFormat</strong></a></p></td>
<td><p>Updates the valid format of the property context for the current minidriver.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549454" data-raw-source="[&lt;strong&gt;wiasValidateItemProperties&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549454)"><strong>wiasValidateItemProperties</strong></a></p></td>
<td><p>Validates a list of simple item properties against their current valid values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549475" data-raw-source="[&lt;strong&gt;wiasWriteMultiple&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549475)"><strong>wiasWriteMultiple</strong></a></p></td>
<td><p>Writes multiple property values to a WIA item (the properties may be of different types).</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549500" data-raw-source="[&lt;strong&gt;wiasWritePropBin&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549500)"><strong>wiasWritePropBin</strong></a></p></td>
<td><p>Writes a single binary property value to a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549507" data-raw-source="[&lt;strong&gt;wiasWritePropFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549507)"><strong>wiasWritePropFloat</strong></a></p></td>
<td><p>Writes a floating-point property value to a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549512" data-raw-source="[&lt;strong&gt;wiasWritePropGuid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549512)"><strong>wiasWritePropGuid</strong></a></p></td>
<td><p>Writes a GUID property value to a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549515" data-raw-source="[&lt;strong&gt;wiasWritePropLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549515)"><strong>wiasWritePropLong</strong></a></p></td>
<td><p>Writes a long integer property value to a WIA item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549525" data-raw-source="[&lt;strong&gt;wiasWritePropStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549525)"><strong>wiasWritePropStr</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549185" data-raw-source="[&lt;strong&gt;wiasDownSampleBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549185)"><strong>wiasDownSampleBuffer</strong></a></p></td>
<td><p>Takes in a buffer of pixel data and downsamples it to the specified size.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549249" data-raw-source="[&lt;strong&gt;wiasGetImageInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549249)"><strong>wiasGetImageInformation</strong></a></p></td>
<td><p>Retrieves transfer context information from an item.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549282" data-raw-source="[&lt;strong&gt;wiasParseEndorserString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549282)"><strong>wiasParseEndorserString</strong></a></p></td>
<td><p>Parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with the tokens.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549351" data-raw-source="[&lt;strong&gt;wiasSendEndOfPage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549351)"><strong>wiasSendEndOfPage</strong></a></p></td>
<td><p>Calls the client callback routine during a data transfer, sending the current total page count.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549441" data-raw-source="[&lt;strong&gt;wiasUpdateScanRect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549441)"><strong>wiasUpdateScanRect</strong></a></p></td>
<td><p>Updates the scanning area sizes of the scanning device.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549473" data-raw-source="[&lt;strong&gt;wiasWriteBufToFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549473)"><strong>wiasWriteBufToFile</strong></a></p></td>
<td><p>Writes the contents of a temporary page buffer to an image file.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549484" data-raw-source="[&lt;strong&gt;wiasWritePageBufToFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549484)"><strong>wiasWritePageBufToFile</strong></a></p></td>
<td><p>Writes the contents of a temporary page buffer to an image file. Use this function to write a page to a multi-page TIFF file.</p></td>
</tr>
</tbody>
</table>

 

 

 




