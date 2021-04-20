---
title: Using a System-Defined Callback Object
description: Using a System-Defined Callback Object
keywords: ["callback objects WDK kernel", "system-defined callback objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using a System-Defined Callback Object





The system defines three callback objects for driver use:

**\\Callback\\SetSystemTime**

**\\Callback\\PowerState**

**\\Callback\\ProcessorAdd**

Drivers that use the system time (for example, file system drivers) might register for the **\\Callback\\SetSystemTime** callback object. This callback provides for notification when the system time changes.

The **\\Callback\\PowerState** callback object provides for notification when one of the following occurs:

-   The system switches from AC to DC power or vice versa.

-   The system power policy changes as the result of a user or application request.

-   A transition to a system sleep or shutdown state is imminent. A driver can request notification so that it can lock code into memory in anticipation of shutdown. Callback routines will be notified before the power manager sends the system set-power IRP.

The **\\Callback\\ProcessorAdd** callback provides notification when a new processor is added to the system.

To use a system-defined callback, a driver initializes an attribute block by calling [**InitializeObjectAttributes**](/windows/win32/api/ntdef/nf-ntdef-initializeobjectattributes) with the callback's name, then opens the callback object ([**ExCreateCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-excreatecallback)), just as for a driver-defined callback. The driver should not request that the callback object be created.

With the handle returned by **ExCreateCallback**, the driver calls [**ExRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exregistercallback) to register a notification routine, passing a pointer to an arbitrary context and a pointer to its routine. A driver can register its callback routine any time. When the specified condition occurs, the system calls the registered callback routine at IRQL&lt;=DISPATCH\_LEVEL.

When the driver no longer requires notification, it should call [**ExUnregisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exunregistercallback) to delete its callback routine from the list of registered callbacks and to remove its reference to the callback object.

 

