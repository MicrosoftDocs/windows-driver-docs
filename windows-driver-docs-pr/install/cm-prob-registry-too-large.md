---
title: CM_PROB_REGISTRY_TOO_LARGE
description: CM_PROB_REGISTRY_TOO_LARGE
keywords:
- CM_PROB_REGISTRY_TOO_LARGE
ms.date: 04/20/2017
---

# Code 49 - CM_PROB_REGISTRY_TOO_LARGE

This Device Manager error message indicates that the registry is too large.

## Error Code

49

### Display Message

"Windows cannot start new hardware devices because the system hive is too large (exceeds the Registry Size Limit). (Code 49)"

### Recommended Resolution

Set the environment variable DEVMGR_SHOW_NONPRESENT_DEVICES to 1. This causes Device Manager to display installed devices that are currently not present. Use Device Manager to remove these devices. If the registry is still too large, reinstall Windows.
