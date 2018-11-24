---
title: Iasphelp get\_IsTCPMonSupported method
description: The IsTCPMonSupported property enables an ASP Web page to determine if Microsoft's standard TCP/IP port monitor is being used with a printer.
MS-HAID:
- 'webfnc\_54f72229-524a-4bf2-917d-6a3ffcc27959.xml'
- 'print.iasphelp\_istcpmonsupported'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 79ec0584-183d-476d-aca2-e85479248091
keywords: ["get_IsTCPMonSupported method Print Devices", "get_IsTCPMonSupported method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IsTCPMonSupported method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_IsTCPMonSupported
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_IsTCPMonSupported method

The **IsTCPMonSupported** property enables an ASP Web page to determine if Microsoft's standard TCP/IP [port monitor](https://docs.microsoft.com/windows-hardware/drivers/print/port-monitors) is being used with a printer.

Syntax
------

```cpp
HRESULT get_IsTCPMonSupported(
  [out] BOOL *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if the TCP/IP port monitor is being used with the printer, or **FALSE** if it is not.

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
<td><strong>E_HANDLE</strong></td>
<td><p>The <a href="iasphelp-open.md" data-raw-source="[&lt;strong&gt;Iasphelp::Open&lt;/strong&gt;](iasphelp-open.md)"><strong>Iasphelp::Open</strong></a> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::IsTCPMonSupported** property can be queried.

```vb
Dim objPrinter, UseStdMon
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
UseStdMon = objPrinter.IsTCPMonSupported
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

[**Iasphelp::Open**](iasphelp-open.md)
