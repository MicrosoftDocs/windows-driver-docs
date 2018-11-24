---
title: USB 802.3 Device Sample
description: USB 802.3 Device Sample
ms.assetid: 647dd493-a7f4-469a-ab2f-f58f9916333d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB 802.3 Device Sample





The following is a sample set of descriptors for a USB Remote NDIS Ethernet Device. It includes a CDC Communication Class interface and a CDC Data Class interface. The Device Descriptor is returned independently. The Configuration descriptor and all following descriptors are returned as a single block in the order shown.

Control messages are sent on the Control endpoint. Notification messages are sent on the Interrupt In endpoint in the CDC Communication Class interface. Data messages are sent on the Bulk In and Bulk Out endpoints in the CDC Data Class interface. String descriptors are not shown.

The Remote NDIS implementation in Windows Millennium Edition assumes that the Communication Class interface precedes the Data Class interface. Vendors should choose this descriptor ordering so that devices initialize correctly on Windows Millennium Edition.

If any portion of this sample contradicts a controlling specification, follow the specification.

 

 





