---
title: Iasphelp get\_MibErrorDscp method
description: The MibErrorDscp property enables an ASP Web page to convert a Simple Network Management Protocol (SNMP) management information base (MIB) error code into a text description of the error.
MS-HAID:
- 'webfnc\_3931fbc6-1960-4d40-a6e3-8816ee832c89.xml'
- 'print.iasphelp\_miberrordscp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b2ab9414-8401-4ec4-a235-f6a8da93523b
keywords: ["get_MibErrorDscp method Print Devices", "get_MibErrorDscp method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MibErrorDscp method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_MibErrorDscp
api_type:
- COM
---

# Iasphelp::get\_MibErrorDscp method


The **MibErrorDscp** property enables an ASP Web page to convert a Simple Network Management Protocol (SNMP) management information base (MIB) error code into a text description of the error.

Syntax
------

```ManagedCPlusPlus
HRESULT get_MibErrorDscp(
  [in]  DWORD dwError,
  [out] BSTR  *pVal
);
```

Parameters
----------

*dwError* \[in\]  
Caller-supplied SNMP MIB error code.

*pVal* \[out\]  
Caller-supplied location to receive a pointer to a string containing a text description of the error.

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
<td><p>Invalid <em>pVal</em> pointer.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_miberrordscp_gg"></span><span id="DDK_IASPHELP_MIBERRORDSCP_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

```
    Dim objPrinter, MIBErrorCode, MIBErrorString
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    ...
 &#39; Get error code from MIB.
    ...
    MIBErrorString = objPrinter.MibErrorDscp(ErrorCodeMIB)
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_MibErrorDscp%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




