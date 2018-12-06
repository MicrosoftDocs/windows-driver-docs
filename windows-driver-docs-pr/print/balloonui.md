---
title: balloonUI element
description: The optional balloonUI element is used to display a message balloon on the client computer.
ms.assetid: 8db15dcb-26ed-429e-ad4c-e5dc59f9bbca
keywords: ["balloonUI element Print Devices"]
topic_type:
- apiref
api_name:
- balloonUI
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# balloonUI element


The optional **balloonUI** element is used to display a message balloon on the client computer.

The **balloonUI** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<balloonUI
  iconID = "xs:string"
  resourceDll = "xs:string">
  child elements
</balloonUI>
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
<td><p><strong>iconID</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies a printer icon to display in the event notification message. The attribute value specifies the location of the icon in the resource DLL. The icon must be 32 x 32 pixels in size, with any color depth.</p></td>
</tr>
<tr class="even">
<td><p><strong>resourceDll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies a resource DLL that contains the printer icon to display in the event notification message. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
</tbody>
</table>

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
<td><p><a href="body.md" data-raw-source="[&lt;strong&gt;body&lt;/strong&gt;](body.md)"><strong>body</strong></a></p></td>
<td><p></p>
<p>A required element that provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
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

If the attributes **iconID** and **resourceDll** are not specified, a generic printer icon is displayed in the balloon message. To display a custom printer icon, specify values for both attributes.

Examples
--------

The following code example shows how to use an interactive balloon to pass **CDATA** type data to a DLL.

```xml
<?xml version="1.0" ?> 
  <asyncPrintUIRequest xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="<5>" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
          <action dll="adc.dll" entrypoint="def" />
            IHV Data to pass into dll
            MUST BE CDATA
          </action>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also


[**action**](action.md)

[**body**](body.md)

[**requestOpen**](requestopen.md)

[**title**](title.md)

 

 




