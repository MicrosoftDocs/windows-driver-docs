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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CCD Example Code


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following pseudocode shows how to use the CCD APIs to set clone view:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CCD%20Example%20Code%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




