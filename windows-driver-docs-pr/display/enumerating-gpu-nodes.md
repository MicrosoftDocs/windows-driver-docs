---
title: Enumerating GPU Engine Capabilities
description: Starting in Windows 8.1, a display miniport driver must implement the DxgkDdiGetNodeMetadata function, which is used to query the engine capabilities of a GPU node.
keywords:
- GPU nodes, enumerating WDK Display Drivers
ms.date: 04/20/2017
---

# Enumerating GPU engine capabilities

Starting in Windows 8.1, a display miniport driver must implement the [*DxgkDdiGetNodeMetadata*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata) function, which is used to query the engine capabilities of a GPU node.

This information helps with the evaluation of how workloads are scheduled and distributed among nodes and improves the ability to debug applications.

## Engine capabilities device driver interface (DDI)

This interface provides the engine capabilities of a specified GPU node:

* [*DxgkDdiGetNodeMetadata*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata)
* [**DXGKARG_GETNODEMETADATA**](./index.md)
* [**DXGK_ENGINE_TYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-dxgk_engine_type)

A pointer to the [*DxgkDdiGetNodeMetadata*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata) function is provided by the **DxgkDdiGetNodeMetadata** member of the [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure.

## GPU node architecture

Each display adapter on the system has a number of different engines available to schedule tasks on. Each engine is assigned to only one node, but each node may contain more than one engine if that node is associated with multiple adapters—such as in linked display adapter (LDA) configuration, where multiple physical GPUs are linked to form a single, faster, virtual GPU.

:::image type="content" source="images/gpu-engine-node-architecture.png" alt-text="Diagram showing the architecture of GPU engines and nodes.":::

Different nodes represent the asymmetrical processing cores of the GPU, while the engines within each node represent the symmetrical processing cores across adapters. That is, a 3-D node contains only identical 3-D engines on several adapters, and never a different engine type.

Because the engines are always grouped together in nodes by engine type, the engine type information can be queried based on a specified node. The types of engine that the display miniport driver can specify are listed in the [**DXGK_ENGINE_TYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-dxgk_engine_type) enumeration.

## Example implementation of node metadata function

This code shows how a display miniport driver can implement some of the engine types that can be returned by the [*DxgkDdiGetNodeMetadata*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata) function.

```ManagedCPlusPlus
NTSTATUS
IHVGetNodeDescription(
        IN_CONST_HANDLE                     hAdapter,
        UINT                                NodeOrdinal,
        OUT_PDXGKARG_GETNODEMETADATA        pGetNodeMetadata
        )
{
    DDI_FUNCTION();
    PAGED_CODE();

    if(NULL == pGetNodeMetadata)
    {
        return STATUS_INVALID_PARAMETER;
    }

    CAdapter *pAdapter = GetAdapterFromHandle(hAdapter);

    //Invalid handle
    if(NULL == pAdapter)
    {
        return STATUS_INVALID_PARAMETER;
    }

    //Node ordinal is out of bounds. Required to return
    //STATUS_INVALID_PARAMETER
    if(NodeOrdinal >= pAdapter->GetNumNodes())
    {
        return STATUS_INVALID_PARAMETER;
    }

    switch(pAdapter->GetEngineType(NodeOrdinal))
    {
        //This is the adapter's 3-D engine. This engine handles a large number
        //of different workloads, but it also handles the adapter's 3-D 
        //workloads. Therefore the 3-D capability is what must be exposed.
        case GPU_ENGINE_3D:
        {
            pGetNodeMetadata->EngineType = DXGK_ENGINE_TYPE_3D;
            break;
        }

        //This is the adapter's video decoding engine
        case GPU_ENGINE_VIDEO_DECODE:
        {
            pGetNodeMetadata->EngineType = DXGK_ENGINE_TYPE_VIDEO_DECODE;
            break;
        }

        //This engine is proprietary and contains no functionality that
        //fits the DXGK_ENGINE_TYPE enumeration
        case GPU_ENGINE_PROPRIETARY_ENGINE_1:
        {
            pGetNodeMetadata->EngineType = DXGK_ENGINE_TYPE_OTHER;

            //Copy over friendly name associated with this engine
            SetFriendlyNameForEngine(pGetNodeMetadata->FriendlyName,
                                     DXGK_MAX_METADATA_NAME_LENGTH,
                                     PROPRIETARY_ENGINE_1_NAME);
            break;
        }
    }

    return STATUS_SUCCESS;
}
```
