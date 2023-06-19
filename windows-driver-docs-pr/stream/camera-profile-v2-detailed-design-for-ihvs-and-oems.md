---
title: Camera Profile V2 detailed design for IHVs and OEMs
description: This article provides information about Camera Profile V2 detailed design for IHVs and OEMs.
ms.date: 06/08/2023
---

# Detailed design for IHVs and OEMs (Camera Profile V2)

To help understand the new Camera Profile V2 schema, we start with a simple profile declaration and dissect it to understand the individual sections.

We take a hypothetical camera that supports the new High Frame Rate profile. We first define some hypothetical hardware constraints for our device.

1. Preview pin is pin 0. In the KSFILTER_DESCRIPTOR defined by the camera driver, when the array of KSPIN_DESCRIPTOR_EX is defined, the first KSPIN_DESCRIPTOR_EX is the Preview pin's descriptor. Similarly, pin 1 is Capture pin and pin 2 is Photo pin.

1. Due to hardware limitation, the device in question can't handle scaling at the frame rates 60 fps or greater. Therefore, both the Preview and Capture streams must have the same resolution.

1. Similarly, the device also can't handle color space conversion for 60 fps or higher, so the subtype must be the same between Preview and Capture.

1. Camera is capable of streaming 4K 16x9 video at 60 fps. Camera is also capable of 3840x2880@60fps (4:3 video at 60 fps).

1. Camera isn't able to provide any photo operations when running at 60 fps.

1. In addition to the High Frame Rate Profile, we declare a Video Recording Profile.

1. The Video Recording Profile allows any combination of media types, but no media type at greater than 30 fps.

1. The Video Recording Profile also supports single photo operation (for example, non-Photo Sequence).

For INF based declaration, in the DDInstall.Interfaces section, the AddReg directive is used to publish the profile information.

Every Pin Media Type Filter must be assigned a registry entry name. This name must be MTF# where # represents an integer value. The integer value doesn't need to be sequential, merely unique as it represents a named value in the OS registry.

Given these constraints, we can declare the following profile:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","BlockedControls",0,"VHDR;VPS;{E0766E84-36A2-4945-906D-092ECBD87445},2;WARM1"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"

; Declare the Video Recording Profile here.
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

## OEMCameraProfileVersion

To enable the Camera Profile V2 support, declare the profile version:

OEMCameraProfileVersion entry defines our profile version and for this revision of the spec, must be 2:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
```

If the OEMCameraProfileVersion registry entry isn't present, and OEMCameraProfile entry is present, the pipeline falls back to the Camera Profile 1507 schema.

This ensures backwards compatibility with existing Camera Profiles.

When the OEMCameraProfileVersion entry is available, any existing Camera Profile 1507 information is ignored and only the Camera Profile V2 will be processed.

**Note**: If OEMCameraProfileVersion entry is set to 2, but no Camera Profile V2 declarations are found, profiles won't be published.

Once declared, all profiles must be stored under the Profiles registry key under the Device Interface node.

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
```

Each profile must be a subkey under the Profiles key using the Profile ID.

Profile ID is a combination of Profile Type, Profile Index.

The Profile Type may be one of the following strings or may be a {GUID} string:

- KSCAMERAPROFILE_VideoRecording

- KSCAMERAPROFILE_HighQualityPhoto

- KSCAMERAPROFILE_BalancedVideoAndPhoto

- KSCAMERAPROFILE_VideoConferencing

- KSCAMERAPROFILE_PhotoSequence

- KSCAMERAPROFILE_FaceAuth_Mode

- KSCAMERAPROFILE_HighFrameRate

- KSCAMERAPROFILE_HDRWithWCGVideo

- KSCAMERAPROFILE_HDRWithWCGPhoto

- KSCAMERAPROFILE_VariablePhotoSequence

- KSCAMERAPROFILE_VideoHDR8

Profile Index may be any value from 0 to 0x7FFFFFFF. Index values with the high order bit set are reserved for internal use.

The basis of Camera Profile V2 is broken down into two main schema entries:

- Profile Constraints

- Pin Media Type Filters

## Profile Constraint

Profile Constraints is a profile wide declaration influencing the processing of Pin Media Type Filters. These are the six tags supported. They may appear in any order separated by a ";":

| Profile Constraint | Description |
|--|--|
| LRS | Lock Resolution across all pins. All pins declared in the profile must have the same resolution when active. |
| LFR | Lock Frame Rate across all pins. All pins declared in the profile must have the same frame rate when active. |
| LST | Lock Subtype across all pins. All pins declared in the profile must have the same subtype when active. |
| AAR | Apply the Pin level profile declaration to all aspect ratios.<br><br>Resolution based filtering is done by using the product of Width * Height of the resolution and that product is used as a value for comparison. However, if the AAR tag isn't set, the comparison will only be done for the resolutions with the same aspect ratio. |
| DIS | Disabled. If this Constraint is used for the Profile Constraint, Pin Media Type Filter is ignored and will be treated as an invalid profile syntax.<br><br>This tag may not be combined with any other Profile Constraint tags. |
| UAR | Allow arbitrary combination of resolution aspect ratios between pins.<br><br>By default, aspect ratios across pins must be the same. This tag removes that default constraint.<br><br>**Note**: Applications are encouraged to keep the same aspect ratio across the available pins. |

If the UAR tag isn't set on a profile declaration, all aspect ratio between the pins must be the same. Specifically, streaming Preview at 16:9 while taking a photo or streaming from the Capture pin at 4:3 isn't supported. Attempts at doing so will result in an error.

Processing the sample profile above:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
```

The Profile Constraint indicates that for the \[KSCAMERAPROFILE_HighFrameRate,0\] profile, resolutions and the subtype across all pins must be the same. This matches our hypothetical camera's HW constraint (no scaling/color space conversion when running at 60 fps or higher).

### Encoder Constraints

An optional set of Profile Constraints may contain recommended encoder parameters for applications that choose to select a profile for video encoding operations. For example, an IHV/OEM may choose to recommend using HEVC over H264 for certain systems when a media type exceeds a predetermined threshold in terms of resolution and/or frame rate.

In addition, because the HW encoder present on the machine may provide a more optimal operation when configured with the encoding parameters, the OEM may choose to author a profile with more "hints" to the application.

To facilitate this support, the following additional Constraints may be added to any profile.

#### Preferred Encoded Subtype

The following list of subtypes are the Preferred Encoded Subtype for the encoder:

- eSPSubtype_H264

- eSPSubtype_HEVC

These two constraints are mutually exclusive. Only one may be declared. Declaring both will result in an invalid profile and will be rejected.

When the Preferred Encoded Subtype Constraint is declared, the IMFSensorProfile's MF attribute store exposes the declared Preferred Encoded Subtype with the MF_MT_SUBTYPE attribute.

#### Preferred Encoder Profile

The following Preferred Encoder Profile list corresponds to the [**eAVEncH264VProfile**](/windows/win32/api/codecapi/ne-codecapi-eavench264vprofile) enumeration.

- eSPProfile_Simple

- eSPProfile_Base

- eSPProfile_Main

- eSPProfile_High

- eSPProfile_422

- eSPProfile_High10

- eSPProfile_444

- eSPProfile_Extended

- eSPProfile_ScalableBase

- eSPProfile_ScalableHigh

- eSPProfile_MultiviewHigh

- eSPProfile_StereoHigh

- eSPProfile_ConstrainedBase

- eSPProfile_UCConstrainedHigh

- eSPProfile_UCScalableConstrainedBase

- eSPProfile_UCScalableConstrainedHigh

- eSPProfileH265_Main_420_8

- eSPProfileH265_Main_420_10

- eSPProfileH265_Main_420_12

- eSPProfileH265_Main_422_10

- eSPProfileH265_Main_422_12

- eSPProfileH265_Main_444_8

- eSPProfileH265_Main_444_10

- eSPProfileH265_Main_444_12

- eSPProfileH265_Monochrome_12

- eSPProfileH265_Monochrome_16

- eSPProfileH265_MainIntra_420_8

- eSPProfileH265_MainIntra_420_10

- eSPProfileH265_MainIntra_420_12

- eSPProfileH265_MainIntra_422_10

- eSPProfileH265_MainIntra_422_12

- eSPProfileH265_MainIntra_444_8

- eSPProfileH265_MainIntra_444_10

- eSPProfileH265_MainIntra_444_12

- eSPProfileH265_MainIntra_444_12

- eSPProfileH265_MainStill_420_8

- eSPProfileH265_MainStill_444_8

- eSPProfileH265_MainStill_444_16

The Preferred Encoder Profiles declaration above are mutually exclusive. Only one may be declared. Declaring more than one will result in an invalid profile and will be rejected.

When the Preferred Encoder Profile Constraint is declared, the IMFSensorProfile's MF attribute store exposes the declared Preferred Encoder Profile with the MF_MT_MPEG2_PROFILE attribute.

NOTE: eSPProfileH265 profiles are valid only for HEVC encoded subtypes.

#### Recommended B Frame Count

The Recommended BFrame Count Constraint provide a way for the OEM to indicate the recommended B frame count for the encoded video:

- eSPBFCount_X

Where X represents the BFrame Count: For example, eSPBFCount_0 indicates 0 B Frame Count.

When the Recommended BFrame Count Constraint is declared, the IMFSensorProfile's MF attribute store exposes the declared Recommended BFrame Count with the CODECAPI_AVEncMPVDefaultBPictureCount attribute.

#### Recommended Bit Rate

The Recommended Bit Rate Constraint provides a way for the OEM to specify both an average encoding bit rate (when using an appropriate encoding rate control mode) and/or maximum bit rate:

- eSPBitRate_XXXXX

- eSPMaxBitRate_XXXXX

These two Constraints may be specified independently or together. The XXXXX represents the bit rate in Kbps. For example, eSPBitRate_5000 represents 5,000,000 bits per second.

The eSPBitRate_XXXXX, when specified by the OEM will be exposed through the IMFSensorProfile's MF attribute store via the CODECAPI_AVEncCommonMeanBitRate attribute.

The eSPMaxBitRate_XXXXX when specified by the OEM, will be exposed through the IMFSensorProfile's MF attribute store via the CODECAPI_AVEncCommonMaxBitRate.

### Sample Encoder Constraint

The following sample INF shows how an OEM may declare the Encoder Constraints:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","Constraint",0,"eSPSubtype_HEVC;eSPProfile_Main;eSPBFCount_1;eSPBitRate_20000;eSPMaxBitRate_50000"
```

The sample Encoder Constraint above would result in the KSCAMERAPROFILE_VideoRecording,0 profile's IMFSensorProfile (see API description below) MF attribute store containing the various encoder attributes as follows:

```cpp
HRESULT
CheckEncoderParameters(
    _In_ IMFSensorProfile* pProfile
    )
{
    HRESULT hr = S_OK;
    ComPtr<IMFAttributes> spAttributes;
    GUID guidSubtype = GUID_NULL;
    UINT32 eProfile = eAVEncH264VProfile_unknown;
    UINT32 uiBFrameCount = 0;
    UINT32 uiBitRate = 0;
    UINT32 uiMaxBitRate = 0;

    if (nullptr == pProfile)
    {
        return E_INVALIDARG;
    }

    RETURN_IF_FAILED (pProfile->QueryInterface(IID_PPV_ARGS(&spAttributes)));
    if (SUCCEEDED(spAttributes->GetGUID(MF_MT_SUBTYPE, &guidSubtype)))
    {
        if (guidSubtype == MFVideoFormat_HEVC)
        {
            // Use HEVC codec.
        }
        else
        {
            // Use H264 codec.
        }
    }
    if (SUCCEEDED(spAttributes->GetUINT32(MF_MT_MPEG2_PROFILE, &eProfile)))
    {
        // Use the eProfile provided for encoder profile.
    }
    if (SUCCEEDED(spAttributes->GetUINT32(CODECAPI_AVEncMPVDefaultBPictureCount, &uiBFrameCount)))
    {
        // This is the BFrame count...
    }
    if (SUCCEEDED(spAttributes->GetUINT32(CODECAPI_AVEncCommonMeanBitRate, &uiBitRate)))
    {
        // This is the average bit rate...
    }
    if (SUCCEEDED(spAttributes->GetUINT32(CODECAPI_AVEncCommonMaxBitRate, &uiMaxBitRate)))
    {
        // This is the max bit rate...
    }

    return hr;
}
```

At the WinRT API surface, these same attributes may be obtained through the CameraProfile.Properties (see WinRT API description below).

## Blocked Controls

Blocked Controls will allow OEM/IHVs to selectively disable certain camera controls based on the selected profile:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","BlockedControls",0,"VHDR;PHSEQ;{E0766E84-36A2-4945-906D-092ECBD87445},2;WARM1"
```

In the example above, the KSCAMERAPROFILE_HighFrameRate,0 is declaring that Video HDR (VHDR), Photo Sequence (PHSEQ), a custom control whose KSPROPERTY.Set = {E0766E84-36A2-4945-906D-092ECBD87445} and KSPROPERTY.Id = 2, and Warm Start on Pin1 isn't supported.

When this profile is selected, the pipeline will explicitly block those controls from being issued to the DMFT/Camera Driver. This allows the DMFT/Camera Driver to expose support for all camera controls and the pipeline will ensure that application using the camera profile won't attempt to touch blocked controls.

Blocked Controls may be defined using one of the tags below for defined camera controls, or may use a {GUID},Id format.

| Tag | Control description |
|--|--|
| PHSEQ | Extended Camera Control - Photo Sequence<br><br>**Note**: Blocking Photo Sequence will also block Variable Photo Sequence. |
| WARM# | Extended Camera Control - Warm Start control.<br><br># represents the Pin ID on which to disable the Warm Start control. |
| SCENE | Extended Camera Control - Scene Mode. |
| TORCH | Extended Camera Control - Torch Mode. |
| FLASH | Extended Camera Control - Flash Mode. |
| ISO | Extended Camera Control - ISO |
| EVCOMP | Extended Camera Control - EV Compensation |
| WBAL | Extended Camera Control - White Balance |
| EXPOS | Extended Camera Control - Exposure |
| FOCUS | Extended Camera Control - Focus |
| ROI | Extended Camera Control - ROI |
| EXTZOOM | Extended Camera Control - Zoom |
| ADVISO | Extended Camera Control - ISO Advanced |
| VIDST | Extended Camera Control - Video Stabilization |
| FACEDT | Extended Camera Control - Face Detection |
| VHDR | Extended Camera Control - Video HDR |
| OIS | Extended Camera Control - Optical Image Stabilization |
| ADVPHOTO | Extended Camera Control - Advanced Photo |
| FACEAUTH | Extended Camera Control - Face Authentication |
| SECURE | Extended Camera Control - Secure Mode |
| VFP | Extended Camera Control - VFR |

In addition to Extended Camera Controls, profiles may also block legacy controls under the PROPSETID_VIDCAP_VIDEOPROCAMP and PROPSETID_VIDCAP_CAMERACONTROL control sets. PROPSETID_VIDCAP_VIDEOPROCAMP controls can be blocked by using the:

VIDPROC#

Where # represents the control ID:

```cpp
KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS // 0
KSPROPERTY_VIDEOPROCAMP_CONTRAST // 1
KSPROPERTY_VIDEOPROCAMP_HUE // 2
KSPROPERTY_VIDEOPROCAMP_SATURATION // 3
KSPROPERTY_VIDEOPROCAMP_SHARPNESS // 4
KSPROPERTY_VIDEOPROCAMP_GAMMA // 5
KSPROPERTY_VIDEOPROCAMP_COLORENABLE // 6
KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE // 7
KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION // 8
KSPROPERTY_VIDEOPROCAMP_GAIN // 9
KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER // 10
KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT // 11
KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT // 12
KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY // 13
```

For example: VIDPROC13 blocks the Power Line Frequency control.

Similarly, the PROPSETID_VIDCAP_CAMERACONTROL can be blocked with:

CAMCTRL#

Where # represents the control ID:

```cpp
KSPROPERTY_CAMERACONTROL_PAN // 0
KSPROPERTY_CAMERACONTROL_TILT // 1
KSPROPERTY_CAMERACONTROL_ROLL // 2
KSPROPERTY_CAMERACONTROL_ZOOM // 3
KSPROPERTY_CAMERACONTROL_EXPOSURE // 4
KSPROPERTY_CAMERACONTROL_IRIS // 5
KSPROPERTY_CAMERACONTROL_FOCUS // 6
KSPROPERTY_CAMERACONTROL_SCANMODE // 7
KSPROPERTY_CAMERACONTROL_PRIVACY // 8
KSPROPERTY_CAMERACONTROL_PANTILT // 9
KSPROPERTY_CAMERACONTROL_PAN_RELATIVE // 10
KSPROPERTY_CAMERACONTROL_TILT_RELATIVE // 11
KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE // 12
KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE // 13
KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE // 14
KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE // 15
KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE // 16
KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE // 17
KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH // 18
KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY // 19
```

## Pin Media Type Filter

Moving on to the sample profile, we see a Pin Media Type Filter for the High Frame Rate profile:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
```

In the section above, Pin0 (the Preview pin) of the High Frame Rate profile, we're allowing any resolution/frame rate available on the pin. For our hypothetical device, the driver won't expose any frame rate greater than 30 fps for the Preview pin.

Pin numbers when declared using an INF corresponds to the 0-based index ordinal of the KSPIN_DESCRIPTOR_EX structure defined in the KSFILTER_DESCRIPTOR structure that AVStream mini-port drivers advertise.

To interpret the Pin Media Type Filter and the corresponding Filter Set, we need to define the syntax schema:

This string definition uses the following Pin Media Type Filter schema. Where \[\] are shown, the included string is optional, otherwise, all string declared in the syntax is mandatory (constraint syntax is case insensitive):

```syntax
PinMediaTypeFilter     : Pin#:[(!)]|(FilterSet0)(FilterSet1)...(FilterSetN)
FilterSet              : [!](ResolutionFilter;FrameRateFilter;FourCCFilter)
Resolution             : RES[==|<=|>=|!=]Width,Height
FrameRate              : FRT[==|<=|>=|!=]Num,Denom
Subtype                : SUT[==|!=]SubtypeValue
SubtypeValue           : <See below>
```

**SubtypeValue** may take the form of either a single hexadecimal representation of the Four CC value (for example, 0x3231564E == NV12), a {GUID} in the case of a custom media type (open/close braces are required and the GUID must take the form of: {55D24460-45B7-450E-829B-91A94FF84180} or a well know tag (NV12, YUY2, and so on)).

{GUID} representation may also be used for MFVideoFormat\_\* subtypes if a known subtype doesn't have a listed tag.

For our sample:

```inf
Pin0:((RES==;FRT==;SUT==ALL))
```

Parses to:

```syntax
Resolution  : Ignore all resolution checks (implies all resolutions are allowed)
Frame rate  : Ignore all frame rate checks (implies all frame rates are allowed)
Subtype     : All
```

This is semantically: "Allow all media types".

See [Frame Rate Filter](#frame-rate-filter) below for definition of individual Resolution, Frame Rate and Subtype tags.

For Pin1 (the Capture pin), the Frame Rate declaration has a different value:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
```

Parses to:

```syntax
Resolution  : Ignore all resolution checks (implies all resolutions are allowed)
Frame rate  : Equal or greater than 60,1
Subtype     : All
```

Only media types with frame rate 60 fps or greater would be allowed under this profile for Pin1.

While for Pin2 (the Photo pin) isn't available:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
; This is our High Frame Rate Profile.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
```

As the syntax implies, a Pin Media Type Filter may optionally be a single (!) declaration, which implies for that pin, there are no supported media format (pins with no supported media types will be hidden to the client).

Moving on to the Video Recording profile, once again, we have no constraints on the Preview pin since our hypothetical camera only exposes 30 fps preview with only media types that are guaranteed to be concurrent in both Video Recording or High Frame Rate scenarios.

```inf
; Declare the Video Recording Profile here.
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

But for the Capture pin, we need to limit this to just 30 fps media types because we can't support higher frame rates for different resolutions between Preview and Capture nor Photo operations.

```inf
; Declare the Video Recording Profile here.
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

This is done using the Frame Rate Equal of Less Than tag (FRT\<=) and specifying a frame rate of 30 fps.

```inf
Pin1:((RES==;FRT<=30,1;SUT==ALL))
```

Parses to:

```syntax
Resolution    : Ignore all resolution checks (implies all resolutions are allowed)
Frame rate    : Equal or less than 30,1
Subtype       : All
```

For Photo pin, we declare no Photo Sequence support by declaring the BlockedControls with PHSEQ as the control to be disallowed.

```inf
; Declare the Video Recording Profile here.
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

## Filter Set

In the previous section, we looked at several Filter Sets and explained what some of those schema strings represent. At this point, it's necessary to describe the schema syntax of the Filter Set for further discussion.

Each Filter Set consist of a specific set of declaration for Resolution, Frame Rate and Subtype. This trio of declaration, in the order specified, is required for a valid Filter Set.

A Pin Media Type Filter may consist of multiple Filter Entries:

```syntax
PinMediaTypeFilter : Pin#:[(!)]|(FilterSet0)(FilterSet1)...(FilterSetN)
FilterSet          : [!](ResolutionFilter;FrameRateFilter;SubtypeFilter)
```

If a Filter Set doesn't meet this schema, the entire profile declaration is rejected.

All the Profile Schema strings are case insensitive.

Each Filter must be separated by a ";" and the trio of Resolution Filter, Frame Rate Filter and Subtype Filter must be bounded by an open/close parenthesis.

Another example of a Filter Set:

```inf
; Allow only 1080p@60fps for any media subtype.
Pin0:((RES==1920,1080;FRT==60,1;SUT==ALL))

; Allow either 1080p@60fps or 1080p@120fps for any subtype but nothing else.
Pin0:((RES==1920,1080;FRT==60,1;SUT==ALL))((RES==1920,1080;FRT==120,1;SUT==ALL))
```

As shown in the second example above, for multiple Filter Set on a pin, the comparison is done with a logical OR of the two Filter Set. For example, if a media type matches either of the two Filter Set, it's allowed.

**Note**: To facilitate read-ability of the declaration, Filter Set can be described in multiple lines. To do so, they must have the same Pin# to be grouped together:

```inf
; Allow only 1080p@60fps or 1080p@120fps
Pin0:((RES==1920,1080;FRT==60,1;SUT==ALL))
Pin0:((RES==1920,1080;FRT==120,1;SUT==ALL))
```

Is semantically identical to the declaration above. However, each line must have a unique MTF# entry.

```syntax
Disabled Pin
```

## Resolution Filter

As defined in the Document Terms, Resolution Filter defines how to filter based on the MF_MT_FRAME_SIZE attribute of a IMFMediaType.

The Resolution Filter syntax:

```syntax
Resolution : RES[==|<=|>=|!=]Width,Height
```

### Resolution Filter Attribute

The Resolution Filter Attribute uses the RES string. This string is case insensitive.

### Resolution Filter Comparison Operators

The following are the supported operators:

| Comparison operators | Description |
|--|--|
| == | Allows if Resolution is equal to declared resolution.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Resolution is equal to the declared resolution.<br><br>**Note**: If the declaration uses == operator and the Filter Value is empty (for example, RES==;), the MF_MT_FRAME_SIZE attribute is ignored. |
| <= | Allow if Resolution equal or less than the declared resolution.<br><br>Resolution comparison is done based on the total pixel count (product of Width *Height) and based on the aspect ratio.<br><br>If the AAR is declared in the Profile Constraint, the total pixel count is applied to all aspect ratios. Otherwise, only matching aspect ratios.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Resolution is equal or less than to the declared resolution. |
| >= | Allow if Resolution equal or greater than the declared resolution.<br><br>Resolution comparison is done based on the total pixel count (product of Width  * Height) and based on the aspect ratio.<br><br>If the AAR is declared in the Profile Constraint, the total pixel count is applied to all aspect ratios. Otherwise, only matching aspect ratios.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Resolution is equal or greater than to the declared resolution. |
| != | Allow if the Resolution is NOT equal to the declared resolution.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Resolution is NOT equal to the declared resolution. |

### Resolution Filter Value

The Width and Height of the Resolution Filter Value must be in decimal format separated by a comma (",") without any white space:

```inf
; 1080p only.
RES==1920,1080
```

The following example:

```inf
; 1080p and any lower resolution.
RES<=1920,1080
```

Will only match 16:9 resolution equal or less than 1080p if the AAR tag isn't declared in the Profile Constraint. However, if AAR is declared, it matches all resolution whose product of Width \* Height is equal or less than (1920 * 1080 = 2073600).

For example:

- If AAR isn't declared, this entry matches 720p, but not 1280x960.

- If AAR is declared, this entry matches 720p, 1280x960 and all lower resolutions.

If AAR isn't declared to ensure selective resolution matches for both aspect ratio of 16:9 and 4:3, multiple Filter Set may be used:

```inf
; This will match any 16:9 resolution of 1080p or lower
; and match any 4:3 resolution of 800x600 or lower.
; Effectively skipping 1280x960.
((RES<=1920,1080;FRT==;SUT==ALL))((RES<=800,600;FRT==;SUT==ALL))
```

To match all resolutions, specify equal or greater than 0,0

```inf
; Match all resolutions.
RES>=0,0
```

## Frame Rate Filter

As defined in the Document Terms, Frame Rate Filter defines how to filter based on the MF_MT_FRAME_RATE attribute of an IMFMediaType.

Frame Rate Filter syntax:

```syntax
FrameRate : FRT[==|<=|>=|!=]Num,Denom
```

### Frame Rate Filter Attribute

The Frame Rate Filter Attribute uses the FRT string. This string is case insensitive.

### Frame Rate Filter Comparison Operators

These are the supported Frame Rate tags:

| Comparison Operators | Description |
|--|--|
| == | Allow if the Frame Rate equals the declared Frame Rate.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Frame Rate is equal to the declared Frame Rate.<br><br>**Note**: If the declaration uses == operator and the Filter Value is empty (for example, FRT==;), the MF_MT_FRAME_RATE attribute is ignored. |
| <= | Allow if the Frame Rate is equal or less than the declared Frame Rate.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Frame Rate is equal or less than to the declared Frame Rate. |
| >= | Allow if the Frame Rate is equal or greater than the declared Frame Rate.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Frame Rate is equal or greater than to the declared Frame Rate. |
| != | Allow only if the Frame Rate is NOT equals the declared Frame Rate.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Frame Rate is NOT equal to the declared Frame Rate. |

```inf
; Allow 30fps.
FRT==30,1

; Allow 30fps or lower.
FRT<=30,1

; Allow 60fps or higher.
FRT>=60,1

; Match for all frame rate.
FRT>=0,0
```

FRT==;, and FRT\>=0,0 have subtle semantic differences.

```syntax
FRT==; : Ignore all frame rate checks for the Filter Set.

FRT>=0,0 : Match any frame rate.
```

The difference between FRT==; and FRT\>=0,0 is the former has the same meaning for both Inclusion Filter Set and Exclusion Filter Set. Whereas the meaning of FRT\>=0,0 will change depending on whether it's an Inclusion Filter Set or an Exclusion Filter Set.

See [Filter Set](#filter-set) for the explanation of the Exclusion Filter Set.

## Subtype Filter

Subtype Filter defines how to filter based on the MF_MT_SUBTYPE attribute of an IMFMediaType.

Subtype Filter syntax:

```syntax
Subtype : SUT[==|!=]SubtypeValue
SubtypeValue : <See Below>
```

### Subtype Filter Attribute

The Subtype Filter Attribute uses the SUT string. This string is case insensitive.

### Subtype Filter Comparison Operators

The following Comparison Operators are supported:

| Comparison Operators | Description |
|--|--|
| == | Allow if the Subtype equals the declared Subtype.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Subtype is equal to the declared Subtype.<br><br>**Note**: If the declaration uses == operator and the Filter Value is empty (for example, FRT==;), the MF_MT_SUBTYPE attribute is ignored. |
| != | Allow if the Subtype does NOT equal the declared Subtype.<br><br>If the Filter Set is an Exclusion Filter Set, this tag will Disallow if the Subtype is NOT equal to the declared Subtype. |

The Equal or Less Than (\<=) and Equal or Greater Than (\>=) operators aren't supported for the Subtype Filter. If declared, the profile is invalid and rejected by the pipeline.

### Subtype Filter Value

Subtype Filter Value may be the hexadecimal representation of the FourCC value, a GUID string declaration if a custom media type is used (known MFVideoFormat subtype GUID may also be used) or a Known Subtype Tag (see list below).

```inf
; Match any media type which has NV12 subtype
SUT==0x3231564E
; Same as above…
SUT=={3231564E-0000-0010-8000-00AA00389B71}
; Still the same (and the recommended declaration).
SUT==NV12

; Allow any subtype except for NV12
SUT!=0x3231564E
; Another way to say the same thing
SUT!={3231564E-0000-0010-8000-00AA00389B71}
; Yet another (and recommended).
SUT!=NV12

; Valid syntax. Profile allow/disallow should ignore
; the subtype and only check against resolution and
; frame rate.
SUT==;
```

The value of 0/GUID_NULL and ALL has a special meaning.

It means "All Four CC values".

```inf
; Match all subtypes
SUT==0
; Another way to say the same thing
SUT=={00000000-0000-0000-0000-000000000000}
; Yet another (and recommended).
SUT==ALL
```

Semantically SUT==; and SUT==0 have subtly different meanings.

When used in an Inclusion filter, they have the same effect: Allow any subtype. But when used in an Exclusion filter, SUT==0 means exclude all subtypes. However, because this has the same effect as marking the entire pin as disabled (!), there's no reason to use SUT==0 in an Exclusion filter.

### Known Subtype Tags

| Tags |
|--|
| RGB32 |
| ARGB32 |
| RGB24 |
| L8 |
| L16 |
| D16 |
| AI44 |
| AYUV |
| YUY2 |
| YVYU |
| YVU9 |
| UYVY |
| NV11 |
| NV12 |
| YV12 |
| I420 |
| IYUV |
| Y210 |
| Y216 |
| Y410 |
| Y416 |
| Y41P |
| Y41T |
| Y42T |
| P210 |
| P216 |
| P010 |
| P016 |
| V210 |
| V216 |
| V410 |
| MP43 |
| MP4S |
| M4S2 |
| MP4V |
| WMV1 |
| WMV2 |
| WMV3 |
| WVC1 |
| MSS1 |
| MSS2 |
| MPG1 |
| DVSL |
| DVSD |
| DVHD |
| DV25 |
| DV50 |
| DVH1 |
| DVC |
| H264 |
| H265 |
| MJPG |
| 420O |
| HEVC |
| HEVS |
| VP80 |
| VP90 |
| ORAW |
| H263 |
| VP10 |
| AV01 |
| JPEG |

## Exclusion Filter Set

All the examples of Filter Set so far are Inclusive Filter Entries. They're semantically "if a media type meets the criteria, allow the media type to be consumed by the client".

Missing from the discussion is the equivalent of "if a media type meets the criteria, disallow the media type from being made available to the client".

For that we need an Exclusion Filter Set.

If the Filter Set is preceded with an "!":

```inf
; Allow everything except 1080p@60fps of any subtype.
Pin0:(!(RES==1920,1080;FRT==60,1;SUT==))
```

It's an Exclusion Filter Set. An Exclusion Filter Set, if the media type matches, will be excluded from the list of available media types.

Declaring multiple Filter Set will result in the Constraint checks of each Filter Set to be logically OR-ed with each other:

```inf
; Allow everything except 1080p@60fps or 1080p@120fps
Pin0:(!(RES==1920,1080;FRT==60,1;SUT==))(!(RES==1920,1080;FRT==120,1;SUT==))
```

## Exclusion vs. Inclusion Filter Set

As shown, a Filter Set can be an Inclusion Filter Set or an Exclusion Filter Set. Mixing different Filter Set is allowed, but depending on what type of Filter Set is added, the meaning of the Pin Media Type Filter may change:

1. If only Inclusion Filter Entries are declared for a Pin Media Type Filter, any media type that doesn't match one of the Filter Entries will be excluded from the available media types.

1. If only Exclusion Filter Entries are declared for a Pin Media Type Filter, any media type that doesn't match one of the Filter Entries will be included from the available media types.

1. If both Inclusion and Exclusion Filter Entries are declared for a Pin Media Type Filter, any media type that matches an Inclusion Filter Set is included unless it also matches an Exclusion Filter Set. Exclusion Filter Set supersedes the Inclusion Filter Set.

To illustrate this example, let's assume for Pin0, we have the following media types available:

- 1920x1080@60fps, NV12

- 1920x1080@30fps, NV12

- 1280x720@60fps, NV12

- 1280x720@30fps, NV12

- 640x360@60fps, NV12

- 640x360@30fps, NV12

If we declare an Inclusion Filter Set only:

```inf
; Allow all media types 720p and lower resolution whose frame
; rate is 30fps or lower. for example, no 60fps is allowed and no
; 1080p is allowed.
Pin0:((RES<=1280,720;FRT<=30,1;SUT==ALL))
```

If we declare an Exclusion Filter Set only:

```inf
; Disallow 1080p resolutions or higher or any media types with
; 60fps or higher. Ignore Subtypes.
Pin0:(!(RES>=1920,1080;FRT>=60,1;SUT==))
```

If we declare both an Inclusion and Exclusion Filter Set:

```inf
; Allow all media types except for 640x360@60fps NV12.
Pin0:((RES<=1920,1080;FRT<=60,1;SUT==ALL))
Pin0:(!(RES==640,360;FRT==60,1;SUT==NV12))
```

**Note**: Because of rule #2 in the filter processing statement, the final example of "Allow all media types except for 640x360@60fps NV12" can be for our sample Pin0:

```inf
; Allow all media types except for 640x360@60fps NV12.
Pin0:(!(RES==640,360;FRT==60,1;SUT==NV12))
```

Since only one Exclusion Filter Set is present, all media types are allowed except for the media types that match the Exclusion Filter Set.

To illustrate the Inclusion and Exclusion Filter Entries, a few more examples:

```inf
; Allow any media type that is 30fps.
Pin0:((RES==;FRT==30,1;SUT==ALL))

; Allow any media type that is NV12.
Pin0:((RES==;FRT==;SUT==0x3132564E))

; Allow any media type, except for 4K@60fps of any subtype.
Pin0:(!(RES==3840,2160;FRT==60,1;SUT==))

; Allow any media type less than equal to 4K resolution,
; except for YUY2 subtypes.
Pin0:((RES<=3840,2160;FRT>=0,0;SUT==ALL))
Pin0:(!(RES==;FRT==;SUT==YUY2))

; Allow any media type equal or less than 4K
; and equal or less than 60fps
Pin0:((RES<=3840,2160;FRT<=60,1;SUT==ALL))

; Allow any NV12 and YUY2 media types
Pin0:((RES==;FRT>=0,0;SUT==NV12))((RES==;FRT>=0,0;SUT==YUY2))

; Allow any except for MJPG and H264
Pin0:((RES==;FRT>=0,0;SUT!=MJPG))((RES==;FRT>=0,0;SUT!=H264))

; Allow any but exclude only 4K@60fps NV12 & 3840x2880@60fps NV12
Pin0:(!(RES==3840,2160;FRT==60,1;SUT==NV12))(!(RES==3840,2880;FRT==60,1;SUT==NV12))
```

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
