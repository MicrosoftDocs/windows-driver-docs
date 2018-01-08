---
title: Iasphelp get\_ErrorDscp method
description: The ErrorDscp property enables an ASP Web page to convert an error code to a descriptive string.
MS-HAID:
- 'webfnc\_55f547fe-4cbe-4905-b268-afd7af400de4.xml'
- 'print.iasphelp\_errordscp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 46d44c54-4fd5-489f-9624-1df3c8917237
keywords: ["get_ErrorDscp method Print Devices", "get_ErrorDscp method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_ErrorDscp method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_ErrorDscp
api_type:
- COM
---

# Iasphelp::get\_ErrorDscp method


The **ErrorDscp** property enables an ASP Web page to convert an error code to a descriptive string.

Syntax
------

```ManagedCPlusPlus
HRESULT get_ErrorDscp(
  [in]  long lErrCode,
  [out] BSTR *pVal
);
```

Parameters
----------

*lErrCode* \[in\]  
Specifies the error code to be converted to a descriptive string.

*pVal* \[out\]  
A caller-supplied pointer to a location that receives the descriptive string that corresponds to the error code in the *lErrCode* parameter.

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
<td><strong>E_POINTER</strong></td>
<td><p>Invalid <em>pVal</em> pointer.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::ErrorDscp** property can be queried.

```
    Dim objPrinter, ErrorCode, ErrorString
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    ...
 &#39; Get error code.
    ...
    ErrorString = objPrinter.ErrorDscp(ErrorCode)
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_ErrorDscp%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





