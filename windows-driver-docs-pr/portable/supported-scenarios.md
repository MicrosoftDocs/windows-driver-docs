---
Description: Supported Scenarios
MS-HAID: 'wpddk.supported\_scenarios'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supported Scenarios
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supported%20Scenarios%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




