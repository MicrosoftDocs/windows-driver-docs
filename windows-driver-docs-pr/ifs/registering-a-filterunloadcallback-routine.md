---
title: Registering a FilterUnloadCallback Routine
description: Registering a FilterUnloadCallback Routine
keywords:
- file system minifilter drivers WDK , FilterUnloadCallback routine
- minifilter drivers WDK , FilterUnloadCallback routine
- FilterUnloadCallback
- unload routines WDK file system minifilter
ms.date: 04/20/2017
---

# Registering a FilterUnloadCallback Routine

A file system minifilter driver can optionally register a [**PFLT_FILTER_UNLOAD_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_filter_unload_callback)-typed routine as the minifilter driver's *FilterUnloadCallback* routine. This callback routine is also referred to as the minifilter driver's *unload routine*.

Minifilter drivers are not required to register a *FilterUnloadCallback* routine. However, we strongly recommend that a minifilter driver registers this callback routine, because if a minifilter driver does not register a *FilterUnloadCallback* routine, the driver cannot be unloaded.

To register this callback routine, the minifilter driver stores the address of a PFLT_FILTER_UNLOAD_CALLBACK-typed routine in the **FilterUnloadCallback** member of the [**FLT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure that the minifilter driver passes as a parameter to [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter) in its **DriverEntry** routine.
