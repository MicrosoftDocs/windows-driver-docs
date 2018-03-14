---
title: ScannerStatusConditionClearedEvent
description: ScannerStatusConditionClearedEvent
ms.assetid: fa8c44d0-21aa-401c-a45b-9a8be4766378
keywords: ["ScannerStatusConditionClearedEvent"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScannerStatusConditionClearedEvent


The scanner sends the **ScannerStatusConditionClearedEvent** event to the control point when a previously reported **DeviceCondition** has been cleared. The body of the **ScannerStatusConditionClearedEvent** element consists of the **DeviceConditonId** element for the condition that has been cleared and the **ConditionClearTime** element that specifies when the condition was cleared.

The **ScannerStatusConditionClearedEvent** element supports the following sub-element:

[ScannerStatusConditionClearedEvent.DeviceConditonCleared](scannerstatusconditionclearedevent-deviceconditoncleared.md)

 

 





