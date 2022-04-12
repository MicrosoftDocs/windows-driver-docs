---
title: Properties and related system-defined items
description: Learn more about properties and related system-defined items.
ms.date: 04/12/2022
---

# Properties and related system-defined items

In Windows Vista and later versions of Windows, the unified device property model manages the correspondence between the following system-defined items that pertain to the installation and management of devices:

- The [system-defined properties](system-defined-device-properties2.md) and their corresponding [property keys](property-keys.md), [property data types](property-data-type-identifiers.md), and property values.

- The SPDRP_*Xxx* device instance property identifiers and the SPCRP_*Xxx* device setup class property identifiers that are defined in *Setupapi.h.* The CM_DRP_*Xxx* device instance property identifiers and the CM_CRP_*Xxx*[device setup class](./overview-of-device-setup-classes.md) identifiers that are defined in *Cfgmgr32.h*.

- The REGSTR_VAL_*Xxx* registry entry value identifiers that pertain to device installation and management. These identifiers are defined in *Regstr.h*.

- Registry entry values that correspond to device properties.

- INF file entry values that modify device properties.

For information about the correspondence between the system-defined items that are associated with the device properties, see the following topics:

[Device instance properties](/previous-versions/ff541334(v=vs.85))

[Device setup class properties](accessing-device-setup-class-properties.md)

[Device interface class properties](accessing-device-interface-class-properties.md)

[Device interface properties](accessing-device-interface-properties.md)
