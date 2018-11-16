---
title: Configuration Manager Callback
description: Configuration Manager Callback
ms.assetid: a8d33bed-3a06-4d61-be42-b9ae195b79f9
keywords: ["callbacks WDK joysticks", "configuration manager callbacks WDK joysticks"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Configuration Manager Callback





```cpp
CONFIGRET CM_HANDLER CfgRoutine( CONFIGFUNC cfFuncName, 
    SUBCONFIGFUNC scfSubFuncName, DEVNODE dnToDevNode, 
    ULONG dwRefData, ULONG ulFlags );
```

General information about how to interface the configuration manager is available in the Plug and Play Environment portion of the Windows Me section of the Windows Driver Development Kit (DDK). (The DDK preceded the Windows Driver Kit \[WDK\].)

Configuration manager callback is passed to the minidrivers only if minidrivers are loaded when VJoyD receives the callback. Because of this a significant problem exists with current implementations of this callback. VJoyD receives callbacks for those device nodes with which it is associated when the device nodes are enumerated during system boot, when the configuration manager sends a message during run time for a special event like device reconfiguration, and when the system is closing down. Therefore, only the devices that are selected on the previous boot are loaded in time to receive these messages. This limits the potential number of functions that are performed when this callback is invoked because a user can boot the system, configure a joystick, play games, de-configure the joystick, and shut down without calling this callback.

For devices that do not need any hardware resources, this is not an issue. Devices that use such resources have several options: they can work only when configured at boot time, they can dynamically allocate the resources from the configuration manager, or they can search for their allocations in the registry for their device node and request the information.

Given the preceding information, driver is initialized properly either when the driver is first loaded and it receives the SYS\_DYNAMIC\_DEVICE\_INIT, or on the first time through the polling routine. Similarly, resources should be made free when a SYS\_DYNAMIC\_DEVICE\_EXIT message is received.

Another issue is that all configuration manager callbacks for currently serviced joystick devices are sent to all loaded minidrivers. However, you can use the *dnToDevNode* parameter to look up the device identifier, and you can check this against the devices that this driver can handle.

 

 




