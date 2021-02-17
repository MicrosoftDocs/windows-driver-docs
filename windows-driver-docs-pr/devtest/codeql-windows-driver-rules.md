---
title: CodeQL Queries for Windows Drivers
description: CodeQL Queries for Drivers
ms.date: 01/11/2021
ms.localizationpriority: medium
---

# Supplemental Windows Driver CodeQL Queries

This section lists and describes a handful of [CodeQL queries](./static-tools-and-codeql.md) that are included as part of the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools) that are specific to driver development for the Windows platform.

## List of Queries

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Query Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="codeql-windows-driver-wdkdeprecatedapi.md" data-raw-source="[WDK Deprecated API](codeql-windows-driver-wdkdeprecatedapi.md)">WDK Deprecated API</a></p></td>
<td align="left"><p>Finds all instances of deprecated pool-allocation APIs</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="codeql-windows-driver-useafterfree.md" data-raw-source="[UseAfterFree](codeql-windows-driver-useafterfree.md)">UseAfterFree</a></p></td>
<td align="left"><p>Finds select instances of UseAfterFree defects in driver source code (high-precision)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="codeql-windows-driver-probableuseafterfree.md" data-raw-source="[Probable UseAfterFree](codeql-windows-driver-probableuseafterfree.md)">Probable UseAfterFree</a></p></td>
<td align="left"><p>Finds almost all instances of UseAfterFree defects in driver source code (low-precision)</p></td>
</tr>
</tbody>
</table>

 

 

