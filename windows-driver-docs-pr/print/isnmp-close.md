---
title: ISNMP Close method
description: The Close method enables an ASP Web page to close a communication path to an SNMP agent.
MS-HAID:
- 'webfnc\_e925ae51-c717-4b4f-8ab2-b18e9d770c63.xml'
- 'print.isnmp\_close'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea3c462d-881d-48ad-8751-d3ee0468697e
keywords: ["Close method Print Devices", "Close method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Close method"]
topic_type:
- apiref
api_name:
- ISNMP.Close
api_location:
- olesnmp.h
api_type:
- COM
---

# ISNMP::Close method


The `Close` method enables an ASP Web page to close a communication path to an SNMP agent.

Syntax
------

```ManagedCPlusPlus
HRESULT Close();
```

Parameters
----------

This method has no parameters.

Return value
------------

The method always returns S\_OK.

## <span id="ddk_isnmp_close_gg"></span><span id="DDK_ISNMP_CLOSE_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

This method calls the **SnmpMgrClose** function, which is described in the Windows SDK documentation, to close the communication path that was created by the previous call to the [**ISNMP::Open**](isnmp-open.md) method.

```
    Dim StrIP, strCommunity, objSNMP
    strIP = Session("MS_IPaddress")
    strCommunity = Session ("MS_Community")
    Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
    objSNMP.Open strIP, strCommunity, 2, 1000
    ...
    objSNMP.Close
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ISNMP::Close%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





