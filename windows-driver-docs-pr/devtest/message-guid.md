---
title: Message GUID
description: Message GUID
keywords:
- message GUIDs WDK
- GUIDs WDK software tracing
- identifiers WDK software tracing
ms.date: 04/20/2017
---

# Message GUID

A *message GUID*, or *decode GUID*, is a GUID assigned to the trace messages from a particular provider. The same GUID is used as the file name of the [trace message format (TMF) file](trace-message-format-file.md) (.tmf extension) that stores the formatting instructions for those messages.

Event Tracing for Windows (ETW) uses the message GUID to associate the trace messages with the correct TMF file. For more information about how this is done, see [Tracepdb](tracepdb.md).
