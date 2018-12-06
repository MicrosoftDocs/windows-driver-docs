---
title: Porting CoNDIS Call Manager Registration
description: Porting CoNDIS Call Manager Registration
ms.assetid: 5e88b0d7-e0e0-4d64-87d8-51439366effc
keywords:
- registering CoNDIS drivers
- entry points WDK networking
- registration porting WDK CoNDIS
- porting CoNDIS drivers WDK networking , registration
- call managers WDK networking , registering
- CoNDIS call managers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Call Manager Registration





In NDIS 5.*x*, protocol drivers register CoNDIS call manager *ProtocolXxx* functions by calling the [**NdisCmRegisterAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff551006) function.

In NDIS 6.0, protocol drivers must call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function. The driver initializes an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

NDIS 6.0 protocol drivers do not call [**NdisCmRegisterAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff551006). Instead, they call the [**NdisCmRegisterAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561685) function to open an address family.

For more information about call manager registration, see [CoNDIS Call Manager Registration](condis-call-manager-registration.md).

 

 





