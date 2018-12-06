---
title: Porting CoNDIS Client Registration
description: Porting CoNDIS Client Registration
ms.assetid: 0e828bda-9474-4c7c-a513-346a313c9901
keywords:
- registering CoNDIS drivers
- entry points WDK networking
- registration porting WDK CoNDIS
- porting CoNDIS drivers WDK networking , registration
- client registration WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Client Registration





In NDIS 5.*x*, protocol drivers register CoNDIS client *ProtocolXxx* functions by calling the [**NdisClOpenAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff550895) function.

In NDIS 6.0, protocol drivers must instead call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function. A protocol driver initializes an [**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564884) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

NDIS 6.0 protocol drivers do not call [**NdisClOpenAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff550895). Instead, they call the [**NdisClOpenAddressFamilyEx**](https://msdn.microsoft.com/library/windows/hardware/ff561639) function to open an address family.

For more information about CoNDIS client registration, see [CoNDIS Client Registration](condis-client-registration.md).

 

 





