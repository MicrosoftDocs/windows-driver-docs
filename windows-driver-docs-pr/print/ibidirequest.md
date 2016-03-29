---
title: IBidiRequest interface
description: The IBidiRequest interface allows an application or other objects to compose a bidi request.
ms.assetid: e7b16853-7f1d-45e4-af5e-4ae9cbb9b191
keywords: ["IBidiRequest interface Print Devices", "IBidiRequest interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IBidiRequest
api_location:
- Bidispl.h
api_type:
- COM
---

# IBidiRequest interface


The **IBidiRequest** interface allows an application or other objects to compose a bidi request.

Members
-------

The **IBidiRequest** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBidiRequest** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBidiRequest** interface has these methods.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">[<strong>GetEnumCount</strong>](ibidirequest-ibidirequest--getenumcount.md)</td>
<td align="left"><p>Gets the number of output items.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>GetOutputData</strong>](ibidirequest-ibidirequest--getoutputdata.md)</td>
<td align="left"><p>Gets the output data coming back from the device.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>GetResult</strong>](ibidirequest-ibidirequest--getresult.md)</td>
<td align="left"><p>Gets the result code.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>SetInputData</strong>](ibidirequest-ibidirequest--setinputdata.md)</td>
<td align="left"><p>Sets the data to send to the device.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>SetSchema</strong>](ibidirequest-ibidirequest--setschema.md)</td>
<td align="left"><p>Sets the bidi schema string.</p></td>
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
<td align="left"><p>Windows XP</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2003</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Bidispl.h</td>
</tr>
</tbody>
</table>

## See also


[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)

[Bidirectional Communication Schema](bidirectional-communication-schema.md)

[Print Spooler Components](print-spooler-components.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest%20interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





