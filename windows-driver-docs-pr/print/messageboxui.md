---
title: messageBoxUI element
description: The optional messageBoxUI element is used to display a message box on the client computer.
ms.assetid: 83fe67fe-72b0-42e2-864e-242b7b9989d9
keywords: ["messageBoxUI element Print Devices"]
topic_type:
- apiref
api_name:
- messageBoxUI
api_type:
- Schema
---

# messageBoxUI element


The optional **messageBoxUI** element is used to display a message box on the client computer.

The **messageBoxUI** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
<messageBoxUI>
  child elements
</messageBoxUI>
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
<td><p>[<strong>bitmap</strong>](bitmap.md)</p></td>
<td><p></p>
<p>An optional element that is used to display a bitmap image to the left of the body text in a message box.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>body</strong>](body.md)</p></td>
<td><p></p>
<p>A required element that provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>buttons</strong>](buttons.md)</p></td>
<td><p></p>
<p>A required element that specifies one or more buttons that are displayed in the event notification message box on the client computer.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>title</strong>](title.md)</p></td>
<td><p></p>
<p>A required element that provides text that is displayed in the title of the event notification message.</p></td>
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
<td><p>[<strong>requestOpen</strong>](requestopen.md)</p></td>
<td><p></p>
<p>An element that is used to open an event notification message on the client computer.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

See [**button**](button.md) for a code example that shows how to place an **OK** button and a **CANCEL** button a message box. See the **Examples** section for information about how to capture a button-click on a message box.

Examples
--------

The following code example shows how to notify the printer driver that the **OK** button was clicked on the message box.

```
<?xml version="1.0" ?> 
  <asyncPrintUIResponse xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/response">
    <v1>
      <requestClose>
        <messageBoxUI>
          <buttonID>IDOK</buttonID>
        </messageBoxUI >
      </requestClose>
    </v1>
  </asyncPrintUIResponse>
```

## <span id="see_also"></span>See also


[**bitmap**](bitmap.md)

[**body**](body.md)

[**button**](button.md)

[**buttons**](buttons.md)

[**requestOpen**](requestopen.md)

[**title**](title.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20messageBoxUI%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





