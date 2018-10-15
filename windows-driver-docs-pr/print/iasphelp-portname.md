---
title: Iasphelp get\_PortName method
author: windows-driver-content
description: The PortName property enables an ASP Web page to obtain a printer's port name.
MS-HAID:
- 'webfnc\_67f21c2f-9caf-4cd0-8a4b-df4ab9f63b43.xml'
- 'print.iasphelp\_portname'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2696d5c4-e1a1-4d9f-b5f5-e2083b548c65
keywords: ["get_PortName method Print Devices", "get_PortName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PortName method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_PortName
api_type:
- COM
ms.localizationpriority: medium
---

# Iasphelp::get\_PortName method


The **PortName** property enables an ASP Web page to obtain a printer's port name.

Syntax
------

```cpp
HRESULT get_PortName(
  [out] BSTR *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied location to receive a pointer to a string representing the printer's port name.

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
<td><p>The [<strong>Iasphelp::Open</strong>](iasphelp-open.md) method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_portname_gg"></span><span id="DDK_IASPHELP_PORTNAME_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PortName** property can be queried.

```cpp
    Dim objPrinter, PtrPortName
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    PtrPortName = objPrinter.PortName
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

 

 




