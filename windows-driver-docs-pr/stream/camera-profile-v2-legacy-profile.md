---
title: Camera Profile V2 legacy profile
description: This article provides information about the Camera Profile V2 legacy profile.
ms.date: 06/08/2023
---

# Legacy Profile - KSCAMERAPROFILE_Legacy (Camera Profile V2)

In Camera Profile 1507, there was no formal way for camera drivers, either through KS APIs or INF to publish a legacy camera profile (a profile designed for legacy applications that didn't use profiles). Instead, it was done purely at runtime by having either the camera driver or the MFT0 filter the available media types when a legacy client initializes the camera.

This has two main drawbacks:

1. It required the camera to be initialized, which results in the camera driver being loaded and in the case of the MFT0, the full capture pipeline created.

1. Because it was only done during initialization time, there was always an added complexity for the driver stack to handle the two states (legacy mode vs. nonlegacy mode). It also added the overhead of dynamically filtering out nonlegacy media types in the case of legacy operation.

To address this, KSCAMERAPROFILE_Legacy must be defined in Camera Profile V2. The definition schema for KSCAMERAPROFILE_Legacy is identical to other camera profiles with one exception: The Camera Profile ID's Index field must always be set to 0.

For cameras that support Camera Profile V2, it's mandatory to publish the KSCAMERAPROFILE_Legacy.

## Legacy Interop

Camera Profiles defined for legacy profile schema (Camera Profile 1507) will be translated by the pipeline to the Camera Profile V2 schema.

Because the Camera Profile 1507 was limited to media information that only contains the resolution and frame rate, all Camera Profile 1507 is translated with SUT==; tag (for example, ignore all subtypes).

Furthermore, in Camera Profile 1507, there were specific media information entries that can define support for either Video HDR or Variable Photo Sequence. This information is no longer available through the Camera Profile V2. Instead, rather than explicitly enabling controls, for Camera Profile V2, controls are disabled based on specific profiles.

To advertise specific subset of media types that can be used for Video HDR or Variable Photo Sequence, IHV/OEMs may publish the VideoHDR8 or VariablePhotoSequence profiles with those set of media types.

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
