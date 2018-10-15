---
title: Iasphelp get\_IsHTTP method
author: windows-driver-content
description: The IsHTTP property enables an ASP Web page to determine whether the printer is connected to an HTTP port.
MS-HAID:
- 'webfnc\_e3e58eea-498f-4e85-8072-2c49ac50d733.xml'
- 'print.iasphelp\_ishttp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 54aaed11-8f18-433b-b774-c695a85b813e
keywords: ["get_IsHTTP method Print Devices", "get_IsHTTP method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IsHTTP method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_IsHTTP
api_type:
- COM
ms.localizationpriority: medium
---

# Iasphelp::get\_IsHTTP method


The **IsHTTP** property enables an ASP Web page to determine whether the printer is connected to an HTTP port.

Syntax
------

```ManagedCPlusPlus
HRESULT get_IsHTTP(
  [out] BOOL *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives **TRUE** if the printer is connected to an HTTP port, and **FALSE** otherwise.

Return value
------------

The property return one of the values in the following table.

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
<td><p>The [<strong>Iasphelp::Open</strong>](iasphelp-open.md) method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::IsHTTP** property can be queried.

```cpp
    Dim objPrinter, IsHTTPPort
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    IsHTTPPort = objPrinter.IsHTTP
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

## See also


[**Iasphelp::Open**](iasphelp-open.md)

 

 




