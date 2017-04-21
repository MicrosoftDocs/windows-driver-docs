---
title: Building a WIA Microdriver
author: windows-driver-content
description: Building a WIA Microdriver
ms.assetid: dcec3079-2844-4d87-b2e4-0c1850118192
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Building a WIA Microdriver


## <a href="" id="ddk-building-a-wia-microdriver-si"></a>


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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Building%20a%20WIA%20Microdriver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


