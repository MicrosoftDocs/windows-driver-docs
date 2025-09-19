---
title: Captive Portal Detection and User Experience in Windows
description: Learn how Windows detects and manages captive portal networks, addresses user challenges, and learn tips for effective portal design.
ms.date: 07/08/2025
ms.topic: concept-article
---

# Captive Portal Detection and User Experience in Windows

Captive portals are commonly used by public Wi-Fi networks to manage user access and authentication. When a device connects to a network with a captive portal, the network redirects all web traffic to a specific web page where users finish actions like accepting terms or entering credentials before they get full internet access. This article explains how Windows interacts with captive portals, outlines common challenges users can face, and gives best practices for designing effective captive portal experiences.

## Understand captive portals

Most hotspots use a captive portal, which is a restricted network connection that redirects all client HTTP requests to the provider’s website. The website then prompts users to agree to the operator’s terms and conditions, enter payment information, or enter credentials to verify prior payment arrangements.

Captive portals can cause several problems:

- Other applications (such as email clients) are also redirected. If the user tries to use an app other than the web browser first, they will encounter errors without knowing how to resolve them.
- If the initial connection uses Secure Sockets Layer (SSL), the browser shows a security warning before redirecting the user to the captive portal. This experience can be confusing because users have to ignore the security warning to connect.

Windows supports captive portal networks by immediately opening the web browser when it detects a captive portal. The user sees your branded web page in the foreground, which helps them learn what actions to take to authenticate with the captive portal.

Windows lets users bypass captive portals on later connection attempts. But, first-time users always see the captive portal experience.

This article covers the following best practices for using captive portals:

- [Consistent connection handling](#ensure-consistent-connection-handling)
- [Touch-friendly web pages](#use-touch-friendly-web-pages)
- [Provision after purchase](#provision-after-purchase)
- [Offer app installation](#offer-app-installation)

> [!NOTE]
> Captive portal functionality is not supported at the Windows login screen.

## Ensure consistent connection handling

To check internet connectivity and captive portal status when a client first connects to a network, Windows runs a series of network tests. These tests use **msftncsi.com**, a reserved domain for connectivity testing. When Windows detects a captive portal, it repeats these tests until the captive portal lets the user connect.

To avoid false positive or false negative test results, don't do these things with your captive portal:

- Allow access to **www.msftncsi.com** when the user doesn't have internet access.
- Change the captive portal behavior shown to clients. For example, don't redirect some requests and drop others. Keep redirecting all requests until authentication succeeds.

> [!NOTE]
> Denial of Service mitigations should be based on the frequency of attempts per client, not the number of attempts per client or the total attempts from all clients.

## Use touch-friendly web pages

The Windows experience is designed to be touch-first. This extends to web pages. Lay out your web page with larger, easy-to-target controls for touch users. Use layouts that don't require excessive scrolling to interact with, and break flows into multiple pages if needed. For more information on touch-friendly web design, see [Designing for Touch Input](/previous-versions/windows/desktop/ms695008(v=vs.85)).


## Provision after purchase

Apply the same provisioning file with an app or a website. In your web page’s JavaScript, check for the [window.external.msProvisionNetworks](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/dn529170(v=vs.85)) method. If it's present, the browser relays a provisioning file to the operating system. For more info about generating this provisioning file, see [Using metadata to configure mobile broadband experiences](using-metadata-to-configure-mobile-broadband-experiences.md).

> [!NOTE]
> This provisioning file must be signed when it is provided by a website or an app that is not the mobile broadband app.

Passing an XML provisioning file lets the operating system automatically connect to other networks in the user’s service, even if they have different service set identifiers (SSIDs). If you use static Wireless Internet Service Provider roaming (WISPr) credentials, Windows automatically authenticates with those credentials in the future for a smoother connection experience.

## Offer app installation

Users get the richest Windows experience with a mobile broadband app. You can't allow access to only one app in the Microsoft Store through a captive portal, so users can't install the app before they have internet connectivity. After users authenticate, send them to the Microsoft Store to install your mobile broadband app.

## Related content

- [Integrating Windows with wireless hotspots](integrating-windows-with-wireless-hotspots.md)

