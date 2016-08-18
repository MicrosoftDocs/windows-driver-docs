---
title: Registry Entries for Still Image Devices
author: windows-driver-content
description: Registry Entries for Still Image Devices
MS-HAID:
- 'stillimg\_c847a9b1-c96d-43b8-ad9b-13dd6580d5e7.xml'
- 'image.registry\_entries\_for\_still\_image\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cedc8afc-54c4-485e-989c-481fe30d899b
---

# Registry Entries for Still Image Devices


## <a href="" id="ddk-registry-entries-for-still-image-devices-si"></a>


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
<td><p>REG_SZ type containing the device's ISIS driver name, such as &quot;epson.pxn&quot;.</p></td>
</tr>
<tr class="odd">
<td><p>STI_DEVICE_VALUE_TIMEOUT</p></td>
<td><p>&quot;PollTimeout&quot;</p></td>
<td><p>REG_DWORD type representing the time-out value, in milliseconds, that should be used when polling the device. The default value is 1000 (1 second).</p></td>
</tr>
<tr class="even">
<td><p>STI_DEVICE_VALUE_TWAIN_NAME</p></td>
<td><p>&quot;TwainDS&quot;</p></td>
<td><p>REG_SZ type containing the displayable name of the device's TWAIN data source, such as &quot;HP PictureScan 3.0&quot;.</p></td>
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
<p>See [<strong>IStillImage::WriteToErrorLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543807).</p></td>
</tr>
<tr class="even">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\StillImage\Logging\STIMON</strong></p></td>
<td><p>Specifies which event monitor messages are written to the still image log file. Can be any combination of the following bitmasks:</p>
<p>0x1 - informational messages</p>
<p>0x2 - warning messages</p>
<p>0x4 - error messages</p></td>
</tr>
<tr class="odd">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\Class\{6BDD1FC6-810F-11D0-BEC7-08002BE2092F}</strong></p></td>
<td><p>Contains information about installed still image devices.</p></td>
</tr>
<tr class="even">
<td><p><strong>HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\StillImage\Registered Applications</strong></p></td>
<td><p>Contains a list of registered imaging applications.</p></td>
</tr>
<tr class="odd">
<td><p><strong>HKLM\SYSTEM\CurrentControlSet\Control\DeviceClass\{6bdd1fc6-810f-11d0-bec7-08002be2092f}</strong></p></td>
<td><p>Contains information about installed still image device interfaces.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Registry%20Entries%20for%20Still%20Image%20Devices%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


