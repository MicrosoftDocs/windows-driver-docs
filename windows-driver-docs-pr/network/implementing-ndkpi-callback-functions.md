---
title: Implementing NDKPI Functions
description: An NDK-capable miniport driver must register entry points for all NDK_FN_XXX callback functions. All of the NDKPI provider callback functions are mandatory; none are optional.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing NDKPI Functions


An NDK-capable miniport driver must register entry points for all [NDK\_FN\_*XXX* callback functions](/windows-hardware/drivers/ddi/_netvista/). All of the NDKPI provider callback functions are mandatory; none are optional.

To register support for these functions, the miniport driver stores their entry points in the structures listed in the "Object's Dispatch Table" column of the following table:

| Object Type                                               | Created By This Function                                                                                                       | Object's Dispatch Table                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**NDK\_ADAPTER**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_adapter)                  | [*OPEN\_NDK\_ADAPTER\_HANDLER*](/windows-hardware/drivers/ddi/ndisndk/nc-ndisndk-open_ndk_adapter_handler)                                                             | [**NDK\_ADAPTER\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_adapter_dispatch)                  |
| [**NDK\_CONNECTOR**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector)              | [*NDK\_FN\_CREATE\_CONNECTOR*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_connector)                                                               | [**NDK\_CONNECTOR\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector_dispatch)              |
| [**NDK\_CQ**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq)                            | [*NDK\_FN\_CREATE\_CQ*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_cq)                                                                             | [**NDK\_CQ\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq_dispatch)                            |
| [**NDK\_LISTENER**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener)                | [*NDK\_FN\_CREATE\_LISTENER*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_listener)                                                                 | [**NDK\_LISTENER\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener_dispatch)                |
| [**NDK\_MR**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr)                            | [*NDK\_FN\_CREATE\_MR*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_mr)                                                                             | [**NDK\_MR\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr_dispatch)                            |
| [**NDK\_MW**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw)                            | [*NDK\_FN\_CREATE\_MW*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_mw)                                                                             | [**NDK\_MW\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw_dispatch)                            |
| [**NDK\_PD**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_pd)                            | [*NDK\_FN\_CREATE\_PD*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_pd)                                                                             | [**NDK\_PD\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_pd_dispatch)                            |
| [**NDK\_QP**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)                            | [*NDK\_FN\_CREATE\_QP*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_qp) or [*NDK\_FN\_CREATE\_QP\_WITH\_SRQ*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_qp_with_srq)   | [**NDK\_QP\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp_dispatch)                            |
| [**NDK\_SHARED\_ENDPOINT**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint) | [*NDK\_FN\_CREATE\_SHARED\_ENDPOINT*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_shared_endpoint)                                                  | [**NDK\_SHARED\_ENDPOINT\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint_dispatch) |
| [**NDK\_SRQ**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq)                          | [*NDK\_FN\_CREATE\_SRQ*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_srq) or [*NDK\_FN\_CREATE\_QP\_WITH\_SRQ*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_qp_with_srq) | [**NDK\_SRQ\_DISPATCH**](/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq_dispatch)                          |

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](./overview-of-network-direct-kernel-provider-interface--ndkpi-.md)

 

