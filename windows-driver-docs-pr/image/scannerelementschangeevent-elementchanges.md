---
title: ScannerElementsChangeEvent.ElementChanges
description: ScannerElementsChangeEvent.ElementChanges
ms.assetid: bf047894-e97d-459d-a126-180e5a725e68
keywords: ["ScannerElementsChangeEvent.ElementChanges"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScannerElementsChangeEvent.ElementChanges


The **ElementChanges** element should contain the entire element of the scanner schema that contains changed values. For example, if this event was sent when an automatic document feeder (ADF) was installed, the complete **ScannerDescription** element would be sent. Likewise, if a value changed in the **DefaultScanTicket**, the complete **DefaultScanTicket** element would be sent.

The **ElementChanges** element supports the following sub-elements:

[ScannerElementsChangeEvent.ElementChanges.ScannerDescription](scannerelementschangeevent-elementchanges-scannerdescription.md)

[ScannerElementsChangeEvent.ElementChanges.ScannerConfiguration](scannerelementschangeevent-elementchanges-scannerconfiguration.md)

[ScannerElementsChangeEvent.ElementChanges.DefaultScanTicket](scannerelementschangeevent-elementchanges-defaultscanticket.md)

 

 





