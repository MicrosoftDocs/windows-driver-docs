---
Description: WPD and Earlier Technologies
title: WPD and Earlier Technologies
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WPD and Earlier Technologies


WPD contains many enhancements for digital still cameras and portable digital media players. WPD is the preferred method for accessing these devices in new versions of Windows, including Windows XP, Windows Vista, and Windows 7. The existing Windows Image Acquisition (WIA) and Windows Media Device Manager (WMDM) APIs in Windows will continue to be supported and compatibility with WPD will be provided by compatibility layers. These compatibility layers ensure WPD devices can be transparently exposed to existing WIA and WMDM applications as WIA devices or WMDM Service Providers respectively. However, these applications may not have the same range of capabilities as they would with the new WPD API and new MTP-based devices.

The WPD MTP driver also supports Picture Transfer Protocol (PTP) devices. PTP devices that were supported in WIA will continue to function in WIA applications through the compatibility layer. Microsoft remains committed to ensuring application and digital still camera compatibility in the next version of Windows and these new technologies are designed to complement and enhance the digital still camera experience in Windows.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





