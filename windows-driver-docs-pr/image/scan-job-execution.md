---
title: Scan Job Execution
author: windows-driver-content
description: Scan Job Execution
ms.assetid: cefc6aee-725d-4dc4-bbdc-3d152c97b203
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Scan Job Execution


The execution phase begins when a user initiates a scan job at a DSM Device. The DSM Device retrieves the scan processes that are available for the user and displays them to the user. The user must select one of the available scan processes. The user may override any individual settings of a scan process that are not marked to disallow user override. The DSM Device uses the scan ticket from the selected scan process or, if the user overrides the scan process settings, creates a new scan ticket from the user-specified settings to use when scanning the document. Insofar as Distributed Scan Device Web Service (WS-DSD) is concerned, the scan job ends when the DSM Device has finished digitizing the final image.

 

 




