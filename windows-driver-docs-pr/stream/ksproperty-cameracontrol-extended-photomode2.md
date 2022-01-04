---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE (submode)
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE property allows a submode to be configured.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/08/2020
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE (submode)

The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE property allows a submode to be configured.

## Usage summary

The following submodes are defined as follows.

```cpp
#define KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_NONE       0x00000000
#define KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_VARIABLE   0x00000001
```

KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE\_SUB\_NONE is used by a regular photo sequence.

KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE\_SUB\_VARIABLE is used to indicate a photo sequence is variable. If per-frame settings are specified, the KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE\_SUB\_VARIABLE flag will be specified in the submode field of the KSCAMERA\_EXTENDEDPROP\_PHOTOMODE structure to indicate a variable photo sequence, even if no item settings are specified (item count is 0 for all frames). When the frame count is 1 and the item count is 0, the variable photo sequence reduces to one frame variable photo sequence using global settings.

The following is a definition of the KSCAMERA\_EXTENDEDPROP\_PHOTOMODE structure defined in ksmedia.h:

```cpp
typedef struct tagKSCAMERA_EXTENDEDPROP_PHOTOMODE {  
    ULONG       RequestedHistoryFrames;  
    ULONG       MaxHistoryFrames;  
    ULONG       SubMode;  
    ULONG       Reserved;  
} KSCAMERA_EXTENDEDPROP_PHOTOMODE, *PKSCAMERA_EXTENDEDPROP_PHOTOMODE;
```

Variable photo sequence mode has the following unique characteristics on a photo sequence.

- Always use a finite photo sequence.

- Per frame settings are applied when the frame count is greater than 0.

- The driver will automatically stop the photo sequence at the end without the need for the KS\_VideoControlFlag\_StopPhotoSequenceCapture trigger when a loop count of greater than 0 is specified.

- The last sample must be marked with the KSSTREAM\_HEADER\_OPTIONSF\_ENDOFPHOTOSEQUENCE flag.

- The capture pipeline will not drop any sample from the driver.

- Neither the pipeline nor the driver\\MFT0 generates any photo thumbnail.

This property is asynchronous and not cancelable.

## Requirements

**Header:** Ksmedia.h (include Ksmedia.h)
