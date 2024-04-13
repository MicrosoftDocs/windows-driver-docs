---
title: Supporting Multiple Processors
description: Supporting Multiple Processors
keywords:
- user-mode display drivers WDK Windows Vista , multiple processors
- multiple processor support WDK display
- runtime-handled multiple-processor optimizations WDK display
- driver-handled multiple-processor optimizations WDK display
- multiple-processor optimizations WDK display
ms.date: 04/20/2017
---

# Supporting Multiple Processors


User-mode display drivers on multiple-processor computers can let the Microsoft Direct3D runtime handle multiple-processor optimizations, or the drivers can perform their own multiple-processor optimizations.

### <span id="Runtime-Handled_Multiple-Processor_Optimizations"></span><span id="runtime-handled_multiple-processor_optimizations"></span><span id="RUNTIME-HANDLED_MULTIPLE-PROCESSOR_OPTIMIZATIONS"></span>Runtime-Handled Multiple-Processor Optimizations

The multiple-processor optimizations that are handled by Direct3D runtime are enabled only on drivers that support the [**LockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lockasync), [**UnlockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlockasync), and [**Rename**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_rename) functions. These functions enable the multiple-processor optimizations to work well with applications that frequently lock dynamic resources. The *LockAsync* and *UnlockAsync* functions--along with the [**GetQueryData**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getquerydata) function--must be reentrant on drivers that expose a DDI version of 0x0000000B or greater. The driver returns the DDI-version value in the **DriverVersion** member of the [**D3D10DDIARG\_OPENADAPTER**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_openadapter) structure in a call to the driver's [**OpenAdapter**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openadapter) function. When the runtime calls a driver function in a reentrant manner, one thread can execute inside that function while another thread that references the same display device executes inside of another driver function.

The Direct3D runtime uses multiple-processor optimizations in some situations to offload work to a separate processor and improve computer performance. When multiple-processor optimizations are enabled, an additional software layer is added between the Direct3D runtime and the user-mode display driver. This software layer intercepts all calls that the Direct3D runtime would otherwise make to the user-mode display driver's functions.

Instead of calling the user-mode display driver directly, the software layer queues commands into batches that a worker thread asynchronously processes. However, the software layer cannot batch all calls that are made to the user-mode display driver's functions. In particular, the software layer cannot batch calls to functions that return information (for example, [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource)). When the software layer must call one of these types of driver functions, it flushes all queued commands through the worker thread, and then the software layer calls the driver function on the main application thread.

### <span id="Driver-Handled_Multiple-Processor_Optimizations"></span><span id="driver-handled_multiple-processor_optimizations"></span><span id="DRIVER-HANDLED_MULTIPLE-PROCESSOR_OPTIMIZATIONS"></span>Driver-Handled Multiple-Processor Optimizations

If a driver will perform its own multiple-processor optimizations, it must not implement [**LockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lockasync), [**UnlockAsync**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlockasync), and [**Rename**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_rename) functions. In this situation, the driver must call the [**pfnSetAsyncCallbacksCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setasynccallbackscb) function to notify the runtime whether the runtime will start or stop receiving calls to the runtime's callback functions from a worker thread.

If the driver performs its own multiple-processor optimizations, it should follow the same policy that the Direct3D runtime uses when it determines to enable multiple-processor optimizations. This policy enables fair sharing of system resources across all processes. In particular, the driver should disable multiple-processor optimizations in the following situations:

-   The application runs in windowed mode.

-   The computer contains only one processor (or processor core); the driver should disable optimizations on single-processor computers with hyper-threading.

-   The application requested that no multiple-processor optimizations be enabled, or the application uses software-vertex processing; this information is passed to the driver's [**CreateDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

If vendors want to enable multiple-processor optimizations in one of these situations, they should first contact Microsoft.

 

