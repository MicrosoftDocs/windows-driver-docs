---
title: Defining default values in .inf
description: Learn how camera drivers and OEMs can define default values for camera controls like Video HDR and Automatic Framing by using INF registry entries.
ms.date: 06/26/2026
ai-usage: ai-assisted
ms.topic: concept-article
#customer intent: As a camera driver developer or a device manufacturer, I want to provision default values for camera controls without requiring user interaction.
---

# Camera driver-defined default control values

Camera driver-defined default control values are preset values that a camera driver automatically applies to supported camera controls, without requiring user interaction. Camera driver developers and OEMs provision these values through INF registry entries to give a device its intended camera behavior by default. This article explains how to define these values in a driver INF.

## Why use camera driver-defined default control values

Some systems require a default camera experience that differs from the camera control specification defaults. Typical examples include:

- Setting Video HDR to a preferred default mode such as Auto or On.
- Enabling Automatic Framing by default.

Camera driver-defined default control values reduce the need for users to discover and configure these settings manually.

## How it works

These default configuration values work similarly to the ones a user can set manually through the camera settings page. The camera default control values get reapplied as current values every time the camera is used. If the user resets the camera control values in the camera settings page, the default control values prescribed through a driver INF are then reapplied as current default selection in the camera settings page. Note that user-configured default values through manual intervention in the camera settings page always take precedence over the default value defined in a driver.

## Configuration schema in INF

Specify the driver-defined default control values by using INF `AddReg` entries under a camera device-interface section (referenced by an `AddInterface` directive).

The entries describe the content of each device driver interface (DDI) SET payload consisting of the necessary parts of a [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) header followed if needed by the related structure as a data blob. Often, specifying only parts of the header is sufficient.

For Extended Camera Controls, use this schema, replacing the content delimited within <>:

```inf
HKR,"ExtendedCameraControl\<controlId>","Version",0x00010001,<version>
HKR,"ExtendedCameraControl\<controlId>","PinId",0x00010001,<pinId>
HKR,"ExtendedCameraControl\<controlId>","Flags",0x000B0001,<flags>
HKR,"ExtendedCameraControl\<controlId>","Capability",0x000B0001,<capability>
HKR,"ExtendedCameraControl\<controlId>","Data",0x1,<data blob>
```

For Windows Studio Effects controls, use this schema:

```inf
HKR,"WindowsCameraEffect\<controlId>","Version",0x00010001,<version>
HKR,"WindowsCameraEffect\<controlId>","PinId",0x00010001,<pinId>
HKR,"WindowsCameraEffect\<controlId>","Flags",0x000B0001,<flags>
HKR,"WindowsCameraEffect\<controlId>","Capability",0x000B0001,<capability>
HKR,"WindowsCameraEffect\<controlId>","Data",0x1,<data blob>
```

## Field requirements and validation

| Field | Required | Type | Behavior |
|--|--|--|--|
| `Version` | No | `FLG_ADDREG_TYPE_DWORD` (`0x00010001`) | If omitted, version `1` is assumed. If provided, it must be `1`. |
| `PinId` | Depends | `FLG_ADDREG_TYPE_DWORD` (`0x00010001`) | Required for pin-scope controls. For filter-scope controls, either omit it or use `KSCAMERA_EXTENDEDPROP_FILTERSCOPE` (`0xFFFFFFFF`). |
| `Flags` | Yes | `FLG_ADDREG_TYPE_QWORD` (`0x000B0001`) | Mandatory. If missing, the entry is invalid and ignored. |
| `Capability` | No | `FLG_ADDREG_TYPE_QWORD` (`0x000B0001`) | If present, it's validated at runtime against driver-reported capability. |
| `Data` | Depends | `FLG_ADDREG_BINVALUETYPE` | Required when `Flags` indicates a payload is needed. If payload is optional and omitted, a zero-initialized payload is used. |

> [!NOTE]
> The camera pipeline ignores invalid or unsupported entries.

## Precedence and reset behavior

Camera driver-defined default control values are baseline values. User settings have higher priority.

- If a user changes a control value manually, the user setting supersedes the camera driver-defined default control value.
- If the user selects **Reset settings** on the camera settings page, the user-defined values are removed.
- After reset, the effective defaults return to the camera driver-defined default control values (if any).

For more information about reset and default behavior, see [Camera settings page](camera-settings-page.md).

## Supported controls

Only a limited subset of extended controls supports camera driver-defined default control values. Windows might ignore attempts to configure unsupported controls. These attempts can also cause Windows Hardware Lab Kit (HLK) failures.

The INF file can define default values for the following extended camera controls:

| Control | Control Id |
|--|--|
| [KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE](ksproperty-cameracontrol-extended-scenemode.md) | 7 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE](ksproperty-cameracontrol-extended-whitebalancemode.md) | 11 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE](ksproperty-cameracontrol-extended-exposuremode.md) | 12 | 
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE](ksproperty-cameracontrol-extended-focusmode.md) | 13 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ISO](ksproperty-cameracontrol-extended-iso.md) | 14 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION](ksproperty-cameracontrol-extended-evcompensation.md) | 16 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY](ksproperty-cameracontrol-extended-focuspriority.md) | 19 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ZOOM](ksproperty-cameracontrol-extended-zoom.md) | 24 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ISO_ADVANCED](ksproperty-cameracontrol-extended-iso-advanced.md) | 26 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR](ksproperty-cameracontrol-extended-videohdr.md) | 30 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION](ksproperty-cameracontrol-extended-eyegazecorrection.md) | 40 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION](ksproperty-cameracontrol-extended-backgroundsegmentation.md) | 41 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW](ksproperty-cameracontrol-extended-digitalwindow.md) | 43 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FRAMERATE_THROTTLE](ksproperty-cameracontrol-extended-framerate-throttle.md) | 44 |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2](ksproperty-cameracontrol-extended-fieldofview2.md) | 46 |

## INF examples

### Enable Automatic Framing (Digital Window)

This example enables automatic framing for Digital Window (control ID `43`). Note that since this is a filter control, the `PinId` is intentionally ommited. Also note that this driver is assumed to be known to advertise `KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING (0x1)` `Capabiity`.

```inf
[SampleCameraInterface.AddReg]
HKR,"ExtendedCameraControl\43","Flags",0xB0001,0x1
```

Set `Flags` to `KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING`, so no payload is required.

## Set field of view (FoV) default to 100

This example sets the default field of view (control ID `46`) value to `100`. Note that since this is a filter control, the `PinId` is intentionally ommited. Also note that this driver is assumed to be known to advertise support for a `DiscreteFoVStops` containing the value `100` via the [`KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW2_CONFIGCAPS`](ksproperty-cameracontrol-extended-fieldofview2-configcaps.md) DDI.

```inf
HKR,"ExtendedCameraControl\46","Flags",0x000B0001,0x0
HKR,"ExtendedCameraControl\46","Data",0x1,64,0,0,0,0,0,0,0
```

### Set Video HDR default to Auto

This example sets Video HDR (control ID `30`) to Auto. Video HDR is a pin-scope control, so `PinId` is required. Note that this driver is assumed to be known to advertise `KSCAMERA_EXTENDEDPROP_VIDEOHDR_AUTO (0x2)` `Capability`.

```inf
[SampleCameraInterface.AddReg]
HKR,"ExtendedCameraControl\30","PinId",0x10001,0x1
HKR,"ExtendedCameraControl\30","Flags",0xB0001,0x2
```

This sample assumes the video capture pin is `1`.

## Windows Studio Effects validation notes

Currently, settable Windows Studio Effects controls share a payload structure composed of a [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) followed by a [KSCAMERA_EXTENDEDPROP_VALUE](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value). For more information, see [Windows Studio Effects (WSE) driver DDIs (on GitHub)](https://github.com/microsoft/Windows-Camera/blob/master/Samples/WindowsStudio/Windows%20Studio%20Effects%20DDIs.md).

## Requirements

**Minimum supported client:** Windows 11, version 25H2

## Related content

- [Camera settings page](camera-settings-page.md)
- [`IMFCameraConfigurationManager`](/windows/win32/api/mfidl/nn-mfidl-imfcameraconfigurationmanager)
- [`KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR`](ksproperty-cameracontrol-extended-videohdr.md)
- [`KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW`](ksproperty-cameracontrol-extended-digitalwindow.md)
- [MSOS descriptor](create-camera-device-property-keys-from-ms-os-descriptor.md)