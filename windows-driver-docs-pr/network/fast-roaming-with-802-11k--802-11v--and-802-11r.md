---
title: Fast Roaming with 802.11k, 802.11v, and 802.11r
description: This section describes improved WLAN roaming experiences with 802.11k, 801.11v, and 802.11r
ms.assetid: EAD532E7-7C43-45BF-8C1A-5645A15F2607
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Fast Roaming with 802.11k, 802.11v, and 802.11r


Improved WLAN roaming experiences are now available to devices running Windows 10. Industry standard implementations that reduce the time needed for a device to roam from one wireless access point (AP) to another are now supported.

## 802.11k (Neighbor Reports)


Wireless Access Points (APs) that support 802.11k are able to provide Neighbor Reports to devices running Windows 10. Neighbor Reports contain information about neighboring access points and allows the device to have a better understanding of its surroundings. Windows 10 takes advantage of this capability by shortening the list of channels that the device needs to scan before finding a neighboring AP to roam to.

## 802.11v (BSS Transition Management Frames)


APs that support 802.11v can now direct Windows 10 devices to roam to another AP that it deems will provide a better WLAN experience for the device. Windows 10 devices can now accept and respond to these Basic Service Set (BSS) Transition Management frames, leading to improved WLAN quality when connected to a network that supports 802.11v.

## 802.11r (Fast BSS Transition)


Fast BSS Transition reduces the time needed for a Windows 10 device to transition to an AP that supports 802.11r. This time reduction results from fewer frames being exchanged with the AP prior to data transfer. By decreasing the time before data transfer when the device roams from one AP to another, the connection quality is improved for latency sensitive applications, such as an active Skype call. Windows 10 supports Fast BSS Transitions over networks using 802.1X as the authentication method. Pre-Shared Key (PSK) and Open Networks are currently not supported.

With the combination of 802.11k, 802.11v, and 802.11r, Windows 10 takes advantage of established industry standards to improve the roaming experience for our users. VoIP applications can now take advantage of this improved roaming to deliver better call quality when users are not stationary.

## Things to note


Not all Windows 10 devices support 802.11k, 802.11v, and 802.11r. The WLAN Radio driver must support these features to enable them to work on Windows 10. Please check with your device manufacturer to determine whether or not your device supports these features. In addition to device-side support, the network (AP Controllers and APs) must also support the features for the experience to work. Please check with your network administrator to see if these features are supported and have been enabled on the network in question.

Windows 10 continues to support Opportunistic Key Caching (OKC) when 802.11r is not available on the device or the network.

All three features require AP-side support and will not work without those features enabled on the APs.

 

 





