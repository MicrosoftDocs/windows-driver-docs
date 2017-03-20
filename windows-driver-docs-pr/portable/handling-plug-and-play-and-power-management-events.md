---
Description: Handling Plug and Play and Power Management Events
MS-HAID: 'wpddk.handling\_plug\_and\_play\_and\_power\_management\_events'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Handling Plug and Play and Power Management Events
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Handling%20Plug%20and%20Play%20and%20Power%20Management%20Events%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




