---
title: action element
description: The optional action element describes an action that will be completed when a user clicks a button in the balloon message.
ms.assetid: dae207ad-072e-4de6-b6a2-f1188ce91065
keywords: ["action element Print Devices"]
topic_type:
- apiref
api_name:
- action
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# action element


The optional **action** element describes an action that will be completed when a user clicks a button in the balloon message.

The **action** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<action
  dll = "xs:string"
  entrypoint = "xs:string">
  text
</action>
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
<td><p><strong>dll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies a DLL, supplied by an IHV, that contains a function to call when a user clicks a button.</p></td>
</tr>
<tr class="even">
<td><p><strong>entrypoint</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the function to call in the DLL supplied by the IHV. This function should return <strong>NULL</strong> when called.</p></td>
</tr>
</tbody>
</table>

Text value
----------

Optional string, formatted as CDATA, to be passed to the driver resource DLL.

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
<td><p><a href="balloonui.md" data-raw-source="[&lt;strong&gt;balloonUI&lt;/strong&gt;](balloonui.md)"><strong>balloonUI</strong></a></p></td>
<td><p></p>
<p>Provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **action** element is used with an interactive balloon, which is similar to a regular balloon, but it includes a button for the user to click.

Examples
--------

The following XML code example will run the *IHV.exe* program on the client computer

```xml
<?xml version="1.0" ?> 
  <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="<5>" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

The following code example shows how to use the **action** element to pass data to a resource DLL.

```xml
<?xml version="1.0" ?>
   <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll"/>
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="<5>" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
          <action dll="adc.dll" entrypoint="def" >
            IHV CDATA to pass into the resource DLL
          </action>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also


[**balloonUI**](balloonui.md)

 

 




