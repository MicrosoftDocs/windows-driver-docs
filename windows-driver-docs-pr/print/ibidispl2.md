---
title: IBidiSpl2 interface
description: The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas.
ms.assetid: 90e8a390-7d30-4bcf-8c81-438c86529ceb
keywords: ["IBidiSpl2 interface Print Devices", "IBidiSpl2 interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IBidiSpl2
api_location:
- Bidispl.h
api_type:
- COM
---

# IBidiSpl2 interface


The **IBidiSpl2** interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. The requests and responses can be either strings or Streams.

Members
-------

The **IBidiSpl2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBidiSpl2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBidiSpl2** interface has these methods.

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
<td align="left">[<strong>BindDevice</strong>](ibidispl2-ibidispl2--binddevice.md)</td>
<td align="left"><p>Binds a printer to a bidirectional communication request.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>SendRecvXMLStream</strong>](ibidispl2-ibidispl2--sendrecvxmlstream.md)</td>
<td align="left"><p>Sends a bidirectional communication request (and receives the response) as Bidi Request and Response-compliant [<strong>IStream</strong>](https://msdn.microsoft.com/library/windows/desktop/aa380034).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>SendRecvXMLString</strong>](ibidispl2-ibidispl2--sendrecvxmlstring.md)</td>
<td align="left"><p>Sends a bidirectional communication request (and receives the response) as Bidi Request and Response-compliant strings.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>UnbindDevice</strong>](ibidispl2-ibidispl2--unbinddevice.md)</td>
<td align="left"><p>Releases a printer from a bidirectional communication request.</p></td>
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
<td align="left"><p>Header</p></td>
<td align="left">Bidispl.h</td>
</tr>
</tbody>
</table>

## See also


[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)

[Bidirectional Communication Schema](bidirectional-communication-schema.md)

[Print Spooler Components](print-spooler-components.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl2%20interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





