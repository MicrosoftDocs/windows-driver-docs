---
title: Storage Class Driver's InterpretRequestSense Routine
author: windows-driver-content
description: Storage Class Driver's InterpretRequestSense Routine
ms.assetid: abfb529d-7fab-40f7-b4cd-e6adb4cf643e
keywords: ["InterpretRequestSense", "request sense WDK storage", "errors WDK storage", "retrying requests WDK storage"]
---

# Storage Class Driver's InterpretRequestSense Routine


## <span id="ddk_storage_class_drivers_interpretrequestsense_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_INTERPRETREQUESTSENSE_ROUTINE_KG"></span>


An *InterpretRequestSense* routine interprets the data returned in the SRB's **SenseInfoBuffer**, determines whether the request should be retried, and, if not, maps the error to an NTSTATUS value for the IRP's I/O status block.

The system port driver indicates whether request-sense information is available by setting SRB\_STATUS\_AUTOSENSE\_VALID or SRB\_STATUS\_REQUEST\_SENSE\_FAILED in **SrbStatus**.

If no request-sense information is available, *InterpretRequestSense* should check the **SrbStatus** value to determine whether to retry a given request or to determine an appropriate mapping to an NTSTATUS value.

The *InterpretRequestSense* routine might call a driver-supplied error-logging routine as well. Whenever a storage class driver logs an I/O error, it should include the **PathId**, **TargetId**, **Lun**, and **SrbStatus** values set by the storage port driver in the SRB, and, if possible, pertinent request-sense information as part of the error log entry's **DumpData**. Note that a storage class driver must not use the **PathId**, **TargetId**, and **Lun** from such SRBs to address other requests.

For more information about logging I/O errors, see [Logging Errors](https://msdn.microsoft.com/library/windows/hardware/ff554312).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20InterpretRequestSense%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


