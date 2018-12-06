---
title: Porting CoNDIS MCM Registration
description: Porting CoNDIS MCM Registration
ms.assetid: 996eb9a5-6ba3-4f37-823a-767a5b7663e7
keywords:
- CoNDIS drivers WDK networking , registering CoNDIS drivers
- connection-oriented drivers WDK networking , registering CoNDIS drivers
- registering CoNDIS drivers WDK networking
- miniport drivers WDK networking , CoNDIS registration
- NDIS miniport driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS MCM Registration





In NDIS 5.*x*, miniport call managers (MCMs) specify CoNDIS *MiniportXxx* functions when they call the [**NdisMRegisterMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff553602) function during driver registration.

In NDIS 6.0, MCMs register CoNDIS *MiniportXxx* functions by calling the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. In *MiniportSetOptions*, an MCM initializes an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

In NDIS 5.*x*, MCMs register CoNDIS call manager *ProtocolXxx* functions by calling the [**NdisMCmRegisterAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff553429) function.

In NDIS 6.0, MCMs must call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. The MCM initializes an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

NDIS 6.0 MCMs do not call [**NdisMCmRegisterAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff553429). Instead, call the [**NdisMCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff563554) function to register an address family.

For more information about MCM registration, see [CoNDIS MCM Registration](condis-mcm-registration.md).

 

 





