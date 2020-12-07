---
title: Storport I/O Model Overview
description: Storport I/O Model Overview
keywords:
- Storport drivers WDK , I/O
- I/O WDK Storport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport I/O Model Overview

This section describes the Storport driver's I/O model and contrasts this model with that of the SCSI Port driver. The Storport I/O model consists of several features designed to make maximum use of the performance potential of high-speed buses and storage devices.

The Storport driver uses a push model of I/O. This means that the driver forwards I/O requests asynchronously to its miniport driver, up to a maximum number of overlapping packets, without waiting for the miniport driver to request input. In the push model, the port driver controls the flow of the I/O requests and pushes requests down to the miniport driver.

On the other hand, the SCSI port driver uses a pull model of I/O. In a pull model of I/O, the SCSI port driver forwards I/O requests to its miniport driver synchronously and waits for the miniport driver to request new input before it sends the next I/O request. Additionally, the miniport driver controls the flow of I/O requests and pulls the requests down from the port driver.

For more information about the I/O model of the SCSI port driver, see [SCSI Port I/O Model](scsi-port-i-o-model.md).
