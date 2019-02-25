---
title: Timings for diagnose call
description: The timing requirements of Diagnose to collect debug information are as follows.
ms.assetid: A21687FE-1398-4722-89E3-BFB511AA48E3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Timings for diagnose call


The timing requirements of Diagnose to collect debug information are as follows.

At the level of **DiagnoseLevelHardwareRegisters**, the LE is expected to collect device control registers no more than 1KB in the output buffer of the Diagnose call. This is the setting for a normal release product. It is intended for collecting the vital information of device control registers. The time limit to collect such information is 25ms.

At the level of **DiagnoseLevelFirmwareImageDump** or **DiagnoseLevelDriverStateDump**, the LE is expected to collect the device control registers and firmware full dump. If time permits, the LE can also collect the driver state, subject to the time limit. Except the control registers collected in the Diagnose output buffer, the firmware dump and driver state should be saved to files with the choice of names in %windir%\\system32\\drivers. The time to collect all debug information at either level should be within 25 seconds. These diagnose levels are meant to be used at the self-host phase.

## Related topics


[**eDiagnoseLevel**](https://msdn.microsoft.com/library/windows/hardware/mt297626)

[*MiniportWdiAdapterHangDiagnose*](https://msdn.microsoft.com/library/windows/hardware/mt297558)

 

 






