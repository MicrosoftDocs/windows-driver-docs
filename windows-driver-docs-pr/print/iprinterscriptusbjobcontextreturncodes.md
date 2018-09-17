---
title: IPrinterScriptUsbJobContextReturnCodes interface
author: windows-driver-content
description: The IPrinterScriptUsbJobContextReturnCodes interface represents an array of return codes that an IHV has defined for their JavaScript functions.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8E34748E-B9F9-4404-9B40-04EA72EEA322
keywords: ["IPrinterScriptUsbJobContextReturnCodes interface Print Devices", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContextReturnCodes
api_type:
- COM
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes interface


The IPrinterScriptUsbJobContextReturnCodes interface represents an array of return codes that an IHV has defined for their JavaScript functions.

This interface is returned by the [**IPrinterScriptUsbJobContext::ReturnCodes**](iprinterscriptusbjobcontext-returncodes.md) method.

Members
-------

The **IPrinterScriptUsbJobContextReturnCodes** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPrinterScriptUsbJobContextReturnCodes** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPrinterScriptUsbJobContextReturnCodes** interface has these methods.

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
<td>[<strong>AbortTheJob</strong>](iprinterscriptusbjobcontextreturncodes-abortthejob.md)</td>
<td><p>Returns a value of '4' to inform USBMon that the print job must be aborted.</p></td>
</tr>
<tr class="even">
<td>[<strong>DeviceBusy</strong>](iprinterscriptusbjobcontextreturncodes-devicebusy.md)</td>
<td><p>Returns a value of '3' to inform USBMon that the device communication channel is not accepting data at this time.</p></td>
</tr>
<tr class="odd">
<td>[<strong>Failure</strong>](iprinterscriptusbjobcontextreturncodes-failure.md)</td>
<td><p>Returns a value of '1' to inform USBMon that the method call failed.</p></td>
</tr>
<tr class="even">
<td>[<strong>Retry</strong>](iprinterscriptusbjobcontextreturncodes-retry.md)</td>
<td><p>Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed.</p></td>
</tr>
<tr class="odd">
<td>[<strong>Success</strong>](iprinterscriptusbjobcontextreturncodes-success.md)</td>
<td><p>Returns a value of zero (0) to inform USBMon that the function call completed successfully.</p></td>
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

 

 




