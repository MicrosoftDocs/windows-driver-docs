---
title: Scanning the Driver
description: Scanning the Driver
ms.assetid: c36960b4-d97e-49b7-a7ad-e71b0820db8a
keywords:
- Static Driver Verifier WDK , DriverEntry routine scans
- StaticDV WDK , DriverEntry routine scans
- SDV WDK , DriverEntry routine scans
- scanning DriverEntry routine WDK Static Driver Verifier
- driver entry points WDK Static Driver Verifier
- entry points WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Scanning the Driver


Scanning the driver using the **/scan** command option is optional. If you do not scan before verifying your driver, SDV scans the function role type declarations and creates an Sdv-map.h file when you verify the driver.

During this scan, SDV tries to detect the driver entry points that it needs to verify the driver. It records the results of the scan in Sdv-map.h, a file that it creates in the driver's sources directory.

However, it is very important that you review this file, either after the scan step or after the verification, to ensure that SDV has detected the correct entry points. If the entry points are missing or wrong, the verification might not be reliable. More importantly, if SDV cannot detect any entry points, it cannot verify the driver. 

You only have to scan once for each driver. Thereafter, SDV retains the Sdv-map.h file for the driver for future verifications.

### <span id="examine_the_sdv_map_h_file"></span><span id="EXAMINE_THE_SDV_MAP_H_FILE"></span>Examine the Sdv-map.h file

After running a scan command or verifying the driver, open the Sdv-map.h file and examine the file. Sdv-map.h is a formatted text file. You can read it any text editor, such as Notepad.

Compare the contents of the Sdv-map.h file with the declared function role types for your driver. Examine the contents of the Sdv-map.h file to see that the driver's callback or dispatch routines have been correctly identified.

The Sdv-map.h file is not required to list all of the entry points in your driver; only the entry points for the IRP major function codes or function role types that are used in the analysis. Do not add any IRP major function codes or function role types to the file.

For detailed information about the Sdv-map.h file, see [Sdv-map.h](sdv-map-h.md). The format is described in [Format of the Sdv-map.h File](format-of-the-sdv-map-h-file.md). The errors that can appear in the Sdv-map.h file are described in [Approving the Sdv-map.h File](approving-the-sdv-map-h-file.md).

The following example shows content of the Sdv-map.h file from Fail\_driver1, a sample WDM driver in the tools\\sdv\\samples\\fail\_drivers\\wdm directory.

```
//Approved=false
//DriverAddDevice
#define fun_AddDevice DriverAddDevice
//DriverEntry
#define fun_DriverEntry DriverEntry
//DriverUnload
#define fun_DriverUnload DriverUnload
//CompletionRoutine
#define fun_IO_COMPLETION_ROUTINE_1 CompletionRoutine
//DpcForIsrRoutine
#define fun_IO_DPC_ROUTINE_1 DpcForIsrRoutine
//DispatchCreate
#define fun_IRP_MJ_CREATE DispatchCreate
//DispatchPnp
#define fun_IRP_MJ_PNP DispatchPnp
//DispatchPower
#define fun_IRP_MJ_POWER DispatchPower
//DispatchRead
#define fun_IRP_MJ_READ DispatchRead
//DispatchSystemControl
#define fun_IRP_MJ_SYSTEM_CONTROL DispatchSystemControl
//InterruptServiceRoutine
#define fun_KSERVICE_ROUTINE_1 InterruptServiceRoutine
```

### <span id="correct_the_sdv_map_h_file"></span><span id="CORRECT_THE_SDV_MAP_H_FILE"></span>Correct the Sdv-map.h File

Before you verify a driver, correct any errors in the Sdv-map.h file. SDV will verify a driver, even if the Sdv-map.h file is incorrect or not approved, but the results of the verification might not be reliable. For example, if you do not declare a driver's dispatch or callback routine by using the corresponding function role type, the driver routine will not appear in the Sdv-map.h file. Consequently, you could miss finding defects in your code because SDV considers rules that use function role types as not applicable, even if you specified those rules as part of the verification.

To correct an Sdv-map.h file, be sure that your driver's dispatch or callback routines are declared by using the appropriate function role types. Then rescan the driver and verify that they appear in the Sdv-map.h file..

### <span id="approve_the_sdv_map_h_file"></span><span id="APPROVE_THE_SDV_MAP_H_FILE"></span>Approve the Sdv-map.h file

After determining that the Sdv-map.h file is correct, you can approve the file. If you did not make any changes to the file, you do not need to approve it.

SDV will verify a driver even if the Sdv-map.h file is not approved.

To approve the Sdv-map.h file, on the first line of the file, change:

```
//Approved=false
```

to:

```
//Approved=true
```

You only have to approve the Sdv-map.h file once for each driver. Thereafter, SDV retains the approved Sdv-map.h file for the driver for future verifications. If you want SDV to scan your source code again for function role type declarations, just delete the file.

The following example shows the approved Sdv-map.h file for the KMDF sample driver, Fail\_Driver1. SDV uses the Sdv-map.h file to map the driver's declared callback functions with the function role types SDV needs for verification.

```
//Approved=true
//DriverEntry
#define fun_DriverEntry DriverEntry
//EvtDriverDeviceAdd
#define fun_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd
//EvtIoDeviceControl
#define fun_WDF_IO_QUEUE_IO_DEVICE_CONTROL EvtIoDeviceControl
//EvtIoInternalDeviceControl
#define fun_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL EvtIoInternalDeviceControl
//EvtIoRead
#define fun_WDF_IO_QUEUE_IO_READ EvtIoRead
//EvtRequestCancel
#define fun_WDF_REQUEST_CANCEL_1 EvtRequestCancel
```

 

 





