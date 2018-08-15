---
title: Post-Scan Job Execution
author: windows-driver-content
description: Post-Scan Job Execution
ms.assetid: 3ce8eee6-0aaa-43da-b3ca-d12063c01d7d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Post-Scan Job Execution


After the DSM Device has scanned an image, the DSM Device creates a post-scan job on the DSM Scan Server and uses Distributed Scan Processing Web Service (WS-DSP) to send the scanned image data to a DSM Scan Server for post-scan processing. The DSM Scan Server performs the post-scan processing that is described in the post-scan instructions of the selected scan process. The post-scan job ends when the DSM Scan Server has processed all image data sent by the DSM Device for the post-scan job.

Distributed scan management supports only device initiated scan jobs. This means that a scan job must be initiated by a user who interacts directly with a DSM Device. The DSM Device must retrieve a scan process from a directory service. The DSM Device must include the post-scan instructions from the scan process with the image data that is transferred to the DSM Scan Server.

 

 




