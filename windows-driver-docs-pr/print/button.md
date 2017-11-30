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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# button element


The required **button** element specifies the characteristics of a button in a message box that is displayed on the client computer.

The **button** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
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
<td><p>[<strong>buttons</strong>](buttons.md)</p></td>
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

```
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

## <span id="see_also"></span>See also


[**buttons**](buttons.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20button%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





