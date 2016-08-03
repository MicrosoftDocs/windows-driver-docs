---
title: Configuration Manager Callback
author: windows-driver-content
description: Configuration Manager Callback
MS-HAID:
- 'di\_afbac7ff-cb48-45c9-9859-80d6d9e72e9c.xml'
- 'hid.configuration\_manager\_callback'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a8d33bed-3a06-4d61-be42-b9ae195b79f9
keywords: ["callbacks WDK joysticks", "configuration manager callbacks WDK joysticks"]
---

# Configuration Manager Callback


## <a href="" id="ddk-configuration-manager-callback-di"></a>


```
CONFIGRET CM_HANDLER CfgRoutine( CONFIGFUNC cfFuncName, 
    SUBCONFIGFUNC scfSubFuncName, DEVNODE dnToDevNode, 
    ULONG dwRefData, ULONG ulFlags );
```

General information about how to interface the configuration manager is available in the Plug and Play Environment portion of the Windows Me section of the Windows Driver Development Kit (DDK). (The DDK preceded the Windows Driver Kit \[WDK\].)

Configuration manager callback is passed to the minidrivers only if minidrivers are loaded when VJoyD receives the callback. Because of this a significant problem exists with current implementations of this callback. VJoyD receives callbacks for those device nodes with which it is associated when the device nodes are enumerated during system boot, when the configuration manager sends a message during run time for a special event like device reconfiguration, and when the system is closing down. Therefore, only the devices that are selected on the previous boot are loaded in time to receive these messages. This limits the potential number of functions that are performed when this callback is invoked because a user can boot the system, configure a joystick, play games, de-configure the joystick, and shut down without calling this callback.

For devices that do not need any hardware resources, this is not an issue. Devices that use such resources have several options: they can work only when configured at boot time, they can dynamically allocate the resources from the configuration manager, or they can search for their allocations in the registry for their device node and request the information.

Given the preceding information, driver is initialized properly either when the driver is first loaded and it receives the SYS\_DYNAMIC\_DEVICE\_INIT, or on the first time through the polling routine. Similarly, resources should be made free when a SYS\_DYNAMIC\_DEVICE\_EXIT message is received.

Another issue is that all configuration manager callbacks for currently serviced joystick devices are sent to all loaded minidrivers. However, you can use the *dnToDevNode* parameter to look up the device identifier, and you can check this against the devices that this driver can handle.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Configuration%20Manager%20Callback%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


