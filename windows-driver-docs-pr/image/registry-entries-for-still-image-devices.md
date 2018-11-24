---
title: Registry Entries for Still Image Devices
description: Registry Entries for Still Image Devices
ms.assetid: cedc8afc-54c4-485e-989c-481fe30d899b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Entries for Still Image Devices





Microsoft STI makes use of several registry entries, some of which can be modified by vendor-supplied components.

### <a href="" id="ddk-vendor-modifiable-registry-values-si"></a>Vendor-Modifiable Registry Values

The following table lists the predefined registry value names and their meanings. Constants are defined in *stireg.h*. A value must be assigned to "TwainDS" if the device supports the still image [push model](creating-push-model-aware-applications.md). Values for the other names are optional.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Constant</th>
<th>Value Name String</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STI_DEVICE_VALUE_ICM_PROFILE</p></td>
<td><p>&quot;ICMProfile&quot;</p></td>
<td><p>REG_MULTI_SZ type containing names of ICM profiles for the device.</p></td>
</tr>
<tr class="even">
<td><p>STI_DEVICE_VALUE_ISIS_NAME</p></td>
<td><p>&quot;ISISDriverName&quot;</p></td>
<td><p>REG_SZ type containing the device&#39;s ISIS driver name, such as &quot;epson.pxn&quot;.</p></td>
</tr>
<tr class="odd">
<td><p>STI_DEVICE_VALUE_TIMEOUT</p></td>
<td><p>&quot;PollTimeout&quot;</p></td>
<td><p>REG_DWORD type representing the time-out value, in milliseconds, that should be used when polling the device. The default value is 1000 (1 second).</p></td>
</tr>
<tr class="even">
<td><p>STI_DEVICE_VALUE_TWAIN_NAME</p></td>
<td><p>&quot;TwainDS&quot;</p></td>
<td><p>REG_SZ type containing the displayable name of the device&#39;s TWAIN data source, such as &quot;HP PictureScan 3.0&quot;.</p></td>
</tr>
</tbody>
</table>

 

Clients of the **StillImage** COM interface should call [**IStillImage::SetDeviceValue**](https://msdn.microsoft.com/library/windows/hardware/ff543801) and [**IStillImage::GetDeviceValue**](https://msdn.microsoft.com/library/windows/hardware/ff543786) to reference the registry. Still image minidrivers can call the Win32 registry API, specifying the registry key received by the minidriver's [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method. Values for predefined registry entries can also be set from within [the INF file](inf-files-for-still-image-devices.md).

### Customized Registry Values

Still image applications and minidrivers can also store customized, device-specific values in the registry. For example, user selections obtained from customized property sheet pages could be stored under a "UserSettings" subkey.

Additionally, values for customized registry entries can be set from within [the INF file](inf-files-for-still-image-devices.md) by including a **DeviceData** entry.

### <a href="" id="ddk-non-modifiable-registry-entries-si"></a>Nonmodifiable Registry Entries

The following table lists registry entries that should not be modified by vendor software.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry Key</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\StillImage\Logging\STICLI</strong></p></td>
<td><p>Specifies which vendor-generated messages are written to the still image log file. Can be any combination of the following bitmasks:</p>
<p>0x1 - informational messages</p>
<p>0x2 - warning messages</p>
<p>0x4 - error messages</p>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff543807" data-raw-source="[&lt;strong&gt;IStillImage::WriteToErrorLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543807)"><strong>IStillImage::WriteToErrorLog</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\StillImage\Logging\STIMON</strong></p></td>
<td><p>Specifies which event monitor messages are written to the still image log file. Can be any combination of the following bitmasks:</p>
<p>0x1 - informational messages</p>
<p>0x2 - warning messages</p>
<p>0x4 - error messages</p></td>
</tr>
<tr class="odd">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\Class{6BDD1FC6-810F-11D0-BEC7-08002BE2092F}</strong></p></td>
<td><p>Contains information about installed still image devices.</p></td>
</tr>
<tr class="even">
<td><p><strong>HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\StillImage\Registered Applications</strong></p></td>
<td><p>Contains a list of registered imaging applications.</p></td>
</tr>
<tr class="odd">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\DeviceClass{6bdd1fc6-810f-11d0-bec7-08002be2092f}</strong></p></td>
<td><p>Contains information about installed still image device interfaces.</p></td>
</tr>
</tbody>
</table>

 

 

 




