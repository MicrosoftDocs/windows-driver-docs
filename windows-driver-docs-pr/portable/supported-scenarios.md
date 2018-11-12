---
Description: Supported Scenarios
title: Supported Scenarios
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supported Scenarios


The Windows Portable Devices (WPD) DDI allows you to transfer content to or from a device, browse device contents, control device behavior, and enabe vertical solutions. This section describes each of these scenarios.

## <span id="Content_Transfer"></span><span id="content_transfer"></span><span id="CONTENT_TRANSFER"></span>Content Transfer


WPD supplies the necessary infrastructure to standardize data transfers between applications and portable devices that are connected to a computer running Windows. It provides applications with a uniform view of devices and their content, as well as standardized mechanisms to access and transfer data.

For example, the WPD DDI enables applications to sync content between the device and the computer.

## <span id="Browsing_Device_Contents"></span><span id="browsing_device_contents"></span><span id="BROWSING_DEVICE_CONTENTS"></span>Browsing Device Contents


By using the WPD namespace, users can apply Windows file management approaches to portable devices of any type. (For more information about how to implement Context Menu and Property Page extensions in a WPD application, see the Windows Portable Devices Programming Guide in the [WPD SDK](http://go.microsoft.com/fwlink/p/?linkid=178695).)

## <span id="Device_Control"></span><span id="device_control"></span><span id="DEVICE_CONTROL"></span>Device Control


In addition to providing standard access to device content, the WPD infrastructure offers ways to standardize device controls. This allows applications to control various device behaviors, as well as issue device commands. For example, WPD application for mobile phones can request a phone send message or receive message while it is connected to the computer.

## <span id="Enabling_Vertical_Solutions"></span><span id="enabling_vertical_solutions"></span><span id="ENABLING_VERTICAL_SOLUTIONS"></span>Enabling Vertical Solutions


The WPD infrastructure offers highly extensible device representation and control mechanisms. This enables vertical solution providers to use the WPD application programming interface (API) to create enhanced user experiences that are outside of the WPD standardized set. Examples of this include the vendor-provided software suites that are included with the device, , firmware updates, and device diagnostics (for remote support).

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





