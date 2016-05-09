---
title: Closing the Communication Server Port
description: Closing the Communication Server Port
ms.assetid: 43dfa162-0098-4a9b-9272-9da429cb0108
keywords: ["communication server ports WDK file system minifilter", "ports WDK , file system minifilter", "closing communication server ports"]
---

# Closing the Communication Server Port


## <span id="ddk_closing_the_communication_server_port_if"></span><span id="DDK_CLOSING_THE_COMMUNICATION_SERVER_PORT_IF"></span>


If the minifilter driver previously opened a kernel-mode communication server port by calling [**FltCreateCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541931), it must close the port by calling [**FltCloseCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541871). To prevent the system from hanging during the unload process, the minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine must close this port before calling [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606).

If a user-mode application has an open connection to the communication server port, any client port for that connection will remain open after [**FltCloseCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff541871) returns. However, the filter manager will close any client ports when the minifilter driver is unloaded.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Closing%20the%20Communication%20Server%20Port%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




