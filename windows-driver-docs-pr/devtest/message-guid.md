---
title: Message GUID
description: Message GUID
keywords:
- message GUIDs WDK
- GUIDs WDK software tracing
- identifiers WDK software tracing
ms.date: 11/22/2022
---

# Message GUID

A *message GUID*, or *decode GUID*, is a GUID assigned to the trace messages for a class of software trace messages. 

The same GUID is used as the file name of the [trace message format (TMF) file](trace-message-format-file.md) (.tmf extension) that stores the formatting instructions for those messages.

Tracefmt can use the message GUID of the trace messages to identify the TMF file that contains formatting instructions for the message in a directory of TMF files. The TMF file names consist of the message GUID with a .tmf file name extension. For more information, see [Understanding Tracefmt](understanding-tracefmt.md).

Event Tracing for Windows (ETW) uses the message GUID to associate the trace messages with the correct TMF file. For more information about how this is done, see [Tracepdb](tracepdb.md).

