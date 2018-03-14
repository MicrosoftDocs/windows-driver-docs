---
title: IPrinterScriptUsbJobContext interface
author: windows-driver-content
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

 

 




