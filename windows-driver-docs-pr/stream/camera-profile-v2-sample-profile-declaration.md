---
title: Camera Profile V2 sample profile declaration
description: This article provides information about Camera Profile V2 sample profile declarations.
ms.date: 06/08/2023
---

# Sample profile declaration (Camera Profile V2)

We take a hypothetical camera that supports the new High Frame Rate profile. Let's define some constraints for our device.

1. Preview pin is pin 0. In the KSFILTER_DESCRIPTOR that is declared by the camera driver, when the array of KSPIN_DESCRIPTOR_EX is defined, the first KSPIN_DESCRIPTOR_EX is the Preview pin's descriptor. Similarly, pin 1 is Capture pin and pin 2 is Photo pin.

1. Due to hardware limitations, the device in question can't handle scaling at the frame rates 60 fps or greater. Therefore, both the Preview and Capture streams must have the same resolution.

1. Similarly, the device also can't handle color space conversion for 60 fps or higher.

1. Camera is capable of streaming 4K 16x9 video at 60 fps. Camera is also capable of 3840x2880@60fps (4:3 video at 60 fps).

1. Camera isn't able to provide any photo operations when running at 60 fps.

1. We'll also declare a Video Recording profile, limited to 30 fps but may allow any resolution combination/subtypes.

1. For the Video Recording profile photo sequence isn't supported (for example, single photo operations work).

For INF based declaration, every Pin Media Type Filter must be assigned a registry entry name. This name must be MTF# where # represents an integer value.

Given these constraints, we can declare the following profile:

```inf
[SampleDriver.CameraInterface.AddReg]
; Declare our schema version.
HKR,,"OEMCameraProfileVersion",0x00010001,2
;
; Declare our HighFrameRate profile with a lock resolution/subtype constraint.
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
;
; Declare our VideoRecording profile.
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

By setting the OEMCameraProfileVersion registry entry to 2, we indicate to the capture pipeline that we support the new Constraint based profile schema.

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
```

Once declared, all profiles must be stored under the Profiles registry key under the Device Interface node.

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
```

Each profile must be configured as a subkey under the Profiles key, using the Profile ID. A Profile ID consists of Profile Type, Profile Index.

Profile Type may be any one of the following well known profile types or a {GUID} string:

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

Profile Index may be any 32-bit unsigned integer except for 0xFFFFFFFF. The index value of 0xFFFFFFFF is reserved and must not be used by any IHV/OEM declaration.

The declaration of the Constraint entry at the profile subkey, indicates we have a Profile level Constraint:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
```

For the High Frame Rate profile, the `LRS;LST` indicates that resolution across all pins must be the same and the subtype must also be the same (no scaling nor color space conversion is allowed from the capture pipeline).

For the Preview pin of the High Frame Rate profile, we're allowing any resolution/frame rate available on the Preview pin. For our hypothetical device, Preview pin will never expose more than 30 fps.

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
```

For the Capture pin, we allow any resolution and any frame rate 60 fps or higher.

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
```

While Photo pin isn't available:

```inf
[SampleDriver.CameraInterface.AddReg]
HKR,,"OEMCameraProfileVersion",0x00010001,2
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","Constraint",0,"LRS;LST"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF1",0,"Pin1:((RES==;FRT>=60,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_HighFrameRate,0","MTF2",0,"Pin2:(!)"
```

In addition to the High Frame Rate profile, we also provide a standard Video Recording profile.

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

Once again, we have no constraints on the Preview pin since our hypothetical camera only exposes 30 fps preview with only media types that are guaranteed to be concurrent in both Video Recording or High Frame Rate scenarios.

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

But for the Capture pin, we need to limit this to 30 fps media types because we can't support higher frame rates for different resolutions between Preview and Capture nor Photo operations.

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

For Photo pin, we declare no Photo Sequence support by declaring the Photo Sequence control as being blocked for this profile.

```inf
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","BlockedControls",0,"PHSEQ"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF0",0,"Pin0:((RES==;FRT==;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF1",0,"Pin1:((RES==;FRT<=30,1;SUT==ALL))"
HKR,"Profiles\KSCAMERAPROFILE_VideoRecording,0","MTF2",0,"Pin2:((RES==;FRT==;SUT==ALL))"
```

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
