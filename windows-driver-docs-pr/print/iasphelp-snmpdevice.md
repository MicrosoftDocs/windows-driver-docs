---
title: Iasphelp get\_SNMPDevice method
description: The SNMPDevice property enables an ASP Web page to obtain a printer's SNMP device index (as defined by RFC 1759).
MS-HAID:
- 'webfnc\_e4a9d1b3-1168-45a7-98cb-9c19fdf83009.xml'
- 'print.iasphelp\_snmpdevice'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4ae42406-6a19-4af0-88c5-bc4375bb648c
keywords: ["get_SNMPDevice method Print Devices", "get_SNMPDevice method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_SNMPDevice method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_SNMPDevice
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_SNMPDevice method

The **SNMPDevice** property enables an ASP Web page to obtain a printer's SNMP device index (as defined by RFC 1759).

Syntax
------

```cpp
HRESULT get_SNMPDevice(
  [out] DWORD *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied location to receive a numeric value representing the printer's SNMP device index.

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

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::SNMPDevice** property can be queried.

```vb
Dim objPrinter, SNMPDeviceIndex
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
SNMPDeviceIndex = objPrinter.SNMPDevice
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
