---
title: parameter element
description: The optional parameter element specifies a text string that is substituted for a percentage ( ) character in the text of an event notification message.
ms.assetid: 6a43af7d-da00-4038-b1a8-a076d07c4c1a
keywords: ["parameter element Print Devices"]
topic_type:
- apiref
api_name:
- parameter
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# parameter element


The optional **parameter** element specifies a text string that is substituted for a percentage (%) character in the text of an event notification message.

The **parameter** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

```xml
<parameter
  stringID = "xs:string"
  resourceDll = "xs:string"
  type = "xs:string"/>
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
<p>An optional attribute that specifies a resource DLL that contains the text to display in the event notification message. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
<tr class="even">
<td><p><strong>stringID</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the text to display at the location of the percentage (%) character in the text of the event notification message. The attribute value specifies the location of the text string in the resource DLL.</p></td>
</tr>
<tr class="odd">
<td><p><strong>type</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies the name of the printer or document. This attribute can take one of the following values:DocumentThe name of the document being printed.PrinterNameThe name of the printer, as listed in the Printers and Faxes folder in Control Panel, for example, &quot;Fabrikam 5000 on \printserver&quot; or &quot;Printer in upstairs bedroom.&quot;</p></td>
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
<td><p><a href="body.md" data-raw-source="[&lt;strong&gt;body&lt;/strong&gt;](body.md)"><strong>body</strong></a></p></td>
<td><p></p>
<p>A required element that provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
</tr>
<tr class="even">
<td><p><a href="title.md" data-raw-source="[&lt;strong&gt;title&lt;/strong&gt;](title.md)"><strong>title</strong></a></p></td>
<td><p></p>
<p>The required title element provides text that is displayed in the title of the event notification message.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The text loaded from the resource DLL can contain percentage (%) characters that will be replaced with text strings specified by the **parameter** element.

Examples
--------

The following code example shows how the **parameter** element can be used to generate a complete event notification message.

In this example, the **stringID** values specify the following:

-   User interface string 100 in the driver resource DLL is "Printer is out of %1 ink; please open %2 and replace the ink cartridge."
-   User interface string 5 in the Microsoft-supplied user interface DLL is "yellow".
-   User interface string 1002 in the driver resource DLL is "Side Access Door B".

```xml
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

With the preceding XML code, the following body text (stringID="100") is displayed in the event notification message: "Printer is out of yellow ink; please open Side Access Door B and replace the ink cartridge."

## See also

[body](body.md)

[title](title.md)
