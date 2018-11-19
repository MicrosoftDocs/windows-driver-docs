---
title: Iasphelp get\_Community method
description: The Community property enables an ASP Web page to obtain a print server's Simple Network Management Protocol (SNMP) community name.
MS-HAID:
- 'webfnc\_1d85e932-6de7-468a-b1dd-8a5678c65615.xml'
- 'print.iasphelp\_community'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 39e8dff6-9eaf-43dd-b8ca-46982f3eae18
keywords: ["get_Community method Print Devices", "get_Community method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Community method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_Community
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_Community method

The **Community** property enables an ASP Web page to obtain a print server's Simple Network Management Protocol (SNMP) community name.

Syntax
------

```cpp
HRESULT get_Community(
  [out] BSTR *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to a community name string.

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

If the printer is not supported by the TCP/IP port monitor, the returned string is empty.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Community** property can be queried.

```vb
Dim objPrinter, CommName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
CommName = objPrinter.Community
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
