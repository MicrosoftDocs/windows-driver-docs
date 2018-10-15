---
title: buttons element
author: windows-driver-content
description: The required buttons element specifies one or more buttons that are displayed in the event notification message box on the client computer.
ms.assetid: bf3718c0-37d9-4b73-a015-8a5a95535381
keywords: ["buttons element Print Devices"]
topic_type:
- apiref
api_name:
- buttons
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# buttons element


The required **buttons** element specifies one or more buttons that are displayed in the event notification message box on the client computer.

The **buttons** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
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

## See also

[button](button.md)

[messageBoxUI](messageboxui.md)
