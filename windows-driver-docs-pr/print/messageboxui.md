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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# messageBoxUI element


The optional **messageBoxUI** element is used to display a message box on the client computer.

The **messageBoxUI** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
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
<td><p><a href="bitmap.md" data-raw-source="[&lt;strong&gt;bitmap&lt;/strong&gt;](bitmap.md)"><strong>bitmap</strong></a></p></td>
<td><p></p>
<p>An optional element that is used to display a bitmap image to the left of the body text in a message box.</p></td>
</tr>
<tr class="even">
<td><p><a href="body.md" data-raw-source="[&lt;strong&gt;body&lt;/strong&gt;](body.md)"><strong>body</strong></a></p></td>
<td><p></p>
<p>A required element that provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
</tr>
<tr class="odd">
<td><p><a href="buttons.md" data-raw-source="[&lt;strong&gt;buttons&lt;/strong&gt;](buttons.md)"><strong>buttons</strong></a></p></td>
<td><p></p>
<p>A required element that specifies one or more buttons that are displayed in the event notification message box on the client computer.</p></td>
</tr>
<tr class="even">
<td><p><a href="title.md" data-raw-source="[&lt;strong&gt;title&lt;/strong&gt;](title.md)"><strong>title</strong></a></p></td>
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
<td><p><a href="requestopen.md" data-raw-source="[&lt;strong&gt;requestOpen&lt;/strong&gt;](requestopen.md)"><strong>requestOpen</strong></a></p></td>
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

```xml
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

## See also

[bitmap](bitmap.md)

[body](body.md)

[button](button.md)

[buttons](buttons.md)

[requestOpen](requestopen.md)

[title](title.md)
