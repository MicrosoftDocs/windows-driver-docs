---
title: Iasphelp get\_MediaReady method
author: windows-driver-content
description: The MediaReady property enables an ASP Web page to obtain a set of strings that name all of the paper forms for the printer that are currently available for use.
MS-HAID:
- 'webfnc\_b10e8434-7e12-4bb5-8c43-77cb890f72a8.xml'
- 'print.iasphelp\_mediaready'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1e90649a-6075-4b78-93fd-781c3e363b5f
keywords: ["get_MediaReady method Print Devices", "get_MediaReady method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MediaReady method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_MediaReady
api_type:
- COM
---

# Iasphelp::get\_MediaReady method


The **MediaReady** property enables an ASP Web page to obtain a set of strings that name all of the paper forms for the printer that are currently available for use.

Syntax
------

```ManagedCPlusPlus
HRESULT get_MediaReady(
  [out] VARIANT *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied location to receive a pointer to a set of strings that name all of the paper forms for a printer that are currently available for use.

Return value
------------

This property returns one of the values in the following table.

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

This method obtains a list of the names of the paper forms that are currently available for use by calling the printer driver's [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function with the DC\_MEDIAREADY flag set.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::MediaReady** property can be queried.

```
    Dim objPrinter, MediaReadyArray
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    MediaReadyArray = objPrinter.MediaReady
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


[**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539)

[**Iasphelp::Open**](iasphelp-open.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_MediaReady%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


