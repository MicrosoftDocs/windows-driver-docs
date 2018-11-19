---
title: Message GUID
description: Message GUID
ms.assetid: 3a51d730-61a4-44d9-aaf6-117736412efe
keywords:
- message GUIDs WDK
- GUIDs WDK software tracing
- identifiers WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Message GUID


## <span id="ddk_message_guid_tools"></span><span id="DDK_MESSAGE_GUID_TOOLS"></span>


A *message GUID* is a GUID assigned to the trace messages from a particular provider. The same GUID is used as the file name of the [trace message format (TMF) file](trace-message-format-file.md) (.tmf extension) that stores the formatting instructions for those messages.

Event Tracing for Windows (ETW) uses the message GUID to associate the trace messages with the correct TMF file. For more information about how this is done, see [Tracepdb](tracepdb.md).

 

 





