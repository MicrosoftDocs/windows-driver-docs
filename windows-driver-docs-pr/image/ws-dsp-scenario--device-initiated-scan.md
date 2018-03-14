---
title: WS-DSP Scenario Device-Initiated Scan
author: windows-driver-content
description: WS-DSP Scenario Device-Initiated Scan
ms.assetid: aa301f2c-64f6-4b4f-bb48-f3b2a10ea08d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WS-DSP Scenario: Device-Initiated Scan


An end-user wants to scan a document for storage in a shared folder. From the directory service, the DSM Device retrieves the scan processes that are associated with the user and displays them to the user. Using a user interface on the DSM Device, the user selects the appropriate scan process for the scan job, places the document on the DSM Device and presses the scan button on the DSM Device.

The DSM Device scans the document using the settings specified in the scan ticket of the selected scan process. After scanning an image of the document, the DSM Device submits a **CreatePostScanJob** operation to the DSM Scan Server for post-scan processing of the scanned images. The **CreatePostScanJob** operation contains the post-scan instructions from the scan process. The DSM Device submits the image data of each scanned document to the DSM Scan Server in a **SendImage** operation and sends an **EndPostScanJob** operation after the last **SendImage** operation.

 

 




