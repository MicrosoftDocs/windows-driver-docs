---
title: Processing Changer Device-Control Requests
description: Processing Changer Device-Control Requests
ms.assetid: 3ee275c7-f2e4-47db-bd4b-db5c0c8ad399
keywords:
- changer drivers WDK storage , request processing
- storage changer drivers WDK , request processing
- IOCTLs WDK changer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Changer Device-Control Requests


## <span id="ddk_processing_changer_device_control_requests_kg"></span><span id="DDK_PROCESSING_CHANGER_DEVICE_CONTROL_REQUESTS_KG"></span>


A changer miniclass driver does not process IOCTLs directly. Instead, it has a routine that corresponds to each IOCTL handled by the changer class driver.

When the class driver receives a request, it checks parameters and performs a certain amount of preprocessing. It then calls the corresponding changer miniclass driver routine, passing a pointer to the changer device object and to the IRP it received.

The changer miniclass driver performs any device-specific verification that might be required and builds one or more SRBs to send to the system port driver.

If the SRB succeeds, the miniclass driver routine fills in the output parameters involved in the request. Whether the SRB succeeds or fails, the miniclass driver routine typically returns the status it receives from the port driver to the changer class driver.

 

 




