---
title: WIA Driver Services Library
author: windows-driver-content
MS-HAID:
- 'WIA\_arch\_34db7cb6-0927-4926-9cbd-7d7dfcdec80f.xml'
- 'image.wia\_driver\_services\_library'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c179483b-74c3-4788-aa04-20cec0e0eb3a
description: 
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
<td><p>[<strong>wiasCreateChildAppItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549156)</p></td>
<td><p>Creates a new application item and inserts it as a child of the specified (parent) item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasCreateDrvItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549160)</p></td>
<td><p>Creates an <strong>IWiaDrvItem</strong> object.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasGetChildrenContexts</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549224)</p></td>
<td><p>Retrieves an array of item contexts belonging to the current item's children.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasGetContextFromName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549233)</p></td>
<td><p>Retrieves the item context for an item name.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasGetDrvItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549243)</p></td>
<td><p>Retrieves a driver item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasGetRootItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549264)</p></td>
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
<td><p>[<strong>wiasCreateLogInstance</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549163)</p></td>
<td><p>Creates an instance of a logging object.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasDebugError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549170)</p></td>
<td><p>Prints a debug error string in the Device Manager debug console. The output color is always red. This function is provided for compatibility only. In Microsoft Windows XP, it is recommended to use [<strong>WIAS_LERROR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549580) instead.</p>
<p>In Windows Vista, it is recommended to use [<strong>WIAS_ERROR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549565) instead.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasDebugTrace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549178)</p></td>
<td><p>Prints a debug trace string in the Device Manager debug console. This function is provided for compatibility only. In Microsoft Windows XP, it is recommended to use [<strong>WIAS_LTRACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549600) instead.</p>
<p>In Windows Vista, it is recommended to use [<strong>WIA_TRACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549619) instead.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasFormatArgs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549190)</p></td>
<td><p>Formats an argument list into a packaged string for logging.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasPrintDebugHResult</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549287)</p></td>
<td><p>Prints an HRESULT string on the Device Manager debug console. This function is provided for compatibility only. It is obsolete for Windows XP and later, and is no longer supported. Use [<strong>WIAS_LHRESULT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549589) instead.</p></td>
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
<td><p>[<strong>wiasCreatePropContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549167)</p></td>
<td><p>Allocates a property context to indicate which of an item's properties are changing.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasFreePropContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549195)</p></td>
<td><p>Releases the memory occupied by a [<strong>WIA_PROPERTY_CONTEXT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552749) structure.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasGetChangedValueFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549200)</p></td>
<td><p>Determines whether a property with a floating-point value has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasGetChangedValueGuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549211)</p></td>
<td><p>Determines whether a property with a GUID value has been changed by an application.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasGetChangedValueLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549214)</p></td>
<td><p>Determines whether a property with a long integer value has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasGetChangedValueStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549219)</p></td>
<td><p>Determines whether a property with a string value has been changed by an application.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasGetItemType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549255)</p></td>
<td><p>Indicates a root or child item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasGetPropertyAttributes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549257)</p></td>
<td><p>Retrieves the access flags and valid values for a set of properties.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasIsPropChanged</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549271)</p></td>
<td><p>Tests whether the specified property has been changed by an application.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasReadMultiple</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549300)</p></td>
<td><p>Reads multiple properties from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasReadPropBin</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549308)</p></td>
<td><p>Reads a single binary property from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasReadPropFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549320)</p></td>
<td><p>Retrieves a floating-point property value from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasReadPropGuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549325)</p></td>
<td><p>Retrieves a GUID property value from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasReadPropLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549330)</p></td>
<td><p>Retrieves a long integer property value from a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasReadPropStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549341)</p></td>
<td><p>Retrieves a string property value from a WIA item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSetItemPropAttribs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549358)</p></td>
<td><p>Sets the access flags and valid values for an item's set of properties.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasSetItemPropNames</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549369)</p></td>
<td><p>Writes property names to item properties.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSetPropChanged</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549374)</p></td>
<td><p>Modifies a property context to indicate that a property is being changed.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasSetPropertyAttributes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549381)</p></td>
<td><p>Sets the access flags and property values of an item's properties.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSetValidFlag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549390)</p></td>
<td><p>Sets the valid values for a WIA_PROP_FLAG property.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasSetValidListFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549399)</p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_R4.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSetValidListGuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549409)</p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of subtype VT_CLSID.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasSetValidListLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549414)</p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_I4.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSetValidListStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549421)</p></td>
<td><p>Sets the valid values for a WIA_PROP_LIST property of type sub-VT_BSTR.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasSetValidRangeFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549425)</p></td>
<td><p>Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_R4.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSetValidRangeLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549434)</p></td>
<td><p>Specifies the range of valid values for a WIA_PROP_RANGE property of subtype VT_I4.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasUpdateValidFormat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549448)</p></td>
<td><p>Updates the valid format of the property context for the current minidriver.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasValidateItemProperties</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549454)</p></td>
<td><p>Validates a list of simple item properties against their current valid values.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasWriteMultiple</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549475)</p></td>
<td><p>Writes multiple property values to a WIA item (the properties may be of different types).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasWritePropBin</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549500)</p></td>
<td><p>Writes a single binary property value to a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasWritePropFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549507)</p></td>
<td><p>Writes a floating-point property value to a WIA item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasWritePropGuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549512)</p></td>
<td><p>Writes a GUID property value to a WIA item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasWritePropLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549515)</p></td>
<td><p>Writes a long integer property value to a WIA item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasWritePropStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549525)</p></td>
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
<td><p>[<strong>wiasDownSampleBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549185)</p></td>
<td><p>Takes in a buffer of pixel data and downsamples it to the specified size.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasGetImageInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549249)</p></td>
<td><p>Retrieves transfer context information from an item.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasParseEndorserString</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549282)</p></td>
<td><p>Parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with the tokens.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasSendEndOfPage</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549351)</p></td>
<td><p>Calls the client callback routine during a data transfer, sending the current total page count.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasUpdateScanRect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549441)</p></td>
<td><p>Updates the scanning area sizes of the scanning device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiasWriteBufToFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549473)</p></td>
<td><p>Writes the contents of a temporary page buffer to an image file.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiasWritePageBufToFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549484)</p></td>
<td><p>Writes the contents of a temporary page buffer to an image file. Use this function to write a page to a multi-page TIFF file.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Services%20Library%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


