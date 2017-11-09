---
title: title element
description: The required title element provides text that is displayed in the title of the event notification message.
MS-HAID:
- 'async\_7dab29a9-385e-4aaa-8ddb-d6b30605781d.xml'
- 'print.title'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 60583593-9fe9-4c3c-ab86-3e7c37a8e199
keywords: ["title element Print Devices"]
topic_type:
- apiref
api_name:
- title
api_type:
- Schema
---

# title element


The required **title** element provides text that is displayed in the title of the event notification message.

The **title** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
<title
  stringID = "xs:string"
  resourceDll = "xs:string"/>
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
<td><p><strong>resourceDll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies a resource DLL that contains the title text to display in the event notification message. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
<tr class="even">
<td><p><strong>stringID</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the text to display in the title of the event notification message. The attribute value specifies the location of the text string in the resource DLL.</p></td>
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
<td><p>[<strong>balloonUI</strong>](balloonui.md)</p></td>
<td><p></p>
<p>An optional element that is used to display a message balloon on the client computer.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the attribute **resourceDll** is not specified, title text is generated from the Microsoft-supplied user interface DLL, Prnntfy.dll.

The body text loaded from the resource DLL can contain percentage (%) characters that will be replaced with text strings specified by the [**parameter**](parameter.md) child element.

Examples
--------

The following code example shows how to use the **title** element to indicate the string location in the resource DLL (in this example, stringID="1234") that contains the text to be used for the title.

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


[**balloonUI**](balloonui.md)

[**parameter**](parameter.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20title%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





