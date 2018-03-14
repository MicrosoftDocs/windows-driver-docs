---
title: Iasphelp get\_LongPaperName method
author: windows-driver-content
description: The LongPaperName property enables an ASP Web page to convert a short paper name to a long paper name.
MS-HAID:
- 'webfnc\_17250b54-29f4-41c5-bdf2-b72e0823d8e4.xml'
- 'print.iasphelp\_longpapername'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 14e6d6db-c429-4d80-840b-c4e0102c9380
keywords: ["get_LongPaperName method Print Devices", "get_LongPaperName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_LongPaperName method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_LongPaperName
api_type:
- COM
---

# Iasphelp::get\_LongPaperName method


The **LongPaperName** property enables an ASP Web page to convert a short paper name to a long paper name.

Syntax
------

```ManagedCPlusPlus
HRESULT get_LongPaperName(
  [in]  BSTR bstrShortName,
  [out] BSTR *pVal
);
```

Parameters
----------

*bstrShortName* \[in\]  
A caller-supplied pointer to a string that contains a short paper name.

*pVal* \[out\]  
A caller-supplied location to receive a pointer to a string that contains a long paper name.

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
<td><strong>E_POINTER</strong></td>
<td><p>At least one of the parameters does not point to a valid memory location.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_longpapername_gg"></span><span id="DDK_IASPHELP_LONGPAPERNAME_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

```
    Dim objPrinter, LongName
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    LongName = objPrinter.LongPaperName("iso-a0")
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

 

 




