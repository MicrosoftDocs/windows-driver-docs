---
title: Using __sdv_save_adapter_context to Track Adapter Context Fields
description: Using __sdv_save_adapter_context to Track Adapter Context Fields
ms.assetid: b43d7ef5-0464-4e07-a5ec-9d7d8a55479e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using \_\_sdv\_save\_adapter\_context to Track Adapter Context Fields


When NDIS calls a miniport driver's *MiniportInitializeEx* callback function to initialize a miniport adapter, the driver creates its own internal data structure to represent the miniport adapter. The driver uses this structure, known as the *miniport adapter context*, to maintain device-specific state information that the driver needs in order to manage the miniport adapter. The driver passes a handle to this structure to NDIS.

When NDIS calls one of the miniport driver's *MiniportXxx* functions that relates to a miniport adapter, NDIS passes the miniport adapter context to identify the correct miniport adapter to the driver. The miniport adapter context is owned and maintained by the miniport driver and is opaque to NDIS and to protocol drivers.

Because the miniport adapter context maintains the state of the miniport driver between NDIS calls, Static Driver Verifier (SDV) must be able to identify the pointer to this structure. To enable SDV to track the state of the miniport driver, you must save the handle to the miniport adapter context by using the **\_\_sdv\_save\_adapter\_context** function.

The **\_\_sdv\_save\_adapter\_context** function has the following syntax:

```
__sdv_save_adapter_context( &adapter_context ) 
```

Where adapter\_context is the handle to the miniport adapter context that is defined by the miniport driver. This function should be called only one time in the context of a miniport driver.

The **\_\_sdv\_save\_adapter\_context** function is only used by the static analysis tools. This function is ignored by the compiler.

The following code example shows when to call \_\_sdv\_save\_adapter\_context and how SDV will track the information in the *miniport adapter context*.

The following code example shows a simplified version of the miniport adapter context sample structure, MP\_Adapter.

```
typedef struct _MP_ADAPTER
{
    NDIS_HANDLE             AdapterHandle;

    BOOLEAN                 InterruptRegistered;
    NDIS_HANDLE             InterruptHandle;

    /* ..................... */

} MP_ADAPTER, *PMP_ADAPTER;
```

During the execution of *MiniportInitializeEx*, the memory for the MP\_ADAPER structure is allocated. Immediately following the memory allocation, **\_\_sdv\_save\_adapter\_context** is called.

You must call the **\_\_sdv\_save\_adapter\_context** function as soon as you have a valid pointer to the miniport adapter context structure.

```
NDIS_STATUS 
MPInitialize(
    IN  NDIS_HANDLE                        MiniportAdapterHandle,
    IN  NDIS_HANDLE                        MiniportDriverContext,
    IN  PNDIS_MINIPORT_INIT_PARAMETERS     MiniportInitParameters
    )
{
    NDIS_STATUS     Status = NDIS_STATUS_SUCCESS;
    PMP_ADAPTER     pAdapter = NULL;
 
    /* ..................... */
 
    do
    {
   // allocate the memory for the AdapterContext
        pAdapter = NdisAllocateMemoryWithTagPriority(
            MiniportAdapterHandle,
            sizeof(MP_ADAPTER),
            NIC_TAG,
            LowPoolPriority
            );

   // save the adapter context, even before we check whether it is NULL or not 
 __sdv_save_adapter_context(&pAdapter);

        if (pAdapter == NULL)
        {
            Status = NDIS_STATUS_RESOURCES;
            break;
        }
 
        NdisZeroMemory(pAdapter, sizeof(MP_ADAPTER));
 
        pAdapter->AdapterHandle = MiniportAdapterHandle;
        pAdapter->PauseState = NicPaused;

   /* ..................... */
```

The following code example shows how SDV tracks values in the miniport adapter context. In this example, the driver registers an interrupt by calling the miniport-provided function, *MpRegisterInterrupt*. If the call is successful, the driver saves the results into the miniport adapter context (*pAdapter*) field, InterruptRegistered.

```
//
// Register the interrupt
   //
        Status = MpRegisterInterrupt(pAdapter);
        if (Status != NDIS_STATUS_SUCCESS)
        {
            break;
        }
 
   // save the value of the result into the AdapterContext
        pAdapter->InterruptRegistered = TRUE;
```

When the miniport driver has to be halted, NDIS calls the driver's *MiniportHaltEx* function by passing the handle to the miniport adapter context. Because SDV also has this handle, from the earlier call to **\_\_sdv\_save\_adapter\_context**, SDV can track the value of the InterruptRegistered field.

```
VOID MPHalt(
    IN  NDIS_HANDLE             MiniportAdapterContext,
    IN  NDIS_HALT_ACTION        HaltAction
    )
{
    PMP_ADAPTER     pAdapter = (PMP_ADAPTER) MiniportAdapterContext;
 
    /* ..................... */

    if (pAdapter->InterruptRegistered)
    {
        NdisMDeregisterInterruptEx(pAdapter->InterruptHandle);
        pAdapter->InterruptRegistered = FALSE;
    }

/* ..................... */
```

 

 





