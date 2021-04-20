---
title: I/O Queue Event Callback Functions
description: I/O Queue Event Callback Functions
keywords:
- I/O queues WDK UMDF
- queues WDK UMDF
- callback functions WDK UMDF
- event callback functions WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# I/O Queue Event Callback Functions


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

When drivers create I/O queues, or configure default I/O queues, they can register the following interfaces so that the framework notifies the driver--by calling the methods associated with the interfaces--when events related to the interfaces occur. For more information about I/O queues and creating and configuring I/O queues, see [Framework I/O Queue Object](framework-i-o-queue-object.md).

[IQueueCallbackCreate](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackcreate)

[IQueueCallbackDeviceIoControl](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackdeviceiocontrol)

[IQueueCallbackRead](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackread)

[IQueueCallbackWrite](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackwrite)

[IQueueCallbackDefaultIoHandler](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackdefaultiohandler)

 

