---
title: customData element
description: The optional customData element specifies a custom data source for this asynchronous notification XML schema.
ms.assetid: 5e14a627-72c0-440d-b616-6963c3d69d2b
keywords: ["customData element Print Devices"]
topic_type:
- apiref
api_name:
- customData
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# customData element


The optional **customData** element specifies a custom data source for this asynchronous notification XML schema.

The **customData** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<customData
  dll = "xs:string"
  entryPoint = "xs:string"
  bidi = "xs:string">
  child elements
</customData>
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
<td><p><strong>bidi</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the type of communication between the printer driver and the event notification message. If the value is <strong>true</strong>, communication is bidirectional, and the driver function in the resource DLL must return a string. If the value is <strong>false</strong>, communication is one-way, from the printer driver to the event notification message. For more information, see the following Example and Remarks sections.</p></td>
</tr>
<tr class="even">
<td><p><strong>dll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies a resource DLL that contains the custom data source. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
<tr class="odd">
<td><p><strong>entryPoint</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the data source entry point in the resource DLL.</p></td>
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
<td><p><strong>Anything</strong></p></td>
<td><p></p>
<p>Specifies any child element according to the custom data schema. For more information, see the following Example section.</p></td>
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

The custom data that you capture must be provided as a **CDATA** type.

Examples
--------

The following code example shows how you can use the **customData** element to obtain your custom data.

```xml
<?xml version="1.0"?>
  <asyncPrintUIRequest xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request"
      xmlns:myco="http://www.myprintercompany.com">
    <requestOpen>
      <customData dll="abc.dll" entrypoint="IHVFunction" bidi="true">
        <IHV:anyXMLData />
          CDATA
      </customData>
    </requestOpen>
</asyncPrintUIRequest>
```

## See also

[requestOpen](requestopen.md)
