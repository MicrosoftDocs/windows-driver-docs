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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# requestClose element


The optional **requestClose** element is used to close an event notification message on the client computer.

The **requestClose** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
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
<td><p>[<strong>asyncPrintUIRequest</strong>](asyncprintuirequest.md)</p></td>
<td><p></p>
<p>A required element that describes a request issued by the printer driver to create a message on a client computer.</p></td>
</tr>
</tbody>
</table>

Examples
--------

The following code example shows how to close an event notification after a button-click on the message box has been captured for the **OK** button.

```
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

## <span id="see_also"></span>See also


[**asyncPrintUIRequest**](asyncprintuirequest.md)

[**requestOpen**](requestopen.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20requestClose%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





