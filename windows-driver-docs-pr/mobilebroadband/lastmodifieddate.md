---
title: LastModifiedDate
description: LastModifiedDate
ms.date: 04/20/2017
---

# LastModifiedDate

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The LastModifiedDate element specifies the timestamp on which the service metadata package was last changed. Based on this information, the operating system selects and loads the most recent service metadata package version.

## Usage


``` syntax
<LastModifiedDate>
  text
</LastModifiedDate>
```

## Attributes


There are no attributes.

## Text value


The timestamp value is represented in the Universal Time Coordinated (UTC) format.

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
<xs:element name="LastModifiedDate" type="xs:dateTime" />
```

## Remarks


-   The value of the LastModifiedDate element must represent the actual time that the metadata package was last changed.

-   Each time you submit your service metadata package to the Windows Hardware Dev Center Dashboard for distribution through Windows Metadata and Internet Services (WMIS), the LastModifiedDate element is updated after your package is validated.

The LastModifiedDate element is required.

 

 





