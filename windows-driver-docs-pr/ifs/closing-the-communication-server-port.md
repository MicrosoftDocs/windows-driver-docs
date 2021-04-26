---
title: Closing the Communication Server Port
description: Closing the Communication Server Port
keywords:
- communication server ports WDK file system minifilter
- ports WDK , file system minifilter
- closing communication server ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing the Communication Server Port


## <span id="ddk_closing_the_communication_server_port_if"></span><span id="DDK_CLOSING_THE_COMMUNICATION_SERVER_PORT_IF"></span>


If the minifilter driver previously opened a kernel-mode communication server port by calling [**FltCreateCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatecommunicationport), it must close the port by calling [**FltCloseCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltclosecommunicationport). To prevent the system from hanging during the unload process, the minifilter driver's [**FilterUnloadCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_filter_unload_callback) routine must close this port before calling [**FltUnregisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltunregisterfilter).

If a user-mode application has an open connection to the communication server port, any client port for that connection will remain open after [**FltCloseCommunicationPort**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltclosecommunicationport) returns. However, the filter manager will close any client ports when the minifilter driver is unloaded.

 

