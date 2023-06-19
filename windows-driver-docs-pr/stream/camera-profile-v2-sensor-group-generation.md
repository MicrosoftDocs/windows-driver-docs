---
title: Camera Profile V2 sensor group generation
description: This article provides information about Camera Profile V2 sensor group generation.
ms.date: 06/08/2023
---

# Sensor group generation (Camera Profile V2)

In RS1, sensor group generation was based on either the existence of Concurrent Profiles, or by the declaration of FSSensorGroupId field in the device interface node. If the FSSensorGroupId matched and the devices all had the same Container ID, a Sensor Group was created.

## Concurrency Profiles

Concurrency Profile, in Camera Profile 1507 required each device to explicitly list the supported concurrent media information of every other device that can stream concurrently. This requirement resulted in a significant amount of redundant information.

To simplify the declaration of Concurrent Profiles, if the OEMCameraProfileVersion is set and the version is 2 or greater, the Frame Server uses the Profile ID to determine concurrency. The FSSensorGroupId generates a Sensor Group and based on the profiles defined by those devices, if the Profile ID matches, they're considered Concurrent Profiles.

For example, we have two devices (Device 1 and Device 2), which support the following Profiles:

| Device | Profiles supported |
|--|--|
| Device 1 | VideoRecording,0<br><br>VideoRecording,1<br><br>VideoRecording,2<br><br>HighQualityPhoto,0<br><br>HighQualityPhoto,1<br><br>HighQualityPhoto,2 |
| Device 2 | VideoRecording,1<br><br>VideoRecording,2<br><br>VideoRecording,3<br><br>VideoRecording,4<br><br>HighQualityPhoto,2<br><br>HighQualityPhoto,3<br><br>HighQualityPhoto,4 |

And both Device 1 and Device 2 declare the FSSensorGroupId under their Device Interface and have the same Container ID. The Frame Server creates a Sensor Group for these two devices.

The Frame Server also publishes concurrency between the two devices for any profiles with matching Profile IDs:

- VideoRecording,1

- VideoRecording,2

- HighQualityPhoto,2

Since \[VideoRecording,1\], \[VideoRecording,2\] and \[HighQualityPhoto,2\] Profile IDs are common between the two devices, Frame Server publishes Concurrent Profiles for those profiles.

This allows individual cameras to declare their profiles along with their concurrent profiles only under their Device Interface nodes.

Concurrent Profiles for Camera Profile V2 are generated as profiles published by Sensor Groups. Application developers can treat Camera Profile V2 in a uniform manner regardless of whether the profile belongs to a single physical device, or a collection of devices virtualized through a Sensor Group.

## Sensor Group Profiles

Because a Sensor Group is a virtual construct, there's no specific profile available for a Sensor Group. Instead, a virtual set of profiles is published by the Frame Server along with the Sensor Group information.

For our sample Device 1 and Device 2, the resulting Sensor Group's Profile set would be:

- VideoRecording,0

- VideoRecording,1

- VideoRecording,2

- VideoRecording,3

- VideoRecording,4

- HighQualityPhoto,0

- HighQualityPhoto,2

- HighQualityPhoto,3

- HighQualityPhoto,4

The highlighted profiles, because they're Concurrent Profiles, are synthesized by Frame Server.

For example:

Device 1's VideoRecording,1 and VideoRecording,2 are declared as:

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF0",0,"Pin0:((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF1",0,"Pin0:((RES<=1280,720;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF2",0,"Pin1:((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF3",0,"Pin1:((RES<=1280,720;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF4",0,"Pin2:((RES<=3840,2880;FRT<=8,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF5",0,"Pin2:((RES<=3840,2160;FRT<=8,1;SUT==ALL))"
```

And Device 2, a world-facing camera, with a larger sensor, declares these profiles:

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF0",0,"Pin0:((RES<=1920,1440;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF1",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF2",0,"Pin1:((RES<=1920,1440;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF3",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF4",0,"Pin2:((RES<=5120,3840;FRT<=8,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF5",0,"Pin2:((RES<=5120,2880;FRT<=8,1;SUT==ALL))"
```

For the Sensor Group that is generated, assume Device 1 is added first, the VideoRecording,1 and VideoRecording,2 profile is:

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF3",0,"Pin3:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF4",0,"Pin4:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,1","MTF5",0,"Pin5:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF0",0,"Pin0:((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF1",0,"Pin0:((RES<=1280,720;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF2",0,"Pin1:((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF3",0,"Pin1:((RES<=1280,720;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF4",0,"Pin2:((RES<=3840,2880;FRT<=8,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF5",0,"Pin2:((RES<=3840,2160;FRT<=8,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF6",0,"Pin3:((RES<=1920,1440;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF7",0,"Pin3:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF8",0,"Pin4:((RES<=1920,1440;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF9",0,"Pin4:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF10",0,"Pin5:((RES<=5120,3840;FRT<=8,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2","MTF11",0,"Pin5:((RES<=5120,2880;FRT<=8,1;SUT==ALL))"
```

As can be seen, just as Sensor Group translates the pin indices to reflect the virtual device, the same pin index translation takes place for the profile declaration.

**Note**: The Profile Constraint for Concurrent profiles MUST be the same. In the above example, neither profile has any Profile Constraints, so they can be merged. Had one of the profiles declared a Profile Constraint or declared a different Profile Constraint, the profile syntax would be invalid and rejected.

## Sample Profile Declaration (Sensor Group Generation)

To illustrate the new declarative profile schema, we can produce a sample camera profile via INF entries for two hypothetical cameras.

Let's assume that we have two cameras, one User Facing (Camera UF) and one World Facing (Camera WF). Let's also assume that the Camera WF has a larger sensor capable of higher resolution and frame rates.

The set of available media types from the two cameras may look something like this:

| Camera | Available Media Type |
|--|--|
| WF: Preview | 3840x2160@30fps<br><br>2560x1920@30fps<br><br>1920x1080@30fp<br><br>1280x960@30fps<br><br>1280x720@30fps<br><br>800x600@30fps<br><br>640x480@30fps<br><br>640x360@30fps<br><br> |
| WF: Capture | 3840x2160@60fps<br><br>3840x2160@30fps<br><br>2560x1920@60fps<br><br>2560x1920@30fps<br><br>1920x1080@120fp<br><br>1920x1080@60fp<br><br>1920x1080@30fp<br><br>1280x960@120fps<br><br>1280x960@60fps<br><br>1280x960@30fps<br><br>1280x720@120fps<br><br>1280x720@60fps<br><br>1280x720@30fps<br><br>800x600@120fps<br><br>800x600@60fps<br><br>800x600@30fps<br><br>640x480@120fps<br><br>640x480@60fps<br><br>640x480@30fps<br><br>640x360@120fps<br><br>640x360@60fps<br><br>640x360@30fps<br><br> |
| WF: Photo | 5120x3840 (no Photo Sequence)<br><br>3840x2160<br><br>2560x1920<br><br>1920x1080<br><br>1280x960<br><br>280x720<br><br> |
| UF: Preview | 1920x1080@30fp<br><br>1280x960@30fps<br><br>1280x720@30fps<br><br>800x600@30fps<br><br>640x480@30fps<br><br>640x360@30fps<br><br> |
| UF: Capture | 1920x1080@120fp<br><br>1920x1080@60fp<br><br>1920x1080@30fp<br><br>1280x960@120fps<br><br>1280x960@60fps<br><br>1280x960@30fps<br><br>1280x720@120fps<br><br>1280x720@60fps<br><br>1280x720@30fps<br><br>800x600@120fps<br><br>800x600@60fps<br><br>800x600@30fps<br><br>640x480@120fps<br><br>640x480@60fps<br><br>640x480@30fps<br><br>640x360@120fps<br><br>640x360@60fps<br><br>640x360@30fps<br><br> |
| UF: Photo | 3840x2160 (no Photo Sequence)<br><br>2560x1920 (no Photo Sequence)<br><br>1920x1080<br><br>1280x960<br><br>1280x720<br><br> |

Let's also add some hypothetical hardware constraints:

1. Preview pin is pin 0. In the KSFILTER_DESCRIPTOR, when the array of KSPIN_DESCRIPTOR_EX is defined, the first KSPIN_DESCRIPTOR_EX is the Preview pin's descriptor. Similarly, pin 1 is Capture pin and pin 2 is Photo pin.

1. Using High Frame Rate capture on the WF camera blocks use of UF camera (any media type whose frame rate is greater than 30 fps is considered High Frame Rate).

1. Use of 4K capture (3840x2160) or higher resolution on the WF camera limits the UF facing camera to 720p.

1. Preview and Capture must be using the same resolution if any High Frame Rate capture is used.

1. All profiles must have the same aspect ratio across preview, record, photo operations.

1. Both cameras are capable of simultaneous Capture and Photo as long as the High Frame Rate capture isn't used and 4K or higher video recording isn't active.

1. Only video recording operations are possible for both cameras when both are active and the resolution is limited to 1080p and frame rate must be 30 fps or lower.

Translating the above constraints into sample profiles, we have the following declaration:

```inf
; Camera WF
[SampleDriver.WorldFacingCameraInterface.AddReg]
HKR,,"FSSensorGroupId",0,"{E770B3DB-F6C9-4303-B767-97F17A6BD123}"
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF1",0,"Pin1:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF2",0,"Pin2:((RES<=3840,2160;FRT==;SUT==ALL))((RES<=2560,1920;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF2",0,"Pin2:(!)"

; Camera UF
[SampleDriver.UserFacingCameraInterface.AddReg]
HKR,,"FSSensorGroupId",0,"{E770B3DB-F6C9-4303-B767-97F17A6BD123}"
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF2",0,"Pin2:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF1",0,"Pin1:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF2",0,"Pin2:((RES<=1920,1080;FRT==;SUT==ALL))((RES<=1280,960;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF2",0,"Pin2:(!)"
```

When these profiles are processed during Sensor Group generation (FSSensorGroupId is declared for the above INF directive), the resulting Sensor Group's "INF" would look something like the following declaration (assuming Camera WF is added to the Sensor Group first).

However, there's no INF generated. This is merely a sample to illustrate how the Sensor Group publishing process synthesizes the profiles across multiple devices.

```inf
; Sensor Group WF & UF
[SampleDriver.SensorGroupInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF0",0,"Pin3:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF1",0,"Pin4:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF2",0,"Pin5:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF1",0,"Pin1:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF2",0,"Pin2:((RES<=3840,2160;FRT==;SUT==ALL))((RES<=2560,1920;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF0",0,"Pin3:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF1",0,"Pin4:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF2",0,"Pin5:((RES<=1920,1080;FRT==;SUT==ALL))((RES<=1280,960;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF0",0,"Pin3:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF1",0,"Pin4:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF2",0,"Pin5:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF2",0,"Pin2:(!)"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF3",0,"Pin3:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF4",0,"Pin4:((RES<=1920,1080;FRT<=30,1;SUT==ALL)) ((RES<=1280,960;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF6",0,"Pin5:(!)"
```

### AAR Profile Constraint

One of the possible shortcuts to declare profiles is to set the AAR Profile Constraint. If the underlying hardware's constraint is purely a bandwidth limitation, the above Profile declaration may be reduced to:

```inf
; Camera WF
[SampleDriver.WorldFacingCameraInterface.AddReg]
HKR,,"FSSensorGroupId",0,"{E770B3DB-F6C9-4303-B767-97F17A6BD123}"
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","Constraint",0,"AAR"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF1",0,"Pin1:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,0","MTF2",0,"Pin2:((RES<=3840,2160;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","Constraint",0,"AAR"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF2",0,"Pin2:(!)"

; Camera UF
[SampleDriver.UserFacingCameraInterface.AddReg]
HKR,,"FSSensorGroupId",0,"{E770B3DB-F6C9-4303-B767-97F17A6BD123}"
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF1",0,"Pin0:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,1000","MTF2",0,"Pin2:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","Constraint",0,"AAR"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF1",0,"Pin1:(!)"
HKR,"Profiles\KSCAMERAPROFILE_PhotoSequence,1000","MTF2",0,"Pin2:((RES<=1920,1080;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","Constraint",0,"AAR"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,1000","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF1",0,"Pin1:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,2000","MTF2",0,"Pin2:(!)"
```

This applies the AAR Profile Constraint so all the resolution based matching logic applies to all aspect ratio.

So instead of:

```inf
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))((RES<=1280,960;FRT<=30,1;SUT==ALL))"
```

To match both 16:9 and 4:3 resolutions of 1080p or lower and 1280x960 or lower, the declaration becomes:

```inf
HKR,"Profiles\KSCAMERAPROFILE_HighQualityPhoto,0","MTF0",0,"Pin0:((RES<=1920,1080;FRT<=30,1;SUT==ALL))"
```

Which applies the matching logic to all resolution whose total pixel count is less than 1920 * 1080.

This shortcut is only valid if the HW constraints are based only on pixel bandwidth.

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
