---
title: Building a WIA Minidriver
description: Building a WIA Minidriver
MS-HAID:
- 'WIA\_GS\_23f2b476-93e7-44cc-a777-691d8d12823a.xml'
- 'image.building\_a\_wia\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7a13d355-f42e-406d-8cba-4739df1af9fa
---

# Building a WIA Minidriver


## <a href="" id="ddk-building-a-wia-minidriver-si"></a>


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
<td><p>Defines the [IStiUSD](https://msdn.microsoft.com/library/windows/hardware/ff543827) interface that all WIA minidrivers must implement.</p></td>
</tr>
<tr class="odd">
<td><p><em>wiamindr.h</em></p></td>
<td><p>Defines the [IWiaMiniDrv](https://msdn.microsoft.com/library/windows/hardware/ff545027) interface that all WIA minidrivers must implement. Other interfaces used by the WIA minidriver are defined here as well.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Building%20a%20WIA%20Minidriver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




