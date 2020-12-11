---
title: Handling Multiple Locks
description: Handling Multiple Locks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Multiple Locks


With the Direct3D runtime, you can allow vertex and index buffers to have more than one lock outstanding. User-mode display drivers must handle multiple locks the same way as the runtime in the [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md).

A user-mode display driver must not fail a call to its [**LockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lockasync) function for a resource that is already locked. That is, the driver cannot fail any calls to its *LockAsync* function for a particular resource after the first call to its *LockAsync* function succeeds in locking that resource. Similarly, the driver cannot fail any calls to its [**Lock**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lock) function for a particular resource after the first call to its *Lock* function succeeds in locking that resource. The runtime matches each call that it makes to the driver's *LockAsync* function with a call to the driver's [**UnlockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlockasync) function. The runtime also matches each call that it makes to the driver's *Lock* function with a call to the driver's [**Unlock**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlock) function.

The user-mode display driver cannot fail a call to its [**UnlockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlockasync) function unless the resource that the [**D3DDDIARG\_UNLOCKASYNC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_unlockasync) structure describes was not actually locked by a previous call to the driver's *LockAsync* function. Similarly, the driver cannot fail a call to its [**Unlock**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlock) function unless the resource that the [**D3DDDIARG\_UNLOCK**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_unlock) structure describes was not actually locked by a previous call to the driver's *Lock* function. In situations in which the resources were not previously locked, *UnlockAsync* and *Unlock* return E\_INVALIDARG.

 

