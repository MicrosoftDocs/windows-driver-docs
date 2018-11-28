---
title: IPrinterBidiSchemaResponses interface
description: The IPrinterBidiSchemaResponses interface represents a set of bidi responses populated by USB Bidi Extension JavaScript methods getSchemas and getStatus.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2E68C4AA-D235-46D2-81D6-D6C7E84C2FEF
keywords: ["IPrinterBidiSchemaResponses interface Print Devices", "IPrinterBidiSchemaResponses interface Print Devices , described"]
topic_type:
- apiref
api_name:
- IPrinterBidiSchemaResponses
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterBidiSchemaResponses interface

The IPrinterBidiSchemaResponses interface represents a set of bidi responses populated by USB Bidi Extension JavaScript methods **getSchemas** and **getStatus**.

Members
-------

The **IPrinterBidiSchemaResponses** interface inherits from the [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPrinterBidiSchemaResponses** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrinterBidiSchemaResponses** interface has these methods.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="iprinterbidischemaresponses--addbool.md" data-raw-source="[&lt;strong&gt;AddBool&lt;/strong&gt;](iprinterbidischemaresponses--addbool.md)"><strong>AddBool</strong></a></td>
<td><p>The AddBool method adds a new response of type BIDI_BOOL to the collection.</p></td>
</tr>
<tr class="even">
<td><a href="iprinterbidischemaresponses--addint32.md" data-raw-source="[&lt;strong&gt;AddInt32&lt;/strong&gt;](iprinterbidischemaresponses--addint32.md)"><strong>AddInt32</strong></a></td>
<td><p>The AddInt32 method adds a new response of type BIDI_INT to the collection.</p></td>
</tr>
<tr class="odd">
<td><a href="iprinterbidischemaresponses-addblob.md" data-raw-source="[&lt;strong&gt;AddBlob&lt;/strong&gt;](iprinterbidischemaresponses-addblob.md)"><strong>AddBlob</strong></a></td>
<td><p>The AddBlob method adds a new response of type BIDI_BLOB to the collection.</p></td>
</tr>
<tr class="even">
<td><a href="iprinterbidischemaresponses-addenum.md" data-raw-source="[&lt;strong&gt;AddEnum&lt;/strong&gt;](iprinterbidischemaresponses-addenum.md)"><strong>AddEnum</strong></a></td>
<td><p>The AddEnum method adds a new response of type BIDI_ENUM to the collection.</p></td>
</tr>
<tr class="odd">
<td><a href="iprinterbidischemaresponses-addfloat.md" data-raw-source="[&lt;strong&gt;AddFloat&lt;/strong&gt;](iprinterbidischemaresponses-addfloat.md)"><strong>AddFloat</strong></a></td>
<td><p>The AddFloat method adds a new response of type BIDI_FLOAT to the collection.</p></td>
</tr>
<tr class="even">
<td><a href="iprinterbidischemaresponses-addnull.md" data-raw-source="[&lt;strong&gt;AddNull&lt;/strong&gt;](iprinterbidischemaresponses-addnull.md)"><strong>AddNull</strong></a></td>
<td><p>The AddNull method adds a new response of type BIDI_NULL to the collection.</p></td>
</tr>
<tr class="odd">
<td><a href="iprinterbidischemaresponses-addrequerykey.md" data-raw-source="[&lt;strong&gt;AddRequeryKey&lt;/strong&gt;](iprinterbidischemaresponses-addrequerykey.md)"><strong>AddRequeryKey</strong></a></td>
<td><p>The AddRequeryKey method adds a new QueryKey to re-query upon return from the getSchemas call.</p></td>
</tr>
<tr class="even">
<td><a href="iprinterbidischemaresponses-addstring.md" data-raw-source="[&lt;strong&gt;AddString&lt;/strong&gt;](iprinterbidischemaresponses-addstring.md)"><strong>AddString</strong></a></td>
<td><p>The AddString method adds a new response of type BIDI_STRING to the collection.</p></td>
</tr>
<tr class="odd">
<td><a href="iprinterbidischemaresponses-addtext.md" data-raw-source="[&lt;strong&gt;AddText&lt;/strong&gt;](iprinterbidischemaresponses-addtext.md)"><strong>AddText</strong></a></td>
<td><p>The AddText method adds a new response of type BIDI_TEXT to the collection.</p></td>
</tr>
</tbody>
</table>
