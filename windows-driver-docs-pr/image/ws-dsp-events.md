---
title: WS-DSP Events
author: windows-driver-content
description: WS-DSP Events
ms.assetid: 660d3110-c695-405e-8bab-c0a9c65fcc8f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# WS-DSP Events


Events are defined to inform the DSM Device of the status of active and finished post-scan jobs. The basic event model is based on Web Service Eventing. The DSM Device will only send events to subscribed clients as specified in WS-Eventing specification at [Web Services Eventing](http://go.microsoft.com/fwlink/p/?linkid=154074).

The following events must be produced by the DSM Scan Server and supported by the DSM Device:

**PostScanJobEndStateEvent** - sent by the DSM Scan Server to the DSM Device when a post-scan job has finished processing.

**PostScanJobStatusEvent** - sent by the DSM Scan Server to the DSM Device when a post-scan job's status has changed.

 

 




