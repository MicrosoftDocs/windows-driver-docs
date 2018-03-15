---
title: WS-DSD Events
author: windows-driver-content
description: WS-DSD Events
ms.assetid: f690cb96-5b51-4909-b50e-77313d00a8de
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WS-DSD Events


The following events are defined to inform a control point when the configuration has changed in the DSM Device, and the status of active and finished scan jobs. The basic event model is based on web service eventing. The DSM Device will only send events to subscribed clients as specified in WS-Eventing specification at [Web Services Eventing](http://go.microsoft.com/fwlink/p/?linkid=154074).

The following events must be produced by the DSM Device:

**JobEndStateEvent** - sent by the DSM Device to the control point when a scan job has finished processing.

**JobStatusEvent** - sent by the DSM Device to the control point when a scan job's status has changed.

**ScannerElementsChangedEvent** - sent by the DSM Device to the control point when something has changed in the **ScannerDescription** element, the **ScannerConfiguration** element, the **DefaultScanTicket** element, or an IHV extension element.

**ScannerStatusConditionClearedEvent** - sent by the DSM Device to the control point when a previously reported status condition has been cleared.

**ScannerStatusConditionEvent** - sent by the DSM Device to provide the control point with detailed information about a status change in the device.

**ScannerStatusSummaryEvent** - sent by the DSM Device to the control point when the device status has changed.

 

 




