---
title: Handling Placeholders
description: Describes how to implement placeholders and how to handle placeholders
keywords:
- filter drivers file system , implementing placeholders
- filter drivers file system, handling placeholders
ms.date: 02/22/2023
prerelease: false
---

# Handling placeholders

## Guidance for minifilters that implement placeholders

All virtualization implementations that use [placeholders](placeholders.md) must set the FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS file attribute on these placeholders. This attribute indicates that:

* Reading such files from below the owning minifilter might return 0s, and
* Reading such files from above the owning minifilter entails the extra cost of furnishing the data.

A minifilter can remove this attribute from the placeholder once the entire data is available locally.  

All minifilters that implement placeholders must be in the [HSM Load Order Group](load-order-groups-and-altitudes-for-minifilter-drivers.md).

## Guidance for all minifilters

Filters must not issue targeted reads/writes from filter instances below the HSM Load Order Group for files that have the attribute FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS set. This situation could lead to file data corruption. A minifilter developer could try to circumvent this situation by issuing an IO request to the top of the stack, but such a request could lead to deadlocks.

Filters should also not issue reads and writes on placeholder files that have the FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS attribute set from above the HSM Load Order Group. Such a read or write causes unnecessary hydration when no user application has requested the file data.  

A minifilter shouldn't issue reads/writes on intercepting attribute-only opens. Such read/writes can cause deadlocks as certain implementations don’t expect attribute-only opens to be converted to data access operations. Further, such read/writes defeat the purpose of a minifilter checking for FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS so it can avoid the two aforementioned situations.

Thus, it's recommended that all minifilters shouldn't issue reads/writes on files that have FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS set.
