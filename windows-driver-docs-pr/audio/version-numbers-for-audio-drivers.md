---
title: Version Numbers for Audio Drivers
description: Version Numbers for Audio Drivers
ms.assetid: 6d621021-eb45-40ab-9452-97c9be2bbdd8
keywords:
- version numbers WDK audio
- audio miniport drivers WDK , version numbers
- miniport drivers WDK audio , version numbers
- audio drivers WDK , version numbers
- audio adapter drivers WDK , version numbers
- adapter drivers WDK audio , version numbers
- audio drivers WDK , models supported
- driver version numbers WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Version Numbers for Audio Drivers


## <span id="version_numbers_for_audio_drivers"></span><span id="VERSION_NUMBERS_FOR_AUDIO_DRIVERS"></span>


Windows operating systems support three types of audio driver models: the VxD, WDM, and NT4 (Microsoft Windows NT 4.0) driver models. The version number that you assign to your audio adapter driver depends on the driver model that you use, the Windows release that you target, and perhaps the Microsoft DirectX release as well. The following four tables list driver version numbers by driver model.

### <span id="driver_model__vxd_drivers_for_windows_95"></span><span id="DRIVER_MODEL__VXD_DRIVERS_FOR_WINDOWS_95"></span>Driver Model: VxD Drivers for Windows 95

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DirectX Release</th>
<th align="left">Driver Version Numbers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 95 without DirectX support</p></td>
<td align="left"><p>4.00.00.0096 to 4.02.00.0094</p></td>
</tr>
<tr class="even">
<td align="left"><p>DX1</p></td>
<td align="left"><p>4.02.00.0096 to 4.02.00.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DX2</p></td>
<td align="left"><p>4.03.00.1097 to 4.03.00.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>DX3</p></td>
<td align="left"><p>4.04.00.1097 to 4.04.00.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DX5</p></td>
<td align="left"><p>4.05.00.1000 to 4.05.00.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>DX6</p></td>
<td align="left"><p>4.06.00.1000 to 4.06.00.9999</p></td>
</tr>
</tbody>
</table>

 

### <span id="driver_model__vxd_drivers_for_windows_98"></span><span id="DRIVER_MODEL__VXD_DRIVERS_FOR_WINDOWS_98"></span>Driver Model: VxD Drivers for Windows 98

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DirectX Release</th>
<th align="left">Driver Version Numbers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DX5</p></td>
<td align="left"><p>4.05.01.2500 to 4.05.99.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>DX6</p></td>
<td align="left"><p>4.06.00.1000 to 4.06.00.9999</p></td>
</tr>
</tbody>
</table>

 

### <span id="driver_model__wdm_drivers_for_windows_me_98__and_windows_2000_and_late"></span><span id="DRIVER_MODEL__WDM_DRIVERS_FOR_WINDOWS_ME_98__AND_WINDOWS_2000_AND_LATE"></span>Driver Model: WDM Drivers for Windows Me/98, and Windows 2000 and Later

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows Release</th>
<th align="left">Driver Version Numbers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 98</p></td>
<td align="left"><p>4.10.00.2500 to 4.10.00.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>5.00.00.3500 to 5.00.00.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Me</p></td>
<td align="left"><p>4.90.00.3500 to 4.90.00.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP</p></td>
<td align="left"><p>5.10.00.3500 to 5.10.00.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Vista</p></td>
<td align="left"><p>6.00.00.3500 to 6.00.00.9999</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 7</p></td>
<td align="left"><p>7.00.00.3500 to 7.00.00.9999</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows 8</p></td>
<td align="left"><p>8.00.00.3500 to 8.00.00.9999</p></td>
</tr>
</tbody>
</table>

 

### <span id="driver_model__nt4_drivers__windows_nt_4_0_only_"></span><span id="DRIVER_MODEL__NT4_DRIVERS__WINDOWS_NT_4_0_ONLY_"></span>Driver Model: NT4 Drivers (Windows NT 4.0 Only)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows Release</th>
<th align="left">Driver Version Numbers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows NT 4.0</p></td>
<td align="left"><p>4.00.00.1400 to 4.00.00.9999</p></td>
</tr>
</tbody>
</table>

 

For device drivers that do not support DirectX, the version number should be greater than or equal to 4.00.00.0096 and less than or equal to 4.02.00.0094. Device drivers that support DirectX version 1.0 should have a version number in the range 4.02.00.0096 to 4.02.00.9999. Device drivers that support later versions of DirectX should have version numbers in the range appropriate for the distributed version of DirectX, as shown in the preceding tables.

All WDM drivers should have version numbers that are greater than or equal to 4.10.00.2500, which is the low end of the Windows 98 version-number range.

Note that WDM drivers that are written for earlier versions of Windows run correctly on later versions as well. For example, a WDM driver that is written to run in Windows 2000 also runs in Microsoft Windows XP and later.

DirectX Version 1.0 drivers work in systems with DirectX 2.0 installed. However, DirectX 2.0 drivers do not work correctly unless DirectX 2.0 is installed. The same is true for DirectX 3.0 and later releases.

A cross-platform driver should set its version number to the highest version number for the platforms on which the driver runs. For example, a vendor should use a driver-version number of 5.00.00.*Xxxx* for a driver that supports Windows 2000, Windows 98, Windows 98 SE, and Windows Me.

This section includes:

[Internal and External Version Numbers](internal-and-external-version-numbers.md)

[INF Driver-Version Entry](inf-driver-version-entry.md)

[DirectX File Version Numbers](directx-file-version-numbers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Version%20Numbers%20for%20Audio%20Drivers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


