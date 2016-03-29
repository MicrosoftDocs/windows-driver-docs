---
title: IBidiRequest IBidiRequest GetEnumCount method
description: The IBidiRequest GetEnumCount method gets the number of output results from the bidi request.
ms.assetid: 4c857ff4-02c1-487b-bdb0-44d62a4cf4a1
keywords: ["IBidiRequest GetEnumCount method Print Devices", "IBidiRequest GetEnumCount method Print Devices , IBidiRequest interface", "IBidiRequest interface Print Devices , IBidiRequest GetEnumCount method"]
topic_type:
- apiref
api_name:
- IBidiRequest.IBidiRequest GetEnumCount
api_location:
- bidispl.dll
api_type:
- COM
---

# IBidiRequest::IBidiRequest::GetEnumCount method


The **IBidiRequest::GetEnumCount** method gets the number of output results from the bidi request.

Syntax
------

```ManagedCPlusPlus
HRESULT IBidiRequest::GetEnumCount(
  [out] DWORD *pdwTotal
);
```

Parameters
----------

*pdwTotal* \[out\]  
A pointer to a variable that receives the number of output results.

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
<td align="left"><p>The method was successful.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>E_HANDLE</strong></td>
<td align="left"><p>The interface handle was invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>E_POINTER</strong></td>
<td align="left"><p>The <em>pdwTotal</em> parameter did not point to a valid memory location.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>None of the above</strong></td>
<td align="left"><p>The <strong>HRESULT</strong> contains an error code corresponding to the last error.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

A single bidi request can have multiple results. After calling **GetEnumCount**, the application can call [**IBidiRequest::GetOutputData**](ibidirequest-ibidirequest--getoutputdata.md) to select a particular result.

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

[**IBidiRequest::GetOutputData**](ibidirequest-ibidirequest--getoutputdata.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::IBidiRequest::GetEnumCount%20method%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





