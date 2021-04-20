---
title: Device Relation Tokens in SDEL
description: A table describing tokens that are available for expressing device relations within SDEL
keywords:
- tokens
- device relation
ms.date: 09/03/2020
ms.localizationpriority: medium
---

# Device Relation Tokens in SDEL

The following table describes tokens that are available for expressing device relations within SDEL. All of these relations have versions with an "-or-self" suffix. These "-or-self" versions return the current device and all of the specified related devices.

|Relation token|Possible results|Description|
|----|----|----|
|above|0 to many|Provides a mapping to all devices above in some way. Currently, this relation is logically equivalent to "disk-or-self/ancestor/ OR ancestor-or-self/disk/".|
|ancestor|0 to many|Extends the parent relation to include all of the parents up to and including the RootDevice.|
|below|0 to many|Provides a mapping to all devices below in some way. Currently, this relation is logically equivalent to "descendant/volume-or-self/ OR volume/descendant-or-self/".|
|child|0 to many|Provides the dependency relationship that is commonly found between devices and their bus or hub. This relationship is also known as bus-relation. Note that phantom devices cannot have children.|
|descendant|0 to many|Extends the child relation to include all children of all children, to the end of the hierarchy.|
|disk|0 to many|Provides a mapping from a volume device to the disks that implement those volumes. Note that a volume can span many disks.|
|parent|0 or 1|Describes the supremacy relationship that is commonly found between devices and their bus or hub. Every device has one parent, except the logical device that is located within the IWDTFDeviceDepot2::RootDevice property.|
|power|0 or 1|All devices with a power relationship to this device. (CM_GETIDLIST_FILTER_POWERRELATIONS)|
|removal|0 to many|Describes the removal-relation that is described in the Configuration Manager APIs (CM API) in the Microsoft Windows SDK documentation in MSDN. Devices that this relationship specifies will be removed whenever the current device is removed. Only a few devices have this kind of relationship.|
|system|1|Maps any target device object to the target system object that contains the device. Every device maps to exactly one system target.|
|volume|0 to many|Provides a mapping from a disk device to the volumes that the disk exposes. A disk can be partitioned into many volumes.|
