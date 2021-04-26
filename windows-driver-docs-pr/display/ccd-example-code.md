---
title: CCD example pseudocode
description: Example pseudocode for using CCD APIs to set clone view
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

# CCD example pseudocode

This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following pseudocode shows how to use the Connecting and Configuring Displays (CCD) APIs to set clone view:

```cpp
SetCloneView
{
    // Determine the size of the path and mode information arrays needed
    // to hold all valid paths by calling GetDisplayConfigBufferSizes
    // with flags=QDC_ALL_PATHS

    // Using the returned numPathArrayElements and numModeInfoArrayElements,
    // allocate memory for the path and mode information arrays as follows:
    // pathArray size is numPathArrayElements*sizeof(DISPLAYCONFIG_PATH_INFO)
    // modeInfoArray size is numModeInfoArrayElements*sizeof(DISPLAYCONFIG_MODE_INFO)

    // Obtain the path and mode information for all possible paths by
    // calling QueryDisplayConfig with flags=QDC_ALL_PATHS and pointers
    // to the allocated path and mode info arrays.

    // Find the primary path by searching the returned array of
    // DISPLAYCONFIG_PATH_INFO structs for an active path that is
    // located at desktop position (0, 0).

    // Determine the user friendly name of the current primary by
    // calling DisplayConfigGetDeviceInfo with a type of
    // DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME, and the
    // adapter ID and target ID from the DISPLAYCONFIG_PATH_TARGET_INFO
    // of the primary path.

    // DisplayConfigGetDeviceInfo can determine the user friendly names
    // for all of the paths that might be part of the clone.
    // Allow the user to pick which monitor the clone is enabled on.
    // Only provide the user options of the paths from the current primary
    // to targets with monitors that are connected or that are forceable.  
    // Store a newClonePath pointer to the DISPLAYCONFIG_PATH_INFO that
    // the user picked.

    // Mark the new clone path as active:
    // NewClonePath->flags |= DISPLAYCONFIG_PATH_ACTIVE;
    // NewClonePath->sourceInfo.modeInfoIdx = DISPLAYCONFIG_PATH_MODE_IDX_INVALID;
    // NewClonePath->targetInfo.modeInfoIdx = DISPLAYCONFIG_PATH_MODE_IDX_INVALID;

    // Set the new topology by calling SetDisplayConfig with flags =
    // (SDC_APPLY | SDC_SAVE_TO_DATABASE | SDC_ALLOW_CHANGES
    //  | SDC_USE_SUPPLIED_DISPLAY_CONFIG) to change to the clone topology.
}
```
