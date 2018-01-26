---
title: ISNMP Open method
author: windows-driver-content
description: The Open method enables an ASP Web page to create a communication path to a specified SNMP agent.
MS-HAID:
- 'webfnc\_2be497fa-98d8-4fb3-997c-fa1345ed4648.xml'
- 'print.isnmp\_open'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a5d1a8a2-5953-4b7f-8f8e-cb84520ae9e8
keywords: ["Open method Print Devices", "Open method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Open method"]
topic_type:
- apiref
api_name:
- ISNMP.Open
api_location:
- olesnmp.h
api_type:
- COM
---

# ISNMP::Open method


The `Open` method enables an ASP Web page to create a communication path to a specified SNMP agent.

Syntax
------

```ManagedCPlusPlus
HRESULT Open(
  [in] BSTR    bstrHost,
  [in] BSTR    bstrCommunity,
  [in] VARIANT varRetry,
  [in] VARIANT varTimeout
);
```

Parameters
----------

*bstrHost* \[in\]  
Caller-supplied pointer to a string identifying the SNMP agent system. This can be either a dotted-decimal IP address or a host name that can be resolved to an IP address, an IPX address (in 8.12 notation), or an ethernet address.

*bstrCommunity* \[in\]  
Caller-supplied pointer to a string representing the SNMP agent system's community name.

*varRetry* \[in\]  
Optional, caller-supplied retry value. If not specified, a default value is used. The recommended value is 2.

*varTimeout* \[in\]  
Optional, caller-supplied time-out value, in milliseconds. If not specified, a default value is used. The recommended value is 1000.

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
<td><p>Either the <em>varRetry</em> or <em>varTimeOut</em> value could not be converted to a short integer.</p></td>
</tr>
<tr class="odd">
<td><strong>E_FAIL</strong></td>
<td><p>The call to <strong>SnmpMgrOpen</strong> failed.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_isnmp_open_gg"></span><span id="DDK_ISNMP_OPEN_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

This method calls the **SnmpMgrOpen** function, which has the same parameters as `ISNMP::Open`. For more information about this function, see the Windows SDK Documentation.

After the `ISNMP::Open` call, the communication path to the SNMP agent remains open until the [**ISNMP::Close**](isnmp-close.md) method is called, or until `ISNMP::Open` is called again.

```
    Dim StrIP, strCommunity, objSNMP
    strIP = Session("MS_IPaddress")
    strCommunity = Session ("MS_Community")
    Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
    objSNMP.Open strIP, strCommunity, 2, 1000
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


[**ISNMP::Close**](isnmp-close.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ISNMP::Open%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


