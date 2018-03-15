---
title: Iasphelp get\_SNMPSupported method
author: windows-driver-content
description: The SNMPSupported property enables an ASP Web page to determine if SNMP is being used with a printer.
MS-HAID:
- 'webfnc\_2128dc9d-a113-4061-a6c9-3ebe2a304dd5.xml'
- 'print.iasphelp\_snmpsupported'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 17e3986b-3eb6-4c9d-ae4f-338e9cce439a
keywords: ["get_SNMPSupported method Print Devices", "get_SNMPSupported method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_SNMPSupported method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_SNMPSupported
api_type:
- COM
---

# Iasphelp::get\_SNMPSupported method


The **SNMPSupported** property enables an ASP Web page to determine if SNMP is being used with a printer.

Syntax
------

```ManagedCPlusPlus
HRESULT get_SNMPSupported(
  [out] BOOL *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if SNMP is being used with the printer, or **FALSE** if it is not.

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

 

## <span id="ddk_iasphelp_snmpsupported_gg"></span><span id="DDK_IASPHELP_SNMPSUPPORTED_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::SNMPSupported** property can be queried.

```
    Dim objPrinter, UsingSNMP
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    UsingSNMP = objPrinter.SNMPSupported
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

 

 




