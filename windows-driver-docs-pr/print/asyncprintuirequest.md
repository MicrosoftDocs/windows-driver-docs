---
title: asyncPrintUIRequest element
author: windows-driver-content
description: The required asyncPrintUIRequest element describes a request issued by the printer driver to create a message on a client computer.
ms.assetid: 992e3c97-b148-4802-be48-3067adb6dd0d
keywords: ["asyncPrintUIRequest element Print Devices"]
topic_type:
- apiref
api_name:
- asyncPrintUIRequest
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# asyncPrintUIRequest element


The required **asyncPrintUIRequest** element describes a request issued by the printer driver to create a message on a client computer.

The **asyncPrintUIRequest** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request.

Usage
-----

``` syntax
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
<td><p>[<strong>requestClose</strong>](requestclose.md)</p></td>
<td><p></p>
<p>An optional element that is used to close an event notification message on the client computer.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>requestOpen</strong>](requestopen.md)</p></td>
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

```
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

## <span id="see_also"></span>See also


[**requestClose**](requestclose.md)

[**requestOpen**](requestopen.md)

 

 




