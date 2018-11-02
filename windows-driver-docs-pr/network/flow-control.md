---
title: Flow Control
description: Flow Control
ms.assetid: e7a0846e-0999-4e40-83e0-f4877871f1e1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flow Control





Flow control for a USB Remote NDIS device is defined by the USB Specification.

Since all communication on USB is based on a host to device transaction, all the host must do to slow the flow of data is stop issuing IN tokens to the device on the bulk pipe. If the device needs to assert flow control, then it should NAK data transfers from the host until it is able to process data again. For a detailed explanation of this process, review Section 8.4.4 in the USB Specification, version 1.1.

 

 





