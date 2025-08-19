---
title: Kernel-Mode Testing of WDDM Features
description: Describes how to test and validate drivers that don't support D3D runtimes.
keywords:
- WDDM kernel-mode testing
- kernel-mode testing without D3D runtimes
ms.date: 06/17/2024
ms.topic: concept-article
---

# Kernel-mode testing of WDDM features

This article describes the design of the kernel-mode testing infrastructure in WDDM that was added in Windows 11 version 24H2 (WDDM 3.2). This infrastructure allows testing and validation of drivers that don't support D3D runtimes, such as drivers for some NPU devices. It can also be used to validate drivers that do support D3D runtimes without involving the D3D runtime.

## Overview

There are scenarios where new compute devices based on WDDM or [MCDM](mcdm.md) are introduced and drivers for these devices don't support D3D runtimes. To help validate such drivers, functionality is added to *Dxgkrnl* to do validation using kernel-mode thunks only; that is, without involving the D3D runtime and user-mode driver (UMD).

This infrastructure also allows testing of the WDDM feature using precise settings without having to go through a D3D runtime or a UMD, which can complicate things.

DDIs are introduced to build a command buffer in kernel mode for a given set of commands. The commands are simple, so almost any execution node should be able to execute them using precompiled shaders or other means.

To support this functionality, the kernel-mode driver (KMD) must provide the following support:

* Report that the [**DXGK_FEATURE_KERNEL_MODE_TESTING**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_id) feature is enabled.
* Implement the [**DXGKDDI_KERNELMODETESTINGINTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkddi_kernelmodetestinginterface) feature interface.
* Provide information about which execution node supports building and execution of the test command buffers.
* Support creation of a context/hardware queue without private driver data. Usually the format of private driver commands is needed to submit a workload to a device. The test interface allows workload submission without private driver data.
* Support execution of command buffers built by [**pfnBuildTestCommandBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildtestcommandbuffer) on any node of the device that supports the feature.
* Support a NULL allocation handle in paging DDIs (TRANSFER, FILL, etc.).

This feature is used only when [test-signing](../install/introduction-to-test-signing.md) is enabled on the machine.

HLK tests that use this feature will be developed.

## DDI changes

The following structures and enumeration were updated to support kernel-mode testing:

* **DXGK_FEATURE_KERNEL_MODE_TESTING** is added to the [**DXGK_FEATURE_ID**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_id) enumeration.

* **SupportBuildTestCommandBuffer** is added to the [**DXGK_NODEMETADATA_FLAGS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_nodemetadata_flags) structure.

* **TestContext** is added to the [**DXGK_CREATECONTEXTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createcontextflags) structure.

* **TestQueue** is added to the [**D3DDDI_CREATEHWQUEUEFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_createhwqueueflags) structure.

The following DDIs, structures, and enumeration are added to support kernel-mode testing:

* The [**DXGKDDI_KERNELMODETESTINGINTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkddi_kernelmodetestinginterface) feature interface is added, with [**DXGKDDI_BUILDTESTCOMMANDBUFFER::pfnBuildTestCommandBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildtestcommandbuffer) as the only interface member.

* [**DXGKARG_BUILDTESTCOMMANDBUFFER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_buildtestcommandbuffer)

* [**D3DDDI_BUILDTESTCOMMANDBUFFERFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-d3dddi_buildtestcommandbufferflags)

* [**D3DDDI_TESTCOMMANDBUFFER**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-d3dddi_testcommandbuffer)

* [**D3DDDI_TESTCOMMANDBUFFEROP**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-d3dddi_testcommandbufferop)

* [**D3DDDI_TESTCOMMANDBUFFER_COPY**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-d3dddi_testcommandbuffer_copy)

* [**D3DDDI_TESTCOMMANDBUFFER_FILL**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-d3dddi_testcommandbuffer_fill)

## Reporting support for the kernel-mode testing feature

The OS calls KMD's [**DxgkDdiQueryFeatureSupport**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryfeaturesupport) function with the added **DXGK_FEATURE_KERNEL_MODE_TESTING** feature ID to check if the driver supports kernel-mode testing. The KMD needs to report that the feature is supported.

The system then calls [**DxgkDdiQueryFeatureInterface**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryfeatureinterface) with the same feature ID to get the interface function pointer for **pfnBuildTestCommandBuffer**. KMD must implement this function and provide its pointer for the [**DXGKDDI_KERNELMODETESTINGINTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkddi_kernelmodetestinginterface) interface.

## Reporting execution nodes that support kernel-mode testing

**SupportBuildTestCommandBuffer** is added to the [**DXGK_NODEMETADATA_FLAGS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_nodemetadata_flags) structure. KMD must set this flag to indicate that the node can execute command buffers built by [**pfnBuildTestCommandBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildtestcommandbuffer). It is recommended that as many nodes as possible support the feature.

## Creating a context without private data

**TestContext** is added to [**DXGK_CREATECONTEXTFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createcontextflags) to indicate that a context is a testing context. This flag has an effect only when test signing is enabled.

KMD's [**DxgkDdiCreateContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcontext) should support creation of a context without private data for every node that supports execution of command buffers produced by [**pfnBuildTestCommandBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildtestcommandbuffer). To indicate this support, set the **TestContext** flag in [**Flags**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createcontext) during context creation.

## Creating a hardware queue without driver private data

**TestQueue** is added to [**D3DDDI_CREATEHWQUEUEFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_createhwqueueflags) to indicate that a hardware queue is a testing queue. This flag has an effect only when test signing is enabled.

KMD's [**DxgkDdiCreateHwQueue**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createhwqueue) should support creation of a hardware queue without driver private data.

## Building a command buffer

KMD's [**pfnBuildTestCommandBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildtestcommandbuffer) builds a command buffer with device-specific instructions for a set of simple commands. KMD returns a pointer to this function from [**DxgkDdiQueryFeatureInterface**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryfeatureinterface)(DXGK_FEATURE_KERNEL_MODE_TESTING).

A single test command is submitted to **pfnBuildTestCommandBuffer**. The following commands are currently supported:

| Command | Description |
| ------- | ----------- |
| [**D3DDDI_TESTCOMMAND_COPY**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-d3dddi_testcommandbuffer_copy) | Copies bytes using source and destination GPU virtual addresses. |
| [**D3DDDI_TESTCOMMANDBUFFER_FILL**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-d3dddi_testcommandbuffer_fill) | Fills a memory location with a pattern. |

Test commands are based on using GPU virtual addresses. The OS guarantees that the GPU VAs are mapped to allocations created with a [standard allocation type](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_d3dkmt_standardallocationtype) of **D3DKMT_STANDARDALLOCATIONTYPE_EXISTINGHEAP** or **D3DKMT_STANDARDALLOCATIONTYPE_INTERNALBACKINGSTORE**.

The generated command buffer and private data are returned back to user mode. When the command buffer is submitted for execution, the call is coming from user mode. A malicious application could change the content of the buffer and the private data. It's KMD's responsibility to validate both the command buffer and the private driver data to avoid bugchecks.

The generated command buffer shouldn't contain privileged instructions.

A user-mode client driver (for example, Cuda) submits the generated command buffer for execution using [**D3DKMTSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtsubmitcommand) or [**D3DKMTSubmitCommandToHwQueue**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtsubmitpresentblttohwqueue). In the future, the buffer content will be submitted as part of user-mode submission.

When a generated command buffer is submitted for execution, it's guaranteed that the command buffer contains device instructions for a single test command.

The generated command buffer is submitted to the node that corresponds to the **hContext** passed to [**pfnBuildTestCommandBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildtestcommandbuffer).

The size of the DMA buffer (**pDmaBuffer**) is limited to 4 KB and the size of the DMA private driver data (**pDmaBufferPrivateData**) is limited to 1 KB.
