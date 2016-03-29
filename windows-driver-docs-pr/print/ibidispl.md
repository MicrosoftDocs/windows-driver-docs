---
title: IBidiSpl interface
description: The IBidiSpl interface allows an application or other objects to send a single bidi request or a list of bidi requests.
ms.assetid: 7e4a30b2-ac3a-475a-b818-455cdb7a91bf
keywords: ["IBidiSpl interface Print Devices", "IBidiSpl interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IBidiSpl
api_location:
- Bidispl.h
api_type:
- COM
---

# IBidiSpl interface


The **IBidiSpl** interface allows an application or other objects to send a single bidi request or a list of bidi requests.

Members
-------

The **IBidiSpl** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBidiSpl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBidiSpl** interface has these methods.

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
<td align="left">[<strong>BindDevice</strong>](ibidispl-ibidispl--binddevice.md)</td>
<td align="left"><p>Binds a printer to a bidi request.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MultiSendRecv</strong>](ibidispl-ibidispl--multisendrecv.md)</td>
<td align="left"><p>Sends a list of bidi requests.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>SendRecv</strong>](ibidispl-ibidispl--sendrecv.md)</td>
<td align="left"><p>Sends a bidi request.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>UnbindDevice</strong>](ibidispl-ibidispl--unbinddevice.md)</td>
<td align="left"><p>Unbinds a printer.</p></td>
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

[**IBidiSpl**](ibidirequestcontainer.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl%20interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





