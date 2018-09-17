---
title: Scan Job Setup
author: windows-driver-content
description: Scan Job Setup
ms.assetid: 9fca3b10-8df9-476a-a319-6f0ab7bbd6e8
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Scan Job Setup


The distributed scan management model defines the scan job setup phase as and when scan tickets are created, validated, and stored in a scan process.

A control point may use the Distributed Scan Device Web Service (WS-DSD) to query a DSM Device in order to determine the capabilities of the DSM Device. The control point may provide a local user interface for the administrator to select and configure scanning options such as color mode, resolution, and so on, depending on what capabilities the DSM Device supports. The control point may then store selected options as a scan ticket in a scan process in the directory service.

 

 




