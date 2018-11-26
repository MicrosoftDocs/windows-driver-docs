---
title: Closing the Communication Server Port
description: Closing the Communication Server Port
ms.assetid: 43dfa162-0098-4a9b-9272-9da429cb0108
keywords:
- communication server ports WDK file system minifilter
- ports WDK , file system minifilter
- closing communication server ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing the Communication Server Port


## <span id="ddk_closing_the_communication_server_port_if"></span><span id="DDK_CLOSING_THE_COMMUNICATION_SERVER_PORT_IF"></span>


If the minifilter driver previously opened a kernel-mode communication server port by calling [**FltCreateCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541931), it must close the port by calling [**FltCloseCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541871). To prevent the system from hanging during the unload process, the minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine must close this port before calling [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606).

If a user-mode application has an open connection to the communication server port, any client port for that connection will remain open after [**FltCloseCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541871) returns. However, the filter manager will close any client ports when the minifilter driver is unloaded.

 

 




