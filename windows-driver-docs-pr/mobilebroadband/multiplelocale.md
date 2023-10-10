---
title: MultipleLocale
description: MultipleLocale
ms.date: 04/20/2017
---

# MultipleLocale

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The MultipleLocale element specifies if the service metadata package supports multiple locales or not.

## Usage


``` syntax
<MultipleLocale>
  text
</MultipleLocale>
```

## Attributes


There are no attributes.

## Text value


A boolean value that is true if the service metadata package supports multiple locales.

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
<td><p><a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a></p></td>
<td><p>The <a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a> element specifies the attributes of the device metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="MultipleLocale" type ="xs:boolean" />
```

## Remarks


-   To support multiple locales in the service metadata package , Set the MultipleLocale element to **true**. This element is not supported on Windows 7. If this element is not specified, the default value is true.

-   If there is both a single locale service metadata package and a multiple-locale service metadata package on a user's computer, Windows uses the multiple-locale service metadata package, if all other ranking values are the same.

 

 





