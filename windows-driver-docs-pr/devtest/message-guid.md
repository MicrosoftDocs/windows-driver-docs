---
title: Message GUID
description: Message GUID
ms.assetid: 3a51d730-61a4-44d9-aaf6-117736412efe
keywords: ["message GUIDs WDK", "GUIDs WDK software tracing", "identifiers WDK software tracing"]
---

# Message GUID


## <span id="ddk_message_guid_tools"></span><span id="DDK_MESSAGE_GUID_TOOLS"></span>


A *message GUID* is a GUID assigned to the trace messages from a particular provider. The same GUID is used as the file name of the [trace message format (TMF) file](trace-message-format-file.md) (.tmf extension) that stores the formatting instructions for those messages.

Event Tracing for Windows (ETW) uses the message GUID to associate the trace messages with the correct TMF file. For more information about how this is done, see [Tracepdb](tracepdb.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Message%20GUID%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




