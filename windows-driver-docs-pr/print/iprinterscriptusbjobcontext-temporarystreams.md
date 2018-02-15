---
title: IPrinterScriptUsbJobContext TemporaryStreams method
author: windows-driver-content
description: Returns an array of IPrinterScriptableSequentialStream interfaces for the persistent data streams that can be used by the IHV JavaScript functions for the current job.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ED9AFB90-287B-4030-AC20-ECCA9841D27E
keywords: ["TemporaryStreams method Print Devices", "TemporaryStreams method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , TemporaryStreams method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContext.TemporaryStreams
api_type:
- COM
---

# IPrinterScriptUsbJobContext::TemporaryStreams method


Returns an array of [IPrinterScriptableSequentialStream](https://msdn.microsoft.com/library/windows/hardware/hh439697) interfaces for the persistent data streams that can be used by the IHV JavaScript functions for the current job.

Syntax
------

```ManagedCPlusPlus
HRESULT TemporaryStreams(
  [out, retval] IDispatch **ppArray
);
```

Parameters
----------

*ppArray* \[out, retval\]  
Pointer to an array of [IPrinterScriptableSequentialStream](https://msdn.microsoft.com/library/windows/hardware/hh439697) interfaces.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**TemporaryStreams** is a read-only method. There are a maximum of 2 temporary streams available to the IHV JavaScript functions. These streams are only available for the duration of the current print job. The IHV can use this to store data that is not yet ready to be sent to the print device. On a later **writePrintData** JavaScript function call, these streams can be used to send the stored data to the print device.

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
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

[IPrinterScriptableSequentialStream](https://msdn.microsoft.com/library/windows/hardware/hh439697)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContext::TemporaryStreams%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


