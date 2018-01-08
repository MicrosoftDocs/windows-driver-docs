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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContextReturnCodes%20interface%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




