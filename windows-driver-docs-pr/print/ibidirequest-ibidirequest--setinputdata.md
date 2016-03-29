---
title: IBidiRequest IBidiRequest SetInputData method
description: The IBidiRequest SetInputData method sets the data to send to the printer.
ms.assetid: 8db7b5cd-b03f-4973-8711-8ac022bfb2b5
keywords: ["IBidiRequest SetInputData method Print Devices", "IBidiRequest SetInputData method Print Devices , IBidiRequest interface", "IBidiRequest interface Print Devices , IBidiRequest SetInputData method"]
topic_type:
- apiref
api_name:
- IBidiRequest.IBidiRequest SetInputData
api_location:
- bidispl.dll
api_type:
- COM
---

# IBidiRequest::IBidiRequest::SetInputData method


The **IBidiRequest::SetInputData** method sets the data to send to the printer.

Syntax
------

```ManagedCPlusPlus
HRESULT IBidiRequest::SetInputData(
  [in] const DWORD dwType,
  [in] const BYTE  *pData,
  [in] const UINT  uSize
);
```

Parameters
----------

*dwType* \[in\]  
The type of data to be sent. This parameter can be one of the following values.

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
<td align="left"><a href="" id="bidi-null"></a>
<strong>BIDI_NULL</strong></td>
<td align="left"><p>No data.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="bidi-int"></a>
<strong>BIDI_INT</strong></td>
<td align="left"><p>Integer data.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="bidi-float"></a>
<strong>BIDI_FLOAT</strong></td>
<td align="left"><p>Floating-point number.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="bidi-bool"></a>
<strong>BIDI_BOOL</strong></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="bidi-string"></a>
<strong>BIDI_STRING</strong></td>
<td align="left"><p>Unicode character string.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="bidi-text"></a>
<strong>BIDI_TEXT</strong></td>
<td align="left"><p>Non-localizable Unicode string.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="bidi-enum"></a>
<strong>BIDI_ENUM</strong></td>
<td align="left"><p>Enumeration data in the form of a Unicode string.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="bidi-blob"></a>
<strong>BIDI_BLOB</strong></td>
<td align="left"><p>Binary data.</p></td>
</tr>
</tbody>
</table>

 

*pData* \[in\]  
A pointer to the byte array that contains the data. For example, if *dwType* is BIDI\_BOOL, *pData* points to a buffer that contains a Boolean value and if *dwType* is BIDI\_BLOB, *pData* points to a buffer that contains the binary data.

*uSize* \[in\]  
Size, in bytes, of the byte array specified by *pData*.

Return value
------------

The method returns one of the following values. For more information about COM error codes, see [Error Handling](_com_error_handling).

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
<td align="left"><p>The operation was successfully carried out.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>E_HANDLE</strong></td>
<td align="left"><p>The interface handle was invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>E_INVALIDARG</strong></td>
<td align="left"><p>The type of the data was not consistent with its size.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>E_OUTOFMEMORY</strong></td>
<td align="left"><p>Memory allocation failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>None of the above</strong></td>
<td align="left"><p>The <strong>HRESULT</strong> contains an error code corresponding to the last error.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If an application calls **SetInputData** more than once, only the value of the last call will be set.

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
<td align="left"><p>Windows XP</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2003</p></td>
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


[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)

[Bidirectional Communication Schema](bidirectional-communication-schema.md)

[**IBidiRequest**](ibidirequest.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::IBidiRequest::SetInputData%20method%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





