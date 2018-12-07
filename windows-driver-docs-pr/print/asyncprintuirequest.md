---
title: asyncPrintUIRequest element
description: The required asyncPrintUIRequest element describes a request issued by the printer driver to create a message on a client computer.
ms.assetid: 992e3c97-b148-4802-be48-3067adb6dd0d
keywords: ["asyncPrintUIRequest element Print Devices"]
topic_type:
- apiref
api_name:
- asyncPrintUIRequest
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# asyncPrintUIRequest element


The required **asyncPrintUIRequest** element describes a request issued by the printer driver to create a message on a client computer.

The **asyncPrintUIRequest** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request.

Usage
-----

```xml
<asyncPrintUIRequest>
  child elements
</asyncPrintUIRequest>
```

Attributes
----------

There are no attributes.

## Child elements


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
<td><p><a href="requestclose.md" data-raw-source="[&lt;strong&gt;requestClose&lt;/strong&gt;](requestclose.md)"><strong>requestClose</strong></a></p></td>
<td><p></p>
<p>An optional element that is used to close an event notification message on the client computer.</p></td>
</tr>
<tr class="even">
<td><p><a href="requestopen.md" data-raw-source="[&lt;strong&gt;requestOpen&lt;/strong&gt;](requestopen.md)"><strong>requestOpen</strong></a></p></td>
<td><p></p>
<p>An element that is used to open an event notification message on the client computer.</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Examples
--------

The following code example shows how to use the **asyncPrintUIRequest** element.

```xml
<?xml version="1.0" ?>
   <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="5" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also


[**requestClose**](requestclose.md)

[**requestOpen**](requestopen.md)

 

 




