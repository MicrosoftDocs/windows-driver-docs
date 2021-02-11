---
title: Guidance for location simulators
description: This section contains guidance for implementing a location simulator driver.
ms.date: 11/17/2020
ms.localizationpriority: medium
---

# Guidance for location simulators

Microsoft Visual Studio 2013 provides a [location simulator](/visualstudio/debugger/run-windows-store-apps-in-the-simulator?view=vs-2015&preserve-view=true) that works together with a location simulator driver that you create. This section contains guidance for implementing a location simulator driver.

> [!IMPORTANT]
> The Visual Studio 2015 simulator does not include the geolocation button. This is because the Windows 10 simulator does not include geolocation simulation. If you need to do this kind of simulation, you can use the Visual Studio 2013 simulator on Windows 8.1 or earlier operating systems.

## Configure the simulator

To enable a simulator driver, edit the registry key `HKLM\Software\Microsoft\Location` by setting the String value named "SimulatorID" to the Sensor ID of your simulator driver.

## Clear data on simulator exit

When the simulator application exits, the simulator driver should change state to NO\_DATA and send a state changed event.

## How simulator data is used

- Data from the simulator driver is only used in the emulator session for the location simulator. Simulator data is never used in normal applications.

- If the simulator driver does not have data when it is running in a simulator, then data from other sources will be used in the location simulator.

## Related topics

[Running UWP apps in the simulator](/visualstudio/debugger/run-windows-store-apps-in-the-simulator?view=vs-2015&preserve-view=true)
