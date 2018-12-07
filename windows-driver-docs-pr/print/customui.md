---
title: customUI element
description: The optional customUI element specifies a custom user interface to be displayed on a client computer.
ms.assetid: 4408dcf2-0928-4ecb-97eb-0027eceef457
keywords: ["customUI element Print Devices"]
topic_type:
- apiref
api_name:
- customUI
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# customUI element


The optional **customUI** element specifies a custom user interface to be displayed on a client computer.

The **customUI** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<customUI
  dll = "xs:string"
  entrypoint = "xs:string"
  bidi = "xs:string">
  child elements
</customUI>
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
<p>A required attribute that specifies the type of communication between the printer driver and the event notification message. If the value is <strong>true</strong>, communication is bidirectional, and the driver function in the resource DLL must return a string; see the Example section. If the value is <strong>false</strong>, communication is one-way, from the printer driver to the event notification message.</p></td>
</tr>
<tr class="even">
<td><p><strong>dll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies a resource DLL that contains the custom user interface display function. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
<tr class="odd">
<td><p><strong>entrypoint</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the function to call in the resource DLL.</p></td>
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
<p>Specifies any child element according to the custom user interface schema. See the Example section.</p></td>
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

Because the **bidi** attribute is set to **true** in the following example, the **IHVFunction** entry point function in the *Abc.dll* DLL will be called. **IHVfunction** returns the **CDATA** type data.

Examples
--------

The following code example shows how to use the **customUI** element to call and display a custom user interface on a client computer.

```cpp
<?xml version="1.0"?>
  <asyncPrintUIRequest xmlns="http://schemas.microsoft.com/2003/print/asyncui/1.0"
      xmlns:myco="http://www.myprintercompany.com">
    <requestOpen>
      <customUI dll="abc.dll" entrypoint="IHVFunction" bidi="true">
        <IHV:anyXMLData />
          CDATA
      </customUI>
    </requestOpen>
  </asyncPrintUIRequest>
```

## See also


[**requestOpen**](requestopen.md)

 

 




