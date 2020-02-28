---
title: Implementing NDKPI Functions
description: An NDK-capable miniport driver must register entry points for all NDK_FN_XXX callback functions. All of the NDKPI provider callback functions are mandatory; none are optional.
ms.assetid: 9A7D5F77-C26A-47B6-9F8E-ECB80D4FF384
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing NDKPI Functions


An NDK-capable miniport driver must register entry points for all [NDK\_FN\_*XXX* callback functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/_netvista/). All of the NDKPI provider callback functions are mandatory; none are optional.

To register support for these functions, the miniport driver stores their entry points in the structures listed in the "Object's Dispatch Table" column of the following table:

| Object Type                                               | Created By This Function                                                                                                       | Object's Dispatch Table                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**NDK\_ADAPTER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_adapter)                  | [*OPEN\_NDK\_ADAPTER\_HANDLER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndisndk/nc-ndisndk-open_ndk_adapter_handler)                                                             | [**NDK\_ADAPTER\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_adapter_dispatch)                  |
| [**NDK\_CONNECTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector)              | [*NDK\_FN\_CREATE\_CONNECTOR*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_connector)                                                               | [**NDK\_CONNECTOR\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_connector_dispatch)              |
| [**NDK\_CQ**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq)                            | [*NDK\_FN\_CREATE\_CQ*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_cq)                                                                             | [**NDK\_CQ\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_cq_dispatch)                            |
| [**NDK\_LISTENER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener)                | [*NDK\_FN\_CREATE\_LISTENER*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_listener)                                                                 | [**NDK\_LISTENER\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_listener_dispatch)                |
| [**NDK\_MR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr)                            | [*NDK\_FN\_CREATE\_MR*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_mr)                                                                             | [**NDK\_MR\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mr_dispatch)                            |
| [**NDK\_MW**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw)                            | [*NDK\_FN\_CREATE\_MW*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_mw)                                                                             | [**NDK\_MW\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_mw_dispatch)                            |
| [**NDK\_PD**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_pd)                            | [*NDK\_FN\_CREATE\_PD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_pd)                                                                             | [**NDK\_PD\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_pd_dispatch)                            |
| [**NDK\_QP**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp)                            | [*NDK\_FN\_CREATE\_QP*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_qp) or [*NDK\_FN\_CREATE\_QP\_WITH\_SRQ*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_qp_with_srq)   | [**NDK\_QP\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_qp_dispatch)                            |
| [**NDK\_SHARED\_ENDPOINT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint) | [*NDK\_FN\_CREATE\_SHARED\_ENDPOINT*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_shared_endpoint)                                                  | [**NDK\_SHARED\_ENDPOINT\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_shared_endpoint_dispatch) |
| [**NDK\_SRQ**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq)                          | [*NDK\_FN\_CREATE\_SRQ*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_srq) or [*NDK\_FN\_CREATE\_QP\_WITH\_SRQ*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_create_qp_with_srq) | [**NDK\_SRQ\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndkpi/ns-ndkpi-_ndk_srq_dispatch)                          |

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






