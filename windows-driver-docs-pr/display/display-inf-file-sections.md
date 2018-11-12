---
title: Display INF File Sections
description: Display INF File Sections
ms.assetid: 2075a10f-a504-4bdc-8112-9c583c5084bb
keywords:
- sideband addressing WDK Windows 2000 display
- AGP transfer rates WDK Windows 2000 display
- SoftwareSettings section
- CapabilityOverride
- INF files WDK Windows 2000 display
- display INF file sections WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Display INF File Sections


## <span id="ddk_display_inf_file_sections_gg"></span><span id="DDK_DISPLAY_INF_FILE_SECTIONS_GG"></span>


This section tells you how to write the setup information file (INF) sections that specifically apply to a graphics-adapter installation. For more general information about INF files, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

### <span id="DDInstall.SoftwareSettings_Section"></span><span id="ddinstall.softwaresettings_section"></span><span id="DDINSTALL.SOFTWARESETTINGS_SECTION"></span>DDInstall.SoftwareSettings Section

A *DDInstall*.**SoftwareSettings** section contains an [**AddReg**](https://msdn.microsoft.com/library/windows/hardware/ff546320) directive and/or a [**DelReg**](https://msdn.microsoft.com/library/windows/hardware/ff547374) directive. Each directive points to a separate, writer-defined INF section that contains registry entries for the installer to add or delete.

For example, the following code shows an **AddReg** directive that points to a writer-defined add-registry section named **ACME-1234\_SoftwareDeviceSettings**. The **DelReg** directive points to a delete-registry section named **ACME-1234\_DeleteSWSettings**.

```inf
[ACME-1234.SoftwareSettings]
AddReg=ACME-1234_SoftwareDeviceSettings
DelReg=ACME-1234_DeleteSWSettings
```

The add-registry section adds four entries to the registry and sets their values, as shown in the following code.

```inf
[ACME-1234_SoftwareDeviceSettings]
HKR,, InstalledDisplayDrivers, %REG_MULTI_SZ%, Acme1
HKR,, OverRideMonitorPower, %REG_DWORD%, 0
HKR,, MultiFunctionSupported, %REG_DWORD%, 1
HKR,, VideoDebugLevel, %REG_DWORD%, 2
```

The preceding code first sets the value of the **InstalledDisplayDrivers** entry to the name of the display driver. The code then sets the value of the **OverRideMonitorPower** entry to 0 (in other words, **FALSE**). This entry, which should be used only by OEM system vendors, controls the power behavior of the monitor device (for example, the LCD, CRT, or TV). When set to 1, **OverRideMonitorPower** limits the possible power states of the monitor device to D0 and D3.

Third, the code sets the value of the **MultiFunctionSupported** entry to 1 (in other words, **TRUE**), which is the required value for an adapter that supports multiple PCI functions. Last, the code sets the value of the **VideoDebugLevel** entry, which controls the global debug level that checked builds use for debug messages. This value ranges from 0 (no debug messages) to 3 (the most verbose messages). For more information about global debug levels, see [**VideoDebugPrint**](https://msdn.microsoft.com/library/windows/hardware/ff570170).

Most video miniport drivers are not VGA-compatible and require no **VgaCompatible** entry in the registry. If your video miniport driver is VGA-compatible, add the **VgaCompatible** entry to the registry and set its value to 1 (**TRUE**) in the add registry section, as shown here:

```registry
[ACME-1234_SoftwareDeviceSettings]
HKR,, VgaCompatible, %REG_DWORD%, 1
```

For more information about VGA-compatible video miniport drivers, see [VGA-Compatible Video Miniport Drivers (Windows 2000 Model)](vga-compatible-video-miniport-drivers--windows-2000-model-.md).

The following delete-registry section deletes three registry entries: **GraphicsClocking**, **MemClocking**, and **CapabilityOverride**.

```inf
[ACME-1234_DeleteSWSettings]
HKR,, GraphicsClocking
HKR,, MemClocking
HKR,, CapabilityOverride
```

The **CapabilityOverride** entry specifies the capabilities that the system turns off for the display driver. For example, even if the display driver implements a [**DrvEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556217) function, that capability cannot be used if the 0x10 flag is set in the **CapabilityOverride** entry.

The value of the **CapabilityOverride** registry entry is a bitwise OR of one or more of the flags that are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Disables all hardware acceleration. Equivalent to moving the hardware-acceleration slide bar (in the <strong>Display</strong> item of Control Panel) to the minimum setting.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Disables all support for Microsoft DirectDraw and Microsoft Direct3D hardware acceleration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Disables all support for Direct3D hardware acceleration. Prevents calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549404" data-raw-source="[&lt;strong&gt;DdGetDriverInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549404)"><strong>DdGetDriverInfo</strong></a><em>,</em> which request Direct3D capability and callback information, from reaching the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>Disables all support for the OpenGL installable client driver (ICD) and miniclient driver (MCD). Prevents calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556285" data-raw-source="[&lt;strong&gt;DrvSetPixelFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556285)"><strong>DrvSetPixelFormat</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556190" data-raw-source="[&lt;strong&gt;DrvDescribePixelFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556190)"><strong>DrvDescribePixelFormat</strong></a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556322" data-raw-source="[&lt;strong&gt;DrvSwapBuffers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556322)"><strong>DrvSwapBuffers</strong></a> from reaching the driver. Also prevents OPENGL_GETINFO, OPENGL_CMD and MCDFUNCS escapes from reaching the driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p>Disables support for all escapes in the driver. Prevents calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556217" data-raw-source="[&lt;strong&gt;DrvEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556217)"><strong>DrvEscape</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556203" data-raw-source="[&lt;strong&gt;DrvDrawEscape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556203)"><strong>DrvDrawEscape</strong></a> from reaching the driver.</p></td>
</tr>
</tbody>
</table>

 

For display drivers that are shipped with Windows, **CapabilityOverride** is typically set to 0x8, which disables OpenGL. Note that it is not necessary to set the 0x10 flag to disable OpenGL, and you should not set the 0x10 flag unless you intend to disable all escapes.

Microsoft Windows XP and earlier operating systems do not delete the **CapabilityOverride** registry entry when a display driver is updated--for example, from a driver that is shipped with Windows to a more recent driver provided by an independent hardware vendor (IHV). The persistent **CapabilityOverride** entry disables the same capabilities in the updated driver that it disabled in the old driver. Therefore, for Windows XP and earlier, include a **DelReg** directive in your INF file that explicitly deletes the existing **CapabilityOverride** entry. Windows XP SP1 and later operating systems automatically delete the **CapabilityOverride** entry when a driver is updated so, for those systems, it is not necessary to delete the **CapabilityOverride** entry.

### <span id="Disabling_AGP_Transfer_Rates_and_Sideband_Addressing"></span><span id="disabling_agp_transfer_rates_and_sideband_addressing"></span><span id="DISABLING_AGP_TRANSFER_RATES_AND_SIDEBAND_ADDRESSING"></span>Disabling AGP Transfer Rates and Sideband Addressing

If necessary, you can modify the INF file for your display adapter to disable certain AGP transfer rates or sideband addressing. Note that a miniport driver can change AGP transfer rates when it calls [**AgpSetRate**](https://msdn.microsoft.com/library/windows/hardware/ff538226), but such calls are not allowed to change transfer rates that are disabled in an INF file.

The *regstr.h* header file, which is shipped with the Windows Driver Kit (WDK), defines the following set of flags.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AGP_FLAG_NO_1X_RATE</p></td>
<td align="left"><p>0x00000001L</p></td>
<td align="left"><p>Disables the single-speed (66 MHz) transfer rate.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AGP_FLAG_NO_2X_RATE</p></td>
<td align="left"><p>0x00000002L</p></td>
<td align="left"><p>Disables two times the single-speed transfer rate.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>AGP_FLAG_NO_4X_RATE</p></td>
<td align="left"><p>0x00000004L</p></td>
<td align="left"><p>Disables four times the single-speed transfer rate.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AGP_FLAG_NO_8X_RATE</p></td>
<td align="left"><p>0x00000008L</p></td>
<td align="left"><p>Disables eight times the single-speed transfer rate.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>AGP_FLAG_NO_SBA_ENABLE</p></td>
<td align="left"><p>0x00000100L</p></td>
<td align="left"><p>Disables sideband addressing (SBA).</p></td>
</tr>
</tbody>
</table>

 

Two types of settings exist: global and platform-specific. The registry contains the global entries at the following location:

```registry
HKLM,"SYSTEM\CurrentControlSet\Control\AGP"
```

You can find the platform-specific entries under "Parameters" in the filter-driver service key. For example, these entries exist for the hypothetical AcmeAGP adapter in the following location in the registry:

```registry
HKLM,"SYSTEM\CurrentControlSet\Services\AcmeAGP\Parameters"
```

To disable sideband addressing for a device that has a DeviceID of 0x012A (Nuclear3D) and a VendorID of 0x1AD0 on VIA Technologies platforms, add a **Nuclear3D\_Install.HW** section to your INF file. (For more information about this type of INF Install section, see [**INF DDInstall.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330).) In this section, include an [**AddReg**](https://msdn.microsoft.com/library/windows/hardware/ff546320) directive similar to the following:

```inf
[Nuclear3D_Install.HW] 
AddReg = Nuclear3D_Reg 
```

Next, create the following section, which the **AddReg** directive points to:

```inf
[Nuclear3D_Reg] 
HKLM,"SYSTEM\CurrentControlSet\Services\viaagp\Parameters","1AD0012A",0x00030003,00,01,00,00,00,00,00,00 
```

The preceding entry indicates that the subkey identified by the string following HKLM is to be added to the registry, under the HKEY\_LOCAL\_MACHINE root. The "1AD0012A" string is the entry name, from which the first four characters compose the DeviceID, and the last four compose the VendorID for this part. The hexadecimal number following the entry name comprises a set of flags, which indicate the data type for the entry. The last part is the entry value, which disables sideband addressing.

**Important**   The bytes in the value entry are in the opposite order from those of the AGP\_FLAG\_NO\_SBA\_ENABLE flag's definition in the preceding table.

 

Suppose you determine that AGP 4X is broken on every chipset for this same device. To indicate this fact, add a second entry to the Nuclear3D\_Reg section:

```inf
[Nuclear3D_Reg] 
HKLM,"SYSTEM\CurrentControlSet\Services\viaagp\Parameters","1AD0012A",0x00030003,00,01,00,00,00,00,00,00 
HKLM,"SYSTEM\CurrentControlSet\Control\AGP","1AD0012A",0x00030003,04,00,00,00,00,00,00,00 
```

The second entry in the preceding code indicates that the subkey identified by the string following HKLM is to be added to the registry, under the HKEY\_LOCAL\_MACHINE root. As in the previous entry, the value name associated with this subkey is a string that is composed of the device's DeviceID and VendorID. The flag value is also the same. The value entry is AGP\_FLAG\_NO\_4X\_RATE, which disables the AGP 4X transfer rate. Notice that, as before, the bytes in this value entry are in the opposite order as those of the flag's value in the preceding table.

 

 





