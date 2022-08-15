---
title: Waits and APCs
description: Waits and APCs
keywords: ["kernel dispatcher objects WDK , alerts", "dispatcher objects WDK kernel , alerts", "APCs WDK kernel", "alerts WDK kernel", "kernel dispatcher objects WDK , APCs", "dispatcher objects WDK kernel , APCs", "Alertable parameter", "WaitMode parameter", "kernel dispatcher objects WDK , waiting for", "dispatcher objects WDK kernel , waiting for"]
ms.date: 07/22/2021
---

# Waits and APCs

Threads that wait for a dispatcher object on behalf of a user-mode caller must be prepared for that wait to be interrupted, either by a user APC or by thread termination. When a thread calls [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject), [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects), **KeWaitForMutexObject**, or [**KeDelayExecutionThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kedelayexecutionthread), the operating system can place the thread in a wait state. Typically, the thread remains in the wait state until the operating system can complete the operation that the caller requests. However, if the caller specifies *WaitMode* = UserMode, the operating system might interrupt the wait. In that case, the routine exits with an NTSTATUS value of STATUS\_USER\_APC.

Any driver that calls one of the preceding four routines with *WaitMode* = UserMode must be prepared to receive a return value of STATUS\_USER\_APC. The driver must complete its current operation with STATUS\_USER\_APC and return control to user mode.

The exact situations in which the operating system interrupts the wait depends on the value of the *Alertable* parameter of the routine. If *Alertable* = **TRUE**, the wait is an alertable wait. Otherwise, the wait is a non-alertable wait. The operating system interrupts alertable waits only to deliver a user APC. The operating system interrupts both kinds of waits to terminate the thread.

The following table explains the relationship between different parameter settings, waits, and user APC delivery.

| Parameters | Wait interrupted? | User APC delivered? |
|--|--|--|
| *Alertable* = **TRUE** *WaitMode* = **UserMode** | Yes | Yes |
| *Alertable* = **TRUE** *WaitMode* = **KernelMode** | Yes | No |
| *Alertable* = **FALSE** *WaitMode* = **UserMode** | Yes, for thread termination. No, for user APCs. | No |
| *Alertable* = **FALSE** *WaitMode* = **KernelMode** | No | No |

You can disable kernel APCs for a thread. If you do disable kernel APCs for a thread, both user APC delivery and thread termination for that thread are also disabled. For more information about how to disable APCs, see [Disabling APCs](disabling-apcs.md).

Alerts, a seldom-used mechanism that are internal to the operating system, can also interrupt alertable wait states. An alert can interrupt a wait when *Alertable* = **TRUE**, regardless of the value of the *WaitMode* parameter. The waiting routine returns a value of STATUS\_ALERTED.

Note that kernel APCs run preemptively, and do not cause **KeWaitFor*Xxx*** or **KeDelayExecutionThread** to return. The system interrupts and resumes the wait internally. Drivers are normally unaffected by this process, but it is possible for the driver to miss a dispatcher object signal for a transient condition, such as a call to [**KePulseEvent**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kepulseevent).
