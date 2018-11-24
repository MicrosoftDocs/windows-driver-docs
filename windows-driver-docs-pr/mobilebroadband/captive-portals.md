---
title: Captive portals
description: Captive portals
ms.assetid: 6f710440-3012-4bf4-92cc-3743b0f4fd34
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Captive portals


Most hotspots implement customer interaction by using a captive portal, which is a restricted network connection in which all client HTTP requests are redirected to the provider’s web site. The web site can then prompt users to agree to the operator’s terms and conditions, enter payment information, or enter credentials to verify prior payment arrangements.

Several problems exist by using such an experience:

-   Other applications (such as email clients) are also redirected. If the user tries to use an app other than the web browser first, they will encounter errors without knowing how to resolve them.

-   If the initial connection attempted is made over Secure Sockets Layer (SSL), the browser displays a security warning to the user before the user is redirected to the captive portal. This creates a confusing experience for users because they must ignore the security warning to get connected.

Windows 8, Windows 8.1, and Windows 10 support captive portal networks by immediately opening the web browser if a captive portal is detected. The user sees your branded web page in the foreground of their device, which helps them to understand what actions they should take to authenticate by using the captive portal.

Windows provides mechanisms that can let users bypass captive portals on subsequent connection attempts. However, the captive portal is always the experience that is encountered by a first-time user.

This topic discusses the following best practices for using captive portals:

-   [Consistent connection handling](#cch)

-   [Touch-friendly web pages](#touchfr)

-   [Provision after purchase](#pap)

-   [Offer app installation](#appinst)

## <span id="cch"></span><span id="CCH"></span>Consistent connection handling


To determine Internet connectivity and captive portal status when a client first connects to a network, Windows performs a series of network tests. The destination site of these tests is **msftncsi.com**, which is a reserved domain that is used exclusively for connectivity testing. When a captive portal is detected, these tests are periodically repeated until the captive portal is released.

To avoid false positive or false negative test results, your captive portal should not do the following:

- Allow access to <strong>www.msftncsi.com</strong> when the user does not have access to the Internet.

- Change the captive portal behavior that is displayed to clients. For example, do not redirect some requests and drop other requests; you should continue to redirect all requests until authentication succeeds.

  **Note**  
  Denial of Service mitigations should be based on the frequency of attempts per client, not the number of attempts per client or the total attempts from all clients.

     

## <span id="touchfr"></span><span id="TOUCHFR"></span>Touch-friendly web pages


The Windows 8, Windows 8.1, and Windows 10 experience is designed to be touch-first. This extends to web pages. Consider laying out your web page with larger, easy-to-target controls for a touch user. Use layouts that do not require excessive scrolling to interact with, and break flows into multiple pages if necessary. For more information on touch-friendly web design, see [Designing for Touch Input](https://msdn.microsoft.com/library/windows/apps/hh465415.aspx).

## <span id="pap"></span><span id="PAP"></span>Provision after purchase


The same provisioning file that can be applied by an app can also be applied by a website. In the web page’s JavaScript, check for the availability of the [**window.external.msProvisionNetworks**](https://msdn.microsoft.com/library/dn529170) method. If it is present, the browser can relay a provisioning file to the operating system. See [Using metadata to configure mobile broadband experiences](using-metadata-to-configure-mobile-broadband-experiences.md) for more information about how to generate this provisioning file.

**Note**  
This provisioning file must be signed when it is provided by a website or an app that is not the mobile broadband app.

 

Passing an XML provisioning file enables the operating system to automatically connect to other networks that are included in the user’s service, even if they have different service set identifiers (SSIDs). If you use static Wireless Internet Service Provider roaming (WISPr) credentials, it also enables a smoother connection experience because in the future, Windows can automatically authenticate with those credentials.

## <span id="appinst"></span><span id="APPINST"></span>Offer app installation


The richest experience of Windows 8, Windows 8.1, and Windows 10 is through the use of a mobile broadband app. It is not possible to allow access to only one app in the Microsoft Store through a captive portal, so the app cannot be installed prior to the user obtaining Internet connectivity. However, after the user has authenticated, consider directing them to the Microsoft Store to install your mobile broadband app.

## <span id="related_topics"></span>Related topics


[Hotspot authentication methods](hotspot-authentication-methods.md)

 

 






