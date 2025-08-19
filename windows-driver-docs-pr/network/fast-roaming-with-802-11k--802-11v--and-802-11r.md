---
title: Fast Roaming in Windows 10 with 802.11k, 802.11v, and 802.11r
description: Learn how fast roaming with 802.11k, 802.11v, and 802.11r improves WLAN performance in Windows 10. Discover benefits and requirements.
ms.date: 05/15/2025
ms.topic: concept-article
---

# Fast Roaming in Windows 10 with 802.11k, 802.11v, and 802.11r

Fast roaming with 802.11k, 802.11v, and 802.11r lets Windows 10 devices switch between wireless access points more quickly. This article explains how these standards improve WLAN performance and give you faster, more reliable connections.

## How 802.11k neighbor reports improve roaming

Wireless access points (APs) that support 802.11k give Neighbor Reports to devices running Windows 10. Neighbor Reports have information about neighboring access points and help the device understand its surroundings. Windows 10 uses this capability to shorten the list of channels the device scans before finding a neighboring AP to roam to.

## How 802.11v transition management improves WLAN

APs that support 802.11v can direct Windows 10 devices to roam to another AP that gives a better WLAN experience. Windows 10 devices accept and respond to these Basic Service Set (BSS) Transition Management frames, which improves WLAN quality when connected to a network that supports 802.11v.

## How 802.11r fast BSS transition enhances roaming

Fast BSS Transition reduces the time a Windows 10 device needs to transition to an AP that supports 802.11r. Fewer frames are exchanged with the AP before data transfer, so latency sensitive applications, like an active Skype call, have better connection quality. Windows 10 supports Fast BSS Transitions over networks that use 802.1X as the authentication method. Pre-Shared Key (PSK) and open networks aren't supported.

With 802.11k, 802.11v, and 802.11r, Windows 10 uses industry standards to improve the roaming experience for you. VoIP applications use this improved roaming to deliver better call quality when you're moving.

## Important considerations for fast roaming

Not all Windows 10 devices support 802.11k, 802.11v, and 802.11r. The WLAN radio driver must support these features for them to work on Windows 10. Check with your device manufacturer to see if your device supports these features. The network (AP controllers and APs) must also support these features. Check with your network admin to see if these features are supported and enabled on your network.

Windows 10 supports Opportunistic Key Caching (OKC) when 802.11r isn't available on the device or the network.

All three features need AP-side support and don't work unless they're enabled on the APs.







