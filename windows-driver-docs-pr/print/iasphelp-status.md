---
title: Iasphelp get\_Status method
author: windows-driver-content
description: The Status property enables an ASP Web page to determine the printer status.
MS-HAID:
- 'webfnc\_30feffa7-1aa0-4b66-9d0a-1f66025272c3.xml'
- 'print.iasphelp\_status'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cff9dd7d-722b-4917-84ca-d6b17e8e64a4
keywords: ["get_Status method Print Devices", "get_Status method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Status method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_Status
api_type:
- COM
ms.localizationpriority: medium
---

# Iasphelp::get\_Status method


The **Status** property enables an ASP Web page to determine the printer status.

Syntax
------

```ManagedCPlusPlus
HRESULT get_Status(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive printer status flags. For more information, see the following Remarks section.

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

 

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The property value is a printer status code that is either 0 or the bitwise OR of one or more of the PRINTER\_STATUS\_*XXX* flags that are defined in header file Winspool.h for the **Status** member of the PRINTER\_INFO\_2 structure. For more information about this structure, see the Windows SDK documentation.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Status** property can be queried.

```cpp
    Dim objPrinter, PtrStatus
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    PtrStatus = objPrinter.Status
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

 

 




