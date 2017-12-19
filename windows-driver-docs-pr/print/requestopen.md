---
title: requestOpen element
description: The requestOpen element is used to open an event notification message on the client computer.
ms.assetid: c1797295-9aca-4986-bd9d-482bb7049942
keywords: ["requestOpen element Print Devices"]
topic_type:
- apiref
api_name:
- requestOpen
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# requestOpen element


The **requestOpen** element is used to open an event notification message on the client computer.

The **requestOpen** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
<requestOpen>
  child elements
</requestOpen>
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
<td><p>[<strong>balloonUI</strong>](balloonui.md)</p></td>
<td><p></p>
<p>An optional element that is used to display a message balloon on the client computer.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>customUI</strong>](customui.md)</p></td>
<td><p></p>
<p>An optional element that specifies a custom user interface to be displayed on a client computer.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>messageBoxUI</strong>](messageboxui.md)</p></td>
<td><p></p>
<p>An optional element that is used to display a message box on the client computer.</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>asyncPrintUIRequest</strong>](asyncprintuirequest.md)</p></td>
<td><p></p>
<p>A required element that describes a request issued by the printer driver to create a message on a client computer.</p></td>
</tr>
</tbody>
</table>

Examples
--------

The following code example opens an event notification message.

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


[**asyncPrintUIRequest**](asyncprintuirequest.md)

[**balloonUI**](balloonui.md)

[**customUI**](customui.md)

[**messageBoxUI**](messageboxui.md)

[**requestClose**](requestclose.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20requestOpen%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





