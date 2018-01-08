---
title: Iasphelp get\_Status method
description: The Status property enables an ASP Web page to determine the printer status.
MS-HAID:
- 'webfnc\_30feffa7-1aa0-4b66-9d0a-1f66025272c3.xml'
- 'print.iasphelp\_status'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cff9dd7d-722b-4917-84ca-d6b17e8e64a4
keywords: ["get_Status method Print Devices", "get_Status method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Status method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_Status
api_type:
- COM
---

# Iasphelp::get\_Status method


The **Status** property enables an ASP Web page to determine the printer status.

Syntax
------

```ManagedCPlusPlus
HRESULT get_Status(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive printer status flags. For more information, see the following Remarks section.

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

 

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The property value is a printer status code that is either 0 or the bitwise OR of one or more of the PRINTER\_STATUS\_*XXX* flags that are defined in header file Winspool.h for the **Status** member of the PRINTER\_INFO\_2 structure. For more information about this structure, see the Windows SDK documentation.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Status** property can be queried.

```
    Dim objPrinter, PtrStatus
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    PtrStatus = objPrinter.Status
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_Status%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





