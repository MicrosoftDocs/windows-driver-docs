---
title: Monitor INF Packages
description: Author monitor INF packages for Windows, including extension INF guidance, monitor registry settings, and current validation requirements.
keywords:
- monitor INF
- monitor extension INF
- DisplayHdrLevel
- EDID override
- DisplayID override
ms.date: 03/31/2026
ms.topic: how-to
---

# Monitor INF packages

Monitor INF packages customize the behavior of the system-supplied [monitor class function driver](monitor-class-function-driver.md) for a specific display. Typical uses include correcting bad descriptor data, overriding monitor timing information, installing a color profile, and setting monitor policy values that the monitor runtime reads from the device's driver PnP store.

> [!IMPORTANT]
> For Windows 10 and later, monitor customizations should be shipped as an [extension INF](../install/using-an-extension-inf-file.md), not as a legacy `Class=Monitor` package. Treat the monitor INF as a customization layer over the system base driver. InfVerif validates this requirement for monitor INF packages. The legacy monitor INF model is only for older operating systems and exceptional legacy scenarios.

## When to use a monitor INF package

Use a monitor INF package when you need to:

- Override incorrect EDID or DisplayID data that the monitor reports.
- Override preferred timing or supported timing ranges.
- Install an ICM profile for the monitor.
- Provide monitor policy values that Windows reads from the driver PnP store, such as HDR or Auto Color Management defaults.

If you only need the standard monitor stack, the system-provided [monitor driver stack](monitor-drivers.md) is sufficient and no vendor monitor driver is required.

## Author the package as an extension INF

Starting with Windows 10, define the monitor package as an extension INF and target the monitor's hardware IDs in the **Models** section. The extension INF then applies its registry customizations after the base driver package.

```inf
[Version]
Signature   = "$WINDOWS NT$"
Class       = Extension
ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
ExtensionId = {11111111-2222-3333-4444-555555555555}
Provider    = %Contoso%
DriverVer   = 03/31/2026,1.0.0.0
CatalogFile = ContosoMonitorExt.cat
PnpLockdown = 1

[Manufacturer]
%Contoso%=Contoso,NTamd64

[Contoso.NTamd64]
%ContosoMonitor%=ContosoMonitor_Ext, MONITOR\CONTOSO1234

[ContosoMonitor_Ext]
AddReg=ContosoMonitor_AddReg

[ContosoMonitor_AddReg]
; Add monitor overrides here

[Strings]
Contoso="Contoso"
ContosoMonitor="Contoso HDR Monitor Extension"
```

For the full extension INF model, see [Using an Extension INF File](../install/using-an-extension-inf-file.md).

## Monitor registry settings you can set from an INF

Monitor INF packages commonly populate values under `HKR` by using [**AddReg**](../install/inf-addreg-directive.md). The following sections summarize the monitor settings that are most relevant for current Windows monitor packages.

### EDID override

**Setting name:** `EDID_OVERRIDE`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,EDID_OVERRIDE,<block number>`<br/>
**Type:** `REG_BINARY`<br/>
**Example:** `HKR,EDID_OVERRIDE,0,0x00000001,00,FF,...,3B`

Use this setting to replace a specific 128-byte EDID block when the monitor reports incorrect descriptor data.

### DisplayID override

**Setting name:** `DISPLAYID_OVERRIDE`<br/>
**Applicable to:** Any display<br/>
**Minimum Windows version:** Windows 11, version 24H2<br/>
**Registry location:** `HKR,DISPLAYID_OVERRIDE,Data`<br/>
**Type:** `REG_BINARY`<br/>
**Example:** `HKR,DISPLAYID_OVERRIDE,Data,0x00000001,20,00,...,7F`

Use this setting to override DisplayID data instead of overriding individual EDID blocks.

### Add custom modes

**Setting name:** `MODES\<width>,<height>\ModeN`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,"MODES\3840,2160",Mode1`<br/>
**Type:** `REG_SZ`<br/>
**Example:** `HKR,"MODES\3840,2160",Mode1,,"30-160,48-144,+,+"`

Use this setting to override the supported timing ranges for a specific resolution.

### Preferred mode override

**Setting name:** `PreferredMode`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,PreferredMode`<br/>
**Type:** `REG_SZ`<br/>
**Example:** `HKR,,PreferredMode,,"3840,2160,60"`

Use this setting to specify the preferred display mode that Windows should use for the monitor.

### Associate a color profile

**Setting name:** `ICMProfile`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,ICMProfile`<br/>
**Type:** `REG_SZ` or `REG_MULTI_SZ`<br/>
**Example:** `HKR,,ICMProfile,0,"ContosoWideGamut.icm"`

Use this setting to associate SDR-mode color profiles with the device. If you store multiple profiles by using `REG_MULTI_SZ`, the first profile in the list is preferred as the default profile. These profiles are also used with Auto Color Management, which provides a Windows Advanced Color experience for SDR.

For more information about color profiles, see [Display calibration MHC](/windows/win32/wcs/display-calibration-mhc).

### Associate a color profile for HDR mode

**Setting name:** `ICMProfileAC`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,ICMProfileAC`<br/>
**Type:** `REG_SZ` or `REG_MULTI_SZ`<br/>
**Example:** `HKR,,ICMProfileAC,0x00010000,"ContosoHdr.icm","ContosoHdrFallback.icm"`

Use this setting to associate color profiles for HDR mode. If you store multiple profiles by using `REG_MULTI_SZ`, the first profile in the list is preferred as the default profile.

For more information about display calibration in advanced color scenarios, see 
[Advanced color ICC profiles](/windows/win32/wcs/advanced-color-icc-profiles) and [Display calibration MHC](/windows/win32/wcs/display-calibration-mhc).

### HDR certifications

**Setting name:** `DisplayHdrLevel`<br/>
**Applicable to:** Any display<br/>
**Minimum Windows version:** Windows 11<br/>
**Registry location:** `HKR,,DisplayHdrLevel`<br/>
**Type:** `REG_MULTI_SZ`<br/>
**Example:** `HKR,,DisplayHdrLevel,0x00010000,"E55026B6-496B-4ACC-B371-A1211D829ABD","20C5A9AF-CD1A-42B1-AA71-4C96A273DEF1"`

Use this setting to declare HDR certification GUIDs that identify certification levels from programs such as VESA DisplayHDR. Multiple certifications can be specified. Each category of certifications has a generic certification value that must also be included along with the specific certification level.

A special GUID can also be used to indicate that the manufacturer of the monitor attests to a good HDR experience and to request enabling HDR by default on a monitor: `F838B10E-FD7B-41E0-B6DC-3DE029FA0F87`.

### Preferred scale factor override

**Setting name:** `PreferredScaleFactor`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,PreferredScaleFactor`<br/>
**Type:** `REG_DWORD`<br/>
**Example:** `HKR,,PreferredScaleFactor,0x00010001,150`

Use this setting to override the preferred scale factor for the monitor as a percentage only if the default preferred scale factor logic does not produce a satisfactory experience. Windows typically calculates a preferred scale factor based on a number of heuristics including the display's physical size and the device type (monitor, laptop, TV, or projector).

### Monitor orientation override

**Setting name:** `MonitorOrientation`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,MonitorOrientation`<br/>
**Type:** `REG_DWORD`<br/>
**Valid values:** `DMDO_DEFAULT` (`0`) or `DMDO_180` (`2`)<br/>
**Example:** `HKR,,MonitorOrientation,0x00010001,2`

Use this setting to override the monitor's native orientation in `DMDO_xxx` format when the panel is installed upside-down. This value is an absolute orientation, not a relative rotation offset. Only `DMDO_DEFAULT` and `DMDO_180` for this setting.

### Docking orientation override

**Setting name:** `DockedOrientation`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,DockedOrientation`<br/>
**Type:** `REG_DWORD`<br/>
**Valid values:** `DMDO_DEFAULT` (`0`), `DMDO_90` (`1`), `DMDO_180` (`2`), or `DMDO_270` (`3`)<br/>
**Example:** `HKR,,DockedOrientation,0x00010001,3`

Use this setting to override the monitor orientation that Windows should use when the system is docked. This value is also stored in `DMDO_xxx` format and is independent of `MonitorOrientation`; it is not interpreted as relative to the monitor's native orientation.

### Enable boost refresh rate by default

**Setting name:** `EnableBoostRefreshRateByDefault`<br/>
**Applicable to:** Any display<br/>
**Registry location:** `HKR,,EnableBoostRefreshRateByDefault`<br/>
**Type:** `REG_DWORD`<br/>
**Example:** `HKR,,EnableBoostRefreshRateByDefault,0x00010001,1`

Use this setting to enable boost refresh rate by default for the display.

### Enable HDR by default

**Setting name:** `EnableIntegratedPanelHdrByDefault`<br/>
**Applicable to:** Integrated displays only<br/>
**Registry location:** `HKR,,EnableIntegratedPanelHdrByDefault`<br/>
**Type:** `REG_DWORD`<br/>
**Example:** `HKR,,EnableIntegratedPanelHdrByDefault,0x00010001,1`

Use this setting to enable HDR by default for an integrated panel.

### Enable Auto Color Management by default

**Setting name:** `EnableIntegratedPanelAcmByDefault`<br/>
**Applicable to:** Integrated displays only<br/>
**Registry location:** `HKR,,EnableIntegratedPanelAcmByDefault`<br/>
**Type:** `REG_DWORD`<br/>
**Example:** `HKR,,EnableIntegratedPanelAcmByDefault,0x00010001,1`

Use this setting to enable Auto Color Management by default for an integrated panel.

## Examples

### Example: EDID and mode overrides

The following example shows a monitor extension INF that overrides EDID data, provides an explicit preferred mode, and constrains the timing range for one resolution:

```inf
[ContosoMonitor_AddReg]
HKR,EDID_OVERRIDE,0,0x00000001,00,FF,FF,FF,FF,FF,FF,00,35,EE,34,12,01,00,00,00,0A
HKR,,PreferredMode,,"3840,2160,60"
HKR,"MODES\3840,2160",Mode1,,"30-160,48-144,+,+"
HKR,,ICMProfile,0,"ContosoWideGamut.icm"
```

> [!NOTE]
> `MaxResolution` and `DPMS` are deprecated and are no longer read by Windows. Don't use them in new monitor INF packages.

### Example: Multiple SDR and HDR color profiles

Use `ICMProfile` for SDR-mode profiles and `ICMProfileAC` for HDR-mode profiles. When either value is stored as `REG_MULTI_SZ`, the first profile in the list is preferred as the default profile.

```inf
[ContosoMonitor_AddReg]
HKR,,ICMProfile,0x00010000,"ContosoSdr.icm","ContosoSdrFallback.icm"
HKR,,ICMProfileAC,0x00010000,"ContosoHdr.icm","ContosoHdrFallback.icm"
```

### Example: DisplayID override

Use `DISPLAYID_OVERRIDE\Data` when you need to override DisplayID data instead of individual EDID blocks:

```inf
[ContosoMonitor_AddReg]
HKR,DISPLAYID_OVERRIDE,Data,0x00000001,20,00,00,01,29,17,01,03,80,73,41,78
```

### Example: HDR and integrated-panel ACM policy values

The following example shows the monitor policy values currently consumed from the driver PnP store by the monitor runtime:

```inf
[ContosoMonitor_AddReg]
HKR,,DisplayHdrLevel,0x00010000,"E55026B6-496B-4ACC-B371-A1211D829ABD","20C5A9AF-CD1A-42B1-AA71-4C96A273DEF1"
HKR,,EnableIntegratedPanelHdrByDefault,0x00010001,1
HKR,,EnableIntegratedPanelAcmByDefault,0x00010001,1
```

These values are intended for integrated panels and other scenarios where the monitor runtime consumes policy from the driver PnP store.

## HDR certification registry rules

`DisplayHdrLevel` is a `REG_MULTI_SZ` list of certification GUID strings. [InfVerif](/windows-hardware/drivers/devtest/infverif) enforces a requirement that a recognized specific certification GUID must be accompanied by its generic family GUID in the same multi-string value.

| If `DisplayHdrLevel` contains | It must also contain |
| --- | --- |
| Any specific VESA DisplayHDR certification GUID | `E55026B6-496B-4ACC-B371-A1211D829ABD` |
| Any specific Dolby Vision certification GUID | `4DDABBE3-5BC1-4F5C-9AA8-D611BC96F6ED` |
| Any specific  NVIDIA G-SYNC HDR certification GUID | `CEB8CBFF-1A53-45DA-895A-29628653C6B9` |
| Any specific AMD FreeSync Premium Pro certification GUID | `AE040E1F-51EC-4CAC-8501-E611C3C29CFE` |

For example, this is valid because it includes both the generic DisplayHDR GUID and a specific certification GUID:

```inf
HKR,,DisplayHdrLevel,0x00010000,"E55026B6-496B-4ACC-B371-A1211D829ABD","20C5A9AF-CD1A-42B1-AA71-4C96A273DEF1"
```

This is invalid because it includes only a specific certification GUID:

```inf
HKR,,DisplayHdrLevel,0x00010000,"20C5A9AF-CD1A-42B1-AA71-4C96A273DEF1"
```

> [!IMPORTANT]
> For a full list of certification GUIDs you should use, consult your certification program owner (for example, VESA, NVIDIA, AMD, or Dolby).

## Current InfVerif validation for monitor packages

The current monitor-specific InfVerif rules check that monitor INFs meet the following requirements:

- Monitor INF packages **must** be extension INFs rather than legacy `Class=Monitor` packages.
- `DisplayHdrLevel` must be `REG_MULTI_SZ`.
- Recognized specific HDR certification GUIDs in `DisplayHdrLevel` must include the corresponding generic family GUID.
- Other registry values are checked for the correct registry data type.

## Related articles

- [Using an INF file to override EDIDs](overriding-monitor-edids.md)
- [Using an Extension INF File](../install/using-an-extension-inf-file.md)
- [Monitor class function driver](monitor-class-function-driver.md)
- [Monitor Filter Drivers](monitor-filter-drivers.md)