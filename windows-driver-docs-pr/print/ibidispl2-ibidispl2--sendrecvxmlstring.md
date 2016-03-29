---
title: IBidiSpl2 IBidiSpl2 SendRecvXMLString method
description: The IBidiSpl2 SendRecvXMLString method sends a bidirectional printer communication request and receives the response as Unicode strings formatted in accordance with the Bidirectional Communication Schemas.
ms.assetid: 7d61402e-e248-4770-a828-9c266e528115
keywords: ["IBidiSpl2 SendRecvXMLString method Print Devices", "IBidiSpl2 SendRecvXMLString method Print Devices , IBidiSpl2 interface", "IBidiSpl2 interface Print Devices , IBidiSpl2 SendRecvXMLString method"]
topic_type:
- apiref
api_name:
- IBidiSpl2.IBidiSpl2 SendRecvXMLString
api_location:
- bidispl.dll
api_type:
- COM
---

# IBidiSpl2::IBidiSpl2::SendRecvXMLString method


The **IBidiSpl2::SendRecvXMLString** method sends a bidirectional printer communication request and receives the response as Unicode strings formatted in accordance with the [Bidirectional Communication Schemas](bidirectional-communication-schema.md).

Syntax
------

```ManagedCPlusPlus
HRESULT IBidiSpl2::SendRecvXMLString(
  [in]  BSTR bstrRequest,
  [out] BSTR *pbstrResponse
);
```

Parameters
----------

*bstrRequest* \[in\]  
The bidi communication request as a Unicode string that complies with one of the [Bidirectional Communication Schemas](bidirectional-communication-schema.md).

*pbstrResponse* \[out\]  
A pointer to the printer's response as a Unicode string that complies with one of the [Bidirectional Communication Schemas](bidirectional-communication-schema.md).

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
<th align="left">Value</th>
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

 

Note that the **HRESULT** may contain a system error code that is defined in [Bidi Error Codes](bidi-error-codes.md).

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

[Print Spooler Components](print-spooler-components.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl2::IBidiSpl2::SendRecvXMLString%20method%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





