---
title: Wi-Fi Direct
description: Wi-Fi Direct
ms.assetid: 52D09B1D-5832-48C9-B200-46B8DDC14BE5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="p_phpartappdev.wi-fi_direct"></span>Wi-Fi Direct


The WDI driver in Windows 10 and the associated Wi-Fi Direct APIs replace the NDIS driver and associated SoftAP APIs in Windows 8.1. While you can continue to use the SoftAP API to work with the NDIS driver in Windows 10, the APIs are deprecated starting in Windows 8.1. That includes IDot11AdHocManager and related interfaces.

For full functionality in Windows 10, you should use the Wi-Fi Direct WinRT APIs with the WDI driver instead.

You can, however, use some of the Wi-Fi Direct WinRT APIs in a Classic Windows application. For instance you can use the Wi-Fi Direct WinRT APIs in place of WFDOpenHandle and related APIs in Classic Windows applications. The WiFiDirectLegacySettings class allows devices that do not support Wi-Fi Direct to connect to a device that does support it, and to use the services offered by the Wi-Fi Direct device.

WiFiDirectLegacySettings allows you to specify the SSID and password. For an example of how to use WiFiDirectLegacySettings in a Classic Windows application, see the [WiFiDirectLegacyAPDemo\_v1.0.zip](http://go.microsoft.com/fwlink/?LinkId=617905) download on the Microsoft download center.

Mobile Hotspots are supported starting in Windows 10, version 1607. A Mobile Hotspot is an enhanced version of the mobile broadband tethering feature. Note that the Mobile Hotspot and legacy Wi-Fi Direct group owner features cannot be used at the same time. Additionally, Mobile Hotspot takes precedence over all Wi-Fi Direct scenarios.

Developers of desktop applications can use this sample to see how to replace the deprecated WlanHostedNetwork\* API's with the new WinRT API's without modifying the application to become a Universal Windows Application. These API's let an application start a Wi-Fi Direct Group Owner (GO) that acts as an Access Point (AP). This allows devices that do not support Wi-Fi Direct to connect to the Windows device running this application and communicate over TCP/UDP. The API's allow the developer to optionally specify an SSID and passphrase, or use randomly generated ones.

**Note**  In Classic Windows apps, you don’t need to set the WinRT device capabilities because there is no Package.appxmanifest file.

 

## <span id="Resources"></span><span id="resources"></span><span id="RESOURCES"></span>Resources


### <span id="Recorded_sessions"></span><span id="recorded_sessions"></span><span id="RECORDED_SESSIONS"></span>Recorded sessions

-   [Wi-Fi Direct and Wi-Fi Direct Services API (including sample code)](http://go.microsoft.com/fwlink/?LinkId=617632)

### <span id="MSDN_Library"></span><span id="msdn_library"></span><span id="MSDN_LIBRARY"></span>MSDN Library

-   [Wi-Fi Direct Services API](http://go.microsoft.com/fwlink/?LinkId=617633)
-   [What's new in driver development?]( http://go.microsoft.com/fwlink/?LinkId=617634)
-   [Using WinRT API in Win32 App]( http://go.microsoft.com/fwlink/?LinkId=617635)

### <span id="Wi-Fi_Direct_in_Windows_8"></span><span id="wi-fi_direct_in_windows_8"></span><span id="WI-FI_DIRECT_IN_WINDOWS_8"></span>Wi-Fi Direct in Windows 8

-   [Understanding Wi-Fi Direct in Windows 8](http://go.microsoft.com/fwlink/?LinkId=617636)
-   [Ask the experts panel: Connected apps](http://go.microsoft.com/fwlink/?LinkId=617637)
-   [Building Windows Apps That Use Wi-Fi Direct (Windows 8.1)](http://go.microsoft.com/fwlink/?LinkId=617638)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_phPartAppDev\p_phPartAppDev%5D:%20Wi-Fi%20Direct%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




