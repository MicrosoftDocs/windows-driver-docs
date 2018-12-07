---
title: Host Process Timeouts in UMDF
description: Host Process Timeouts in UMDF
ms.assetid: b8a0a4cc-9c6d-40e2-a3f1-9807dbcf15d9
keywords:
- User-Mode Driver Framework WDK , time-outs
- UMDF WDK , time-outs
- user-mode drivers WDK UMDF , time-outs
- time-outs WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Host Process Timeouts in UMDF


When the reflector sends a critical request to the driver host process, the host starts an internal timer. The default timeout interval is 60 seconds. Critical requests include Plug and Play, power, and I/O cancellation.

As long as the User-Mode Driver Framework (UMDF) driver performs operations on a regular basis toward completing the request, the reflector extends the timeout period. For example, for a remove request, the driver needs to return from the remove callbacks at regular intervals.

If the timeout period expires, the reflector generates a WER error report, terminates the host process, and attempts to restart the device. For info about automatic restart, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

For info about the fields in this report, see [Accessing UMDF Metadata in WER Reports](accessing-umdf-metadata-in-wer-reports.md).

Timeout expiration is the most common reason for the reflector to terminate the host process.

You can extend the timeout period by using the [WDF Verifier Control Application](https://msdn.microsoft.com/library/windows/hardware/ff556129).

 

 





