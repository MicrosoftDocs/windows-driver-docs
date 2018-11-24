---
title: Implementing NDKPI Functions
description: An NDK-capable miniport driver must register entry points for all NDK_FN_XXX callback functions. All of the NDKPI provider callback functions are mandatory; none are optional.
ms.assetid: 9A7D5F77-C26A-47B6-9F8E-ECB80D4FF384
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing NDKPI Functions


An NDK-capable miniport driver must register entry points for all [NDK\_FN\_*XXX* callback functions](https://msdn.microsoft.com/library/windows/hardware/jj206453). All of the NDKPI provider callback functions are mandatory; none are optional.

To register support for these functions, the miniport driver stores their entry points in the structures listed in the "Object's Dispatch Table" column of the following table:

| Object Type                                               | Created By This Function                                                                                                       | Object's Dispatch Table                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**NDK\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/hh439848)                  | [*OPEN\_NDK\_ADAPTER\_HANDLER*](https://msdn.microsoft.com/library/windows/hardware/hh440105)                                                             | [**NDK\_ADAPTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439850)                  |
| [**NDK\_CONNECTOR**](https://msdn.microsoft.com/library/windows/hardware/hh439852)              | [*NDK\_FN\_CREATE\_CONNECTOR*](https://msdn.microsoft.com/library/windows/hardware/hh439872)                                                               | [**NDK\_CONNECTOR\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439853)              |
| [**NDK\_CQ**](https://msdn.microsoft.com/library/windows/hardware/hh439854)                            | [*NDK\_FN\_CREATE\_CQ*](https://msdn.microsoft.com/library/windows/hardware/hh439873)                                                                             | [**NDK\_CQ\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439855)                            |
| [**NDK\_LISTENER**](https://msdn.microsoft.com/library/windows/hardware/hh439918)                | [*NDK\_FN\_CREATE\_LISTENER*](https://msdn.microsoft.com/library/windows/hardware/hh439874)                                                                 | [**NDK\_LISTENER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439919)                |
| [**NDK\_MR**](https://msdn.microsoft.com/library/windows/hardware/hh439922)                            | [*NDK\_FN\_CREATE\_MR*](https://msdn.microsoft.com/library/windows/hardware/hh439875)                                                                             | [**NDK\_MR\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439924)                            |
| [**NDK\_MW**](https://msdn.microsoft.com/library/windows/hardware/hh439926)                            | [*NDK\_FN\_CREATE\_MW*](https://msdn.microsoft.com/library/windows/hardware/hh439876)                                                                             | [**NDK\_MW\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439927)                            |
| [**NDK\_PD**](https://msdn.microsoft.com/library/windows/hardware/hh439931)                            | [*NDK\_FN\_CREATE\_PD*](https://msdn.microsoft.com/library/windows/hardware/hh439877)                                                                             | [**NDK\_PD\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439932)                            |
| [**NDK\_QP**](https://msdn.microsoft.com/library/windows/hardware/hh439933)                            | [*NDK\_FN\_CREATE\_QP*](https://msdn.microsoft.com/library/windows/hardware/hh439878) or [*NDK\_FN\_CREATE\_QP\_WITH\_SRQ*](https://msdn.microsoft.com/library/windows/hardware/hh439880)   | [**NDK\_QP\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439934)                            |
| [**NDK\_SHARED\_ENDPOINT**](https://msdn.microsoft.com/library/windows/hardware/hh439937) | [*NDK\_FN\_CREATE\_SHARED\_ENDPOINT*](https://msdn.microsoft.com/library/windows/hardware/hh439882)                                                  | [**NDK\_SHARED\_ENDPOINT\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439938) |
| [**NDK\_SRQ**](https://msdn.microsoft.com/library/windows/hardware/hh439939)                          | [*NDK\_FN\_CREATE\_SRQ*](https://msdn.microsoft.com/library/windows/hardware/hh439883) or [*NDK\_FN\_CREATE\_QP\_WITH\_SRQ*](https://msdn.microsoft.com/library/windows/hardware/hh439880) | [**NDK\_SRQ\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/hh439940)                          |

 

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






