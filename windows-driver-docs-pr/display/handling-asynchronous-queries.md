---
title: Handling Asynchronous Queries
description: Handling Asynchronous Queries
ms.assetid: b5e289db-eb9f-46e6-b221-4aa6661a9ce1
keywords: ["asynchronous query operations WDK DirectX 9.0", "query operations WDK DirectX 9.0 , asynchronous"]
---

# Handling Asynchronous Queries


## <span id="ddk_handling_asynchronous_queries_gg"></span><span id="DDK_HANDLING_ASYNCHRONOUS_QUERIES_GG"></span>


A driver handles asynchronous query operations that are received in the [command stream](command-stream.md) of its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function as discussed in the following sequence:

1.  The driver creates resources for a query after it receives a D3DDP2OP\_CREATEQUERY operation code along with a [**D3DHAL\_DP2CREATEQUERY**](https://msdn.microsoft.com/library/windows/hardware/ff545469) structure in the command stream.

2.  The driver starts to process a query after it receives a D3DDP2OP\_ISSUEQUERY operation code along with a [**D3DHAL\_DP2ISSUEQUERY**](https://msdn.microsoft.com/library/windows/hardware/ff545638) structure in the command stream.

3.  If previously submitted queries using the D3DDP2OP\_ISSUEQUERY operation completed, the driver sets the size of the response buffer in the **dwErrorOffset** member of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) structure and sets the **ddrval** member of D3DHAL\_DRAWPRIMITIVES2DATA to D3D\_OK for successful completion. The driver overwrites the command buffer in the incoming [command stream](command-stream.md) with the response buffer in the outgoing stream. The driver sets the [**D3DHAL\_DP2RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/ff545710) structure's **bCommand** member to D3DDP2OP\_RESPONSEQUERY to indicate that responses to previously issued queries are available in the response buffer. Each [**D3DHAL\_DP2RESPONSEQUERY**](https://msdn.microsoft.com/library/windows/hardware/ff545714) in the response buffer is followed by the following data related to the query:

    -   BOOL for D3DQUERYTYPE\_EVENT. Before responding with D3DDP2OP\_RESPONSEQUERY for an event, the driver must ensure that the graphics processing unit (GPU) is finished processing all [**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678) operations that are related to the event. That is, the driver only responds after the event's ISSUE\_END state occurs. Before the driver sets the event to the signaled state (set to **TRUE**), the GPU might be required to perform a flush to ensure that the pixels are finished rasterizing, blts are completed, resources are no longer being used, and so on. The driver must always set the event's BOOL value to **TRUE** when responding.
    -   DWORD for D3DQUERYTYPE\_OCCLUSION. The driver sets this DWORD to the number of pixels for which the z-test passed for all primitives between the begin and end of the query. If the depth buffer is multisampled, the driver determines the number of pixels from the number of samples. However, if the display device is capable of per-multisample z-test accuracy, the conversion to number of pixels should generally be rounded up. An application can then check the occlusion result against 0, to effectively mean "fully occluded." Drivers that convert multisampled quantities to pixel quantities should detect render target multisampling changes and continue to compute the query results appropriately.
    -   [**D3DDEVINFO\_VCACHE**](https://msdn.microsoft.com/library/windows/hardware/ff544702) structure for D3DQUERYTYPE\_VCACHE.

    If the supplied command buffer is too small for the driver to write all the responses, the driver also sends D3DDP2OP\_RESPONSECONTINUE in the outgoing stream.

4.  If the runtime determines that the driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function succeeded (**ddrval** member of D3DHAL\_DRAWPRIMITIVES2DATA set to D3D\_OK), the runtime examines the **dwErrorOffset** member of D3DHAL\_DRAWPRIMITIVES2DATA to determine if responses are available from the driver. This **dwErrorOffset** member is zero if no responses are available; otherwise, **dwErrorOffset** is the size of the response buffer in bytes. Therefore, on success of *D3dDrawPrimitives2* (**ddrval** set to D3D\_OK), the driver must ensure that it only sets **dwErrorOffset** to nonzero when responses are available.

5.  The runtime parses the returned response buffer and updates its internal data structures.

6.  If the driver sent D3DDP2OP\_RESPONSECONTINUE, the runtime submits an empty command buffer in the incoming [command stream](command-stream.md) so that the driver can continue to write more responses. The driver must ensure that it can process empty command buffers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Asynchronous%20Queries%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




