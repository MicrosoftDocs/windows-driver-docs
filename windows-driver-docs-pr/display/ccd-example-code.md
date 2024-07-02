---
title: CCD Example Code
description: Example code for using CCD APIs to set clone view
keywords:
- connecting displays WDK , CCD APIs, example code
- connecting displays Windows , CCD APIs, example code
- configuring displays WDK , CCD APIs, example code
- configuring displays Windows , CCD APIs, example code
- CCD APIs WDK Windows display , example code
ms.date: 07/02/2024
---

# CCD example code

The following sample code shows how to use the Connecting and Configuring Displays (CCD) APIs to set clone view. In a clone view, two or more displays show the same content simultaneously, essentially mirroring the output from one display to another.

This code can be extended for more complex scenarios, such as setting one monitor as the primary display and setting two other monitors that aren't the primary to clone each other.

``` Cplusplus
#include <iostream>
#include <windows.h>
#include <stdio.h>
#include <vector>

INT64 Int64FromLuid(LUID value)
{
    LARGE_INTEGER largeInt;
    largeInt.HighPart = value.HighPart;
    largeInt.LowPart = value.LowPart;
    return largeInt.QuadPart;
}

std::wstring GetMonitorFriendlyName(LUID adapterId, UINT32 targetId)
{
    DISPLAYCONFIG_TARGET_DEVICE_NAME targetName = {};
    targetName.header.type = DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME;
    targetName.header.size = sizeof(DISPLAYCONFIG_TARGET_DEVICE_NAME);
    targetName.header.adapterId = adapterId;
    targetName.header.id = targetId;

    LONG status = DisplayConfigGetDeviceInfo(&targetName.header);

    if (status != ERROR_SUCCESS)
    {
        printf("DisplayConfigGetDeviceInfo failed, error: %ld\n", status);
        return L"";
    }

    return targetName.monitorFriendlyDeviceName;
}

int SetupPathsInClone()
{
    UINT32 numPathArrayElements = 0;
    UINT32 numModeInfoArrayElements = 0;
    std::vector<DISPLAYCONFIG_PATH_INFO> pathArray;
    std::vector<DISPLAYCONFIG_MODE_INFO> modeInfoArray;
    LONG status;

    // Determine the size of the path and mode information arrays to hold all valid paths
    status = GetDisplayConfigBufferSizes(QDC_ONLY_ACTIVE_PATHS | QDC_VIRTUAL_MODE_AWARE, &numPathArrayElements, &numModeInfoArrayElements);

    if (status != ERROR_SUCCESS)
    {
        printf("GetDisplayConfigBufferSizes failed, error: %ld\n", status);
        return 1;
    }

    // Allocate memory for the path and mode information arrays

    pathArray.resize(numPathArrayElements);
    modeInfoArray.resize(numModeInfoArrayElements);

    // Obtain the path and mode information for all possible paths
    status = QueryDisplayConfig(QDC_ONLY_ACTIVE_PATHS | QDC_VIRTUAL_MODE_AWARE, &numPathArrayElements, pathArray.data(), &numModeInfoArrayElements, modeInfoArray.data(), nullptr);

    if (status != ERROR_SUCCESS)
    {
        printf("QueryDisplayConfig failed, error: %ld\n", status);
        return 1;
    }

    // Find the primary path by searching for an active path that is located at desktop position (0, 0)
    DISPLAYCONFIG_PATH_INFO* primaryPath = nullptr;
    for (UINT32 i = 0; i < numPathArrayElements; ++i)
    {
        if (pathArray[i].flags & DISPLAYCONFIG_PATH_ACTIVE)
        {
            DISPLAYCONFIG_SOURCE_MODE& sourceMode = modeInfoArray[pathArray[i].sourceInfo.sourceModeInfoIdx].sourceMode;

            if (sourceMode.position.x == 0 && sourceMode.position.y == 0)
            {
                primaryPath = &pathArray[i];
                break;
            }
        }
    }

    if (!primaryPath)
    {
        printf("Primary path not found\n");
        return 1;
    }

    // Determine the user-friendly name of the primary monitor
    std::wstring primaryMonitorName = GetMonitorFriendlyName(primaryPath->sourceInfo.adapterId, primaryPath->targetInfo.id);
    printf("Primary monitor: %ws\n", primaryMonitorName.c_str());

    // TODO: Pick which monitors to clone
    // For this sample, we pick the first active monitor other than the primary
    DISPLAYCONFIG_PATH_INFO* newClonePath = nullptr;
    for (UINT32 i = 0; i < numPathArrayElements; ++i)
    {
        if (&pathArray[i] != primaryPath && (pathArray[i].flags & DISPLAYCONFIG_PATH_ACTIVE))
        {
            newClonePath = &pathArray[i];
            break;
        }
    }

    if (!newClonePath)
    {
        printf("No suitable path found for cloning\n");
        return 1;
    }

    // Determine the user-friendly name of the clone monitor
    std::wstring newCloneMonitorName = GetMonitorFriendlyName(newClonePath->sourceInfo.adapterId, newClonePath->targetInfo.id);
    printf("Will clone with monitor: %ws\n", newCloneMonitorName.c_str());

    // If the paths don't have the same support for virtual topology, we can't clone them together
    if ((primaryPath->flags & DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE) != (newClonePath->flags & DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE))
    {
        printf("Primary and clone paths do not have the same support for virtual topology\n");
        return 1;
    }

    // How to apply clone depends on whether the paths support virtual modes
    if (primaryPath->flags & DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE)
    {
        // In virtual clone, there are two possible options to setup clone depending on
        // whether we want to specify the resolution for the cloned paths

        bool shouldCloneWithoutSpecifyingMode = false;

        if (shouldCloneWithoutSpecifyingMode)
        {
            // Pick an arbitrary clone group ID to use to associate the paths
            // (anything that isn't DISPLAYCONFIG_PATH_CLONE_GROUP_INVALID).
            // QueryDisplayConfig will not return existing clone group IDs since it returns
            // the paths with their full source modes, so we can just use a constant value.
            const UINT cloneGroupId = 1;

            primaryPath->sourceInfo.sourceModeInfoIdx = DISPLAYCONFIG_PATH_SOURCE_MODE_IDX_INVALID;
            primaryPath->targetInfo.desktopModeInfoIdx = DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID;
            primaryPath->targetInfo.targetModeInfoIdx = DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID;
            primaryPath->sourceInfo.cloneGroupId = cloneGroupId;

            newClonePath->sourceInfo.sourceModeInfoIdx = DISPLAYCONFIG_PATH_SOURCE_MODE_IDX_INVALID;
            newClonePath->targetInfo.desktopModeInfoIdx = DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID;
            newClonePath->targetInfo.targetModeInfoIdx = DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID;
            newClonePath->sourceInfo.cloneGroupId = cloneGroupId;
        }
        else
        {
            // Alternatively, we can use the same source mode for all the cloned paths if we want to specifically control
            // the resolution (in this case we are just copying the source mode info from the primary path to the newly
            // selected path which takes the resolution, position, and pixel format). They are implicitly cloned because
            // they share the same position.

            DISPLAYCONFIG_SOURCE_MODE& primaryPathSourceMode = modeInfoArray[primaryPath->sourceInfo.sourceModeInfoIdx].sourceMode;

            DISPLAYCONFIG_SOURCE_MODE& newPathSourceMode = modeInfoArray[newClonePath->sourceInfo.sourceModeInfoIdx].sourceMode;
            newPathSourceMode = primaryPathSourceMode;

            // We should also clear the desktop mode info since we are adjusting the source mode on the newly cloned path and
            // it may need to be recalculated
            newClonePath->targetInfo.desktopModeInfoIdx = DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID;
        }
    }
    else
    {
        // Since the paths don't support virtual clone, we need to check if they are on the same adapter to support hardware clone
        if (Int64FromLuid(primaryPath->sourceInfo.adapterId) != Int64FromLuid(newClonePath->sourceInfo.adapterId))
        {
            printf("Primary and clone paths are not on the same adapter\n");
            return 1;
        }

        // For hardware clone, we simply assign the same source ID to both paths and clear all the
        // mode information from the second path since the hardware may not support the same mode
        newClonePath->sourceInfo.id = primaryPath->sourceInfo.id;

        primaryPath->targetInfo.targetModeInfoIdx = DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID;
        primaryPath->targetInfo.desktopModeInfoIdx = DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID;
        
        newClonePath->sourceInfo.sourceModeInfoIdx = DISPLAYCONFIG_PATH_SOURCE_MODE_IDX_INVALID;
        newClonePath->targetInfo.targetModeInfoIdx = DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID;
        newClonePath->targetInfo.desktopModeInfoIdx = DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID;
    }

    // Apply the topology changes temporarily. If we want to persist the changes we should also set SDC_SAVE_TO_DATABASE.
    status = SetDisplayConfig(numPathArrayElements, pathArray.data(), numModeInfoArrayElements, modeInfoArray.data(),
        SDC_APPLY | SDC_USE_SUPPLIED_DISPLAY_CONFIG | SDC_ALLOW_CHANGES | SDC_VIRTUAL_MODE_AWARE);

    if (status != ERROR_SUCCESS)
    {
        printf("SetDisplayConfig failed, error: %ld\n", status);
        return 1;
    }

    return 0;
}
```
