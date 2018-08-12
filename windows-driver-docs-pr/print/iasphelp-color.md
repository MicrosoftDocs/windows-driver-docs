---
title: Iasphelp get\_Color method
author: windows-driver-content
description: The Color property enables an ASP Web page to determine if a printer supports color printing.
MS-HAID:
- 'webfnc\_1eb57c03-7aa3-4acb-8a2c-3327a37e019d.xml'
- 'print.iasphelp\_color'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: aa075ce7-15fd-4c24-b704-b7b240414d05
keywords: ["get_Color method Print Devices", "get_Color method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Color method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_Color
api_type:
- COM
ms.localizationpriority: medium
---

# Iasphelp::get\_Color method


The **Color** property enables an ASP Web page to determine if a printer supports color printing.

Syntax
------

```ManagedCPlusPlus
HRESULT get_Color(
  [out] BOOL *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if the printer supports color printing, or **FALSE** if it does not.

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
<td><p>The <strong>Iasphelp::Open</strong> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_color_gg"></span><span id="DDK_IASPHELP_COLOR_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Color** property can be queried.

```
    Dim objPrinter, HasColor
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    HasColor = objPrinter.Color
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


[**Iasphelp::Open**](iasphelp-open.md)

 

 




