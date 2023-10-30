---
title: Camera Profiles
description: This article discusses the format of camera profiles and various ways to define them
ms.date: 08/16/2019
---

# Camera Profiles

## KS API Profile

### KsInitializeDeviceProfile

To publish the device profiles, all miniport drivers must initialize the
profile store, to do this, the following KS API must be called:

```c
__drv_maxIRQL(PASSIVE_LEVEL)
KSDDKAPI
NTSTATUS
NTAPI
KsInitializeDeviceProfile(
    __in PKSFILTERFACTORY FilterFactory
    );
```

#### FilterFactory (KSFILTERFACTORY)

This is the KSFILTERFACTORY that was created by the camera driver to
uniquely identify the camera's filter factory.

It's required that the ReferenceGuid field of the KSFILTER\_DESCRIPTOR
structure contained with the KSFILTERFACTORY be set with a unique GUID
for this filter type. And the Flags field of the KSFILTER\_DESCRIPTOR
has the KSFILTER\_FLAG\_PRIORITIZE\_REFERENCEGUID flag set.

If the provided KSFILTERFACTORY doesn't contain a device interface
associated with the KSCATEGORY\_VIDEO\_CAMERA, this API call fails
with STATUS\_INVALID\_PARAMETER.

To delete all profiles from the profile store associated with the device
interface for this KSFILTERFACTORY, the driver may call
KsInitializeDeviceProfile followed immediately by
KsPersistDeviceProfile. This would result in an empty profile
information, which would remove the profile information from the profile
store.

### KsPublishDeviceProfile

To publish this information, the following new KS API is introduced:

```c
__drv_maxIRQL(PASSIVE_LEVEL)
KSDDKAPI
NTSTATUS
NTAPI
KsPublishDeviceProfile(
    __in PKSFILTERFACTORY FilterFactory,
    __in PKSDEVICE_PROFILE_INFO Profile
    );
```

This API is called repeatedly for each profile the camera driver
supports. Each call may have different set of concurrency and data range
information. The ProfileId field of the KSCAMERA\_PROFILE\_INFO must be
unique. If the same ProfileId is used and the content of the profile
information is different, the subsequent call overwrites the earlier
profile information.

#### FilterFactory (KSFILTERFACTORY)

This is the same FilterFactory used in the KsInitializeDeviceProfile
API.

The Camera profile information will only be associated with the
KSCATEGORY\_VIDEO\_CAMERA interface category. Any filter factory created
without this interface category and attempting to register a Camera
profile will result in this API returning a STATUS\_INVALID\_PARAMETER.

#### Profile (KSDEVICE\_PROFILE\_INFO)

The KSDEVICE\_PROFILE\_INFO is a generic structure designed to handle
profile information for various device types:

```c
##define KSDEVICE_PROFILE_TYPE_CAMERA 0x00000001

typedef struct _KSDEVICE_PROFILE_INFO
{
    UINT32 Type;
    UINT32 Size;
    union
    {
        struct
        {
            KSCAMERA_PROFILE_INFO Info;
            UINT32 Reserved;
            UINT32 ConcurrencyCount;
            PKSCAMERA_PROFILE_CONCURRENCYINFO Concurrency;
        } Camera;

        // Add other device type specific "profiles" here.
    };
} KSDEVICE_PROFILE_INFO, *PKSDEVICE_PROFILE_INFO;
```

***Type***

Defines the type of profile. Currently the only defined type is
KSDEVICE\_PROFILE\_TYPE\_Camera.

***Size***

This must be set to sizeof(KSDEVICE\_PROFILE\_INFO) structure.

***Camera.Info***

Structure of KSCAMERA\_PROFILE\_INFO defining the profile information
of a Camera.

***Camera.Reserved***

Unused. Must be set to 0.

***Camera.ConcurrencyCount***

Number of KSCAMERA\_PROFILE\_CONCURRENCYINFO structures in the
Concurrency array. For Windows Threshold this must be less than or
equal 1.
>
A value of 0 (with Camera.Concurrency set to NULL), indicates this
profile is nonconcurrent.

***Camera.Concurrency***

Array of KSCAMERA\_PROFILE\_CONCURRENCYINFO structures describing the
concurrency support for this profile. If Camera.CountOfConcurrency is
0, this parameter must be NULL. If Camera.CountOfConcurrency is \>0,
this parameter must not be NULL.

#### KSCAMERA_PROFILE_INFO

The KSCAMERA\_PROFILE\_INFO structure is used to uniquely identify a
given profile:

```c
typedef struct _KSCAMERA_PROFILE_INFO
{
    UINT32 ProfileId;
    UINT32 Index;
    UINT32 PinCount;
    PKSCAMERA_PROFILE_PININFO Pins
} KSCAMERA_PROFILE_INFO, *PKSCAMERA_PROFILE_INFO;
```

***ProfileId***

GUID representing a unique ID for the Profile. This GUID may be a
unique IHV/OEM created GUID representing a custom profile or it may be
one of the predefined GUIDs described in section 3.1.

NOTE: This field must NOT be set to KSCAMERAPROFILE\_Legacy. The
Legacy profile must not be published by the camera driver. The Legacy
profile ID is sent to the camera driver during Capture
Engine/Media Capture initialization if the application hasn't
indicated that it can support profiles. In such cases, the camera
driver must revert its behavior to the Windows 8.1 mode of operation
and expose only the Reduced Set Media Types along with the
corresponding
KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_EXCLUSIVE\_WITH\_RECORD
and
KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_SEQUENCE\_EXCLUSIVE\_WITH\_RECORD
capability bits indicating whether the camera driver is capable of
supporting simultaneous recording/photo and/or recording/photo
sequence within the Reduced Set Media Type.

***Index***

Each profile within a given ProfileId group must have a unique Index
value. This allows any profile for a device to be uniquely identified
with ProfileId + Index.

***PinCount***

The number of KSCAMERA\_PROFILE\_PININFO structures pointed to by
Pins. This value must be \>0.

***Pins***

Array of KSCAMERA\_PROFILE\_PININFO structures defining the supported
media types on each of the pins of this profile.

This field must not be NULL.

#### Concurrency (KSCAMERA\_PROFILE\_CONCURRENCYINFO)

Currently, an application has no knowledge as to whether it can attempt
to stream from more than one camera until the attempt succeeds or fails.
In the case of Web Blogging scenario, this means the application has to attempt to activate both streams before it paints the UI with a
picture in picture video element.

The Concurrency parameter provides a hint to the application that
both front and back cameras can be activated at the same time using a
specific profile (or set of profiles). With this knowledge, the
application can draw the UI elements for both streams before activating
them.

For multiple applications, Concurrency won't be sufficient to
guarantee concurrent operation. The Concurrency information won't
attempt to solve this scenario. Instead, the existing Camera Yanking
feature of Windows 8 will be leveraged.

The Concurrency parameter represents an array of
KSCAMERA\_PROFILE\_CONCURRENCYINFO structure (whose array size is
specified by Camera.CountOfConcurrency parameter) indicating which
profiles the profile identified in the KSCAMERA\_PROFILE\_INFO structure
may run simultaneously on different cameras.

If both Camera.CountOfConcurrency and the Camera.Concurrency fields are
0 & NULL respectively, it indicates to the OS that the profile defined
by the KSCAMERA\_PROFILE\_INFO isn't a concurrent profile.

```c
typedef struct _KSCAMERA_PROFILE_CONCURRENCYINFO
{
    GUID ReferenceGuid;
    UINT32 Reserved;
    UINT32 ProfileCount;
    PKSCAMERA_PROFILE_INFO Profiles;
} KSCAMERA_PROFILE_CONCURRENCYINFO,*PKSCAMERA_PROFILE_CONCURRENCYINFO;
```

***ReferenceGuid***

Must be set to the ReferenceGuid of the KSFILTER\_DESCRIPTOR which
corresponds to the other device with which this profile is concurrent.

***Reserved***

Unused. Must be 0.

***ProfileCount***

Number of profile IDs contained in the Profiles array. Must be greater
than 0.

***Profiles***

This is an array of the KSCAMERA\_PROFILE\_INFO that can be
simultaneously used on the other camera device specified by the
ReferenceGuid.

This field must not be NULL.

#### Pins (KSCAMERA\_PROFILE\_PININFO)

To specify the available list of media types for each of the pins, an
array of KSCAMERA\_PROFILE\_PININFO must be specified, the array size of
which, is specified by the CountOfPins parameter.

```c
typedef struct _KSCAMERA_PROFILE_PININFO
{
    GUID PinCategory;
    UINT32 Reserved;
    UINT32 MediaInfoCount;
    PKSCAMERA_PROFILE_MEDIAINFO MediaInfos;
} KSCAMERA_PROFILE_PININFO, *PKSCAMERA_PROFILE_PININFO;
```

***PinCategory***

This is the PINNAME category corresponding to Capture, Preview or
Still image pin. For Windows Threshold, the only supported pin
categories are: PINNAME\_VIDEO\_CAPTURE, PINNAME\_VIDEO\_PREVIEW,
PINNAME\_VIDEO\_STILL. All other categories result in an
STATUS\_INVALID\_PARAMETER error.

***Reserved***

Unused. Must be 0.

***MediaInfoCount***

Array size of KSCAMERA\_PROFILE\_MEDIAINFO structures specified in the
MediaInfos field.

***MediaInfo***

Array of KSCAMERA\_PROFILE\_MEDIAINFO structures.

#### MediaInfos (KSCAMERA\_PROFILE\_MEDIAINFO)

The relevant media type information presented for each profile is
described by:

```c
##define KSCAMERAPROFILE_FLAGS_VIDEOHDR              0x0000000000000002
##define KSCAMERAPROFILE_FLAGS_VARIABLEPHOTOSEQUENCE 0x0000000000000010

typedef struct _KSCAMERA_PROFILE_MEDIAINFO
{
    struct
    {
        UINT32 X;
        UINT32 Y;
    } Resolution;
    struct
    {
        UINT32 Numerator;
        UINT32 Denominator;
    } MaxFrameRate;
    ULONGLONG Flags;
    UINT32 Data0;
    UINT32 Data1;
    UINT32 Data2;
    UINT32 Data3;
} KSCAMERA_PROFILE_MEDIAINFO, *PKSCAMERA_PROFILE_MEDIAINFO;
```

***Resolution***

The X (horizontal) and Y (vertical) frame size in pixels.

***MaxFrameRate***

The num/denom ratio of frame rate (for example, 30 / 1 = 30 fps). This frame
rate represents the maximum frame rate of the specified resolution
under ideal lighting conditions. Actual frame rate may be lower than
this value.

For photo media information, if photo sequence can't be enabled
because of hardware constraints for the given photo resolution, the
frame rate must be set to 0 (num=0,denom=0). This informs the
application layer that photo sequence control will be rejected by the
driver when that particular photo media type is selected.

***Flags***

May be bitwise OR of one or more of the following flags:

- **KSCAMERAPROFILE\_FLAGS\_VIDEOHDR**
  When the video HDR flag is set for the media info, for that media
  setting, video HDR may be enabled for the record stream.

  This flag may not be set for media info on the photo pin.
- **KSCAMERAPROFILE\_FLAGS\_VARIABLEPHOTOSEQUENCE**
  When the Variable Photo Sequence flag is set for the media info, VPS
  support is available even if the photo media info doesn't provide a
  frame rate.

  If this flag is set & frame rate is nonzero, for that photo media
  info, VPS and Photo Sequence is available.

  If this flag is set & frame rate is zero, for that photo media info,
  VPS is available but not Photo Sequence.

  If this flag isn't set & frame rate is nonzero, for that photo media
  info, VPS isn't available but Photo Sequence is available.

  If this flag isn't set & frame rate is zero, neither VPS nor Photo
  Sequence is available for that media info.

  This flag may only be set for media info on the photo pin. Presence of
  this flag on nonphoto pin media info results in the profile set
  being rejected.

***Data0…3***

Value determined based on Flags. Unused at this time, must be set to 0.

### KsPersistDeviceProfile

To commit the profile information to the persistent store, the following
KS API must be invoked.

```c
__drv_maxIRQL(PASSIVE_LEVEL)
KSDDKAPI
NTSTATUS
NTAPI
KsPersistDeviceProfile(
    __in PKSFILTERFACTORY FilterFactory
    );
```

#### FilterFactory (KSFILTERFACTORY)

This is the KSFILTERFACTORY that was used to initialize the profile
store in KsInitializeDeviceProfile. If KsPersistDeviceProfile is called
without first initializing the profile store with
KsInitializeDeviceProfile the call to KsPersistDeviceProfile fails
with STATUS\_INVALID\_DEVICE\_REQUEST.

Furthermore, this API may also fail with STATUS\_INSUFFICIENT\_RESOURCE
if the page pool is exhausted when profile information is being
persisted.

### KSPROPERTY_CAMERACONTROL_EXTENDED_PROFILE

> ***Scope: Version 1***
>
> ***Control: Filter***
>
> ***Type: Asynchronous, Not Cancellable***

A new Extended Property Control is introduced to allow the capture
framework to inform the camera driver which profile was selected.

#### KSCAMERA_EXTENDEDPROP_HEADER

**Version**

Defined for Extended Property Control version 1.

**PinId**

Must be `KSCAMERA_EXTENDEDPROP_FILTERSCOPE` (0xFFFFFFFF).

**Size**

Must be `sizeof(KSCAMERA_EXTENDEDPROP_HEADER) +
sizeof(KSCAMERA_EXTENDEDPROP_PROFILE)`.

**Result**

Indicates the error results of the last SET operation. If no SET
operation has taken place, this must be 0. 0 indicates no errors were
detected.

**Capability**

Must be `KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL`. No other modes are
supported.

**Flags**

Must be 0.

#### KSCAMERA_EXTENDEDPROP_PROFILE

The payload of the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROFILE control
contains the KSCAMERA\_EXTENDEDPROP\_HEADER +
KSCAMERA\_EXTENDEDPROP\_PROFILE.

```c
typedef struct _KSCAMERA_EXTENDEDPROP_PROFILE
{
    GUID ProfileId;
    UINT32 Index;
    UINT32 Reserved;
} KSCAMERA_EXTENDEDPROP_PROFILE, *PKSCAMERA_EXTENDEDPROP_PROFILE;
```

**ProfileId**

GUID representing the selected profile. If this is
KSCAMERAPROFILE\_Legacy, no profile was selected, the camera driver
must expose the Reduced Set Media Type.

If this field is GUID\_NULL, no profile was selected, but the
application is profile aware so the camera driver must expose the full
range of media types.

**Index**

Index value associated with the identified profile.

**Reserved**

Unused. Must be 0.

## INF Profile

To allow OEMs the flexibility, based on different SKUs that may use the
same reference driver but different sensors (or even in the case of
different performance levels), the profiles can be published or
overridden by using the following INF sections:

Each profile, new or existing, must have their \[ProfildId GUID, Index\]
value in a semi-colon delimited string stored under the Device Interface
Node:

```reg
OEMCameraProfiles: REG_SZ:
KSCAMERAPROFILE_VideoRecording,0;KSCAMERAPROFILE_HighQualityPhoto,0;KSCAMERAPROFILE_BalancedVideoPhoto,0;KSCAMERAPROFILE_VideoConferencing,0;{3074C75C-1D69-4A0A-895D-EB9EFDE1CF30},0
```

In the example above, we're overriding the 0<sup>th</sup> indexed,
KSCAMERAPROFILE\_VideoRecording, KSCAMERAPROFILE\_HighQualityPhoto,
KSCAMERAPROFILE\_BalancedVideoPhoto and
KSCAMERAPROFILE\_VideoConferencing along with a new custom profile with
the ID of {3074C75C-1D69-4A0A-895D-EB9EFDE1CF30}

For each profile GUID in the OEMCameraProfiles, a new subkey must be
created in the Device Interface Node matching the name specified in the
delimited string.

Under this subkey, OEM may indicate the profile has been disabled (thus
overriding the setting published by the driver) by adding the following
value:

```reg
Disabled: REG_DWORD: 0x1
```

If the OEM, instead wishes to change or publish the available media
types instead of simply disabling the profile, another subkey matching
the PinCategory of the stream must be created.

For example, to publish the Preview pin of the 0<sup>th</sup> indexed,
KSCAMERAPROFILE\_VideoRecording:

```reg
<Device Interface Node>KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW

MediaCount: REG_DWORD: N
Media0: REG_SZ: <MediaInfo Format>
...
MediaN-1: REG_SZ: <MediaInfo Format>
```

MediaCount registry value indicates the number of MediaInfo present for
this pin. Each MediaInfo must be given a registry entry name of
"Media\#" where \ represents a 0 based index of N count (for example,
Media0, Media1, Media2 ...,MediaN-1).

The MediaInfo specified by Media0 will be treated as the Preferred Media
Type for the profile.

The MediaInfo Format above takes the following syntax:

```reg
MediaInfo Format = <ResolutionX>, <ResolutionY>, <MaxFrameRateNum>,<MaxFrameRateDenom>, Flags, Data0, Data1, Data2, Data3
```

So the following:

```reg
<Device Interface Node>KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW

MediaCount: REG_DWORD: 2
Media0: REG_SZ: 1280,720,30,1,0,0,0,0,0
Media1: REG_SZ: 640,360,30,1,0,0,0,0,0

<Device Interface
Node>KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_CAPTURE

MediaCount: REG_DWORD: 3
Media0: REG_SZ: 1280,720,30,1,0,0,0,0,0
Media1: REG_SZ: 1920,1080,30,1,0,0,0,0,0
Media2: REG_SZ: 640,360,30,1,0,0,0,0,0
```

Will publish the VideoRecording profile from the IHV's setting to only
allow 1080p, 720p, 360p recording (with the 720p made the Preferred
Media Type) while allowing only 720p and 360p previews without any photo
support.

To define a custom profile, the same syntax may be used, but with the
profile name being replaced with the custom profile's GUID ID:

```reg
<Device Interface
Node>{3074C75C-1D69-4A0A-895D-EB9EFDE1CF30},0\PINNAME_VIDEO_PREVIEW

MediaCount: REG_DWORD: 2
Media0: REG_SZ: 1280,720,30,1,0,0,0,0,0
Media1: REG_SZ: 640,360,30,1,0,0,0,0,0

<Device Interface
Node>{3074C75C-1D69-4A0A-895D-EB9EFDE1CF30},0\PINNAME_VIDEO_CAPTURE
MediaCount: REG_DWORD: 2
Media0: REG_SZ: 1280,720,30,1,0,0,0,0,0
Media2: REG_SZ: 640,360,30,1,0,0,0,0,0

<Device Interface
Node>{3074C75C-1D69-4A0A-895D-EB9EFDE1CF30},0\PINNAME_IMAGE
MediaCount: REG_DWORD: 2
Media0: REG_SZ: 1920,1080,0,0,0,0,0,0,0
Media1: REG_SZ: 1280,720,0,0,0,0,0,0,0
```

The modification to the registry can be handled in any manner suitable
for the OEM. The recommended process is to create an AddReg section to
the camera driver's INF file so that the registry entries can be created
during camera installation (and removed when the driver is removed):

```INF
[SampleDriver.DeviceInterface.AddReg]
HKR,,"OEMCameraProfiles",0,"KSCAMERAPROFILE_VideoRecording,0",
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW","MediaCount",0x00010001,2,
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW","Media0",0,"1280,720,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW","Media1",0,"640,360,30,1,0,0,0,0,0",
```

…

### INF Profile : Concurrency

To publish the Concurrency setting of a profile, the following registry
value may be added:

```reg
<Device Interface Node>KSCAMERAPROFILE_VideoConferencing,0

Concurrency: REG_SZ:
{ConcurrentDeviceReferenceGUID};{ProfileID},{Index};…
```

The ConcurrentDeviceRefefenceGUID is the ReferenceGUID of the
KSFILTER\_DESCRIPTOR that is associated with the camera that this
profile may run concurrently.

### Example INF

```INF
;---------------------------------------------------------------
; S t r i n g s
;---------------------------------------------------------------

[Strings]
; non-localizable
RefGUIDFrontCamera="{C3FDE193-01D1-4A78-AA0F-0D2395611C3D}"
RefGUIDRearCamera="{3E5169E8-8DB8-4951-A33F-CFF94F2C87BE}"

;---------------------------------------------------------------
; A d d R e g
;---------------------------------------------------------------

[SampleDriver.FrontCameraInterface.AddReg]
HKR,,"OEMCameraProfiles",0,"KSCAMERAPROFILE_VideoRecording;KSCAMERAPROFILE_VideoConferencing;KSCAMERAPROFILE_HighQualityPhoto;KSCAMERAPROFILE_PhotoSequence",
HKR,,"ReferenceGUID",0,%RefGUIDFrontCamera%
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW","MediaCount",0x00010001,2,
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW","Media0",0,"1280,720,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_PREVIEW","Media1",0,"640,360,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_CAPTURE","MediaCount",0x00010001,2,
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_CAPTURE","Media0",0,"1280,720,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoRecording,0\PINNAME_VIDEO_CAPTURE","Media1",0,"640,360,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_PhotoSequence,0","Disabled",0x00010001,1,
HKR,"KSCAMERAPROFILE_HighQualityPhoto,0\PINNAME_VIDEO_PREVIEW","Media0",0,"1280,720,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_HighQualityPhoto,0\PINNAME_VIDEO_PREVIEW","Media1",0,"640,360,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_HighQualityPhoto,0\PINNAME_IMAGE","MediaCount",0x00010001,2,
HKR,"KSCAMERAPROFILE_HighQualityPhoto,0\PINNAME_IMAGE","Media0",0,"1920,1080,0,0,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_HighQualityPhoto,0\PINNAME_IMAGE","Media1",0,"1280,720,5,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoConferencing,0\PINNAME_VIDEO_PREVIEW","MediaCount",0x00010001,2,
HKR,"KSCAMERAPROFILE_VideoConferencing,0\PINNAME_VIDEO_PREVIEW","Media0",0,"1280,720,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoConferencing,0\PINNAME_VIDEO_PREVIEW","Media1",0,"640,360,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoConferencing,0\PINNAME_VIDEO_CAPTURE","MediaCount",0x00010001,2,
HKR,"KSCAMERAPROFILE_VideoConferencing,0\PINNAME_VIDEO_CAPTURE","Media0",0,"1280,720,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoConferencing,0\PINNAME_VIDEO_CAPTURE","Media1",0,"640,360,30,1,0,0,0,0,0",
HKR,"KSCAMERAPROFILE_VideoConferencing,0","Concurrency",0,"%RefGUIDRearCamera%;KSCAMERAPROFILE_VideoConferencing,0",
```

The sample section of an INF above shows how and OEM may publish (or
override the default IHV) settings for profiles. In the sample above,
the 0th indexed VideoRecording for the front camera is
limited to only 720p30 for both preview and record with no photo
support.

The PhotoSequence for the front camera is also disabled (overriding the
IHV's published profile).

HighQualityPhoto profile is limited to 720p preview with 1080p single
shot or 720p photo at 5 fps.

The VideoConferencing profile is limited to just 720p30 for both preview
and capture while indicating that it can be concurrently run with the
rear camera's VideoConferencing profile (the rear camera's
VideoConferencing profile isn't shown in the INF—if not specified in
the INF, the rear camera's VideoConferencing profile uses whatever
the IHV published or if it's not present, profiles are disabled
since the above override is invalid).

## INF vs. KS API Profile

The INF profile information will always supersede the profile
information published by the KS API. The precedence is at the per
profile level.

If a driver publishes VideoRecording, HighQualityPhoto,
VideoConferencing profile using the KS API and the INF settings contain
the profile entries for HighQualityPhoto, only the HighQualityPhoto
profile published by the driver will be overwritten with the profile
information from the INF.

This is done with the expectation that a single reference driver
(implemented by the IHV) may publish a set of profiles available for a
given sensor, but the OEM may decide to select a different sensor and/or
because of the final form factor, may choose to change/limit the
available profiles.

The INF Profile also allows OEMs to, without changing the driver binary,
to publish profiles for existing Windows 8.1 drivers simply by updating
their INF.
