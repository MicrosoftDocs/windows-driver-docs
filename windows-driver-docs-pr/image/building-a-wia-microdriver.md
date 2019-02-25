---
title: Building a WIA Microdriver
description: Building a WIA Microdriver
ms.assetid: dcec3079-2844-4d87-b2e4-0c1850118192
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building a WIA Microdriver





The following header files and library files are required by all WIA microdrivers.

### Header Files

All WIA microdrivers must include the header files that are shown in the following table.

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
<td><p><em>wiamicro.h</em></p></td>
<td><p>Defines the function prototypes and structures that the WIA microdriver requires.</p></td>
</tr>
</tbody>
</table>

 

WIA microdrivers may require additional header files. The headers that are required depend on the device type and the functionality that is implemented. These requirements are noted in the reference section.

### Library Files

WIA uses the library files shown in the following table.

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
<td><p>Exports class identifiers (CLSIDs) and interface identifiers (IIDs). All WIA microdrivers require this library.</p></td>
</tr>
</tbody>
</table>

 

In your build environment, the WDK *Include* and *Lib* directories should be the first directories in the search path. This ensures that you are using the most recent versions of the headers and library files.

**Note**   If you wish to use logging with Visual C++ 6.0 when building a microdriver, turn on logging for *Wiafbdrv.dll* by using the *Wialogcfg.exe* program that came with the Windows Me Driver Development Kit (DDK). Also, check the INF file to make sure that the microdriver name is correct. In the INF, check the **DeviceData** section for MicroDriver="YOURNAME.DLL".

 

 

 




