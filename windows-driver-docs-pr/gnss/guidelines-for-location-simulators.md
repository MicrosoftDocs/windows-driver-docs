---
title: Guidance for location simulators
author: windows-driver-content
description: Microsoft Visual Studio 2012 provides a location simulator that works together with a location simulator driver that you create. This section contains guidance for implementing a location simulator driver.
ms.assetid: 4AA6C3EE-0150-45A8-ACC2-D0267591D33D
---

# Guidance for location simulators


Microsoft Visual Studio 2012 provides a [location simulator](http://msdn.microsoft.com/library/windows/apps/hh441475.aspx#bkmk-set-the-simulated-geo-location-of-the-device) that works together with a location simulator driver that you create. This section contains guidance for implementing a location simulator driver.

## Configure the simulator


To enable a simulator driver, edit the registry key `HKLM\Software\Microsoft\Location` by setting the String value named “SimulatorID” to the Sensor ID of your simulator driver.

## Clear data on simulator exit


When the simulator application exits, the simulator driver should change state to NO\_DATA and send a state changed event.

## How simulator data is used


-   Data from the simulator driver is only used in the emulator session for the location simulator. Simulator data is never used in normal applications.
-   If the simulator driver does not have data when it is running in a simulator, then data from other sources will be used in the location simulator.

## Related topics
[Running Windows Store apps in the simulator](http://msdn.microsoft.com/library/windows/apps/hh441475.aspx)  
[Set the simulated geolocation of the device](http://msdn.microsoft.com/library/windows/apps/hh441475.aspx#bkmk-set-the-simulated-geo-location-of-the-device)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Guidance%20for%20location%20simulators%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


