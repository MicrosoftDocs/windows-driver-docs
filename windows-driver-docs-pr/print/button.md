---
title: button element
description: The required button element specifies the characteristics of a button in a message box that is displayed on the client computer.
ms.assetid: 3e210599-9412-4eea-a024-338e39852199
keywords: ["button element Print Devices"]
topic_type:
- apiref
api_name:
- button
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# button element


The required **button** element specifies the characteristics of a button in a message box that is displayed on the client computer.

The **button** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<button
  stringID = "xs:string"
  resourceDll = "xs:string"
  buttonID = "xs:string"/>
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>buttonID</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the string that will be returned to the printer driver when the user clicks the button. This attribute can take one of the following values:</p>
IDOK
A button with the name &quot;OK&quot; will be displayed in the message box. When the user clicks the button, the message box returns the string &quot;IDOK&quot;.
IDCANCEL
A button with the name &quot;CANCEL&quot; will be displayed in the message box. When the user clicks the button, the message box returns the string &quot;IDCANCEL&quot;.</td>
</tr>
<tr class="even">
<td><p><strong>resourceDll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies a resource DLL that contains the text to display on the button. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
<tr class="odd">
<td><p><strong>stringID</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the text to display on the button. The attribute value specifies the location of the text string in the resource DLL.</p></td>
</tr>
</tbody>
</table>

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
<td><p><a href="buttons.md" data-raw-source="[&lt;strong&gt;buttons&lt;/strong&gt;](buttons.md)"><strong>buttons</strong></a></p></td>
<td><p></p>
<p>A required element that specifies one or more buttons that are displayed in the event notification message box on the client computer.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Buttons will be displayed at the bottom of the message box.

Examples
--------

The following code example shows how to use the **button** element to display **OK** and **CANCEL** buttons next to each other.

```xml
<?xml version="1.0" ?>
  <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <messageBoxUI>
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="5" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
          <buttons>
            <button stringID="1" resourceDll="IHV.dll" buttonID="IDOK"/>
            <button stringID="2" resourceDll="IHV.dll" buttonID="IDCANCEL"/>
          </buttons>
        </messageBoxUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also

[buttons](buttons.md)
