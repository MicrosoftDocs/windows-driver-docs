---
title: Iasphelp Open method
author: windows-driver-content
description: The Open method enables an ASP Web page to open access to a printer.
MS-HAID:
- 'webfnc\_7fa3a36d-4bf6-46d2-9336-e024d3aa1eec.xml'
- 'print.iasphelp\_open'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f4e39b76-3118-41d8-a5f8-501d884cbcdb
keywords: ["Open method Print Devices", "Open method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , Open method"]
topic_type:
- apiref
api_name:
- Iasphelp.Open
api_type:
- COM
---

# Iasphelp::Open method


The **Open** method enables an ASP Web page to open access to a printer.

Syntax
------

```ManagedCPlusPlus
HRESULT Open(
  [in] BSTR bstrPrinterName
);
```

Parameters
----------

*bstrPrinterName* \[in\]  
Caller-supplied pointer to a string containing a printer name.

Return value
------------

Win32 error codes can also be returned.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>S_OK</strong></td>
<td><p>The operation succeeded.</p></td>
</tr>
<tr class="even">
<td><strong>ERROR_INVALID_PRINTER_NAME</strong></td>
<td><p>Invalid printer name.</p></td>
</tr>
<tr class="odd">
<td><strong>ERROR_NOT_ENOUGH_MEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_open_gg"></span><span id="DDK_IASPHELP_OPEN_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

This method obtains access to the specified printer by calling the print spooler's **OpenPrinter** function. For more information about this function, see the Windows SDK Documentation.

After the **Iasphelp::Open** call, the printer remains open until the [**Iasphelp::Close**](iasphelp-close.md) method is called, or until **Iasphelp::Open** is called again with a different printer name.

```
    Dim objPrinter
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows 2000 and later versions of the Windows operating systems.</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**Iasphelp::Close**](iasphelp-close.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::Open%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


