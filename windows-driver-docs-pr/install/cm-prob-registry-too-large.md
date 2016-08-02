---
title: CM\_PROB\_REGISTRY\_TOO\_LARGE
description: CM\_PROB\_REGISTRY\_TOO\_LARGE
ms.assetid: 8870ea57-4ae4-48a0-9d56-c5d0da8e1525
keywords: ["CM_PROB_REGISTRY_TOO_LARGE"]
---

# CM\_PROB\_REGISTRY\_TOO\_LARGE


## <a href="" id="ddk-cm-prob-registry-too-large-dg"></a>


The registry is too large.

### Error Code

49

### Display Message (Windows XP and later versions of Windows)

"Windows cannot start new hardware devices because the system hive is too large (exceeds the Registry Size Limit). (Code 49)"

### Recommended Resolution (Windows XP and later versions of Windows)

Set the environment variable DEVMGR\_SHOW\_NONPRESENT\_DEVICES to 1. This causes Device Manager to display installed devices that are currently not present. Use Device Manager to remove these devices. If the registry is still too large, reinstall Windows.

 

 





