---
title: IPrinterScriptUsbWritePrintDataProgress interface
author: windows-driver-content
description: The IPrinterScriptUsbWritePrintDataProgress interface is passed as a parameter in the writePrintData JavaScript function call.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: E22725DA-2BD5-4FBC-A3E4-A3C5678A9E57
keywords: ["IPrinterScriptUsbWritePrintDataProgress interface Print Devices", "IPrinterScriptUsbWritePrintDataProgress interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbWritePrintDataProgress
api_type:
- COM
---

# IPrinterScriptUsbWritePrintDataProgress interface


The IPrinterScriptUsbWritePrintDataProgress interface is passed as a parameter in the **writePrintData** JavaScript function call.

Members
-------

The **IPrinterScriptUsbWritePrintDataProgress** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPrinterScriptUsbWritePrintDataProgress** also has these types of members:

-   [Methods](#methods)

### <span id="methods"></span>Methods

The **IPrinterScriptUsbWritePrintDataProgress** interface has these methods.

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
<td>[<strong>ProcessedByteCount</strong>](iprinterscriptusbwriteprintdataprogress-processedbytecount.md)</td>
<td><p>Returns the number of bytes that the IHV JavaScript function has processed by the time this method was called.</p></td>
</tr>
<tr class="even">
<td>[<strong>ProcessedByteCount</strong>](iprinterscriptusbwriteprintdataprogress-processedbytecount-in.md)</td>
<td><p>Sets the number of bytes that the IHV JavaScript function has processed at the time this method was called.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbWritePrintDataProgress%20interface%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


