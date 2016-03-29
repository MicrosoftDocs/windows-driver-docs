---
title: Bidirectional Communication Interfaces
description: Bidirectional Communication Interfaces
ms.assetid: 5dbc3e61-3346-4e89-96c8-b214719177f0
keywords: ["bidi communication interfaces WDK print", "bidirectional communication interfaces WDK print"]
---

# Bidirectional Communication Interfaces


The following interfaces are used in bidi communication.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Interface</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[IBidiRequest](ibidirequest.md)</p></td>
<td align="left"><p>Compose a bidi request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[IBidiRequestContainer](ibidirequestcontainer.md)</p></td>
<td align="left"><p>Compose and retrieve a list of bidi requests.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[IBidiSpl](ibidispl.md)</p></td>
<td align="left"><p>Send a bidi request or a list of bidi requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[IBidiSpl2](ibidispl2.md)</p></td>
<td align="left"><p>Send bidi requests as XML strings or streams.</p></td>
</tr>
</tbody>
</table>

 

The [IBidiSpl2](ibidispl2.md) interface, which is introduced in Windows Vista, enables an application or driver to send bidi requests by using XML rather than function calls. This XML exchange uses the bidi communication request and response schema, and the XML objects can be either strings or IStreams.

For more information about the bidirectional communication interfaces, see the [Printing and Print Spooler Interfaces](http://go.microsoft.com/fwlink/p/?linkid=70002) section in the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidirectional%20Communication%20Interfaces%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




