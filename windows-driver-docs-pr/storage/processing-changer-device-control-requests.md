---
title: Processing Changer Device-Control Requests
author: windows-driver-content
description: Processing Changer Device-Control Requests
ms.assetid: 3ee275c7-f2e4-47db-bd4b-db5c0c8ad399
keywords: ["changer drivers WDK storage , request processing", "storage changer drivers WDK , request processing", "IOCTLs WDK changer"]
---

# Processing Changer Device-Control Requests


## <span id="ddk_processing_changer_device_control_requests_kg"></span><span id="DDK_PROCESSING_CHANGER_DEVICE_CONTROL_REQUESTS_KG"></span>


A changer miniclass driver does not process IOCTLs directly. Instead, it has a routine that corresponds to each IOCTL handled by the changer class driver.

When the class driver receives a request, it checks parameters and performs a certain amount of preprocessing. It then calls the corresponding changer miniclass driver routine, passing a pointer to the changer device object and to the IRP it received.

The changer miniclass driver performs any device-specific verification that might be required and builds one or more SRBs to send to the system port driver.

If the SRB succeeds, the miniclass driver routine fills in the output parameters involved in the request. Whether the SRB succeeds or fails, the miniclass driver routine typically returns the status it receives from the port driver to the changer class driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Processing%20Changer%20Device-Control%20Requests%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


