---
title: IBidiRequestContainer IBidiRequestContainer AddRequest method
description: The IBidiRequestContainer AddRequest method adds a request to the request list.
ms.assetid: 69a97816-2994-4eec-b2ab-a545195e3776
keywords: ["IBidiRequestContainer AddRequest method Print Devices", "IBidiRequestContainer AddRequest method Print Devices , IBidiRequestContainer interface", "IBidiRequestContainer interface Print Devices , IBidiRequestContainer AddRequest method"]
topic_type:
- apiref
api_name:
- IBidiRequestContainer.IBidiRequestContainer AddRequest
api_location:
- bidispl.dll
api_type:
- COM
---

# IBidiRequestContainer::IBidiRequestContainer::AddRequest method


The **IBidiRequestContainer::AddRequest** method adds a request to the request list.

Syntax
------

```ManagedCPlusPlus
HRESULT IBidiRequestContainer::AddRequest(
  [in] IBidiRequest *pRequest
);
```

Parameters
----------

*pRequest* \[in\]  
A pointer to the [**IBidiRequest**](ibidirequest.md) interface.

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
<td align="left"><strong>None of the above</strong></td>
<td align="left"><p>The <strong>HRESULT</strong> contains an error code corresponding to the last error.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This is similar to adding an item in a link list. In this case, [**IBidiRequestContainer**](ibidirequestcontainer.md) will hold a reference to *pRequest* by calling pRequest-&gt;AddRef.

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

[**IBidiRequestContainer**](ibidirequestcontainer.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequestContainer::IBidiRequestContainer::AddRequest%20method%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





