---
title: Iasphelp Open method
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::Open method

The **Open** method enables an ASP Web page to open access to a printer.

Syntax
------

```cpp
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

## VBScript Example

This method obtains access to the specified printer by calling the print spooler's **OpenPrinter** function. For more information about this function, see the Windows SDK Documentation.

After the **Iasphelp::Open** call, the printer remains open until the [**Iasphelp::Close**](iasphelp-close.md) method is called, or until **Iasphelp::Open** is called again with a different printer name.

```vb
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
</tbody>
</table>

## See also

[**Iasphelp::Close**](iasphelp-close.md)
