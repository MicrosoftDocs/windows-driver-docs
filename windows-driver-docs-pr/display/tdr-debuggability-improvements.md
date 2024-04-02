---
title: TDR Debuggability Improvements
description: Describes the GPU fence synchronization object that can be used for true GPU-to-GPU synchronization in GPU hardware scheduling stage 2.
keywords:
- WDDM, native GPU fence object
- WDDM, GPU fence synchronization object
- WDDM, hardware scheduling
ms.date: 04/01/2024
---

# TDR debuggability improvements

To aid TDR (timeout detection and recovery) analysis, the OS has historically called into a kernel-mode driver's (KMD) provided[**DxgkddiCollectDbgInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo) callback to allow the driver to write its own payload into the TDR report that's uploaded from the customer machine.

Starting in Windows 11, version 24H2 (WDDM 3.2), the system has added TDR debug improvements, which this article describes. Graphics driver developers should be familiar with GPU timeout detection and recovery in Windows as described in [Timeout detection and recovery](timeout-detection-and-recovery.md) and [TDR in Windows 8 and later](tdr-changes-in-windows-8.md).

## DDI changes

### DxgkddiCollectDbgInfo2

[**DxgkddiCollectDbgInfo2**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo2) is added as a TDR debug extension. This callback allows the OS to pass more detailed information to KMD about the root cause of the TDR. KMD, in turn, can save state that is relevant to the part of the GPU responsible for the TDR.

**DxgkddiCollectDbgInfo2** is a superset to the existing **DxgkddiCollectDbgInfo**.

* A WDDM 3.2 driver isn't required to implement **DxgkddiCollectDbgInfo2**, in which case the OS calls [**DxgkddiCollectDbgInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo).

* If KMD does implement **DxgkddiCollectDbgInfo2**, the OS invokes it instead of **DxgkddiCollectDbgInfo** in all cases.

The [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure is extended to include a pointer to **DxgkddiCollectDbgInfo2**.

### DXGKARG_COLLECTDBGINFO2

The OS passes the added [**DXGKARG_COLLECTDBGINFO2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkarg_collectdbginfo2) structure to [**DxgkddiCollectDbgInfo2**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo2).

The layout of **DXGKARG_COLLECTDBGINFO2** is backwards compatible with the existing [**DXGKARG_COLLECTDBGINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_collectdbginfo) structure to allow the **DxgkDdiCollectDbgInfo2** implementation to re-use existing [**DxgkDdiCollectDbgInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo) helpers as needed. For this reason, the **Reason**, **pBuffer**, **BufferSize**, and **pExtension** fields have the same semantics.

The following additional fields are in **DXGKARG_COLLECTDBGINFO2**, but not in **DXGKARG_COLLECTDBGINFO**.

* [**TdrType**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-dxgk_tdr_type)
* **TdrPayloadSize**
* **TdrPayload**

For some TDR types, the OS provides additional information in the **TdrPayload** buffer of **TdrPayloadSize** bytes. It can be NULL, and the driver is expected to handle this case without crashing.

When the payload isn't NULL, it can be cast to a structure that corresponds to the TDR type. The OS might grow these structures in a backwards compatible manner, adding new fields at the end. The driver must check **TdrPayloadSize** prior to accessing **TdrPayload** fields to make sure the OS implements the desired payload version or later.

Memory that **TdrPayload** points to is only valid for the duration of the [**DxgkddiCollectDbgInfo2**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo2) call. The driver shouldn't store a pointer to **TdrPayload** past the end of **DxgkddiCollectDbgInfo2** call.

Starting in WDDM 3.2, the following payload structures are added as possible payloads for **TdrPayload** to point to.

* [**DXGK_TDR_PAYLOAD_ENGINE_TIMEOUT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_tdr_payload_engine_timeout) for an engine timeout payload (**TdrType** equals DXGK_TDR_TYPE_ENGINE_TIMEOUT).

* [**DXGK_TDR_PAYLOAD_VSYNC_TIMEOUT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_tdr_payload_vsync_timeout) for a VSync timeout payload (**TdrType** equals DXGK_TDR_TYPE_VSYNC_TIMEOUT).
