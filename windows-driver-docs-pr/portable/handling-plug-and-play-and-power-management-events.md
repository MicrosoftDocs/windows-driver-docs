---
Description: Handling Plug and Play and Power Management Events
title: Handling Plug and Play and Power Management Events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Plug and Play and Power Management Events


When a Plug and Play (PnP) or Power Management (PM) event occurs, the user-mode driver framework (UMDF) calls one or more methods in the CDevice class to handle the event. (The CDevice class is defined in the file *Device.cpp*.) The event handlers are found in three interfaces: **IPnpCallback**, **IPnpCallbackHardware**, and **IPnpCallbackSelfManagedIo**.

In the WpdHelloWorldDriver sample, most of the PnP and PM event handlers either return no value or S\_OK. There are two exceptions: **IPnpCallbackHardware::OnPrepareHardware**and **IPnPCallbackHardware::OnReleaseHardware**. The following table describes each method.

|                                             |                                                                                                                           |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **IPnpCallbackHardware::OnPrepareHardware** | Calls the **WpdBaseDriver::Initialize** method. Initializes the WPD class extension and updates the device-friendly name. |
| **IPnPCallbackHardware::OnReleaseHardware** | Calls the **WpdBaseDriver::Uninitialize** method and uninitializes the WPD class extension.                               |

 

For a description of each interface and its methods, see the [UMDF documentation](http://go.microsoft.com/fwlink/p/?linkid=153678)..

## <span id="related_topics"></span>Related topics


****
[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





