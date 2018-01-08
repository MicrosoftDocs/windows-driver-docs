---
title: IPrinterScriptUsbJobContext interface
description: The IPrinterScriptUsbJobContext interface is passed as a parameter to the startPrintJob JavaScript function.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 236F6B00-39D8-4084-BAE0-C349AD550040
keywords: ["IPrinterScriptUsbJobContext interface Print Devices", "IPrinterScriptUsbJobContext interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContext
api_type:
- COM
---

# IPrinterScriptUsbJobContext interface


The IPrinterScriptUsbJobContext interface is passed as a parameter to the **startPrintJob** JavaScript function.

Members
-------

The **IPrinterScriptUsbJobContext** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPrinterScriptUsbJobContext** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPrinterScriptUsbJobContext** interface has these methods.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>JobPropertyBag</strong>](iprinterscriptusbjobcontext-jobpropertybag.md)</td>
<td><p>Returns the property bag associated with the current print job.</p></td>
</tr>
<tr class="even">
<td>[<strong>PrintedPageCount</strong>](iprinterscriptusbjobcontext-printedpagecount.md)</td>
<td><p>Returns the number of pages that have been printed by the print device in the current job.</p></td>
</tr>
<tr class="odd">
<td>[<strong>PrintedPageCount</strong>](iprinterscriptusbjobcontext-printedpagecount-in.md)</td>
<td><p>Sets the number of pages that have been printed by the print device in the current job.</p></td>
</tr>
<tr class="even">
<td>[<strong>ReturnCodes</strong>](iprinterscriptusbjobcontext-returncodes.md)</td>
<td><p>Returns an object that can supply return code values that an IHV has defined for their JavaScript functions.</p></td>
</tr>
<tr class="odd">
<td>[<strong>TemporaryStreams</strong>](iprinterscriptusbjobcontext-temporarystreams.md)</td>
<td><p>Returns an array of [IPrinterScriptableSequentialStream](https://msdn.microsoft.com/library/windows/hardware/hh439697) interfaces for the persistent data streams that can be used by the IHV JavaScript functions for the current job.</p></td>
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
<td><p>Minimum supported client</p></td>
<td><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012 R2</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContext%20interface%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




