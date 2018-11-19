---
title: requestClose element
description: The optional requestClose element is used to close an event notification message on the client computer.
ms.assetid: b2f21ab2-9205-483c-9f56-1c877edb7da2
keywords: ["requestClose element Print Devices"]
topic_type:
- apiref
api_name:
- requestClose
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# requestClose element


The optional **requestClose** element is used to close an event notification message on the client computer.

The **requestClose** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<requestClose/>
```

Attributes
----------

There are no attributes.

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="asyncprintuirequest.md" data-raw-source="[&lt;strong&gt;asyncPrintUIRequest&lt;/strong&gt;](asyncprintuirequest.md)"><strong>asyncPrintUIRequest</strong></a></p></td>
<td><p></p>
<p>A required element that describes a request issued by the printer driver to create a message on a client computer.</p></td>
</tr>
</tbody>
</table>

Examples
--------

The following code example shows how to close an event notification after a button-click on the message box has been captured for the **OK** button.

```cpp
<?xml version="1.0" ?>
   <asyncPrintUIResponse
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/response">
    <v1>
      <requestClose>
        <messageBoxUI>
          <buttonID>IDOK</buttonID>
        </messageBoxUI>
      </requestClose>
    </v1>
  </asyncPrintUIResponse>
```

## See also

[asyncPrintUIRequest](asyncprintuirequest.md)

[requestOpen](requestopen.md)
