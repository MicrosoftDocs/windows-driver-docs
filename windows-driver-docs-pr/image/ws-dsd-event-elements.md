---
title: WS-DSD Event Elements
description: WS-DSD Event Elements
ms.assetid: 329dbfe5-b430-443e-922a-43694bff0d50
keywords: ["WS-DSD Event Elements"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# WS-DSD Event Elements


The scanner must implement eventing as it is defined by the WS-Eventing specification. The scanner will be an extension of the WS-Eventing port type and must add the operations that are defined for the scan service to create and manage event subscriptions.

The eventing model for WS-DSD notifies the control point of changes in the scanner status and the job status.

A WS-DSD system must support the following events:

[JobEndStateEvent](jobendstateevent.md)

[JobStatusEvent](jobstatusevent.md)

[ScannerElementsChangeEvent](scannerelementschangeevent.md)

[ScannerStatusConditionClearedEvent](scannerstatusconditionclearedevent.md)

[ScannerStatusConditionEvent](scannerstatusconditionevent.md)

[ScannerStatusSummaryEvent](scannerstatussummaryevent.md)

 

 





