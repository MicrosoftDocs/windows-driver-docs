---
title: Universal camera driver controls for Windows 10
description: Provides information about universal camera driver controls for Windows 10.
ms.date: 03/23/2021
---

# Universal camera driver controls for Windows 10

The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The following topics provide information about universal camera driver controls for Windows 10:

| Title | Description |
|--|--|
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ADVANCEDPHOTO](ksproperty-cameracontrol-extended-advancedphoto.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_ADVANCEDPHOTO is an extended property control that is used to control photo HDR, flash no flash, and ultra low light fusion on the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FACEDETECTION](ksproperty-cameracontrol-extended-facedetection.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_FACEDETECTION is an extended property control that is used to turn on and off face detection. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE](ksproperty-cameracontrol-extended-flashmode2.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE is an extended property control that is used to support assistant flash. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY](ksproperty-cameracontrol-extended-focuspriority.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY is an extended property control that is used to configure the focus priority. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSSTATE](ksproperty-cameracontrol-extended-focusstate.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSSTATE is an extended property control that is used to get the focus state from the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM](ksproperty-cameracontrol-extended-histogram.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM is an extended property control that is used to control the histogram metadata produced by the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ISO_ADVANCED](ksproperty-cameracontrol-extended-iso-advanced.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_ISO_ADVANCED is an extended property control that allows more global ISO control with more granularity. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_METADATA](ksproperty-cameracontrol-extended-metadata.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_METADATA is an extended property control that is used by the client to query the driver for the metadata buffer requirements. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_OIS](ksproperty-cameracontrol-extended-ois.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_OIS is an extended property control that is used to control optical image stabilization (OIS) on the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT](ksproperty-cameracontrol-extended-optimizationhint-.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT is an extended property control that is used to inform the driver to set its performance strategy based on what operation is likely used the most. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION](ksproperty-cameracontrol-extended-photoconfirmation.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION is an extended property control that is used to set and get the photo confirmation settings in the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE](ksproperty-cameracontrol-extended-photomode2.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE is an extended property control that allows a submode to be configured. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_PROFILE](ksproperty-cameracontrol-extended-profile.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_PROFILE is an extended property control that is used to allow the capture framework to inform the camera driver which profile was selected. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_CONFIGCAPS](ksproperty-cameracontrol-extended-roi-configcaps.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_CONFIGCAPS is an extended property control that is used to query ROI capabilities. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL](ksproperty-cameracontrol-extended-roi-ispcontrol.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL is an extended property control that is used to get or configure the ROI settings and apply the desired processing. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE](ksproperty-cameracontrol-extended-scenemode2.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE is an extended property control that is used to select a driver defined mode which represents a collection of preset controls. The driver determines the presets assigned to a scene mode and enables those control settings when a scene is selected. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_VFR](ksproperty-cameracontrol-extended-vfr.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_VFR is an extended property control that is used to specify whether variable frame rate is desired on the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR](ksproperty-cameracontrol-extended-videohdr.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR is an extended property control that is used to enable or disable high dynamic range (HDR) video on the driver. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOSTABILIZATION](ksproperty-cameracontrol-extended-videostabilization.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOSTABILIZATION is an extended property control that is used to control digital video stabilization in driver\MFT0. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_ZOOM](ksproperty-cameracontrol-extended-zoom.md) | KSPROPERTY_CAMERACONTROL_EXTENDED_ZOOM is an extended property control that is used to get and set the zoom ratio and get zoom ranges from the driver. In Windows 10, this control is extended to also support smooth zoom. |
| [KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY](ksproperty-cameracontrol-perframesetting-capability.md) | KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY is a property control that is used to get the per-frame capabilities from the driver. |
| [KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR](ksproperty-cameracontrol-perframesetting-clear.md) | KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR is a property control that is used to clear the per-frame settings in the driver.  |
| [KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_SET](ksproperty-cameracontrol-perframesetting-set.md) | KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_SET is a property control that is used to set per-frame settings in the driver. |

## See also

[Universal camera driver design guide for Windows 10](windows-10-technical-preview-camera-drivers-design-guide.md)

[Universal camera driver enumerations for Windows 10](camera-driver-enumerations.md)

[Universal camera driver functions for Windows 10](camera-driver-functions.md)

[Universal camera driver structures for Windows 10](camera-driver-structures.md)

[Streaming media device driver reference](/windows-hardware/drivers/ddi/_stream/index)
