---
title: Losing and Regaining Packet Data Service
description: Losing and Regaining Packet Data Service
ms.assetid: 1e9d6c34-f7fc-47e9-aa52-409b9e9ff4f4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Losing and Regaining Packet Data Service


The following diagram shows the process that miniport drivers should follow when they lose signal strength and packet service for various intervals. The labels in bold are OID identifiers or transactional flow control, and the labels in regular text are the important flags within the OID structure.

![diagram illustrating losing and regaining signals for packet data service](images/wwanregainingpacketdataservice.png)

To regain packet data service after it has been lost, use the following procedure:

1.  The miniport driver sends NDIS\_WWAN\_LINK\_STATE to the MB Service.

2.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567931) to the MB Service.

3.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567931) to the MB Service.

4.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567931) to the MB Service.

5.  The miniport driver sends NDIS\_WWAN\_REGISTER\_STATE to the MB Service.

6.  The miniport driver sends [**NDIS\_STATUS\_WWAN\_PACKET\_SERVICE**](https://msdn.microsoft.com/library/windows/hardware/ff567850) to the MB Service.

7.  The miniport driver sends [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) to the MB Service.

8.  The miniport driver sends [**NDIS\_WWAN\_SIGNAL\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567931) to the MB Service.

 

 





