---
title: ISNMP GetList method
description: The GetList method enables an ASP Web page to obtain the values associated with an array of SNMP OIDs.
MS-HAID:
- 'webfnc\_44ada708-01e2-42c3-8080-bd7cf0e46b0e.xml'
- 'print.isnmp\_getlist'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6ee90c77-578e-4c2c-b955-4b549625ca14
keywords: ["GetList method Print Devices", "GetList method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetList method"]
topic_type:
- apiref
api_name:
- ISNMP.GetList
api_location:
- olesnmp.h
api_type:
- COM
---

# ISNMP::GetList method


The `GetList` method enables an ASP Web page to obtain the values associated with an array of SNMP OIDs.

Syntax
------

```ManagedCPlusPlus
HRESULT GetList(
  [in]  VARIANT *varList,
  [out] VARIANT *varValue
);
```

Parameters
----------

*varList* \[in\]  
Caller-supplied pointer to an array of SNMP OID strings.

*varValue* \[out\]  
Caller-supplied pointer to a location that receives the address of an array of SNMP OID values.

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
<td><strong>E_FAIL</strong></td>
<td><p>The <strong>ISNMP::Open</strong> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_INVALIDARG</strong></td>
<td><p>The specified SNMP OID is not valid.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_isnmp_getlist_gg"></span><span id="DDK_ISNMP_GETLIST_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

This method calls the **SnmpMgrRequest** function to obtain SNMP OID values. For more information about this function, see the Windows SDK Documentation.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::GetList` method can be called.

```
    Dim StrIP, strCommunity, objSNMP, OIDArray, OIDValueArray
    strIP = Session("MS_IPaddress")
    strCommunity = Session ("MS_Community")
    Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
    objSNMP.Open strIP, strCommunity, 2, 1000
    OIDArray = Array("25.3.2.1.5", "25.3.5.1.1")
    OIDValueArray = objSNMP.GetList (OIDArray)
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

## <span id="see_also"></span>See also


[**ISNMP::Open**](isnmp-open.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ISNMP::GetList%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





