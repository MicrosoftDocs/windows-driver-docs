---
title: Wi-Fi Direct
description: Provides information on the use of Wi-Fi Direct WinRT APIs in Windows applications.
ms.date: 08/04/2021
ms.localizationpriority: medium
---

# Wi-Fi Direct

The WDI driver in Windows 10 and the associated Wi-Fi Direct APIs replace the NDIS driver and associated SoftAP APIs in Windows 8.1. While you can continue to use the SoftAP API to work with the NDIS driver in Windows 10, the APIs are deprecated starting in Windows 8.1. That includes IDot11AdHocManager and related interfaces.

For full functionality in Windows 10, you should use the Wi-Fi Direct WinRT APIs with the WDI driver instead.

You can, however, use some of the Wi-Fi Direct WinRT APIs in a Classic Windows application. For instance you can use the Wi-Fi Direct WinRT APIs in place of WFDOpenHandle and related APIs in Classic Windows applications. The WiFiDirectLegacySettings class allows devices that do not support Wi-Fi Direct to connect to a device that does support it, and to use the services offered by the Wi-Fi Direct device.

WiFiDirectLegacySettings allows you to specify the SSID and password. For an example of how to use WiFiDirectLegacySettings in a Classic Windows application, see the [WiFiDirectLegacyAPDemo_v1.0.zip](https://download.microsoft.com/download/7/8/7/787469FC-99B4-4726-9932-945111BDC809/WiFiDirectLegacyAPDemo_v1.0.zip) download on the Microsoft download center.

Mobile Hotspots are supported starting in Windows 10, version 1607. A Mobile Hotspot is an enhanced version of the mobile broadband tethering feature. Note that the Mobile Hotspot and legacy Wi-Fi Direct group owner features cannot be used at the same time. Additionally, Mobile Hotspot takes precedence over all Wi-Fi Direct scenarios.

Developers of desktop applications can use this sample to see how to replace the deprecated WlanHostedNetwork\* API's with the new WinRT API's without modifying the application to become a Universal Windows Application. These API's let an application start a Wi-Fi Direct Group Owner (GO) that acts as an Access Point (AP). This allows devices that do not support Wi-Fi Direct to connect to the Windows device running this application and communicate over TCP/UDP. The API's allow the developer to optionally specify an SSID and passphrase, or use randomly generated ones.

> [!NOTE]
> In Classic Windows apps, you don't need to set the WinRT device capabilities because there is no Package.appxmanifest file.

## See also

[Build 2015 video: Wi-Fi Direct and Wi-Fi Direct Services API (including sample code)](https://channel9.msdn.com/Events/Build/2015/3-98)

[Wi-Fi Direct Services API](/uwp/api/windows.devices.wifidirect.services)

[Build 2011 video: Understanding Wi-Fi Direct in Windows 8](https://channel9.msdn.com/Events/Build/BUILD2011/HW-329T)

[Build 2013 video: Building Windows Apps That Use Wi-Fi Direct (Windows 8.1)](https://channel9.msdn.com/Events/Build/2013/3-9030)
