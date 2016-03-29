---
title: IBidiRequest IBidiRequest GetOutputData method
description: The IBidiRequest GetOutputData method gets the specified output data coming back from the printer.
ms.assetid: 0757dbc2-850b-4267-9339-b87591f85767
keywords: ["IBidiRequest GetOutputData method Print Devices", "IBidiRequest GetOutputData method Print Devices , IBidiRequest interface", "IBidiRequest interface Print Devices , IBidiRequest GetOutputData method"]
topic_type:
- apiref
api_name:
- IBidiRequest.IBidiRequest GetOutputData
api_location:
- bidispl.dll
api_type:
- COM
---

# IBidiRequest::IBidiRequest::GetOutputData method


The **IBidiRequest::GetOutputData** method gets the specified output data coming back from the printer.

Syntax
------

```ManagedCPlusPlus
HRESULT IBidiRequest::GetOutputData(
  [in]  const DWORD  dwIndex,
  [out]       LPWSTR *ppszSchema,
  [out]       DWORD  *pdwType,
  [out]       BYTE   **ppData,
  [out]       ULONG  *uSize
);
```

Parameters
----------

*dwIndex* \[in\]  
A zero-based index of the output data that is requested. For more information, see Remarks.

*ppszSchema* \[out\]  
A pointer to a NULL-terminated string that receives the schema string. The caller must call the [**CoTaskMemFree**](_com_cotaskmemfree) function to free this pointer.

*pdwType* \[out\]  
A pointer to a variable that receives the type of the output data. This parameter can be one of the following values.

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

 

*ppData* \[out\]  
A pointer to the variable that receives a pointer to the byte array containing the output data. The buffer is allocated by the COM interface to store the output data. The caller is responsible for calling [**CoTaskMemFree**](_com_cotaskmemfree) to free the buffer.

*uSize* \[out\]  
A pointer to a variable that receives the size of the byte array specified by \*\*ppData.

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
<th align="left">Return code</th>
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
<td align="left"><strong>E_POINTER</strong></td>
<td align="left"><p>At least one of the pointer variable parameters did not reference a valid memory location.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>None of the above</strong></td>
<td align="left"><p>The <strong>HRESULT</strong> contains an error code corresponding to the last error.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

A single bidi request can have multiple results. The application calls [**IBidiRequest::GetEnumCount**](ibidirequest-ibidirequest--getenumcount.md) to get the number of results from the bidi request.

If an application calls **GetOutputData** with the same index twice, the interface allocates two different buffers and thus the application must free both buffers.

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

[**IBidiRequest::GetEnumCount**](ibidirequest-ibidirequest--getenumcount.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::IBidiRequest::GetOutputData%20method%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





