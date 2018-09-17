---
title: ScannerElementsChangeEvent
description: ScannerElementsChangeEvent
ms.assetid: b6a7d972-2376-499b-b063-88de733a1068
keywords: ["ScannerElementsChangeEvent"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScannerElementsChangeEvent


The scanner sends the **ScannerElementsChangeEvent** event to the control point when something has changed in the **ScannerDescription** element, the **ScannerConfiguration** element, the **DefaultScanTicket** element, or an IHV extension in the scanner. The body of the **ScannerElementsChangeEvent** element contains the complete XML data of the element that has changed. If an optional element is missing from returned XML, the implication is that that element is no longer supported by the scanner. For example, such a case might occur after the removal of a film scan option or a duplex scanning mode. The client on the control point is then responsible for comparing the incoming element to previous data to determine which values have changed.

The **ScannerElementsChangeEvent** event supports the following sub-element:

[ScannerElementsChangeEvent.ElementChanges](scannerelementschangeevent-elementchanges.md)

 

 





