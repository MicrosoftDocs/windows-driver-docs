---
title: Universal camera driver enumerations for Windows 10
description: Provides information about universal camera driver enumerations for Windows 10.
ms.date: 03/23/2021
---

# Universal camera driver enumerations for Windows 10

The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The following topics provide information about universal camera driver enumerations for Windows 10:

| Title | Description |
|--|--|
| [KSCAMERA_EXTENDEDPROP_FOCUSSTATE](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_extendedprop_focusstate) | This enumeration contains the focus states. |
| [KSCAMERA_EXTENDEDPROP_MetadataAlignment](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_extendedprop_metadataalignment) | This enumeration contains identifiers for the metadata alignment. |
| [KSCAMERA_EXTENDEDPROP_ROITYPE](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_extendedprop_roitype) | This enumeration contains the ROI types. |
| [KSCAMERA_MetadataId](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_metadataid) | This enumeration contains identifiers for a metadata item. |
| [KSCAMERA_PERFRAMESETTING_ITEM_TYPE](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_perframesetting_item_type) | This enumeration contains the different item types for the per-frame settings DDI. |
| [KSDEVICE_THERMAL_STATE](/windows-hardware/drivers/ddi/ks/ne-ks-ksdevice_thermal_state) | A KS-defined enumeration for thermal state changes. |
| [KSEVENT_CAMERAEVENT](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksevent_cameraevent) | KSEVENT_CAMERAEVENT enumerates a kernel streaming event set that can be used by the pipeline to enable or disable camera event notifications from the driver. |
| [KSPIN_MDL_CACHING_EVENT](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_mdl_caching_event) | This enumeration is used internally by the operating system. |
| [KSPPROPERTY_ALLOCATOR_MDLCACHING](/windows-hardware/drivers/ddi/ks/ne-ks-kspproperty_allocator_mdlcaching) | This enumeration is used internally by the operating system. |
| [KSPROPERTY_CAMERACONTROL_EXTENDED_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property) | This enumeration contains extended camera controls. |
| [KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_perframesetting_property) | This enumeration contains the property IDs defined for the per-frame property set. |

## See also

[Universal camera driver design guide for Windows 10](windows-10-technical-preview-camera-drivers-design-guide.md)

[Universal camera driver controls for Windows 10](camera-driver-controls.md)

[Universal camera driver functions for Windows 10](camera-driver-functions.md)

[Universal camera driver structures for Windows 10](camera-driver-structures.md)

[Streaming media device driver reference](/windows-hardware/drivers/ddi/_stream/index)
