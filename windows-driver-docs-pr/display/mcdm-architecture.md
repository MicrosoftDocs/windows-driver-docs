---
title: MCDM architecture
description: Microsoft Compute Driver Model architecture
ms.date: 01/06/2023
---

# MCDM architecture

This article describes Microsoft Compute Driver Model (MCDM) architectural concepts. An MCDM driver, or compute-only driver, has both a kernel-mode driver (*.sys* driver) and a user-mode dynamic link library (DLL).

See also:

* [Microsoft Compute Driver Model overview](mcdm.md)
* [MCDM KM driver implementation guidelines](mcdm-implementation-guidelines.md)
* [WDDM operation flow](windows-vista-and-later-display-driver-model-operation-flow.md)

## Command Queue

A **Command Queue** is a [**DirectCompute**](/windows/win32/direct3d11/direct3d-11-advanced-stages-compute-shader) construct used for the submission of work. The driver is responsible for creating one or more **Contexts** which it will use to carry out the execution of the submitted work. The driver is responsible for turning work expressed through calls to its DDI into **DMA Buffers** which it then submits to a **Context** for execution.

## Context

A **Context** is a queue of computational work submitted by a driver targeting an **Engine** with instance-specific state. The computational work is expressed as **DMA Buffers** which are held in a **SW Queue** awaiting submission to the **Engine**.

## SW Queue

**DMA Buffers** submitted for execution to a context are held in a **SW Queue**. A **SW Queue**'s length is bounded only by resources. There's a one-to-one association between a **Context** and its corresponding **SW Queue**. It's the responsibility of the **Scheduler** to remove **DMA Buffers** from the **SW Queue** and submit the buffers to the appropriate **Engine** which in turns places the buffer on its own **HW Queue**.

## Scheduler

The **Scheduler** is implemented by the OS and the driver has no control over this scheduling.

The **Scheduler** is responsible for scheduling the enqueued work in **SW Queues** which target **Engines**. It ensures fair use of limited **Engine** resources across all **SW Queues** and will preempt work as needed to ensure this fairness and to ensure that higher priority work completes in a timely manner.

When the **Scheduler** preempts work, it's responsible for re-enqueuing as appropriate the work that was preempted.

## Engine

An **Engine** executes the necessary actions to complete the work expressed in a sequence of **DMA Buffers**. Each **DMA Buffer** is executed in a given **Context** and **Address Space**. The **Engine** must indicate when the execution of a **DMA Buffer** is complete and these indications must be given in the same order in which the **DMA Buffers** were received.

It's expected that an **Engine** is able to make forward progress independently in the absence of explicit or implicit dependencies expressed in the **DMA Buffers**. If two or more **Engines** exist, they'll be scheduled with the assumption that each **Engine's** work will proceed in a timely manner and without impairment of work conducted in other **Engines**.

Since a **DMA Buffer** is executed with a given **Address Space**, multiple **Engines** can only be supported if each **Engine** is capable of executing **DMA Buffers** in different **Address Spaces**.

A driver determines how many **Engines** it reports and how these **Engines** are used by the **Context** it creates.

## HW Queue

An **Engine** will be given a sequence of **DMA Buffers** which are conceptually placed in a queue called the **HW Queue**. Currently, this queue is only filled with at most two **DMA Buffer** entries. An **Engine** must complete the **DMA Buffers** in the order of submission.

## Preemption

An **Engine** must be capable of preemption, allowing the execution of partially completed **DMA Buffers** to be interrupted or canceled.

When requested to preempt outstanding work, an **Engine** must minimally support the completion of any partially completed **DMA Buffers** and cancel all **DMA Buffers** that aren't yet started.

The indication of completion or preemption of **DMA Buffers** must still be done in the order in which the **DMA Buffers** were submitted. If a **DMA Buffer** is preempted, all subsequent **DMA Buffers** (currently at most one other buffer) are also preempted.

If a **DMA Buffer** is partially executed, the driver must save enough information for the resumption of its execution.

## DMA Buffer

The driver converts work submitted via calls to its DDI into **DMA Buffers** which are then submitted for execution. An **Engine** executes the necessary actions to complete the work expressed in a sequence of **DMA Buffers**. Each **DMA Buffer** is executed in a given **Context** and **Address Space**. The **Engine** must indicate when the execution of a **DMA Buffer** is complete and these indications must be given in the same order in which the **DMA Buffers** were received.

## Address Space

An **Address Space** is used to map virtual device addresses to physical device addresses. A single **Address Space** is used for each host side process.

**Engines** are a shared resource across processes and thus must support switching between **Address Spaces** as **DMA Buffers** are executed from different processes.

Devices that support only one **Address Space** must be restricted in how they're used. Only one process at time will be allowed to use the device. While one process is using the device, all
attempts by other processes to access the device will fail. Devices that can only support access by a single process are referred to as **Single Use** devices.

An **Address Space** is specified by a single pointer to the root page table of the address space. A change to a different address space requires only specifying a different root page table address.

An address space page table is managed by the OS. To make changes to the page table, the OS makes requests to the driver to record these changes into **DMA Buffers** which are later submitted to the
appropriate engine at the appropriate time.
