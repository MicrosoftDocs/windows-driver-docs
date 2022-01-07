---
title: Building a WIA Minidriver
description: Building a WIA Minidriver
ms.date: 04/20/2017
---

# Building a WIA Minidriver





The following header files and library files are required by all WIA minidrivers.

### Header Files

All WIA minidrivers must include the header files that are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Header File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>sti.h</em></p></td>
<td><p>Defines the STI interfaces, structures, and event GUIDs that WIA minidrivers can use.</p></td>
</tr>
<tr class="even">
<td><p><em>stiusd.h</em></p></td>
<td><p>Defines the <a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[IStiUSD](/windows-hardware/drivers/ddi/_image/index)">IStiUSD</a> interface that all WIA minidrivers must implement.</p></td>
</tr>
<tr class="odd">
<td><p><em>wiamindr.h</em></p></td>
<td><p>Defines the <a href="/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv" data-raw-source="[IWiaMiniDrv](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv)">IWiaMiniDrv</a> interface that all WIA minidrivers must implement. Other interfaces used by the WIA minidriver are defined here as well.</p></td>
</tr>
</tbody>
</table>

 

WIA minidrivers may require additional header files. The headers that are required depend on the device type and the functionality that is implemented. These requirements are noted in the reference section.

### Library Files

WIA uses the library files that are shown in the following table. All minidrivers require these libraries.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Library File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>wiaguid.lib</em></p></td>
<td><p>Exports class identifiers (CLSIDs) and interface identifiers (IIDs).</p></td>
</tr>
<tr class="even">
<td><p><em>wiaservc.lib</em></p></td>
<td><p>Exports the WIA service helper functions.</p></td>
</tr>
</tbody>
</table>

 

In your build environment, the WDK *Include* and *Lib* directories should be the first directories in the search path. This ensures that you are using the most recent versions of headers and library files.

