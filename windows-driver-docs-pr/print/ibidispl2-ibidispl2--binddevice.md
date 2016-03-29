---
title: IBidiSpl2 IBidiSpl2 BindDevice method
description: The IBidiSpl2 BindDevice method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the OpenPrinter function.
ms.assetid: c5bd238d-4b85-4463-aa73-ff3a7798ccff
keywords: ["IBidiSpl2 BindDevice method Print Devices", "IBidiSpl2 BindDevice method Print Devices , IBidiSpl2 interface", "IBidiSpl2 interface Print Devices , IBidiSpl2 BindDevice method"]
topic_type:
- apiref
api_name:
- IBidiSpl2.IBidiSpl2 BindDevice
api_location:
- bidispl.dll
api_type:
- COM
---

# IBidiSpl2::IBidiSpl2::BindDevice method


The **IBidiSpl2::BindDevice** method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the [**OpenPrinter**](openprinter.md) function.

Syntax
------

```ManagedCPlusPlus
HRESULT IBidiSpl2::BindDevice(
  [in] const LPCWSTR pszDeviceName,
  [in] const DWORD   dwAccess
);
```

Parameters
----------

*pszDeviceName* \[in\]  
A pointer to a null-terminated string that contains the name of the printer or print server. If **NULL**, this parameter indicates the local print server.

*dwAccess* \[in\]  
The access privileges for the printer. This parameter can be one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="" id="bidi-access-administrator"></a>
<strong>BIDI_ACCESS_ADMINISTRATOR</strong></td>
<td align="left"><p>Permits users to perform all administrative tasks and basic printing operations except for SYNCHRONIZE. This is the same as PRINTER_ALL_ACCESS in [<strong>OpenPrinter</strong>](openprinter.md).</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="bidi-access-user"></a>
<strong>BIDI_ACCESS_USER</strong></td>
<td align="left"><p>Permits users to perform basic printing operations. This is the same as PRINTER_ACCESS_USE in [<strong>OpenPrinter</strong>](openprinter.md).</p></td>
</tr>
</tbody>
</table>

 

Return value
------------

The method returns one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>S_OK</strong></td>
<td align="left"><p>The operation was successful.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>E_HANDLE</strong></td>
<td align="left"><p>The interface handle is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>None of the above</strong></td>
<td align="left"><p>The <strong>HRESULT</strong> contains an error code that corresponds to the last error.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows Vista</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2008</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Bidispl.h</td>
</tr>
<tr class="odd">
<td align="left"><p>DLL</p></td>
<td align="left">Bidispl.dll</td>
</tr>
</tbody>
</table>

## See also


[**IBidiSpl2**](ibidispl2.md)

[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)

[Bidirectional Communication Schema](bidirectional-communication-schema.md)

[Print Spooler Components](print-spooler-components.md)

[**OpenPrinter**](openprinter.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl2::IBidiSpl2::BindDevice%20method%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





