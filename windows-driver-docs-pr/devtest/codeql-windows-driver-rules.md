---
title: CodeQL Queries for Windows Drivers
description: CodeQL Queries for Drivers
ms.date: 01/11/2021
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
<td align="left"><p>Finds instances of deprecated pool-allocation APIs</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="codeql-windows-driver-useafterfree.md" data-raw-source="[UseAfterFree](codeql-windows-driver-useafterfree.md)">UseAfterFree</a></p></td>
<td align="left"><p>Finds select instances of UseAfterFree defects in driver source code (high-precision)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="codeql-windows-driver-probableuseafterfree.md" data-raw-source="[Probable UseAfterFree](codeql-windows-driver-probableuseafterfree.md)">Probable UseAfterFree</a></p></td>
<td align="left"><p>Finds almost all instances of UseAfterFree defects in driver source code (low-precision)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="codeql-windows-driver-padding-byte-information-disclosure.md" data-raw-source="[PaddingByteInformationDisclosure](codeql-windows-driver-padding-byte-information-disclosure.md)">PaddingByteInformationDisclosure</a></p></td>
<td align="left"><p>Checks for newly allocated structs or classes that are initialized member-by-member as they may leak information if they include padding bytes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="codeql-windows-driver-badoverflowguard.md" data-raw-source="[BadOverflowGuard](codeql-windows-driver-badoverflowguard.md)">BadOverflowGuard</a></p></td>
<td align="left"><p>Checking for overflow of an addition by comparing against one of the arguments of the addition.  Fails if the size of all the argument types are smaller than 4 bytes.</p></td>
<tr class="even">
<td align="left"><p><a href="codeql-windows-driver-infiniteloop.md" data-raw-source="[InfiniteLoop](codeql-windows-driver-infiniteloop.md)">InfiniteLoop</a></p></td>
<td align="left"><p>Finds comparisons between types of different widths in a loop condition which can cause the loop to fail to terminate.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="codeql-windows-driver-uninitializedptrfield.md" data-raw-source="[UninitializedPtrField](codeql-windows-driver-uninitiazliedptrfield.md)">UninitializedPtrField</a></p></td>
<td align="left"><p>Looks for a pointer field which was not initialized during or since class construction will cause a null pointer dereference.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="codeql-windows-driver-hardcodedivcng.md" data-raw-source="[HardcodedIVCNG](codeql-windows-driver-hardcodedivcng.md)">HardcodedIVCNG</a></p></td>
<td align="left"><p>Finds incorrect usage of initialization vectors.</p></td>
</tr>
</tbody>
</table>

 

 

