---
title: Boot-Time Global Logger Session
description: Boot-Time Global Logger Session
ms.assetid: f1f5bbee-48bd-4e4d-8849-9d21a4f85d44
keywords: ["boot-time tracing WDK , Global Logger trace session", "Global Logger trace session WDK", "boot-time Global Logger trace session WDK", "Global Logger trace session WDK , about Global Logger sessions", "boot-time Global Logger trace session WDK , about Global Logger sessions", "tracing WDK , during boot"]
---

# Boot-Time Global Logger Session


You can create a Global Logger trace session that traces Windows kernel events during system boot. This method combines the features of the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md), which traces the kernel, with those of the [Global Logger trace session](global-logger-trace-session.md), which traces events that take place during system boot.

The procedure described in this section creates a Global Logger trace session, and then adds a special registry entry, **EnableKernelFlags**. The presence of the **EnableKernelFlags** entry, with a valid value, converts the Global Logger trace session to an NT Kernel Logger trace session. The valid values for **EnableKernelFlags** are taken from the values of the **EnableFlags** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure. The procedure is described in [How to Create a Boot-Time Global Logger Session](how-to-create-a-boot-time-global-logger-session.md).

Trace providers, including drivers, can log trace messages to this type of session. The procedure for doing so is described in [Logging to the Global Logger Session](logging-to-the-global-logger-session.md).

This section includes:

[How to Create a Boot-Time Global Logger Session](how-to-create-a-boot-time-global-logger-session.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Boot-Time%20Global%20Logger%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




