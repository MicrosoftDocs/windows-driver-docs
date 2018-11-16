---
title: Feeder Scanner Architecture
description: Feeder Scanner Architecture
ms.assetid: 02157a88-fccd-4a23-a4ee-174755c8d3aa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Feeder Scanner Architecture





Scanner devices that have document feeder units must implement a feeder item in their WIA item tree if any images are to be produced from documents that are placed in the document feeder. The feeder item represents a programmable data source and produces images from documents that are placed in the scanner's document feeder scanning unit when a data transfer is requested from this item. The scanner feeder item should be located directly off the WIA root item and may contain one or more child items that represent the front and back pages of a document.

The following topics describe examples of flatbed scanners that support document feeder scanning:

[Non-Duplex-Capable Document Feeder](non-duplex-capable-document-feeder.md)

[Simple Duplex-Capable Document Feeder](simple-duplex-capable-document-feeder.md)

[Advanced Duplex-Capable Document Feeder](advanced-duplex-capable-document-feeder.md)

 

 




