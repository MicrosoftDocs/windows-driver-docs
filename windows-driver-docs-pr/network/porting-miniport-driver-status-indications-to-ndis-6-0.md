---
title: Porting Miniport Driver Status Indications to NDIS 6.0
description: Porting Miniport Driver Status Indications to NDIS 6.0
ms.assetid: f502bd7d-adef-44a9-9ac6-8bb9dba1ca33
keywords:
- NDIS miniport drivers WDK networking , status indications
- miniport drivers WDK networking , status indications
- porting miniport drivers WDK networking , status indications
- status indications WDK networking , porting
- porting status indications WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Status Indications to NDIS 6.0





The [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function replaces the [**NdisMIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff553538) and [**NdisMIndicateStatusComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553540) functions. Status indication parameters are packaged within an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that contains the source handle, status code, buffer, and size.

The initialization of status indication structure is shown in the following example.

```cpp
StatusIndication.Header.Type = NDIS_OBJECT_TYPE_STATUS_INDICATION;
StatusIndication.Header.Revision = NDIS_STATUS_INDICATION_REVISION_1;
StatusIndication.Header.Size = sizeof(NDIS_STATUS_INDICATION);
StatusIndication.SourceHandle = Adapter->AdapterHandle;
StatusIndication.StatusCode = NDIS_STATUS_LINK_STATE;
StatusIndication.StatusBuffer = (PVOID)&LinkState;
StatusIndication.StatusBufferSize = sizeof(LinkState);
```

 

 





