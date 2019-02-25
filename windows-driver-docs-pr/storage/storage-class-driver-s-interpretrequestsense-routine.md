---
title: Storage Class Driver's InterpretRequestSense Routine
description: Storage Class Driver's InterpretRequestSense Routine
ms.assetid: abfb529d-7fab-40f7-b4cd-e6adb4cf643e
keywords:
- InterpretRequestSense
- request sense WDK storage
- errors WDK storage
- retrying requests WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's InterpretRequestSense Routine


## <span id="ddk_storage_class_drivers_interpretrequestsense_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_INTERPRETREQUESTSENSE_ROUTINE_KG"></span>


An *InterpretRequestSense* routine interprets the data returned in the SRB's **SenseInfoBuffer**, determines whether the request should be retried, and, if not, maps the error to an NTSTATUS value for the IRP's I/O status block.

The system port driver indicates whether request-sense information is available by setting SRB\_STATUS\_AUTOSENSE\_VALID or SRB\_STATUS\_REQUEST\_SENSE\_FAILED in **SrbStatus**.

If no request-sense information is available, *InterpretRequestSense* should check the **SrbStatus** value to determine whether to retry a given request or to determine an appropriate mapping to an NTSTATUS value.

The *InterpretRequestSense* routine might call a driver-supplied error-logging routine as well. Whenever a storage class driver logs an I/O error, it should include the **PathId**, **TargetId**, **Lun**, and **SrbStatus** values set by the storage port driver in the SRB, and, if possible, pertinent request-sense information as part of the error log entry's **DumpData**. Note that a storage class driver must not use the **PathId**, **TargetId**, and **Lun** from such SRBs to address other requests.

For more information about logging I/O errors, see [Logging Errors](https://msdn.microsoft.com/library/windows/hardware/ff554312).

 

 




