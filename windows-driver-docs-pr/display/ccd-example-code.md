---
title: CCD Example Code
description: CCD Example Code
ms.assetid: 8ca2c7c4-8e6f-4e4f-9234-eb3e5dc164cc
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, example code
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, example code
- configuring displays WDK Windows 7 display , CCD APIs, example code
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, example code
- CCD APIs WDK Windows 7 display , example code
- CCD APIs WDK Windows Server 2008 R2 display , example code
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CCD Example Code


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following pseudocode shows how to use the CCD APIs to set clone view:

```cpp
SetCloneView
{
    // Determine the size of the path array that is required to hold all valid paths.
  Call GetDisplayConfigBufferSizes(QDC_ALL_PATHS) to retrieve the sizes of
  the DISPLAYCONFIG_PATH_INFO and DISPLAYCONFIG_MODE_INFO buffers that are required.

    // Allocate memory for path and mode information arrays.
    Allocate PathArraySize*sizeof(DISPLAYCONFIG_PATH_INFO) for the path information array
    Allocate ModeArraySize*sizeof(DISPLAYCONFIG_MODE_INFO) for the mode information array.

    // Request all of the path information.
  Call QueryDisplayConfig(QDC_ALL_PATHS) to obtain the path and mode information for all posible paths.

    // Find and store the primary path.
    Search the DISPLAYCONFIG_PATH_INFO array for an active path that is located at desktop position (0, 0).

    // Determine the user friendly name of the current primary.
  Call DisplayConfigGetDeviceInfo() by using the
    DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME type and the adapter ID and target ID
  from the DISPLAYCONFIG_PATH_TARGET_INFO of the primary path.

    // DisplayConfigGetDeviceInfo can determine the user friendly names 
    // for all of the paths that might be part of the clone. 
    // Allow the user to pick which monitor the clone is enabled on.
    // Only provide the user options of the paths from the current primary 
    // to targets with monitors that are connected or that are forceable.  
    Store a pointer to the DISPLAYCONFIG_PATH_INFO that the user picked.

    // Mark the new path as active.
    Set the DISPLAYCONFIG_PATH_ACTIVE in the DISPLAYCONFIG_PATH_INFO.flags of the new clone path.
  NewClonePath->flags |= DISPLAYCONFIG_PATH_ACTIVE;
  NewClonePath->sourceInfo.modeInfoIdx = DISPLAYCONFIG_PATH_MODE_IDX_INVALID;
  NewClonePath->targetInfo.modeInfoIdx = DISPLAYCONFIG_PATH_MODE_IDX_INVALID;

    // Set the new topology.
  Call SetDisplayConfig
    (SDC_APPLY | SDC_SAVE_TO_DATABASE | SDC_ALLOW_CHANGES | SDC_USE_SUPPLIED_DISPLAY_CONFIG)
  to change to the clone topology.
}
```

 

 





