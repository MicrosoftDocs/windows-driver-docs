---
title: IPrinterScriptUsbJobContextReturnCodes interface
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes interface

The IPrinterScriptUsbJobContextReturnCodes interface represents an array of return codes that an IHV has defined for their JavaScript functions.

This interface is returned by the [**IPrinterScriptUsbJobContext::ReturnCodes**](iprinterscriptusbjobcontext-returncodes.md) method.

Members
-------

The **IPrinterScriptUsbJobContextReturnCodes** interface inherits from the [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPrinterScriptUsbJobContextReturnCodes** also has these types of members:

-   [Methods](#methods)

### Methods

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
<td><a href="iprinterscriptusbjobcontextreturncodes-abortthejob.md" data-raw-source="[&lt;strong&gt;AbortTheJob&lt;/strong&gt;](iprinterscriptusbjobcontextreturncodes-abortthejob.md)"><strong>AbortTheJob</strong></a></td>
<td><p>Returns a value of &#39;4&#39; to inform USBMon that the print job must be aborted.</p></td>
</tr>
<tr class="even">
<td><a href="iprinterscriptusbjobcontextreturncodes-devicebusy.md" data-raw-source="[&lt;strong&gt;DeviceBusy&lt;/strong&gt;](iprinterscriptusbjobcontextreturncodes-devicebusy.md)"><strong>DeviceBusy</strong></a></td>
<td><p>Returns a value of &#39;3&#39; to inform USBMon that the device communication channel is not accepting data at this time.</p></td>
</tr>
<tr class="odd">
<td><a href="iprinterscriptusbjobcontextreturncodes-failure.md" data-raw-source="[&lt;strong&gt;Failure&lt;/strong&gt;](iprinterscriptusbjobcontextreturncodes-failure.md)"><strong>Failure</strong></a></td>
<td><p>Returns a value of &#39;1&#39; to inform USBMon that the method call failed.</p></td>
</tr>
<tr class="even">
<td><a href="iprinterscriptusbjobcontextreturncodes-retry.md" data-raw-source="[&lt;strong&gt;Retry&lt;/strong&gt;](iprinterscriptusbjobcontextreturncodes-retry.md)"><strong>Retry</strong></a></td>
<td><p>Returns a value of &#39;2&#39; to inform USBMon that the method call was successful, with more work to be completed.</p></td>
</tr>
<tr class="odd">
<td><a href="iprinterscriptusbjobcontextreturncodes-success.md" data-raw-source="[&lt;strong&gt;Success&lt;/strong&gt;](iprinterscriptusbjobcontextreturncodes-success.md)"><strong>Success</strong></a></td>
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
