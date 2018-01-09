---
title: ISNMP OIDFromString method
description: The OIDFromString method enables an ASP Web page to convert an SNMP OID string to a numeric array.
MS-HAID:
- 'webfnc\_de08026f-5b6b-4c82-a653-2e16606e6b85.xml'
- 'print.isnmp\_oidfromstring'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a0e12657-c34e-4aff-a068-911a6aa6959d
keywords: ["OIDFromString method Print Devices", "OIDFromString method Print Devices , ISNMP interface", "ISNMP interface Print Devices , OIDFromString method"]
topic_type:
- apiref
api_name:
- ISNMP.OIDFromString
api_location:
- olesnmp.h
api_type:
- COM
---

# ISNMP::OIDFromString method


The `OIDFromString` method enables an ASP Web page to convert an SNMP OID string to a numeric array.

Syntax
------

```ManagedCPlusPlus
HRESULT OIDFromString(
  [in]  BSTR    bstrOID,
  [out] VARIANT *varOID
);
```

Parameters
----------

*bstrOID* \[in\]  
Caller-supplied pointer to an SNMP OID string.

*varOID* \[out\]  
Caller-supplied location to receive a pointer to an array of integer values representing the SNMP OID.

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
<td><strong>E_INVALIDARG</strong></td>
<td><p>The specified SNMP OID is not valid.</p></td>
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

This method calls the **SnmpMgrStrToOid** function to convert the SNMP OID string to its corresponding internal object-identifier structure. For more information about this function, see the Windows SDK documentation.

```
    Dim StrIP, strCommunity, objSNMP, OIDArray
    strIP = Session("MS_IPaddress")
    strCommunity = Session ("MS_Community")
    Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
    objSNMP.Open strIP, strCommunity, 2, 1000
    OIDArray = objSNMP.OIDFromString (". 43.18.1.1.2")
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
<tr class="odd">
<td><p>Header</p></td>
<td>Olesnmp.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ISNMP::OIDFromString%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




