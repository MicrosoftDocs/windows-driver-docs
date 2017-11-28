---
title: buttons element
description: The required buttons element specifies one or more buttons that are displayed in the event notification message box on the client computer.
ms.assetid: bf3718c0-37d9-4b73-a015-8a5a95535381
keywords: ["buttons element Print Devices"]
topic_type:
- apiref
api_name:
- buttons
api_type:
- Schema
---

# buttons element


The required **buttons** element specifies one or more buttons that are displayed in the event notification message box on the client computer.

The **buttons** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
<buttons>
  child elements
</buttons>
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
<td><p>[<strong>button</strong>](button.md)</p></td>
<td><p></p>
<p>A required element that specifies the characteristics of a button in a message box that is displayed on the client computer.</p></td>
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
<td><p>[<strong>messageBoxUI</strong>](messageboxui.md)</p></td>
<td><p></p>
<p>An optional element that is used to display a message box on the client computer.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

See [**button**](button.md) for a code exapmle that shows how to use the **buttons** element to enclose two **button** elements that display an **OK** and a **CANCEL** button.

## <span id="see_also"></span>See also


[**button**](button.md)

[**messageBoxUI**](messageboxui.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20buttons%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





