---
title: Driver Capabilities
author: windows-driver-content
description: Driver Capabilities
MS-HAID:
- 'WIA\_arch\_6fc7181b-5344-4baf-bd5a-b99813c0ce9e.xml'
- 'image.driver\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 639eff56-655d-4b6a-95f0-daa1daf62fae
---

# Driver Capabilities


## <a href="" id="ddk-driver-capabilities-si"></a>


All WIA minidrivers must define the device's ability to handle notification events and commands. This section describes these minidriver capabilities.

The WIA minidriver is responsible for building a table that lists all of the events and commands that it supports. The following diagram illustrates the capabilities table that the WIA minidriver builds.

![diagram illustrating the wia minidriver capabilities table](images/wia-capabilitiestable.png)

The capabilities table is defined as an array of [**WIA\_DEV\_CAP\_DRV**](https://msdn.microsoft.com/library/windows/hardware/ff550233) structures. The minidriver must construct this array and return it to the WIA service when the WIA service calls the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method.

### Defining Supported Events and Commands

WIA minidrivers must describe the events and commands that the device supports to the WIA service.

### Events

An *event* is an action at the device level that must be reported to the driver. For example, a scanner might have a front panel button that is labeled "Scan". When users press this button, they expect the scanner to begin scanning, or at the very least, that an application will start to initiate the scan.

WIA supports two types of events:

<a href="" id="action-event"></a>Action Event  
An *action event* starts the application that is registered to handle such an event. For example, the Microsoft Scanner and Camera Wizard is a registered handler for the Scan event (other applications can register for this event as well). When a driver sends the Scan event, the WIA service starts the Scanner and Camera Wizard to handle this event. This type of event is frequently referred to as a *persistent event*.

<a href="" id="notification-event"></a>Notification Event  
A *notification event* is sent only to applications that are already running and have indicated to the WIA service that they should receive this event. If the application is not running, it is not started to handle this event.

An event can be both an action event and a notification event.

### Commands

A WIA device command is a request that the WIA service sends (on behalf of the imaging application) to the WIA minidriver that instructs the minidriver to perform some action. For example, a WIA camera minidriver might handle the **Take Picture** command. This command instructs the minidriver to order the digital camera device to take a new picture.

**Note**   The Scanner and Camera Wizard responds immediately to the user, even if it still has clean-up to do in the background. For example, the Scanner and Camera Wizard window closes immediately when the user requests to cancel an action; however, the Scanner and Camera Wizard has a separate acquisition thread that continues to run after the window is closed. This separate thread enables an immediate response to the user's request but enables necessary tasks and tasks that cannot be interrupted to complete without impacting the user experience.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Driver%20Capabilities%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


