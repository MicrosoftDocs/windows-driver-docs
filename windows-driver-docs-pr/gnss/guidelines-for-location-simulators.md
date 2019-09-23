---
title: Guidance for location simulators
description: This section contains guidance for implementing a location simulator driver.
ms.assetid: 4AA6C3EE-0150-45A8-ACC2-D0267591D33D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guidance for location simulators


Microsoft Visual Studio 2012 provides a [location simulator](https://docs.microsoft.com/visualstudio/debugger/run-windows-store-apps-in-the-simulator?view=vs-2015#bkmk-set-the-simulated-geo-location-of-the-device) that works together with a location simulator driver that you create. This section contains guidance for implementing a location simulator driver. Note that starting with Visual Studio 2017, location simulator functionality is no longer present, so simulating a sensor driver is not supported.

## Configure the simulator


To enable a simulator driver, edit the registry key `HKLM\Software\Microsoft\Location` by setting the String value named “SimulatorID” to the Sensor ID of your simulator driver.

## Clear data on simulator exit


When the simulator application exits, the simulator driver should change state to NO\_DATA and send a state changed event.

## How simulator data is used


-   Data from the simulator driver is only used in the emulator session for the location simulator. Simulator data is never used in normal applications.
-   If the simulator driver does not have data when it is running in a simulator, then data from other sources will be used in the location simulator.

## Related topics
[Running UWP apps in the simulator](https://docs.microsoft.com/visualstudio/debugger/run-windows-store-apps-in-the-simulator?view=vs-2015)  
[Set the simulated geolocation of the device](https://docs.microsoft.com/visualstudio/debugger/run-windows-store-apps-in-the-simulator?view=vs-2015#bkmk-set-the-simulated-geo-location-of-the-device)  



